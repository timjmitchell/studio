Source: https://music21.org/music21docs/moduleReference/moduleStreamBase.html

# music21.stream.base

The `Stream` and its subclasses
(which are themselves subclasses of the [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"))
are the fundamental containers of offset-positioned notation and
musical elements in music21. Common Stream subclasses, such
as the `Measure`, `Part`
and `Score` objects, are also in this module.

## Stream

class music21.stream.base.Stream(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Stream)
:   This is the fundamental container for Music21Objects;
    objects may be ordered and/or placed in time based on
    offsets from the start of this container.

    As a subclass of Music21Object, Streams have offsets,
    priority, id, and groups.

    Streams may be embedded within other Streams. As each
    Stream can have its own offset, when Streams are
    embedded the offset of an element is relatively only
    to its parent Stream. The `flatten()`
    method provides access to a flat version of all
    embedded Streams, with offsets relative to the
    top-level Stream.

    The Stream `elements` attribute
    returns the contents of the Stream as a list. Direct access
    to, and manipulation of, the elements list is not recommended.
    Instead, use the host of high-level methods available.

    The Stream, like all Music21Objects, has a
    [`music21.duration.Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") that is usually the
    “release” time of the chronologically last element in the Stream
    (that is, the highest onset plus the duration of
    any element in the Stream).
    The duration, however, can be “unlinked” and explicitly
    set independent of the Stream’s contents.

    The first element passed to the Stream is an optional single
    Music21Object or a list, tuple, or other Stream of Music21Objects
    which is used to populate the Stream by inserting each object at
    its [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset")
    property. One special case is when every such object, such as a newly created
    one, has no offset. Then, so long as the entire list is not composed of
    non-Measure Stream subclasses representing synchrony like Parts or Voices,
    each element is appended, creating a sequence of elements in time,
    rather than synchrony.

    Other arguments and keywords are ignored, but are
    allowed so that subclassing the Stream is easier.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(note.Note('C#4', type='half'))
    >>> s1.append(note.Note('D5', type='quarter'))
    >>> s1.duration.quarterLength
    3.0
    >>> for thisNote in s1.notes:
    ...     print(thisNote.octave)
    ...
    4
    5
    ```

    This is a demonstration of creating a Stream with other elements,
    including embedded Streams (in this case, `music21.stream.Part`,
    a Stream subclass):

    ```python
    >>> c1 = clef.TrebleClef()
    >>> c1.offset = 0.0
    >>> c1.priority = -1
    >>> n1 = note.Note('E-6', type='eighth')
    >>> n1.offset = 1.0
    >>> p1 = stream.Part()
    >>> p1.offset = 0.0
    >>> p1.id = 'embeddedPart'
    >>> p1.append(note.Rest())  # quarter rest
    >>> s2 = stream.Stream([c1, n1, p1])
    >>> s2.duration.quarterLength
    1.5
    >>> s2.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.stream.Part embeddedPart>
        {0.0} <music21.note.Rest quarter>
    {1.0} <music21.note.Note E->
    ```

    * New in v7: providing a single element now works:

    ```python
    >>> s = stream.Stream(meter.TimeSignature())
    >>> s.first()
    <music21.meter.TimeSignature 4/4>
    ```

    Providing a list of objects or Measures or Scores (but not other Stream
    subclasses such as Parts or Voices) positions sequentially, i.e. appends, if they
    all have offset 0.0 currently:

    ```python
    >>> s2 = stream.Measure([note.Note(), note.Note(), bar.Barline()])
    >>> s2.show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C>
    {2.0} <music21.bar.Barline type=regular>
    ```

    A list of measures will thus each be appended:

    ```python
    >>> m1 = stream.Measure(n1, number=1)
    >>> m2 = stream.Measure(note.Rest(), number=2)
    >>> s3 = stream.Part([m1, m2])
    >>> s3.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {1.0} <music21.note.Note E->
    {1.5} <music21.stream.Measure 2 offset=1.5>
        {0.0} <music21.note.Rest quarter>
    ```

    Here, every element is a Stream that’s not a Measure (or Score), so it
    will be inserted at 0.0, rather than appending:

    ```python
    >>> s4 = stream.Score([stream.PartStaff(n1), stream.PartStaff(note.Rest())])
    >>> s4.show('text')
    {0.0} <music21.stream.PartStaff 0x...>
        {1.0} <music21.note.Note E->
    {0.0} <music21.stream.PartStaff 0x...>
        {0.0} <music21.note.Rest quarter>
    ```

    Create nested streams in one fell swoop:

    ```python
    >>> s5 = stream.Score(stream.Part(stream.Measure(chord.Chord('C2 A2'))))
    >>> s5.show('text')
    {0.0} <music21.stream.Part 0x...>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.chord.Chord C2 A2>
    ```

    This behavior can be modified by the givenElementsBehavior keyword to go against the norm
    of ‘OFFSETS’:

    ```python
    >>> from music21.stream.enums import GivenElementsBehavior
    >>> s6 = stream.Stream([note.Note('C'), note.Note('D')],
    ...                    givenElementsBehavior=GivenElementsBehavior.INSERT)
    >>> s6.show('text')  # all notes at offset 0.0
    {0.0} <music21.note.Note C>
    {0.0} <music21.note.Note D>
    ```

    ```python
    >>> p1 = stream.Part(stream.Measure(note.Note('C')), id='p1')
    >>> p2 = stream.Part(stream.Measure(note.Note('D')), id='p2')
    >>> s7 = stream.Score([p1, p2],
    ...                   givenElementsBehavior=GivenElementsBehavior.APPEND)
    >>> s7.show('text')  # parts following each other (not recommended)
    {0.0} <music21.stream.Part p1>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.note.Note C>
    {1.0} <music21.stream.Part p2>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.note.Note D>
    ```

    For developers of subclasses, please note that because of how Streams
    are copied, there cannot be
    required parameters (i.e., without defaults) in initialization.
    For instance, this would not
    be allowed, because craziness and givenElements are required:

    ```python
    class CrazyStream(Stream):
        def __init__(self, givenElements, craziness, **keywords):
            ...
    ```

    * New in v7: smart appending
    * New in v8: givenElementsBehavior keyword configures the smart appending.

[`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream") bases

* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream") read-only properties

Stream.beat
:   beat returns None for a Stream.

Stream.beatDuration
:   unlike other Music21Objects, streams always have beatDuration of None

Stream.beatStr
:   unlike other Music21Objects, streams always have beatStr (beat string) of None

    May change to ‘’ soon.

Stream.beatStrength
:   unlike other Music21Objects, streams always have beatStrength of None

Stream.highestOffset
:   Get start time of element with the highest offset in the Stream.
    Note the difference between this property and highestTime
    which gets the end time of the highestOffset

    ```python
    >>> stream1 = stream.Stream()
    >>> for offset in [0, 4, 8]:
    ...     n = note.Note('G#', type='whole')
    ...     stream1.insert(offset, n)
    >>> stream1.highestOffset
    8.0
    >>> stream1.highestTime
    12.0
    ```

Stream.highestTime
:   Returns the maximum of all Element offsets plus their Duration
    in quarter lengths. This value usually represents the last
    “release” in the Stream.

    Stream.duration is normally equal to the highestTime
    expressed as a Duration object, but it can be set separately
    for advanced operations.

    Example: Insert a dotted half note at position 0 and see where
    it cuts off:

    ```python
    >>> p1 = stream.Stream()
    >>> p1.highestTime
    0.0
    ```

    ```python
    >>> n = note.Note('A-')
    >>> n.quarterLength = 3
    >>> p1.insert(0, n)
    >>> p1.highestTime
    3.0
    ```

    Now insert in the same stream, the dotted half note
    at positions 1, 2, 3, 4 and see when the final note cuts off:

    ```python
    >>> p1.repeatInsert(n, [1, 2, 3, 4])
    >>> p1.highestTime
    7.0
    ```

    Another example.

    ```python
    >>> n = note.Note('C#')
    >>> n.quarterLength = 3
    ```

    ```python
    >>> q = stream.Stream()
    >>> for i in [20, 0, 10, 30, 40]:
    ...    p = stream.Stream()
    ...    p.repeatInsert(n, [0, 1, 2, 3, 4])
    ...    q.insert(i, p)  # insert out of order
    >>> len(q.flatten())
    25
    >>> q.highestTime  # this works b/c the component Stream has a duration
    47.0
    >>> r = q.flatten()
    ```

    * Changed in v6.5: highestTime can return a Fraction.

Stream.isGapless
:   Returns True if there are no gaps between the lowest offset and the highest time.
    Otherwise returns False

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('C'))
    >>> s.append(note.Note('D'))
    >>> s.isGapless
    True
    >>> s.insert(10.0, note.Note('E'))
    >>> s.isGapless
    False
    ```

Stream.lowestOffset
:   Get the start time of the Element with the lowest offset in the Stream.

    ```python
    >>> stream1 = stream.Stream()
    >>> for x in range(3, 5):
    ...     n = note.Note('G#')
    ...     stream1.insert(x, n)
    ...
    >>> stream1.lowestOffset
    3.0
    ```

    If the Stream is empty, then the lowest offset is 0.0:

    ```python
    >>> stream2 = stream.Stream()
    >>> stream2.lowestOffset
    0.0
    ```

    ```python
    >>> p = stream.Stream()
    >>> p.repeatInsert(note.Note('D5'), [0, 1, 2, 3, 4])
    >>> q = stream.Stream()
    >>> q.repeatInsert(p, list(range(0, 50, 10)))
    >>> len(q.flatten())
    25
    >>> q.lowestOffset
    0.0
    >>> r = stream.Stream()
    >>> r.repeatInsert(q, list(range(97, 500, 100)))
    >>> len(r.flatten())
    125
    >>> r.lowestOffset
    97.0
    ```

Stream.notes
:   The .notes property of a Stream returns an iterator
    that consists only of the notes (that is,
    [`Note`](moduleNote.html#music21.note.Note "music21.note.Note"),
    [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"), etc.) found
    in the stream. This excludes [`Rest`](moduleNote.html#music21.note.Rest "music21.note.Rest") objects.

    ```python
    >>> p1 = stream.Part()
    >>> k1 = key.KeySignature(0)  # key of C
    >>> n1 = note.Note('B')
    >>> r1 = note.Rest()
    >>> c1 = chord.Chord(['A', 'B-'])
    >>> p1.append([k1, n1, r1, c1])
    >>> p1.show('text')
    {0.0} <music21.key.KeySignature of no sharps or flats>
    {0.0} <music21.note.Note B>
    {1.0} <music21.note.Rest quarter>
    {2.0} <music21.chord.Chord A B->
    ```

    ```python
    >>> noteStream = p1.notes.stream()
    >>> noteStream.show('text')
    {0.0} <music21.note.Note B>
    {2.0} <music21.chord.Chord A B->
    ```

    Notice that .notes returns a [`StreamIterator`](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator") object

    ```python
    >>> p1.notes
    <music21.stream.iterator.StreamIterator for Part:0x105b56128 @:0>
    ```

    Let’s add a measure to p1:

    ```python
    >>> m1 = stream.Measure()
    >>> n2 = note.Note('D')
    >>> m1.insert(0, n2)
    >>> p1.append(m1)
    ```

    Now note that n2 is *not* found in p1.notes

    ```python
    >>> p1.notes.stream().show('text')
    {0.0} <music21.note.Note B>
    {2.0} <music21.chord.Chord A B->
    ```

    We need to call p1.flatten().notes to find it:

    ```python
    >>> p1.flatten().notes.stream().show('text')
    {0.0} <music21.note.Note B>
    {2.0} <music21.chord.Chord A B->
    {3.0} <music21.note.Note D>
    ```

    (Technical note: All elements of class NotRest are being found
    right now. This will eventually change to also filter out
    Unpitched objects, so that all elements returned by
    .notes have a .pitches attribute.

Stream.notesAndRests
:   The notesAndRests property of a Stream returns a StreamIterator
    that consists only of the [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote") objects found in
    the stream. The new Stream will contain
    mostly notes and rests (including
    [`Note`](moduleNote.html#music21.note.Note "music21.note.Note"),
    [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"),
    [`Rest`](moduleNote.html#music21.note.Rest "music21.note.Rest")) but also their subclasses, such as
    Harmony objects (ChordSymbols, FiguredBass), etc.

    ```python
    >>> s1 = stream.Stream()
    >>> k1 = key.KeySignature(0)  # key of C
    >>> n1 = note.Note('B')
    >>> r1 = note.Rest()
    >>> c1 = chord.Chord(['A', 'B-'])
    >>> s1.append([k1, n1, r1, c1])
    >>> s1.show('text')
    {0.0} <music21.key.KeySignature of no sharps or flats>
    {0.0} <music21.note.Note B>
    {1.0} <music21.note.Rest quarter>
    {2.0} <music21.chord.Chord A B->
    ```

    .notesAndRests removes the KeySignature object but keeps the Rest.

    ```python
    >>> notes1 = s1.notesAndRests.stream()
    >>> notes1.show('text')
    {0.0} <music21.note.Note B>
    {1.0} <music21.note.Rest quarter>
    {2.0} <music21.chord.Chord A B->
    ```

    The same caveats about Stream classes and .flatten() in .notes apply here.

Stream.pitches
:   Returns all [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects found in any
    element in the Stream as a Python List. Elements such as
    Streams, and Chords will have their Pitch objects accumulated as
    well. For that reason, a flat representation is not required.

    Note that this does not include any ornamental pitches implied
    by any ornaments on those Notes and Chords. To get those, use
    the makeNotation.ornamentalPitches(s) method.

    Pitch objects are returned in a List, not a Stream. This usage
    differs from the .notes property, but makes sense since Pitch
    objects usually have by default a Duration of zero. This is an important difference
    between them and [`music21.note.Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects.

    key.Key objects are subclasses of Scales, which DO have a .pitches list, but
    they are specifically exempt from looking for pitches, since that is unlikely
    what someone wants here.

    N.B., TODO: This may turn to an Iterator soon.

    ```python
    >>> a = corpus.parse('bach/bwv324.xml')
    >>> partOnePitches = a.parts[0].pitches
    >>> len(partOnePitches)
    25
    >>> partOnePitches[0]
    <music21.pitch.Pitch B4>
    >>> [str(p) for p in partOnePitches[0:10]]
    ['B4', 'D5', 'B4', 'B4', 'B4', 'B4', 'C5', 'B4', 'A4', 'A4']
    ```

    Note that the pitches returned above are
    objects, not text:

    ```python
    >>> partOnePitches[0].octave
    4
    ```

    Since all elements with a .pitches list are returned and streams themselves have
    .pitches properties (the docs you are reading now), pitches from embedded streams
    are also returned. Flattening a stream is not necessary. Whether this is a
    feature or a bug is in the eye of the beholder.

    ```python
    >>> len(a.pitches)
    104
    ```

    Chords get their pitches found as well:

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'G4'])
    >>> n = note.Note('F#4')
    >>> m = stream.Measure()
    >>> m.append(n)
    >>> m.append(c)
    >>> m.pitches
    [<music21.pitch.Pitch F#4>, <music21.pitch.Pitch C4>,
     <music21.pitch.Pitch E4>, <music21.pitch.Pitch G4>]
    ```

Stream.secondsMap
:   Returns a list where each element is a dictionary
    consisting of the ‘offsetSeconds’ in seconds of each element in a Stream,
    the ‘duration’ in seconds, the ‘endTimeSeconds’ in seconds (that is, the offset
    plus the duration), and the ‘element’ itself. Also contains a ‘voiceIndex’ entry which
    contains the voice number of the element, or None if there
    are no voices.

    ```python
    >>> mm1 = tempo.MetronomeMark(number=120)
    >>> n1 = note.Note(type='quarter')
    >>> c1 = clef.AltoClef()
    >>> n2 = note.Note(type='half')
    >>> s1 = stream.Stream()
    >>> s1.append([mm1, n1, c1, n2])
    >>> om = s1.secondsMap
    >>> om[3]['offsetSeconds']
    0.5
    >>> om[3]['endTimeSeconds']
    1.5
    >>> om[3]['element'] is n2
    True
    >>> om[3]['voiceIndex']
    ```

Stream.spanners
:   Return all [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner") objects
    (things such as Slurs, long trills, or anything that
    connects many objects)
    in an Iterator

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, spanner.Slur())
    >>> s.insert(0, spanner.Slur())
    >>> len(s.spanners)
    2
    ```

Stream.voices
:   Return all `Voices` objects
    in an iterator

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, stream.Voice())
    >>> s.insert(0, stream.Voice())
    >>> len(s.voices)
    2
    ```

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream") read/write properties

Stream.atSoundingPitch
:   Get or set the atSoundingPitch status, that is whether the
    score is at concert pitch or may have transposing instruments
    that will not sound as notated.

    Valid values are True, False, and ‘unknown’.

    Note that setting “atSoundingPitch” does not actually transpose the notes. See
    toSoundingPitch() for that information.

    ```python
    >>> s = stream.Stream()
    >>> s.atSoundingPitch = True
    >>> s.atSoundingPitch = False
    >>> s.atSoundingPitch = 'unknown'
    >>> s.atSoundingPitch
    'unknown'
    >>> s.atSoundingPitch = 'junk'
    Traceback (most recent call last):
    music21.exceptions21.StreamException: not a valid at sounding pitch value: junk
    ```

Stream.clef
:   Finds or sets a [`Clef`](moduleClef.html#music21.clef.Clef "music21.clef.Clef") at offset 0.0 in the Stream
    (generally a Measure):

    ```python
    >>> m = stream.Measure()
    >>> m.number = 10
    >>> m.clef = clef.TrebleClef()
    >>> thisTrebleClef = m.clef
    >>> thisTrebleClef.sign
    'G'
    >>> thisTrebleClef.getOffsetBySite(m)
    0.0
    ```

    Setting the clef for the measure a second time removes the previous clef
    from the measure and replaces it with the new one:

    ```python
    >>> m.clef = clef.BassClef()
    >>> m.clef.sign
    'F'
    ```

    And the TrebleClef is no longer in the measure:

    ```python
    >>> thisTrebleClef.getOffsetBySite(m)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object <music21.clef.TrebleClef> is not
          stored in stream <music21.stream.Measure 10 offset=0.0>
    ```

    The .clef appears in a .show() or other call
    just like any other element

    ```python
    >>> m.append(note.Note('D#', type='whole'))
    >>> m.show('text')
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.note.Note D#>
    ```

Stream.duration
:   Returns the total duration of the Stream, from the beginning of the
    stream until the end of the final element.
    May be set independently by supplying a Duration object.

    ```python
    >>> a = stream.Stream()
    >>> q = note.Note(type='quarter')
    >>> a.repeatInsert(q, [0, 1, 2, 3])
    >>> a.highestOffset
    3.0
    >>> a.highestTime
    4.0
    >>> a.duration
    <music21.duration.Duration 4.0>
    >>> a.duration.quarterLength
    4.0
    ```

    Advanced usage: override the duration from what is set:

    ```python
    >>> newDuration = duration.Duration('half')
    >>> newDuration.quarterLength
    2.0
    ```

    ```python
    >>> a.duration = newDuration
    >>> a.duration.quarterLength
    2.0
    ```

    Restore normal behavior by setting duration to None:

    ```python
    >>> a.duration = None
    >>> a.duration
    <music21.duration.Duration 4.0>
    ```

    Note that the highestTime for the stream is the same
    whether duration is overridden or not:

    ```python
    >>> a.highestTime
    4.0
    ```

Stream.elements
:   .elements is a Tuple representing the elements contained in the Stream.

    Directly getting, setting, and manipulating this Tuple is
    reserved for advanced usage. Instead, use the
    provided high-level methods. The elements retrieved here may not
    have this stream as an activeSite, therefore they might not be properly ordered.

    In other words: Don’t use unless you really know what you’re doing.
    Treat a Stream like a list!

    See how these are equivalent:

    ```python
    >>> m = stream.Measure([note.Note('F4'), note.Note('G4')])
    >>> m.elements
    (<music21.note.Note F>, <music21.note.Note G>)
    >>> tuple(m)
    (<music21.note.Note F>, <music21.note.Note G>)
    ```

    When setting .elements, a list of Music21Objects can be provided, or a complete Stream.
    If a complete Stream is provided, elements are extracted
    from that Stream. This has the advantage of transferring
    offset correctly and getting elements stored at the end.

    ```python
    >>> a = stream.Stream()
    >>> a.repeatInsert(note.Note('C'), list(range(10)))
    >>> b = stream.Stream()
    >>> b.repeatInsert(note.Note('D'), list(range(10)))
    >>> b.offset = 6
    >>> c = stream.Stream()
    >>> c.repeatInsert(note.Note('E'), list(range(10)))
    >>> c.offset = 12
    >>> b.insert(c)
    >>> b.isFlat
    False
    ```

    ```python
    >>> a.isFlat
    True
    ```

    Assigning from a Stream works well, and is actually much safer than assigning
    from .elements of the other Stream, since the active sites may have changed
    of that stream’s elements in the meantime.

    ```python
    >>> a.elements = b
    >>> a.isFlat
    False
    ```

    ```python
    >>> len(a.recurse().notes) == len(b.recurse().notes) == 20
    True
    ```

    There is one good use for .elements as opposed to treating a Stream like a list,
    and that is that in for Streams compares on object identity, i.e.,
    id(a) == id(b) [this is for historical reasons], while since .elements
    is a tuple. Recall our measure with the notes F4 and G4 above.

    ```python
    >>> other_g = note.Note('G4')
    ```

    This new G can’t be found in m, because it is not physically in the Measure

    ```python
    >>> other_g in m
    False
    ```

    But it is *equal* to something in the Measure:

    ```python
    >>> other_g in m.elements
    True
    ```

    But again, this could be done simply with:

    ```python
    >>> other_g in tuple(m)
    True
    ```

    One reason to use .elements is to iterate quickly without setting
    activeSite:

    ```python
    >>> n = note.Note()
    >>> m1 = stream.Measure([n])
    >>> m2 = stream.Measure([n])
    >>> n.activeSite is m2
    True
    >>> for el in m1.elements:
    ...     pass
    >>> n.activeSite is m2
    True
    >>> for el in m1:
    ...     pass
    >>> n.activeSite is m1
    True
    ```

Stream.finalBarline
:   Get or set the final barline of this Stream’s Measures,
    if and only if there are Measures defined as elements in this Stream.
    This method will not create Measures if none exist.

    ```python
    >>> p = stream.Part()
    >>> m1 = stream.Measure()
    >>> m1.rightBarline = bar.Barline('double')
    >>> p.append(m1)
    >>> p.finalBarline
    <music21.bar.Barline type=double>
    >>> m2 = stream.Measure()
    >>> m2.rightBarline = bar.Barline('final')
    >>> p.append(m2)
    >>> p.finalBarline
    <music21.bar.Barline type=final>
    ```

    This property also works on Scores that contain one or more Parts.
    In that case a list of barlines can be used to set the final barline.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> s.finalBarline
    [<music21.bar.Barline type=final>,
     <music21.bar.Barline type=final>,
     <music21.bar.Barline type=final>,
     <music21.bar.Barline type=final>]
    ```

    ```python
    >>> s.finalBarline = 'none'
    >>> s.finalBarline
    [<music21.bar.Barline type=none>,
     <music21.bar.Barline type=none>,
     <music21.bar.Barline type=none>,
     <music21.bar.Barline type=none>]
    ```

    Getting or setting a final barline on a Measure (or another Stream
    with a rightBarline attribute) is the same as getting or setting the rightBarline.

    ```python
    >>> m = stream.Measure()
    >>> m.finalBarline is None
    True
    >>> m.finalBarline = 'final'
    >>> m.finalBarline
    <music21.bar.Barline type=final>
    >>> m.rightBarline
    <music21.bar.Barline type=final>
    ```

    Getting on a generic Stream, Voice, or Opus always returns a barline of None,
    and setting on a generic Stream, Voice, or Opus always returns None:

    ```python
    >>> s = stream.Stream()
    >>> s.finalBarline is None
    True
    >>> s.finalBarline = 'final'
    >>> s.finalBarline is None
    True
    ```

    * Changed in v6.3: does not raise an exception if queried or set on a measure-less stream.
      Previously raised a StreamException

Stream.keySignature
:   Find or set a Key or KeySignature at offset 0.0 of a stream.

    ```python
    >>> a = stream.Measure()
    >>> a.keySignature = key.KeySignature(-2)
    >>> ks = a.keySignature
    >>> ks.sharps
    -2
    >>> a.show('text')
    {0.0} <music21.key.KeySignature of 2 flats>
    ```

    A key.Key object can be used instead of key.KeySignature,
    since the former derives from the latter.

    ```python
    >>> a.keySignature = key.Key('E', 'major')
    >>> for k in a:
    ...     print(k.offset, repr(k))
    0.0 <music21.key.Key of E major>
    ```

    Notice that setting a new key signature replaces any previous ones:

    ```python
    >>> len(a.getElementsByClass(key.KeySignature))
    1
    ```

    .keySignature can be set to None:

    ```python
    >>> a.keySignature = None
    >>> a.keySignature is None
    True
    ```

Stream.metadata
:   Get or set the [`Metadata`](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") object
    found at the beginning (offset 0) of this Stream.

    ```python
    >>> s = stream.Stream()
    >>> s.metadata = metadata.Metadata()
    >>> s.metadata.composer = 'frank'
    >>> s.metadata.composer
    'frank'
    ```

    May also return None if nothing is there.

Stream.seconds
:   Get or set the duration of this Stream in seconds, assuming that
    this object contains a [`MetronomeMark`](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") or
    [`MetricModulation`](moduleTempo.html#music21.tempo.MetricModulation "music21.tempo.MetricModulation").

    ```python
    >>> s = corpus.parse('bwv66.6')  # piece without a tempo
    >>> sFlat = s.flatten()
    >>> t = tempo.MetronomeMark('adagio')
    >>> sFlat.insert(0, t)
    >>> sFlat.seconds
    38.57142857...
    >>> tFast = tempo.MetronomeMark('allegro')
    >>> sFlat.replace(t, tFast)
    >>> sFlat.seconds
    16.363...
    ```

    Setting seconds on streams is not supported. Ideally it would instead
    scale all elements to fit, but this is a long way off.

    If a stream does not have a tempo-indication in it then the property
    returns 0.0 if an empty Stream (or self.highestTime is 0.0) or ‘nan’
    if there are non-zero duration objects in the stream:

    ```python
    >>> s = stream.Stream()
    >>> s.seconds
    0.0
    >>> s.insert(0, clef.TrebleClef())
    >>> s.seconds
    0.0
    >>> s.append(note.Note(type='half'))
    >>> s.seconds
    nan
    >>> import math
    >>> math.isnan(s.seconds)
    True
    ```

    * Changed in v6.3: return nan rather than raising an exception. Do not
      attempt to change seconds on a stream, as it did not do what you would expect.

Stream.staffLines
:   Returns the number of staffLines for the Stream, as defined by
    the first StaffLayout object found at offset 0 that defines staffLines

    ```python
    >>> m = stream.Measure()
    >>> m.staffLines
    5
    >>> m.staffLines = 4
    >>> m.staffLines
    4
    >>> m.show('text')
    {0.0} <music21.layout.StaffLayout distance None, staffNumber None,
              staffSize None, staffLines 4>
    ```

    ```python
    >>> staffLayout = m.getElementsByClass(layout.StaffLayout).first()
    >>> staffLayout.staffLines = 1
    >>> m.staffLines
    1
    ```

    ```python
    >>> p = stream.Part()
    >>> p.insert(0, m)
    >>> p.staffLines
    1
    ```

    ```python
    >>> p2 = stream.Part()
    >>> m0 = stream.Measure()
    >>> m0.insert(0, note.Note(type='whole'))
    >>> p2.append(m0)
    >>> p2.append(m)
    >>> p2.staffLines
    5
    ```

Stream.timeSignature
:   Gets or sets the timeSignature at offset 0.0 of the Stream (generally a Measure)

    ```python
    >>> m1 = stream.Measure(number=1)
    >>> m1.timeSignature = meter.TimeSignature('2/4')
    >>> m1.timeSignature.numerator, m1.timeSignature.denominator
    (2, 4)
    >>> m1.show('text')
    {0.0} <music21.meter.TimeSignature 2/4>
    ```

    Setting timeSignature to None removes any TimeSignature at offset 0.0:

    ```python
    >>> m1.timeSignature = None
    >>> m1.elements
    ()
    ```

    Only the time signature at offset 0 is found:

    ```python
    >>> m2 = stream.Measure(number=2)
    >>> m2.insert(0.0, meter.TimeSignature('5/4'))
    >>> m2.insert(2.0, meter.TimeSignature('7/4'))
    >>> ts = m2.timeSignature
    >>> ts.numerator, ts.denominator
    (5, 4)
    ```

    ```python
    >>> m2.timeSignature = meter.TimeSignature('2/8')
    >>> m2.timeSignature
    <music21.meter.TimeSignature 2/8>
    ```

    After setting a new .timeSignature, the old one is no longer in the Stream:

    ```python
    >>> ts in m2
    False
    ```

    This property is not recursive, so a Part will not have the time signature of
    the measure within it:

    ```python
    >>> p = stream.Part()
    >>> p.append(m2)
    >>> p.timeSignature is None
    True
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream") methods

Stream.\_\_eq\_\_(*other*)[[source]](../_modules/music21/stream/base.html#Stream.__eq__)
:   No two streams are ever equal unless they are the same Stream

Stream.\_\_getitem\_\_(*k: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [RecursiveIterator](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType][[source]](../_modules/music21/stream/base.html#Stream.__getitem__)

Stream.\_\_getitem\_\_(*k: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → M21ObjType

Stream.\_\_getitem\_\_(*k: [slice](https://docs.python.org/3/library/functions.html#slice "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[M21ObjType]

Stream.\_\_getitem\_\_(*k: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[ChangedM21ObjType]*) → [RecursiveIterator](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[ChangedM21ObjType]

Stream.\_\_getitem\_\_(*k: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")*) → [RecursiveIterator](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType]

Stream.\_\_getitem\_\_(*k: [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")]*) → [RecursiveIterator](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType]
:   Get a Music21Object from the Stream using a variety of keys or indices.

    If an int is given, the Music21Object at the index is returned, as if it were a list
    or tuple:

    ```python
    >>> c = note.Note('C')
    >>> d = note.Note('D')
    >>> e = note.Note('E')
    >>> r1 = note.Rest()
    >>> f = note.Note('F')
    >>> g = note.Note('G')
    >>> r2 = note.Rest()
    >>> a = note.Note('A')
    >>> s = stream.Stream([c, d, e, r1, f, g, r2, a])
    ```

    ```python
    >>> s[0]
    <music21.note.Note C>
    >>> s[-1]
    <music21.note.Note A>
    ```

    Out of range notes raise an IndexError:

    ```python
    >>> s[99]
    Traceback (most recent call last):
    IndexError: attempting to access index 99 while elements is of size 8
    ```

    If a slice of indices is given, a list of elements is returned, as if the Stream
    were a list or Tuple.

    ```python
    >>> subslice = s[2:5]
    >>> subslice
    [<music21.note.Note E>, <music21.note.Rest quarter>, <music21.note.Note F>]
    >>> len(subslice)
    3
    >>> s[1].offset
    1.0
    >>> subslice[1].offset
    3.0
    ```

    If a class is given, then a [`RecursiveIterator`](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")
    of elements matching the requested class is returned, similar
    to Stream().recurse().getElementsByClass().

    ```python
    >>> len(s)
    8
    >>> len(s[note.Rest])
    2
    >>> len(s[note.Note])
    6
    ```

    ```python
    >>> for n in s[note.Note]:
    ...     print(n.name, end=' ')
    C D E F G A
    ```

    Note that this iterator is recursive: it will find elements inside of streams
    within this stream:

    ```python
    >>> c_sharp = note.Note('C#')
    >>> v = stream.Voice()
    >>> v.insert(0, c_sharp)
    >>> s.insert(0.5, v)
    >>> len(s[note.Note])
    7
    ```

    When using a single Music21 class in this way, your type checker will
    be able to infer that the only objects in any loop are in fact note.Note
    objects, and catch programming errors before running.

    Multiple classes can be provided, separated by commas. Any element matching
    any of the requested classes will be matched.

    ```python
    >>> len(s[note.Note, note.Rest])
    9
    ```

    ```python
    >>> for note_or_rest in s[note.Note, note.Rest]:
    ...     if isinstance(note_or_rest, note.Note):
    ...         print(note_or_rest.name, end=' ')
    ...     else:
    ...         print('Rest', end=' ')
    C C# D E Rest F G Rest A
    ```

    The actual object returned by s[module.Class] is a
    [`RecursiveIterator`](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator") and has all the functions
    available on it:

    ```python
    >>> s[note.Note]
    <...>
    ```

    If no elements of the class are found, no error is raised in version 7:

    ```python
    >>> list(s[layout.StaffLayout])
    []
    ```

    If the key is a string, it is treated as a querySelector as defined in
    `getElementsByQuerySelector()`, namely that bare strings
    are treated as class names, strings beginning with # are id-queries, and strings
    beginning with . are group queries.

    We can set some ids and groups for demonstrating.

    ```python
    >>> a.id = 'last_a'
    >>> c.groups.append('ghost')
    >>> e.groups.append('ghost')
    ```

    ‘.ghost’, because it begins with ., is treated as a class name and
    returns a RecursiveIterator:

    ```python
    >>> for n in s['.ghost']:
    ...     print(n.name, end=' ')
    C E
    ```

    A query selector with a # returns the single element matching that
    element or returns None if there is no match:

    ```python
    >>> s['#last_a']
    <music21.note.Note A>
    ```

    ```python
    >>> s['#nothing'] is None
    True
    ```

    Any other query raises a TypeError:

    ```python
    >>> s[0.5]
    Traceback (most recent call last):
    TypeError: Streams can get items by int, slice, class, class iterable, or string query;
       got <class 'float'>
    ```

    * Changed in v7:
      - out of range indexes now raise an IndexError, not StreamException
      - strings (‘music21.note.Note’, ‘#id’, ‘.group’) are now treated like a query selector.
      - slices with negative indices now supported
      - Unsupported types now raise TypeError
      - Class and Group searches now return a recursive StreamIterator rather than a Stream
      - Slice searches now return a list of elements rather than a Stream
    * Changed in v8:
      - for strings: only fully-qualified names such as “music21.note.Note” or
      partially-qualified names such as “note.Note” are
      supported as class names. Better to use a literal type or explicitly call
      .recurse().getElementsByClass to get the earlier behavior. Old behavior
      still works until v9. This is an attempt to unify \_\_getitem\_\_ behavior in
      StreamIterators and Streams.
      - allowed iterables of qualified class names, e.g. [note.Note, note.Rest]

Stream.activateVariants(*group=None*, *\**, *matchBySpan=True*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.activateVariants)
:   For any [`Variant`](moduleVariant.html#music21.variant.Variant "music21.variant.Variant") objects defined in this Stream
    (or selected by matching the group parameter),
    replace elements defined in the Variant with those in the calling Stream.
    Elements replaced will be gathered into a new Variant
    given the group ‘default’. If a variant is activated with
    .replacementDuration different from its length, the appropriate elements
    in the stream will have their offsets shifted, and measure numbering
    will be fixed. If matchBySpan is True, variants with lengthType
    ‘replacement’ will replace all the elements in the
    replacement region of comparable class. If matchBySpan is False,
    elements will be swapped in when a match is found between an element
    in the variant and an element in the replacement region of the string.

    ```python
    >>> sStr   = 'd4 e4 f4 g4   a2 b-4 a4    g4 a8 g8 f4 e4    d2 a2              '
    >>> v1Str  = '              a2. b-8 a8 '
    >>> v2Str1 = '                                             d4 f4 a2 '
    >>> v2Str2 = '                                                      d4 f4 AA2 '
    ```

    ```python
    >>> sStr += "d4 e4 f4 g4    a2 b-4 a4    g4 a8 b-8 c'4 c4    f1"
    ```

    ```python
    >>> s = converter.parse('tinynotation: 4/4 ' + sStr, makeNotation=False)
    >>> s.makeMeasures(inPlace=True)  # maybe not necessary?
    >>> v1stream = converter.parse('tinynotation: 4/4 ' + v1Str, makeNotation=False)
    >>> v2stream1 = converter.parse('tinynotation: 4/4 ' + v2Str1, makeNotation=False)
    >>> v2stream2 = converter.parse('tinynotation: 4/4 ' + v2Str2, makeNotation=False)
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
    >>> v2.replacementDuration = 4.0
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
    >>> v3.replacementDuration = 4.0
    >>> v1.groups = ['docVariants']
    >>> v2.groups = ['docVariants']
    >>> v3.groups = ['docVariants']
    ```

    ```python
    >>> s.insert(4.0, v1)   # replacement variant
    >>> s.insert(12.0, v2)  # insertion variant (2 bars replace 1 bar)
    >>> s.insert(20.0, v3)  # deletion variant (0 bars replace 1 bar)
    >>> s.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {4.0} <music21.variant.Variant object of length 4.0>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {1.5} <music21.note.Note G>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note E>
    {12.0} <music21.variant.Variant object of length 8.0>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note D>
        {2.0} <music21.note.Note A>
    {16.0} <music21.stream.Measure 5 offset=16.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {20.0} <music21.variant.Variant object of length 0.0>
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    {24.0} <music21.stream.Measure 7 offset=24.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {1.5} <music21.note.Note B->
        {2.0} <music21.note.Note C>
        {3.0} <music21.note.Note C>
    {28.0} <music21.stream.Measure 8 offset=28.0>
        {0.0} <music21.note.Note F>
        {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> docVariant = s.activateVariants('docVariants')
    ```

    ```python
    >>> s.show()
    ```

    [![../_images/stream_activateVariants1.png](../_images/stream_activateVariants1.png)](../_images/stream_activateVariants1.png)

    ```python
    >>> docVariant.show()
    ```

    [![../_images/stream_activateVariants2.png](../_images/stream_activateVariants2.png)](../_images/stream_activateVariants2.png)

    ```python
    >>> docVariant.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {4.0} <music21.variant.Variant object of length 4.0>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note A>
        {3.0} <music21.note.Note B->
        {3.5} <music21.note.Note A>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {1.5} <music21.note.Note G>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note E>
    {12.0} <music21.variant.Variant object of length 4.0>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note A>
    {16.0} <music21.stream.Measure 5 offset=16.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note A>
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {24.0} <music21.variant.Variant object of length 4.0>
    {24.0} <music21.stream.Measure 7 offset=24.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {1.5} <music21.note.Note B->
        {2.0} <music21.note.Note C>
        {3.0} <music21.note.Note C>
    {28.0} <music21.stream.Measure 8 offset=28.0>
        {0.0} <music21.note.Note F>
        {4.0} <music21.bar.Barline type=final>
    ```

    After a variant group has been activated, the regions it replaced are
    stored as variants with the group ‘default’.
    It should be noted that this means .activateVariants should rarely if
    ever be used on a stream which is returned
    by activateVariants because the group information is lost.

    ```python
    >>> defaultVariant = docVariant.activateVariants('default')
    >>> defaultVariant.show()
    ```

    [![../_images/stream_activateVariants3.png](../_images/stream_activateVariants3.png)](../_images/stream_activateVariants3.png)

    ```python
    >>> defaultVariant.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {4.0} <music21.variant.Variant object of length 4.0>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {1.5} <music21.note.Note G>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note E>
    {12.0} <music21.variant.Variant object of length 8.0>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note D>
        {2.0} <music21.note.Note A>
    {16.0} <music21.stream.Measure 5 offset=16.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {20.0} <music21.variant.Variant object of length 0.0>
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    {24.0} <music21.stream.Measure 7 offset=24.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {1.5} <music21.note.Note B->
        {2.0} <music21.note.Note C>
        {3.0} <music21.note.Note C>
    {28.0} <music21.stream.Measure 8 offset=28.0>
        {0.0} <music21.note.Note F>
        {4.0} <music21.bar.Barline type=final>
    ```

Stream.addGroupForElements(*group: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *classFilter=None*, *\**, *recurse=False*, *setActiveSite=True*)[[source]](../_modules/music21/stream/base.html#Stream.addGroupForElements)
:   Add the group to the groups attribute of all elements.
    if classFilter is set then only those elements whose objects
    belong to a certain class (or for Streams which are themselves of
    a certain class) are set.

    ```python
    >>> a = stream.Stream()
    >>> a.repeatAppend(note.Note('A-'), 30)
    >>> a.repeatAppend(note.Rest(), 30)
    >>> a.addGroupForElements('flute')
    >>> a[0].groups
    ['flute']
    >>> a.addGroupForElements('quietTime', note.Rest)
    >>> a[0].groups
    ['flute']
    >>> a[50].groups
    ['flute', 'quietTime']
    >>> a[1].groups.append('quietTime')  # set one note to it
    >>> a[1].step = 'B'
    >>> b = a.getElementsByGroup('quietTime')
    >>> len(b)
    31
    >>> c = b.getElementsByClass(note.Note)
    >>> len(c)
    1
    >>> c[0].name
    'B-'
    ```

    If recurse is True then all sub-elements will get the group:

    ```python
    >>> s = converter.parse('tinyNotation: 4/4 c4 d e f g a b- b')
    >>> s.addGroupForElements('scaleNote', 'Note')
    >>> s.recurse().notes[3].groups
    []
    >>> s.addGroupForElements('scaleNote', 'Note', recurse=True)
    >>> s.recurse().notes[3].groups
    ['scaleNote']
    ```

    No group will be added more than once:

    ```python
    >>> s.addGroupForElements('scaleNote', 'Note', recurse=True)
    >>> s.recurse().notes[3].groups
    ['scaleNote']
    ```

    * New in v6.7.1: recurse

Stream.allPlayingWhileSounding(*el*, *elStream=None*)[[source]](../_modules/music21/stream/base.html#Stream.allPlayingWhileSounding)
:   Returns a new Stream of elements in this stream that sound
    at the same time as el, an element presumably in another Stream.

    The offset of this new Stream is set to el’s offset, while the
    offset of elements within the Stream are adjusted relative to
    their position with respect to the start of el. Thus, a note
    that is sounding already when el begins would have a negative
    offset. The duration of otherStream is forced
    to be the length of el – thus a note sustained after el ends
    may have a release time beyond that of the duration of the Stream.

    As above, elStream is an optional Stream to look up el’s offset in. Use
    this to work on an element in another part.

    The method always returns a Stream, but it might be an empty Stream.

Stream.analyze(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Stream.analyze)
:   Runs a particular analytical method on the contents of the
    stream to find its ambitus (range) or key.

    * ambitus – runs [`Ambitus`](moduleAnalysisDiscrete.html#music21.analysis.discrete.Ambitus "music21.analysis.discrete.Ambitus")
    * key – runs [`KrumhanslSchmuckler`](moduleAnalysisDiscrete.html#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler")

    Some of these methods can take additional arguments. For details on
    these arguments, see
    [`analyzeStream()`](moduleAnalysisDiscrete.html#music21.analysis.discrete.analyzeStream "music21.analysis.discrete.analyzeStream").

    Example:

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> s.analyze('ambitus')
    <music21.interval.Interval m21>
    >>> s.analyze('key')
    <music21.key.Key of f# minor>
    ```

    Example: music21 allows you to automatically run an
    analysis to get the key of a piece or excerpt not
    based on the key signature but instead on the
    frequency with which some notes are used as opposed
    to others (first described by Carol Krumhansl). For
    instance, a piece with mostly Cs and Gs, some Fs,
    and Ds, but fewer G#s, C#s, etc. is more likely to
    be in the key of C major than in D-flat major
    (or A minor, etc.). You can easily get this analysis
    from a stream by running:

    ```python
    >>> myStream = corpus.parse('luca/gloria')
    >>> analyzedKey = myStream.analyze('key')
    >>> analyzedKey
    <music21.key.Key of F major>
    ```

    analyzedKey is a [`Key`](moduleKey.html#music21.key.Key "music21.key.Key")
    object with a few extra parameters.
    correlationCoefficient shows how well this key fits the
    profile of a piece in that key:

    ```python
    >>> analyzedKey.correlationCoefficient
    0.86715...
    ```

    alternateInterpretations is a list of the other
    possible interpretations sorted from most likely to least:

    ```python
    >>> analyzedKey.alternateInterpretations
    [<music21.key.Key of d minor>,
     <music21.key.Key of C major>,
     <music21.key.Key of g minor>,
     ...]
    ```

    Each of these can be examined in turn to see its correlation coefficient:

    ```python
    >>> analyzedKey.alternateInterpretations[1].correlationCoefficient
    0.788528...
    >>> analyzedKey.alternateInterpretations[22].correlationCoefficient
    -0.86728...
    ```

Stream.append(*others*)[[source]](../_modules/music21/stream/base.html#Stream.append)
:   Add a Music21Object (including another Stream) to the end of the current Stream.

    If given a list, will append each element in order after the previous one.

    The “end” of the stream is determined by the highestTime property
    (that is the latest “release” of an object, or directly after the last
    element ends).

    Runs fast for multiple addition and will preserve isSorted if True

    ```python
    >>> a = stream.Stream()
    >>> notes = []
    >>> for x in range(3):
    ...     n = note.Note('G#')
    ...     n.duration.quarterLength = 3
    ...     notes.append(n)
    >>> a.append(notes[0])
    >>> a.highestOffset, a.highestTime
    (0.0, 3.0)
    >>> a.append(notes[1])
    >>> a.highestOffset, a.highestTime
    (3.0, 6.0)
    >>> a.append(notes[2])
    >>> a.highestOffset, a.highestTime
    (6.0, 9.0)
    >>> notes2 = []
    ```

    Notes’ naive offsets will
    change when they are added to a stream.

    ```python
    >>> for x in range(3):
    ...     n = note.Note('A-')
    ...     n.duration.quarterLength = 3
    ...     n.offset = 0
    ...     notes2.append(n)
    >>> a.append(notes2)  # add em all again
    >>> a.highestOffset, a.highestTime
    (15.0, 18.0)
    >>> a.isSequence()
    True
    ```

    Adding a note that already has an offset set does nothing different
    from above! That is, it is still added to the end of the Stream:

    ```python
    >>> n3 = note.Note('B-')
    >>> n3.offset = 1
    >>> n3.duration.quarterLength = 3
    >>> a.append(n3)
    >>> a.highestOffset, a.highestTime
    (18.0, 21.0)
    >>> n3.getOffsetBySite(a)
    18.0
    ```

    Prior to v5.7 there was a bug where appending a Clef after a KeySignature
    or a Measure after a KeySignature, etc. would not cause sorting to be re-run.
    This bug is now fixed.

    ```python
    >>> s = stream.Stream()
    >>> s.append([meter.TimeSignature('4/4'),
    ...           clef.TrebleClef()])
    >>> s.elements[0]
    <music21.clef.TrebleClef>
    >>> s.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> s.append(metadata.Metadata(composer='Cage'))
    >>> s.show('text')
    {0.0} <music21.metadata.Metadata object at 0x11ca356a0>
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.meter.TimeSignature 4/4>
    ```

Stream.attachIntervalsBetweenStreams(*cmpStream*)[[source]](../_modules/music21/stream/base.html#Stream.attachIntervalsBetweenStreams)
:   For each element in self, creates an interval.Interval object in the element’s
    editorial that is the interval between it and the element in cmpStream that
    is sounding at the moment the element in srcStream is attacked.

    Remember that if you are comparing two streams with measures, etc.,
    you’ll need to flatten each stream as follows:

    ```python
    >>> stream1.flatten().attachIntervalsBetweenStreams(stream2.flatten())
    ```

    Example usage:

    ```python
    >>> s1 = converter.parse('tinynotation: 7/4 C4 d8 e f# g A2 d2', makeNotation=False)
    >>> s2 = converter.parse('tinynotation: 7/4 g4 e8 d c4   a2 r2', makeNotation=False)
    >>> s1.attachIntervalsBetweenStreams(s2)
    >>> for n in s1.notes:
    ...     if n.editorial.harmonicInterval is None:
    ...         print('None')  # Wil print if other voice had a rest.
    ...     else:
    ...         print(n.editorial.harmonicInterval.directedName)
    P12
    M2
    M-2
    A-4
    P-5
    P8
    None
    ```

Stream.attachMelodicIntervals()[[source]](../_modules/music21/stream/base.html#Stream.attachMelodicIntervals)
:   For each element in self, creates an interval.Interval object in the element’s
    editorial that is the interval between it and the previous element in the stream. Thus,
    the first element will have a value of None.

    DEPRECATED sometime soon. A replacement to come presently.

    ```python
    >>> s1 = converter.parse('tinyNotation: 7/4 C4 d8 e f# g A2 d2', makeNotation=False)
    >>> s1.attachMelodicIntervals()
    >>> for n in s1.notes:
    ...     if n.editorial.melodicInterval is None:
    ...         print('None')
    ...     else:
    ...         print(n.editorial.melodicInterval.directedName)
    None
    M9
    M2
    M2
    m2
    m-7
    P4
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('C'))
    >>> s.append(note.Note('D'))
    >>> s.append(note.Rest(quarterLength=4.0))
    >>> s.append(note.Note('D'))
    >>> s.attachMelodicIntervals()
    >>> for n in s.notes:
    ...     if n.editorial.melodicInterval is None:
    ...         print('None')  # Will print if other voice had a rest.
    ...     else:
    ...         print(n.editorial.melodicInterval.directedName)
    None
    M2
    P1
    ```

Stream.augmentOrDiminish(*amountToScale*, *\**, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.augmentOrDiminish)
:   Given a number greater than zero,
    multiplies the current quarterLength of the
    duration of each element by this number
    as well as their offset and returns a new Stream.
    Or if inPlace is
    set to True, modifies the durations of each
    element within the stream.

    A number of 0.5 will halve the durations and relative
    offset positions; a number of 2 will double the
    durations and relative offset positions.

    Note that the default for inPlace is the opposite
    of what it is for augmentOrDiminish on a Duration.
    This is done purposely to reflect the most common
    usage.

    ```python
    >>> s = stream.Stream()
    >>> n = note.Note()
    >>> s.repeatAppend(n, 10)
    >>> s.highestOffset, s.highestTime
    (9.0, 10.0)
    >>> s1 = s.augmentOrDiminish(2)
    >>> s1.highestOffset, s1.highestTime
    (18.0, 20.0)
    >>> s1 = s.augmentOrDiminish(0.5)
    >>> s1.highestOffset, s1.highestTime
    (4.5, 5.0)
    ```

Stream.beatAndMeasureFromOffset(*searchOffset*, *fixZeros=True*)[[source]](../_modules/music21/stream/base.html#Stream.beatAndMeasureFromOffset)
:   Returns a two-element tuple of the beat and the Measure object (or the first one
    if there are several at the same offset; unlikely but possible) for a given
    offset from the start of this Stream (that contains measures).

    Recursively searches for measures. Note that this method assumes that all parts
    have measures of consistent length. If that’s not the case, this
    method can be called on the relevant part.

    This algorithm should work even for weird time signatures such as 2+3+2/8.

    ```python
    >>> bach = corpus.parse('bach/bwv1.6')
    >>> bach.parts[0].measure(2).getContextByClass(meter.TimeSignature)
    <music21.meter.TimeSignature 4/4>
    >>> returnTuples = []
    >>> for offset in [0.0, 1.0, 2.0, 5.0, 5.5]:
    ...     returnTuples.append(bach.beatAndMeasureFromOffset(offset))
    >>> returnTuples
    [(4.0, <music21.stream.Measure 0 offset=0.0>),
     (1.0, <music21.stream.Measure 1 offset=1.0>),
     (2.0, <music21.stream.Measure 1 offset=1.0>),
     (1.0, <music21.stream.Measure 2 offset=5.0>),
     (1.5, <music21.stream.Measure 2 offset=5.0>)]
    ```

    To get just the measureNumber and beat, use a transformation like this:
    >>> [(beat, measureObj.number) for beat, measureObj in returnTuples]
    [(4.0, 0), (1.0, 1), (2.0, 1), (1.0, 2), (1.5, 2)]

    Adapted from contributed code by Dmitri Tymoczko. With thanks to DT.

Stream.chordify(*\**, *addTies=True*, *addPartIdAsGroup=False*, *removeRedundantPitches=True*, *toSoundingPitch=True*, *copyPitches=True*)[[source]](../_modules/music21/stream/base.html#Stream.chordify)
:   Create a chordal reduction of polyphonic music, where each
    change to a new pitch results in a new chord. If a Score or
    Part of Measures is provided, a Stream of Measures will be
    returned. If a flat Stream of notes, or a Score of such
    Streams is provided, no Measures will be returned.

    If using chordify with chord symbols, ensure that the ChordSymbol objects
    have durations (by default, the duration of a ChordSymbol object is 0, unlike
    a Chord object). If Harmony objects are not provided a duration, they
    will not be included in the chordified output pitches but may appear as chord symbols
    in notation on the score. To realize the chord symbol durations on a score, call
    [`music21.harmony.realizeChordSymbolDurations()`](moduleHarmony.html#music21.harmony.realizeChordSymbolDurations "music21.harmony.realizeChordSymbolDurations") and pass in the score.

    This functionality works by splitting all Durations in
    all parts, or if there are multiple parts by all unique offsets. All
    simultaneous durations are then gathered into single chords.

    If addPartIdAsGroup is True, all elements found in the
    Stream will have their source Part id added to the
    element’s pitches’ Group. These groups names are useful
    for partially “de-chordifying” the output. If the element chordifies to
    a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") object, then the group will be found in each
    [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") element’s .groups in Chord.pitches. If the
    element chordifies to a single [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") then .pitch.groups
    will hold the group name.

    The addTies parameter currently does not work for pitches in Chords.

    If toSoundingPitch is True, all parts that define one or
    more transpositions will be transposed to sounding pitch before chordification.
    True by default.

    ```python
    >>> s = stream.Score()
    >>> p1 = stream.Part()
    >>> p1.id = 'part1'
    >>> p1.insert(4, note.Note('C#4'))
    >>> p1.insert(5.3, note.Rest())
    >>> p2 = stream.Part()
    >>> p2.id = 'part2'
    >>> p2.insert(2.12, note.Note('D-4', type='half'))
    >>> p2.insert(5.5, note.Rest())
    >>> s.insert(0, p1)
    >>> s.insert(0, p2)
    >>> s.show('text', addEndTimes=True)
    {0.0 - 6.3} <music21.stream.Part part1>
        {4.0 - 5.0} <music21.note.Note C#>
        {5.3 - 6.3} <music21.note.Rest quarter>
    {0.0 - 6.5} <music21.stream.Part part2>
        {2.12 - 4.12} <music21.note.Note D->
        {5.5 - 6.5} <music21.note.Rest quarter>
    ```

    ```python
    >>> cc = s.chordify()
    ```

    ```python
    >>> cc[3]
    <music21.chord.Chord C#4>
    >>> cc[3].duration.quarterLength
    Fraction(22, 25)
    ```

    ```python
    >>> cc.show('text', addEndTimes=True)
    {0.0 - 2.12} <music21.note.Rest 53/25ql>
    {2.12 - 4.0} <music21.chord.Chord D-4>
    {4.0 - 4.12} <music21.chord.Chord C#4 D-4>
    {4.12 - 5.0} <music21.chord.Chord C#4>
    {5.0 - 6.5} <music21.note.Rest dotted-quarter>
    ```

    Here’s how addPartIdAsGroup works:

    ```python
    >>> cc2 = s.chordify(addPartIdAsGroup=True)
    >>> cSharpDFlatChord = cc2[2]
    >>> for p in cSharpDFlatChord.pitches:
    ...     (str(p), p.groups)
    ('C#4', ['part1'])
    ('D-4', ['part2'])
    ```

    ```python
    >>> s = stream.Stream()
    >>> p1 = stream.Part()
    >>> p1.insert(0, harmony.ChordSymbol('Cm', quarterLength=4.0))
    >>> p1.insert(2, note.Note('C2'))
    >>> p1.insert(4, harmony.ChordSymbol('D', quarterLength=4.0))
    >>> p1.insert(7, note.Note('A2'))
    >>> s.insert(0, p1)
    >>> s.chordify().show('text')
    {0.0} <music21.chord.Chord C3 E-3 G3>
    {2.0} <music21.chord.Chord C2 C3 E-3 G3>
    {3.0} <music21.chord.Chord C3 E-3 G3>
    {4.0} <music21.chord.Chord D3 F#3 A3>
    {7.0} <music21.chord.Chord A2 D3 F#3 A3>
    ```

    Note that [`ChordSymbol`](moduleHarmony.html#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") objects can also be chordified:

    ```python
    >>> s = stream.Stream()
    >>> p2 = stream.Part()
    >>> p1 = stream.Part()
    >>> p2.insert(0, harmony.ChordSymbol('Cm', quarterLength=4.0))
    >>> p1.insert(2, note.Note('C2'))
    >>> p2.insert(4, harmony.ChordSymbol('D', quarterLength=4.0))
    >>> p1.insert(7, note.Note('A2'))
    >>> s.insert(0, p1)
    >>> s.insert(0, p2)
    >>> s.chordify().show('text')
    {0.0} <music21.chord.Chord C3 E-3 G3>
    {2.0} <music21.chord.Chord C2 C3 E-3 G3>
    {3.0} <music21.chord.Chord C3 E-3 G3>
    {4.0} <music21.chord.Chord D3 F#3 A3>
    {7.0} <music21.chord.Chord A2 D3 F#3 A3>
    ```

    If addPartIdAsGroup is True, and there are redundant pitches,
    ensure that the merged pitch has both groups

    ```python
    >>> s = stream.Score()
    >>> p0 = stream.Part(id='p0')
    >>> p0.insert(0, note.Note('C4'))
    >>> p1 = stream.Part(id='p1')
    >>> p1.insert(0, note.Note('C4'))
    >>> s.insert(0, p0)
    >>> s.insert(0, p1)
    >>> s1 = s.chordify(addPartIdAsGroup=True)
    >>> c = s1.recurse().notes[0]
    >>> c
    <music21.chord.Chord C4>
    >>> c.pitches[0].groups
    ['p0', 'p1']
    ```

    With copyPitches = False, then the original pitches are retained, which
    together with removeRedundantPitches=False can be a powerful tool for
    working back to the original score:

    ```python
    >>> n00 = note.Note('C4')
    >>> n01 = note.Note('E4')
    >>> n10 = note.Note('E4', type='half')
    >>> p0 = stream.Part(id='p0')
    >>> p1 = stream.Part(id='p1')
    >>> p0.append([n00, n01])
    >>> p1.append(n10)
    >>> s = stream.Score()
    >>> s.insert(0, p0)
    >>> s.insert(0, p1)
    >>> ss = s.chordify(removeRedundantPitches=False, copyPitches=False, addPartIdAsGroup=True)
    >>> ss.show('text')
    {0.0} <music21.chord.Chord C4 E4>
    {1.0} <music21.chord.Chord E4 E4>
    ```

    ```python
    >>> c1 = ss.recurse().notes[1]
    >>> for p in c1.pitches:
    ...     if 'p0' in p.groups:
    ...         p.step = 'G'  # make a complete triad
    >>> n01
    <music21.note.Note G>
    ```

    * Changed in v5:
      - Runs a little faster for small scores and run a TON faster for big scores
      running in O(n) time not O(n^2)
      - no longer supported: displayTiedAccidentals=False,
    * Changed in v6.3: Added copyPitches

Stream.clear() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.clear)
:   Remove all elements in a stream.

    ```python
    >>> m = stream.Measure(number=3)
    >>> m.append(note.Note('C'))
    >>> m.storeAtEnd(bar.Barline('final'))
    >>> len(m)
    2
    >>> m.clear()
    >>> len(m)
    0
    ```

    Does not remove any other attributes

    ```python
    >>> m.number
    3
    ```

Stream.cloneEmpty(*derivationMethod: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.cloneEmpty)
:   Create a Stream that is identical to this one except that the elements are empty
    and set derivation.

    ```python
    >>> p = stream.Part()
    >>> p.autoSort = False
    >>> p.id = 'hi'
    >>> p.insert(0, note.Note())
    >>> q = p.cloneEmpty(derivationMethod='demo')
    >>> q.autoSort
    False
    >>> q
    <music21.stream.Part hi>
    >>> q.derivation.origin is p
    True
    >>> q.derivation.method
    'demo'
    >>> len(q)
    0
    ```

Stream.containerInHierarchy(*el: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *setActiveSite=True*) → [Stream](#music21.stream.base.Stream "music21.stream.base.Stream") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.containerInHierarchy)
:   Returns the container in a hierarchy that this element belongs to.

    For instance, assume a Note (n) is in a Measure (m1) which is in a Part, in a Score (s1),
    and the Note is also in another hierarchy (say, a chordified version of a Score, s2).
    if s1.containerInHierarchy(n) is called, it will return m1,
    the Measure that contains the note.

    Unless setActiveSite is False, n’s activeSite will be set to m1, and
    its .offset will be the offset in m1.

    ```python
    >>> s1 = stream.Score(id='s1')
    >>> p1 = stream.Part()
    >>> m1 = stream.Measure(id='m1')
    >>> n = note.Note('D')
    >>> m1.append(n)
    >>> p1.append(m1)
    >>> s1.insert(0, p1)
    >>> s2 = stream.Stream(id='s2')
    >>> s2.append(n)
    >>> n.activeSite.id
    's2'
    >>> s1.containerInHierarchy(n).id
    'm1'
    >>> n.activeSite.id
    'm1'
    >>> n.activeSite = s2
    >>> s1.containerInHierarchy(n, setActiveSite=False).id
    'm1'
    >>> n.activeSite.id
    's2'
    ```

    If the element cannot be found in the hierarchy then None is returned.

    ```python
    >>> s3 = stream.Stream()
    >>> s3.containerInHierarchy(n) is None
    True
    ```

Stream.elementOffset(*element: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *returnSpecial: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [OffsetSpecial](moduleCommonEnums.html#music21.common.enums.OffsetSpecial "music21.common.enums.OffsetSpecial")[[source]](../_modules/music21/stream/base.html#Stream.elementOffset)

Stream.elementOffset(*element: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *returnSpecial: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")
:   Return the offset as an opFrac (float or Fraction) from the offsetMap.
    highly optimized for speed.

    ```python
    >>> m = stream.Measure(number=1)
    >>> m.append(note.Note('C'))
    >>> d = note.Note('D')
    >>> m.append(d)
    >>> m.elementOffset(d)
    1.0
    ```

    If returnSpecial is True then returns like OffsetSpecial.AT\_END are allowed.

    ```python
    >>> b = bar.Barline()
    >>> m.storeAtEnd(b)
    >>> m.elementOffset(b)
    2.0
    >>> m.elementOffset(b, returnSpecial=True)
    <OffsetSpecial.AT_END>
    ```

    Unlike element.getOffsetBySite(self), this method will NOT follow derivation chains
    and in fact will raise a sites.SitesException

    ```python
    >>> import copy
    >>> p = stream.Part(id='sPart')
    >>> p.insert(20, m)
    >>> m.getOffsetBySite(p)
    20.0
    >>> p.elementOffset(m)
    20.0
    ```

    ```python
    >>> mCopy = copy.deepcopy(m)
    >>> mCopy.number = 10
    >>> mCopy.derivation
    <Derivation of <music21.stream.Measure 10 offset=0.0> from
        <music21.stream.Measure 1 offset=20.0> via '__deepcopy__'>
    >>> mCopy.getOffsetBySite(p)
    20.0
    >>> p.elementOffset(mCopy)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object 0x... is not stored in
        stream <music21.stream.Part sPart>
    ```

    Performance note: because it will not follow derivation chains, and does
    not need to unwrap a weakref, this method
    should usually be about 3x faster than element.getOffsetBySite(self) –
    currently 600ns instead of 1.5 microseconds.

Stream.expandRepeats(*copySpanners: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.expandRepeats)
:   Expand this Stream with repeats. Nested repeats
    given with [`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat") objects, or
    repeats and sections designated with
    [`RepeatExpression`](moduleRepeat.html#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") objects, are all expanded.

    This method always returns a new Stream, with
    deepcopies of all contained elements at all levels.

    Uses the [`Expander`](moduleRepeat.html#music21.repeat.Expander "music21.repeat.Expander") object in the repeat module.

Stream.explode()[[source]](../_modules/music21/stream/base.html#Stream.explode)
:   Create a multiple Part representation from a single polyphonic Part.

    Currently just runs `voicesToParts()`
    but that will change as part explosion develops, and this
    method will use our best available quick method for part
    extraction.

Stream.extendDuration(*objClass*, *\**, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.extendDuration)
:   Given a Stream and an object class name, go through the Stream
    and find each instance of the desired object. The time between
    adjacent objects is then assigned to the duration of each object.
    The last duration of the last object is assigned to extend to the
    end of the Stream.

    If inPlace is True, this is done in-place; if inPlace is
    False, this returns a modified deep copy.

    ```python
    >>> stream1 = stream.Stream()
    >>> n = note.Note(type='quarter')
    >>> n.duration.quarterLength
    1.0
    >>> stream1.repeatInsert(n, [0, 10, 20, 30, 40])
    ```

    ```python
    >>> dyn = dynamics.Dynamic('ff')
    >>> stream1.insert(15, dyn)
    >>> stream1[-1].offset  # offset of last element
    40.0
    >>> stream1.duration.quarterLength  # total duration
    41.0
    >>> len(stream1)
    6
    ```

    ```python
    >>> stream2 = stream1.flatten().extendDuration(note.GeneralNote, inPlace=False)
    >>> len(stream2)
    6
    >>> stream2[0].duration.quarterLength
    10.0
    ```

    The Dynamic does not affect the second note:

    ```python
    >>> stream2[1].offset
    10.0
    >>> stream2[1].duration.quarterLength
    10.0
    ```

    ```python
    >>> stream2[-1].duration.quarterLength  # or extend to end of stream
    1.0
    >>> stream2.duration.quarterLength
    41.0
    >>> stream2[-1].offset
    40.0
    ```

Stream.extendTies(*ignoreRests=False*, *pitchAttr='nameWithOctave'*)[[source]](../_modules/music21/stream/base.html#Stream.extendTies)
:   Connect any adjacent pitch space values that are the
    same with a Tie. Adjacent pitches can be Chords, Notes, or Voices.

    If ignoreRests is True, rests that occur between events will not be
    considered in matching pitches.

    The pitchAttr determines the pitch attribute that is
    used for comparison. Any valid pitch attribute name can be used.

Stream.extractContext(*searchElement*, *before=4.0*, *after=4.0*, *maxBefore=None*, *maxAfter=None*)[[source]](../_modules/music21/stream/base.html#Stream.extractContext)
:   Extracts elements around the given element within (before)
    quarter notes and (after) quarter notes (default 4), and
    returns a new Stream.

    ```python
    >>> qn = note.Note(type='quarter')
    >>> qtrStream = stream.Stream()
    >>> qtrStream.repeatInsert(qn, [0, 1, 2, 3, 4, 5])
    >>> hn = note.Note(type='half')
    >>> hn.name = 'B-'
    >>> qtrStream.append(hn)
    >>> qtrStream.repeatInsert(qn, [8, 9, 10, 11])
    >>> hnStream = qtrStream.extractContext(hn, 1.0, 1.0)
    >>> hnStream.show('text')
    {5.0} <music21.note.Note C>
    {6.0} <music21.note.Note B->
    {8.0} <music21.note.Note C>
    ```

    * Changed in v7: forceOutputClass removed.

Stream.findConsecutiveNotes(*\**, *skipRests: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipChords: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *skipUnisons: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipOctaves: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipGaps: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *getOverlaps: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *noNone: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *\*\*keywords*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")][[source]](../_modules/music21/stream/base.html#Stream.findConsecutiveNotes)

Stream.findConsecutiveNotes(*\**, *skipRests: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipChords: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *skipUnisons: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipOctaves: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipGaps: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *getOverlaps: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *noNone: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *\*\*keywords*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Note](moduleNote.html#music21.note.Note "music21.note.Note")]

Stream.findConsecutiveNotes(*\**, *skipRests: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipChords: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipUnisons: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipOctaves: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipGaps: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *getOverlaps: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *noNone: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *\*\*keywords*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]
:   Returns a list of consecutive *pitched* Notes in a Stream.

    A single “None” is placed in the list
    at any point there is a discontinuity (such as if there is a
    rest between two pitches), unless the noNone parameter is True.

    How to determine consecutive pitches is a little tricky and there are many options:

    * The skipUnisons parameter uses the midi-note value (.ps) to determine unisons,
      so enharmonic transitions (F# -> Gb) are
      also skipped if skipUnisons is true. We believe that this is the most common usage.
    * However, because
      of this, you cannot completely be sure that the
      x.findConsecutiveNotes() - x.findConsecutiveNotes(skipUnisons=True)
      will give you the number of P1s in the piece, because there could be
      d2’s in there as well.

    See test.TestStream.testFindConsecutiveNotes() for usage details.

    This example is adapted from the tutorials/Examples page.

    ```python
    >>> s = converter.parse("tinynotation: 4/4 f8 d'8~ d'8 d'8~ d'4 b'-8 a'-8 a-8")
    >>> m = s.measure(1)
    >>> m.findConsecutiveNotes(skipUnisons=True, skipOctaves=True,
    ...                        skipRests=True, noNone=True)
    [<music21.note.Note F>, <music21.note.Note D>,
     <music21.note.Note B->, <music21.note.Note A->]
    ```

    ```python
    >>> m.findConsecutiveNotes(skipUnisons=False,
    ...                        skipRests=True, noNone=True)
    [<music21.note.Note F>, <music21.note.Note D>,
     <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note D>,
     <music21.note.Note B->, <music21.note.Note A->]
    ```

    * Changed in v7:

      + now finds notes in Voices without requiring getOverlaps=True
        and iterates over Parts rather than flattening.
      + If noNone=False, inserts None
        when backing up to scan a subsequent voice or part.
    * Changed in v8: all parameters are keyword only.

Stream.findGaps()[[source]](../_modules/music21/stream/base.html#Stream.findGaps)
:   Returns either (1) a Stream containing empty Music21Objects
    whose offsets and durations
    are the length of gaps in the Stream
    or (2) None if there are no gaps.

    N.B. there may be gaps in the flattened representation of the stream
    but not in the unflattened. Hence why “isSequence” calls self.flatten().isGapless

    ```python
    >>> s = stream.Stream()
    >>> s.insert(1.0, note.Note('E', type='half'))
    >>> s.insert(5.0, note.Note('F', type='whole'))
    >>> s.storeAtEnd(bar.Barline('final'))
    >>> gapStream = s.findGaps()
    >>> gapStream.show('text', addEndTimes=True)
    {0.0 - 1.0} <music21.note.Rest quarter>
    {3.0 - 5.0} <music21.note.Rest half>
    ```

    Returns None if not gaps:

    ```python
    >>> s2 = stream.Stream()
    >>> s2.append(note.Note('G'))
    >>> s2.findGaps() is None
    True
    ```

    * Changed in v7: gapStream is filled with rests instead of Music21Objects

Stream.first() → M21ObjType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.first)
:   Return the first element of a Stream. (Added for compatibility with StreamIterator)
    Or None if the Stream is empty.

    Unlike s.iter().first(), which is a significant performance gain, s.first() is the
    same speed as s[0], except for not raising an IndexError.

    ```python
    >>> nC = note.Note('C4')
    >>> nD = note.Note('D4')
    >>> s = stream.Stream()
    >>> s.append([nC, nD])
    >>> s.first()
    <music21.note.Note C>
    ```

    ```python
    >>> empty = stream.Stream()
    >>> print(empty.first())
    None
    ```

    * New in v7.

Stream.flatten(*retainContainers=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.flatten)
:   A very important method that returns a new Stream
    that has all sub-containers “flattened” within it,
    that is, it returns a new Stream where no elements nest within
    other elements. (Prior to v7 this was the property .flat)

    Here is a simple example of the usefulness of .flatten(). We
    will create a Score with two Parts in it, each with two Notes:

    ```python
    >>> sc = stream.Score()
    >>> p1 = stream.Part()
    >>> p1.id = 'part1'
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> p1.append(n1)
    >>> p1.append(n2)
    ```

    ```python
    >>> p2 = stream.Part()
    >>> p2.id = 'part2'
    >>> n3 = note.Note('E4')
    >>> n4 = note.Note('F4')
    >>> p2.append(n3)
    >>> p2.append(n4)
    ```

    ```python
    >>> sc.insert(0, p1)
    >>> sc.insert(0, p2)
    ```

    When we look at sc, we will see only the two parts:

    ```python
    >>> sc.elements
    (<music21.stream.Part part1>, <music21.stream.Part part2>)
    ```

    We can get at the notes by using the indices of the
    stream to get the parts and then looking at the .elements
    there:

    ```python
    >>> sc[0].elements
    (<music21.note.Note C>, <music21.note.Note D>)
    ```

    ```python
    >>> sc.getElementById('part2').elements
    (<music21.note.Note E>, <music21.note.Note F>)
    ```

    If, however, we want to get all the notes, storing their
    offsets related to the beginning of the containing stream,
    one way
    is via calling .flatten() on sc and looking at the elements
    there:

    ```python
    >>> sc.flatten().elements
    (<music21.note.Note C>, <music21.note.Note E>,
     <music21.note.Note D>, <music21.note.Note F>)
    ```

    Flattening a stream is a great way to get at all the notes in
    a larger piece. For instance if we load a four-part
    Bach chorale into music21 from the integrated corpus, it
    will appear at first that there are no notes in the piece:

    ```python
    >>> bwv66 = corpus.parse('bach/bwv66.6')
    >>> len(bwv66.notes)
    0
    ```

    This is because all the notes in the piece lie within `music21.stream.Measure`
    objects and those measures lie within `music21.stream.Part`
    objects. It’d be a pain to navigate all the way through all those
    objects just to count notes. Fortunately we can get a Stream of
    all the notes in the piece with .flatten().notes and then use the
    length of that Stream to count notes:

    ```python
    >>> bwv66flat = bwv66.flatten()
    >>> len(bwv66flat.notes)
    165
    ```

    When, as is commonly the case, we want to find all the notes,
    but do not care to have offsets related to the origin of the stream,
    then .recurse() is a more efficient way of working:

    ```python
    >>> len(bwv66.recurse().notes)
    165
    ```

    If retainContainers=True then a “semiFlat” version of the stream
    is returned where Streams are also included in the output stream.
    (Prior to v7 this was the property semiFlat)

    In general, you will not need to use this because .recurse() is
    more efficient and does not lead to problems of the same
    object appearing in the hierarchy more than once.

    ```python
    >>> n1 = note.Note('C5')
    >>> m1 = stream.Measure([n1], number='1a')
    >>> p1 = stream.Part([m1])
    >>> p1.id = 'part1'
    ```

    ```python
    >>> n2 = note.Note('D5')
    >>> m2 = stream.Measure([n2], number='1b')
    >>> p2 = stream.Part([m2])
    >>> p2.id = 'part2'
    ```

    ```python
    >>> sc = stream.Score([p1, p2])
    ```

    sf will be the “semi-flattened” version of the score.

    ```python
    >>> sf = sc.flatten(retainContainers=True)
    >>> sf.elements
    (<music21.stream.Part part1>,
     <music21.stream.Measure 1a offset=0.0>,
     <music21.stream.Part part2>,
     <music21.stream.Measure 1b offset=0.0>,
     <music21.note.Note C>,
     <music21.note.Note D>)
    >>> sf[0]
    <music21.stream.Part part1>
    ```

    Notice that these all return the same object:

    ```python
    >>> sf[0][0][0]
    <music21.note.Note C>
    >>> sf[1][0]
    <music21.note.Note C>
    >>> sf[4]
    <music21.note.Note C>
    ```

    Unless it is important to iterate in order from
    front of score to back of the score, you are generally better off using recurse
    instead of .flatten(retainContainers=True), with .getOffsetInHierarchy()
    to figure out where in the score each element lies.

    For instance, this is how we can iterate using recurse():

    ```python
    >>> for el in sc.recurse():
    ...     print(el)
    <music21.stream.Part part1>
    <music21.stream.Measure 1a offset=0.0>
    <music21.note.Note C>
    <music21.stream.Part part2>
    <music21.stream.Measure 1b offset=0.0>
    <music21.note.Note D>
    ```

    If you look back to our simple example of four notes above,
    you can see that the E (the first note in part2) comes before the D
    (the second note of part1). This is because the flat stream
    is automatically sorted like all streams are by default. The
    next example shows how to change this behavior.

    ```python
    >>> s = stream.Stream()
    >>> s.autoSort = False
    >>> s.repeatInsert(note.Note('C#'), [0, 2, 4])
    >>> s.repeatInsert(note.Note('D-'), [1, 3, 5])
    >>> s.isSorted
    False
    ```

    ```python
    >>> g = ''
    >>> for myElement in s:
    ...    g += f'{myElement.offset}: {myElement.name}; '
    >>> g
    '0.0: C#; 2.0: C#; 4.0: C#; 1.0: D-; 3.0: D-; 5.0: D-; '
    ```

    ```python
    >>> y = s.sorted()
    >>> y.isSorted
    True
    ```

    ```python
    >>> g = ''
    >>> for myElement in y:
    ...    g += f'{myElement.offset}: {myElement.name}; '
    >>> g
    '0.0: C#; 1.0: D-; 2.0: C#; 3.0: D-; 4.0: C#; 5.0: D-; '
    ```

    ```python
    >>> q = stream.Stream()
    >>> for i in range(5):
    ...     p = stream.Stream()
    ...     p.repeatInsert(base.Music21Object(), [0, 1, 2, 3, 4])
    ...     q.insert(i * 10, p)
    ...
    ```

    ```python
    >>> len(q)
    5
    ```

    ```python
    >>> qf = q.flatten()
    >>> len(qf)
    25
    >>> qf[24].offset
    44.0
    ```

    Note that combining .flatten(retainContainers=True) with pure .flatten()
    can lead to unstable Streams where the same object appears more than once,
    in violation of a music21 lookup rule.

    ```python
    >>> sc.flatten(retainContainers=True).flatten().elements
    (<music21.note.Note C>,
     <music21.note.Note C>,
     <music21.note.Note C>,
     <music21.note.Note D>,
     <music21.note.Note D>,
     <music21.note.Note D>)
    ```

    Changed in v.10 - Derivation method names changed to flatten and flatten\_retain\_containers

Stream.flattenUnnecessaryVoices(*\**, *force=False*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.flattenUnnecessaryVoices)
:   If this Stream defines one or more internal voices, do the following:

    * If there is more than one voice, and a voice has no elements,
      remove that voice.
    * If there is only one voice left that has elements, place those
      elements in the parent Stream.
    * If force is True, even if there is more than one Voice left,
      all voices will be flattened.

    This leaves a stream where all voices appear when another appears in
    the same measure.

    More demonstrations of recurse=True:

    ```python
    >>> s = stream.Stream(note.Note())
    >>> s.insert(0, note.Note())
    >>> s.insert(0, note.Note())
    >>> s.makeVoices(inPlace=True)
    >>> len(s.voices)
    3
    ```

    ```python
    >>> s.remove(s.voices[1].notes[0], recurse=True)
    >>> s.remove(s.voices[2].notes[0], recurse=True)
    >>> voicesFlattened = s.flattenUnnecessaryVoices()
    >>> len(voicesFlattened.voices)
    0
    ```

    * Changed in v5: inPlace is default False and a keyword only arg.

Stream.getElementAfterElement(*element*, *classList=None*)[[source]](../_modules/music21/stream/base.html#Stream.getElementAfterElement)
:   Given an element, get the next element. If classList is specified,
    check to make sure that the element is an instance of the class list

    ```python
    >>> st1 = stream.Stream()
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> r3 = note.Rest()
    >>> st1.append([n1, n2, r3])
    >>> t2 = st1.getElementAfterElement(n1)
    >>> t2 is n2
    True
    >>> t3 = st1.getElementAfterElement(t2)
    >>> t3 is r3
    True
    >>> t4 = st1.getElementAfterElement(t3)
    >>> t4
    ```

    ```python
    >>> t5 = st1.getElementAfterElement(n1, [note.Rest])
    >>> t5
    <music21.note.Rest quarter>
    >>> t5 is r3
    True
    >>> t6 = st1.getElementAfterElement(n1, [note.Rest, note.Note])
    >>> t6 is n2
    True
    ```

    ```python
    >>> t7 = st1.getElementAfterElement(r3)
    >>> t7 is None
    True
    ```

    If the element is not in the stream, it will raise a StreamException:

    ```python
    >>> st1.getElementAfterElement(note.Note('C#'))
    Traceback (most recent call last):
    music21.exceptions21.StreamException:
        cannot find object (<music21.note.Note C#>) in Stream
    ```

Stream.getElementAtOrBefore(*offset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *classList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[M21ObjType] | [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *\_beforeNotAt: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.getElementAtOrBefore)
:   Given an offset, find the element at this offset,
    or with the offset less than and nearest to.

    Return one element or None if no elements are at or preceded by this
    offset.

    If the classList parameter is used, it should be a
    list of class names or strings, and only objects that
    are instances of
    these classes or subclasses of these classes will be returned.

    ```python
    >>> stream1 = stream.Stream()
    >>> x = note.Note('D4')
    >>> x.id = 'x'
    >>> y = note.Note('E4')
    >>> y.id = 'y'
    >>> z = note.Rest()
    >>> z.id = 'z'
    ```

    ```python
    >>> stream1.insert(20, x)
    >>> stream1.insert(10, y)
    >>> stream1.insert( 0, z)
    ```

    ```python
    >>> b = stream1.getElementAtOrBefore(21)
    >>> b.offset, b.id
    (20.0, 'x')
    ```

    ```python
    >>> b = stream1.getElementAtOrBefore(19)
    >>> b.offset, b.id
    (10.0, 'y')
    ```

    ```python
    >>> b = stream1.getElementAtOrBefore(0)
    >>> b.offset, b.id
    (0.0, 'z')
    >>> b = stream1.getElementAtOrBefore(0.1)
    >>> b.offset, b.id
    (0.0, 'z')
    ```

    You can give a list of acceptable classes to return, and non-matching
    elements will be ignored

    ```python
    >>> c = stream1.getElementAtOrBefore(100, [clef.TrebleClef, note.Rest])
    >>> c.offset, c.id
    (0.0, 'z')
    ```

    Getting an object via getElementAtOrBefore sets the activeSite
    for that object to the Stream, and thus sets its offset

    ```python
    >>> stream2 = stream.Stream()
    >>> stream2.insert(100.5, x)
    >>> x.offset
    100.5
    >>> d = stream1.getElementAtOrBefore(20)
    >>> d is x
    True
    >>> x.activeSite is stream1
    True
    >>> x.offset
    20.0
    ```

    If no element is before the offset, returns None

    ```python
    >>> s = stream.Stream()
    >>> s.insert(10, note.Note('E'))
    >>> print(s.getElementAtOrBefore(9))
    None
    ```

    The sort order of returned items is the reverse
    of the normal sort order, so that, for instance,
    if there’s a clef and a note at offset 20,
    getting the object before offset 21 will give
    you the note, and not the clef, since clefs
    sort before notes:

    ```python
    >>> clef1 = clef.BassClef()
    >>> stream1.insert(20, clef1)
    >>> e = stream1.getElementAtOrBefore(21)
    >>> e
    <music21.note.Note D>
    ```

Stream.getElementBeforeOffset(*offset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *classList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[M21ObjType] | [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.getElementBeforeOffset)
:   Get element before (and not at) a provided offset.

    If the classList parameter is used, it should be a
    list of class names or strings, and only objects that
    are instances of
    these classes or subclasses of these classes will be returned.

    ```python
    >>> stream1 = stream.Stream()
    >>> x = note.Note('D4')
    >>> x.id = 'x'
    >>> y = note.Note('E4')
    >>> y.id = 'y'
    >>> z = note.Rest()
    >>> z.id = 'z'
    >>> stream1.insert(20, x)
    >>> stream1.insert(10, y)
    >>> stream1.insert( 0, z)
    ```

    ```python
    >>> b = stream1.getElementBeforeOffset(21)
    >>> b.offset, b.id
    (20.0, 'x')
    >>> b = stream1.getElementBeforeOffset(20)
    >>> b.offset, b.id
    (10.0, 'y')
    ```

    ```python
    >>> b = stream1.getElementBeforeOffset(10)
    >>> b.offset, b.id
    (0.0, 'z')
    ```

    ```python
    >>> b = stream1.getElementBeforeOffset(0)
    >>> b is None
    True
    >>> b = stream1.getElementBeforeOffset(0.1)
    >>> b.offset, b.id
    (0.0, 'z')
    ```

    ```python
    >>> w = note.Note('F4')
    >>> w.id = 'w'
    >>> stream1.insert( 0, w)
    ```

    This should get w because it was inserted last.

    ```python
    >>> b = stream1.getElementBeforeOffset(0.1)
    >>> b.offset, b.id
    (0.0, 'w')
    ```

    But if we give it a lower priority than z then z will appear first.

    ```python
    >>> w.priority = z.priority - 1
    >>> b = stream1.getElementBeforeOffset(0.1)
    >>> b.offset, b.id
    (0.0, 'z')
    ```

Stream.getElementById(*elementId*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.getElementById)
:   Returns the first encountered element for a given id. Return None
    if no match. Note: this uses the id attribute stored on elements,
    which may not be the same as id(e).

    ```python
    >>> a = stream.Stream()
    >>> ew = note.Note()
    >>> a.insert(0, ew)
    >>> a[0].id = 'green'
    >>> None == a.getElementById(3)
    True
    >>> a.getElementById('green').id
    'green'
    >>> a.getElementById('Green').id  # case does not matter
    'green'
    ```

    Getting an element by getElementById changes its activeSite

    ```python
    >>> b = stream.Stream()
    >>> b.append(ew)
    >>> ew.activeSite is b
    True
    >>> ew2 = a.getElementById('green')
    >>> ew2 is ew
    True
    >>> ew2.activeSite is a
    True
    >>> ew.activeSite is a
    True
    ```

    * Changed in v7: remove classFilter.

Stream.getElementsByClass(*classFilterList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[M21ObjType][[source]](../_modules/music21/stream/base.html#Stream.getElementsByClass)

Stream.getElementsByClass(*classFilterList: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[ChangedM21ObjType]*) → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[ChangedM21ObjType]

Stream.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[ChangedM21ObjType]]*) → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[M21ObjType]
:   Return a StreamIterator that will iterate over Elements that match one
    or more classes in the classFilterList. A single class
    can also be used for the classFilterList parameter instead of a List.

    ```python
    >>> a = stream.Score()
    >>> a.repeatInsert(note.Rest(), list(range(10)))
    >>> for x in range(4):
    ...     n = note.Note('G#')
    ...     n.offset = x * 3
    ...     a.insert(n)
    >>> found = a.getElementsByClass(note.Note)
    >>> found
    <music21.stream.iterator.StreamIterator for Score:0x118d20710 @:0>
    ```

    ```python
    >>> len(found)
    4
    >>> found[0].pitch.accidental.name
    'sharp'
    ```

    ```python
    >>> foundStream = found.stream()
    >>> isinstance(foundStream, stream.Score)
    True
    ```

    Notice that we do not find elements that are in
    sub-streams of the main Stream. We’ll add 15 more rests
    in a sub-stream, and they won’t be found:

    ```python
    >>> b = stream.Stream()
    >>> b.repeatInsert(note.Rest(), list(range(15)))
    >>> a.insert(b)
    >>> found = a.getElementsByClass(note.Rest)
    >>> len(found)
    10
    ```

    To find them either (1) use .flatten() to get at everything:

    ```python
    >>> found = a.flatten().getElementsByClass(note.Rest)
    >>> len(found)
    25
    ```

    Or, (2) recurse over the main stream and call .getElementsByClass
    on each one. Notice that the first subStream is actually the outermost
    Stream:

    ```python
    >>> totalFound = 0
    >>> for subStream in a.recurse(streamsOnly=True, includeSelf=True):
    ...     found = subStream.getElementsByClass(note.Rest)
    ...     totalFound += len(found)
    >>> totalFound
    25
    ```

    The class name of the Stream created is usually the same as the original:

    ```python
    >>> found = a.getElementsByClass(note.Note).stream()
    >>> found.__class__.__name__
    'Score'
    ```

    An exception is if returnStreamSubClass is False, which makes the method
    return a generic Stream:

    ```python
    >>> found = a.getElementsByClass(note.Rest).stream(returnStreamSubClass=False)
    >>> found.__class__.__name__
    'Stream'
    ```

    Make a list from a StreamIterator:

    ```python
    >>> foundList = list(a.recurse().getElementsByClass(note.Rest))
    >>> len(foundList)
    25
    ```

Stream.getElementsByGroup(*groupFilterList*) → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[[source]](../_modules/music21/stream/base.html#Stream.getElementsByGroup)
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
    >>> tboneSubStream = s1.getElementsByGroup('trombone')
    >>> for thisNote in tboneSubStream:
    ...     print(thisNote.name)
    C
    D
    >>> tubaSubStream = s1.getElementsByGroup('tuba')
    >>> for thisNote in tubaSubStream:
    ...     print(thisNote.name)
    D
    E
    ```

Stream.getElementsByOffset(*offsetStart*, *offsetEnd=None*, *\**, *includeEndBoundary=True*, *mustFinishInSpan=False*, *mustBeginInSpan=True*, *includeElementsThatEndAtStart=True*, *classList=None*) → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[[source]](../_modules/music21/stream/base.html#Stream.getElementsByOffset)
:   Returns a StreamIterator containing all Music21Objects that
    are found at a certain offset or within a certain
    offset time range (given the offsetStart and (optional) offsetEnd values).

    There are several attributes that govern how this range is
    determined:

    If mustFinishInSpan is True then an event that begins
    between offsetStart and offsetEnd but which ends after offsetEnd
    will not be included. The default is False.

    For instance, a half note at offset 2.0 will be found in
    getElementsByOffset(1.5, 2.5) or getElementsByOffset(1.5, 2.5,
    mustFinishInSpan=False) but not by getElementsByOffset(1.5, 2.5,
    mustFinishInSpan=True).

    The includeEndBoundary option determines if an element
    begun just at the offsetEnd should be included. For instance,
    the half note at offset 2.0 above would be found by
    getElementsByOffset(0, 2.0) or by getElementsByOffset(0, 2.0,
    includeEndBoundary=True) but not by getElementsByOffset(0, 2.0,
    includeEndBoundary=False).

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
    mustBeginInSpan=True) but it would be found by
    getElementsByOffset(3.0, 3.5, mustBeginInSpan=False)

    Setting includeElementsThatEndAtStart to False is useful for zeroLength
    searches that set mustBeginInSpan == False to not catch notes that were
    playing before the search but that end just before the end of the search type.
    This setting is *ignored* for zero-length searches.
    See the code for allPlayingWhileSounding for a demonstration.

    This chart and the examples below demonstrate the various
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
    >>> out1 = st1.getElementsByOffset(2)
    >>> len(out1)
    1
    >>> out1[0].step
    'D'
    ```

    ```python
    >>> out2 = st1.getElementsByOffset(1, 3)
    >>> len(out2)
    1
    >>> out2[0].step
    'D'
    >>> out3 = st1.getElementsByOffset(1, 3, mustFinishInSpan=True)
    >>> len(out3)
    0
    >>> out4 = st1.getElementsByOffset(1, 2)
    >>> len(out4)
    1
    >>> out4[0].step
    'D'
    >>> out5 = st1.getElementsByOffset(1, 2, includeEndBoundary=False)
    >>> len(out5)
    0
    >>> out6 = st1.getElementsByOffset(1, 2, includeEndBoundary=False, mustBeginInSpan=False)
    >>> len(out6)
    1
    >>> out6[0].step
    'C'
    >>> out7 = st1.getElementsByOffset(1, 3, mustBeginInSpan=False)
    >>> len(out7)
    2
    >>> [el.step for el in out7]
    ['C', 'D']
    ```

    Note, that elements that end at the start offset are included if mustBeginInSpan is False

    ```python
    >>> out8 = st1.getElementsByOffset(2, 4, mustBeginInSpan=False)
    >>> len(out8)
    2
    >>> [el.step for el in out8]
    ['C', 'D']
    ```

    To change this behavior set includeElementsThatEndAtStart=False

    ```python
    >>> out9 = st1.getElementsByOffset(2, 4,
    ...                     mustBeginInSpan=False, includeElementsThatEndAtStart=False)
    >>> len(out9)
    1
    >>> [el.step for el in out9]
    ['D']
    ```

    Note how zeroLengthSearches implicitly set includeElementsThatEndAtStart=False.
    These two are the same:

    ```python
    >>> out1 = st1.getElementsByOffset(2, mustBeginInSpan=False)
    >>> out2 = st1.getElementsByOffset(2, 2, mustBeginInSpan=False)
    >>> len(out1) == len(out2) == 1
    True
    >>> out1[0] is out2[0] is n2
    True
    ```

    But this is different:

    ```python
    >>> out3 = st1.getElementsByOffset(2, 2.1, mustBeginInSpan=False)
    >>> len(out3)
    2
    >>> out3[0] is n0
    True
    ```

    Explicitly setting includeElementsThatEndAtStart=False does not get the
    first note:

    ```python
    >>> out4 = st1.getElementsByOffset(2, 2.1, mustBeginInSpan=False,
    ...                                includeElementsThatEndAtStart=False)
    >>> len(out4)
    1
    >>> out4[0] is n2
    True
    ```

    Testing multiple zero-length elements with mustBeginInSpan:

    ```python
    >>> tc = clef.TrebleClef()
    >>> ts = meter.TimeSignature('4/4')
    >>> ks = key.KeySignature(2)
    >>> s = stream.Stream()
    >>> s.insert(0.0, tc)
    >>> s.insert(0.0, ts)
    >>> s.insert(0.0, ks)
    >>> len(s.getElementsByOffset(0.0, mustBeginInSpan=True))
    3
    >>> len(s.getElementsByOffset(0.0, mustBeginInSpan=False))
    3
    ```

Stream.getElementsNotOfClass(*classFilterList*) → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[[source]](../_modules/music21/stream/base.html#Stream.getElementsNotOfClass)
:   Return a list of all Elements that do not
    match the one or more classes in the classFilterList.

    In lieu of a list, a single class can be used as the classFilterList parameter.

    ```python
    >>> a = stream.Stream()
    >>> a.repeatInsert(note.Rest(), list(range(10)))
    >>> for x in range(4):
    ...     n = note.Note('G#')
    ...     n.offset = x * 3
    ...     a.insert(n)
    >>> found = a.getElementsNotOfClass(note.Note)
    >>> len(found)
    10
    ```

    ```python
    >>> b = stream.Stream()
    >>> b.repeatInsert(note.Rest(), list(range(15)))
    >>> a.insert(b)
    ```

    Here, it gets elements from within a stream
    this probably should not do this, as it is one layer lower

    ```python
    >>> found = a.flatten().getElementsNotOfClass(note.Rest)
    >>> len(found)
    4
    >>> found = a.flatten().getElementsNotOfClass(note.Note)
    >>> len(found)
    25
    ```

Stream.getInstrument(*\**, *searchActiveSite=True*, *returnDefault=True*, *recurse=False*) → [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.getInstrument)
:   Return the first Instrument found in this Stream, or None.

    ```python
    >>> s = stream.Score()
    >>> p1 = stream.Part()
    >>> p1.insert(instrument.Violin())
    >>> m1p1 = stream.Measure()
    >>> m1p1.append(note.Note('g'))
    >>> p1.append(m1p1)
    ```

    ```python
    >>> p2 = stream.Part()
    >>> p2.insert(instrument.Viola())
    >>> m1p2 = stream.Measure()
    >>> m1p2.append(note.Note('f#'))
    >>> p2.append(m1p2)
    ```

    ```python
    >>> s.insert(0, p1)
    >>> s.insert(0, p2)
    >>> p1.getInstrument(returnDefault=False).instrumentName
    'Violin'
    >>> p2.getInstrument(returnDefault=False).instrumentName
    'Viola'
    ```

    * Changed in v7: added recurse (default False)

Stream.getInstruments(*\**, *searchActiveSite=True*, *returnDefault=True*, *recurse=True*) → [Stream](#music21.stream.base.Stream "music21.stream.base.Stream")[[Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")][[source]](../_modules/music21/stream/base.html#Stream.getInstruments)
:   Search this stream (and, by default, its subStreams) or activeSite streams for
    [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") objects, and return a new stream
    containing them.

    ```python
    >>> m1 = stream.Measure([meter.TimeSignature('4/4'),
    ...                      instrument.Clarinet(),
    ...                      note.Note('C5', type='whole')])
    >>> m2 = stream.Measure([instrument.BassClarinet(),
    ...                      note.Note('C3', type='whole')])
    >>> p = stream.Part([m1, m2])
    >>> instruments = p.getInstruments()
    >>> instruments
    <music21.stream.Part 0x112ac26e0>
    ```

    ```python
    >>> instruments.show('text')
    {0.0} <music21.instrument.Clarinet 'Clarinet'>
    {4.0} <music21.instrument.BassClarinet 'Bass clarinet'>
    ```

    If there are no instruments, returns a Stream containing a single default Instrument,
    unless returnDefault is False.

    ```python
    >>> p = stream.Part()
    >>> m = stream.Measure([note.Note()])
    >>> p.insert(0, m)
    >>> instrumentStream = p.getInstruments(returnDefault=True)
    >>> defaultInst = instrumentStream.first()
    >>> defaultInst
    <music21.instrument.Instrument ': '>
    ```

    Insert an instrument into the Part (not the Measure):

    ```python
    >>> p.insert(0, instrument.Koto())
    ```

    Searching the measure will find this instrument only if the measure’s activeSite is
    searched, as it is by default:

    ```python
    >>> searchedActiveSite = p.measure(1).getInstruments()
    >>> searchedActiveSite.first()
    <music21.instrument.Koto 'Koto'>
    ```

    ```python
    >>> searchedNaive = p.measure(1).getInstruments(searchActiveSite=False, returnDefault=False)
    >>> len(searchedNaive)
    0
    ```

    * Changed in v8: recurse is True by default.

Stream.getOverlaps()[[source]](../_modules/music21/stream/base.html#Stream.getOverlaps)
:   Find any elements that overlap. Overlapping might include elements
    that have zero-length duration simultaneous.

    This method returns a dictionary, where keys
    are the start time of the first overlap and
    value are a list of all objects included in
    that overlap group.

    This example demonstrates that end-joining overlaps do not count.

    ```python
    >>> a = stream.Stream()
    >>> for x in range(4):
    ...     n = note.Note('G#')
    ...     n.duration = duration.Duration('quarter')
    ...     n.offset = x * 1
    ...     a.insert(n)
    ...
    >>> d = a.getOverlaps()
    >>> len(d)
    0
    ```

    Notes starting at the same time overlap:

    ```python
    >>> a = stream.Stream()
    >>> for x in [0, 0, 0, 0, 13, 13, 13]:
    ...     n = note.Note('G#')
    ...     n.duration = duration.Duration('half')
    ...     n.offset = x
    ...     a.insert(n)
    ...
    >>> d = a.getOverlaps()
    >>> len(d[0])
    4
    >>> len(d[13])
    3
    >>> a = stream.Stream()
    >>> for x in [0, 0, 0, 0, 3, 3, 3]:
    ...     n = note.Note('G#')
    ...     n.duration = duration.Duration('whole')
    ...     n.offset = x
    ...     a.insert(n)
    ...
    ```

    Default is to not include coincident boundaries

    ```python
    >>> d = a.getOverlaps()
    >>> len(d[0])
    7
    ```

Stream.getTimeSignatures(*\**, *searchContext=True*, *returnDefault=True*, *recurse=True*, *sortByCreationTime=True*)[[source]](../_modules/music21/stream/base.html#Stream.getTimeSignatures)
:   Collect all `TimeSignature` objects in this stream.
    If no TimeSignature objects are defined, get a default (4/4 or whatever
    is defined in the defaults.py file).

    ```python
    >>> s = stream.Part(id='changingMeter')
    >>> s.repeatInsert(note.Note('C#'), list(range(11)))
    ```

    ```python
    >>> threeFour = meter.TimeSignature('3/4')
    >>> s.insert(0.0, threeFour)
    >>> twoTwo = meter.TimeSignature('2/2')
    >>> s.insert(3.0, twoTwo)
    >>> tsStream = s.getTimeSignatures()
    >>> tsStream.derivation.method
    'getTimeSignatures'
    ```

    ```python
    >>> tsStream
    <music21.stream.Part changingMeter>
    >>> tsStream.show('text')
    {0.0} <music21.meter.TimeSignature 3/4>
    {3.0} <music21.meter.TimeSignature 2/2>
    ```

    The contents of the time signature stream are the original, not copies
    of the original:

    ```python
    >>> tsStream[0] is threeFour
    True
    ```

    Many time signatures are found within measures, so this method will find
    them also and place them at the appropriate point within the overall Stream.

    N.B. if there are different time signatures for different parts, this method
    will not distinguish which parts use which time signatures.

    ```python
    >>> sm = s.makeMeasures()
    >>> sm.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C#>
        {1.0} <music21.note.Note C#>
        {2.0} <music21.note.Note C#>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.meter.TimeSignature 2/2>
        {0.0} <music21.note.Note C#>
        {1.0} <music21.note.Note C#>
        {2.0} <music21.note.Note C#>
        {3.0} <music21.note.Note C#>
    {7.0} <music21.stream.Measure 3 offset=7.0>
        {0.0} <music21.note.Note C#>
        {1.0} <music21.note.Note C#>
        {2.0} <music21.note.Note C#>
        {3.0} <music21.note.Note C#>
        {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> tsStream2 = sm.getTimeSignatures()
    >>> tsStream2.show('text')
    {0.0} <music21.meter.TimeSignature 3/4>
    {3.0} <music21.meter.TimeSignature 2/2>
    ```

    If you do not want this recursion, set recurse=False

    ```python
    >>> len(sm.getTimeSignatures(recurse=False, returnDefault=False))
    0
    ```

    We set returnDefault=False here, because otherwise a default time signature
    of 4/4 is returned:

    ```python
    >>> sm.getTimeSignatures(recurse=False)[0]
    <music21.meter.TimeSignature 4/4>
    ```

    Note that a measure without any time signature can still find a context TimeSignature
    with this method so long as searchContext is True (as by default):

    ```python
    >>> m3 = sm.measure(3)
    >>> m3.show('text')
    {0.0} <music21.note.Note C#>
    {1.0} <music21.note.Note C#>
    {2.0} <music21.note.Note C#>
    {3.0} <music21.note.Note C#>
    {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> m3.getTimeSignatures()[0]
    <music21.meter.TimeSignature 2/2>
    ```

    The oldest context for the measure will be used unless sortByCreationTime is False, in which
    case the typical order of context searching will be used.

    ```python
    >>> p2 = stream.Part()
    >>> p2.insert(0, meter.TimeSignature('1/1'))
    >>> p2.append(m3)
    >>> m3.getTimeSignatures()[0]
    <music21.meter.TimeSignature 2/2>
    ```

    If searchContext is False then the default will be returned (which is somewhat
    acceptable here, since there are 4 quarter notes in the measure) but not generally correct:

    ```python
    >>> m3.getTimeSignatures(searchContext=False)[0]
    <music21.meter.TimeSignature 4/4>
    ```

    * Changed in v8: time signatures within recursed streams are found by default.
      Added recurse. Removed option for recurse=False and still getting the
      first time signature in the first measure. This was wholly inconsistent.

Stream.hasElement(*obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.hasElement)
:   DEPRECATED: just use el in stream instead of stream.hasElement(el)

    Return True if an element, provided as an argument, is contained in
    this Stream.

Stream.hasElementOfClass(*className*, *forceFlat=False*)[[source]](../_modules/music21/stream/base.html#Stream.hasElementOfClass)
:   Given a single class name as string,
    return True or False if an element with the
    specified class is found.

    Only a single class name can be given.

    ```python
    >>> s = stream.Stream()
    >>> s.append(meter.TimeSignature('5/8'))
    >>> s.append(note.Note('d-2'))
    >>> s.insert(dynamics.Dynamic('fff'))
    >>> s.hasElementOfClass(meter.TimeSignature)
    True
    >>> s.hasElementOfClass('Measure')
    False
    ```

    To be deprecated in v10 – to be removed in v11, use:

    ```python
    >>> bool(s.getElementsByClass(meter.TimeSignature))
    True
    >>> bool(s.getElementsByClass(stream.Measure))
    False
    ```

    forceFlat does nothing, while getElementsByClass can be done on recurse()

Stream.hasMeasures()[[source]](../_modules/music21/stream/base.html#Stream.hasMeasures)
:   Return a boolean value showing if this Stream contains Measures.

    ```python
    >>> p = stream.Part()
    >>> p.repeatAppend(note.Note(), 8)
    >>> p.hasMeasures()
    False
    >>> p.makeMeasures(inPlace=True)
    >>> len(p.getElementsByClass(stream.Measure))
    2
    >>> p.hasMeasures()
    True
    ```

    Only returns True if the immediate Stream has measures, not if there are nested measures:

    ```python
    >>> sc = stream.Score()
    >>> sc.append(p)
    >>> sc.hasMeasures()
    False
    ```

Stream.hasPartLikeStreams() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.hasPartLikeStreams)
:   Return a boolean value showing if this Stream contains any Parts,
    or Part-like sub-Streams.

    Part-like sub-streams are Streams that contain Measures or Notes.
    And where no sub-stream begins at an offset besides zero.

    ```python
    >>> s = stream.Score()
    >>> s.hasPartLikeStreams()
    False
    >>> p1 = stream.Part()
    >>> p1.repeatAppend(note.Note(), 8)
    >>> s.insert(0, p1)
    >>> s.hasPartLikeStreams()
    True
    ```

    A stream that has a measure in it is not a part-like stream.

    ```python
    >>> s = stream.Score()
    >>> m1 = stream.Measure()
    >>> m1.repeatAppend(note.Note(), 4)
    >>> s.append(m1)
    >>> s.hasPartLikeStreams()
    False
    ```

    A stream with a single generic Stream substream at the beginning has part-like Streams:

    ```python
    >>> s = stream.Score()
    >>> m1 = stream.Stream()
    >>> m1.repeatAppend(note.Note(), 4)
    >>> s.append(m1)
    >>> s.hasPartLikeStreams()
    True
    ```

    Adding another though makes it not part-like.

    ```python
    >>> m2 = stream.Stream()
    >>> m2.repeatAppend(note.Note(), 4)
    >>> s.append(m2)
    >>> s.hasPartLikeStreams()
    False
    ```

    Flat objects do not have part-like Streams:

    ```python
    >>> sf = s.flatten()
    >>> sf.hasPartLikeStreams()
    False
    ```

Stream.hasVoices()[[source]](../_modules/music21/stream/base.html#Stream.hasVoices)
:   Return a boolean value showing if this Stream contains Voices

Stream.haveAccidentalsBeenMade()[[source]](../_modules/music21/stream/base.html#Stream.haveAccidentalsBeenMade)
:   If Accidentals.displayStatus is None for all
    contained pitches, it as assumed that accidentals
    have not been set for display and/or makeAccidentals
    has not been run. If any Accidental has displayStatus
    other than None, this method returns True, regardless
    of if makeAccidentals has actually been run.

Stream.index(*el: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.index)
:   Return the first matched index for
    the specified object.

    Raises a StreamException if the object cannot be found.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('G')
    >>> n2 = note.Note('A')
    ```

    ```python
    >>> s.insert(0.0, n1)
    >>> s.insert(5.0, n2)
    >>> len(s)
    2
    >>> s.index(n1)
    0
    >>> s.index(n2)
    1
    ```

    Note that this is done via Object identity, so another identical
    G won’t be found in the stream.

    ```python
    >>> n3 = note.Note('G')
    >>> s.index(n3)
    Traceback (most recent call last):
    music21.exceptions21.StreamException: cannot find object (<music21.note.Note G>) in Stream
    ```

    To find the index of something equal to the object in the stream, cast the
    stream to a tuple or list first:

    ```python
    >>> tuple(s).index(n3)
    0
    ```

Stream.insert(*offsetOrItemOrList*, *itemOrNone=None*, *\**, *ignoreSort: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *setActiveSite: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/stream/base.html#Stream.insert)
:   Inserts an item(s) at the given offset(s).

    If ignoreSort is True then the inserting does not
    change whether the Stream is sorted or not (much faster if you’re
    going to be inserting dozens
    of items that don’t change the sort status)

    The setActiveSite parameter should nearly always be True; only for
    advanced Stream manipulation would you not change
    the activeSite after inserting an element.

    Has three forms: in the two argument form, inserts an
    element at the given offset:

    ```python
    >>> st1 = stream.Stream()
    >>> st1.insert(32, note.Note('B-'))
    >>> st1.highestOffset
    32.0
    ```

    In the single argument form with an object, inserts the element at its
    stored offset:

    ```python
    >>> n1 = note.Note('C#')
    >>> n1.offset = 30.0
    >>> st1 = stream.Stream()
    >>> st1.insert(n1)
    >>> st2 = stream.Stream()
    >>> st2.insert(40.0, n1)
    >>> n1.getOffsetBySite(st1)
    30.0
    ```

    In single argument form with a list, the list should
    contain pairs that alternate
    offsets and items; the method then, obviously, inserts the items
    at the specified offsets.

    Note: This functionality will be deprecated in v9 and replaced
    with a list of tuples of [(offset, element), (offset, element)]
    and removed in v10

    ```python
    >>> n1 = note.Note('G')
    >>> n2 = note.Note('F#')
    >>> st3 = stream.Stream()
    >>> st3.insert([1.0, n1, 2.0, n2])
    >>> n1.getOffsetBySite(st3)
    1.0
    >>> n2.getOffsetBySite(st3)
    2.0
    >>> len(st3)
    2
    ```

    Raises an error if offset is not a number:

    ```python
    >>> stream.Stream().insert('l', note.Note('B'))
    Traceback (most recent call last):
    music21.exceptions21.StreamException: Offset 'l' must be a number.
    ```

    Also raises an error if the object is not a music21 object (or a list of them)

    ```python
    >>> stream.Stream().insert(3.3, 'hello')
    Traceback (most recent call last):
    music21.exceptions21.StreamException: The object you tried to add
        to the Stream, 'hello', is not a Music21Object.
        Use an ElementWrapper object if this is what you intend.
    ```

    The error message is slightly different in the one-element form:

    ```python
    >>> stream.Stream().insert('hello')
    Traceback (most recent call last):
    music21.exceptions21.StreamException: Cannot insert item 'hello' to
        stream -- is it a music21 object?
    ```

Stream.insertAndShift(*offsetOrItemOrList*, *itemOrNone=None*)[[source]](../_modules/music21/stream/base.html#Stream.insertAndShift)
:   Insert an item at a specified or native offset,
    and shift any elements found in the Stream to start at
    the end of the added elements.

    This presently does not shift elements that have durations
    that extend into the lowest insert position.

    ```python
    >>> st1 = stream.Stream()
    >>> st1.insertAndShift(32, note.Note('B'))
    >>> st1.highestOffset
    32.0
    >>> st1.insertAndShift(32, note.Note('C'))
    >>> st1.highestOffset
    33.0
    >>> st1.show('text', addEndTimes=True)
    {32.0 - 33.0} <music21.note.Note C>
    {33.0 - 34.0} <music21.note.Note B>
    ```

    Let’s insert an item at the beginning, note that
    since the C and B are not affected, they do not shift.

    ```python
    >>> st1.insertAndShift(0, note.Note('D'))
    >>> st1.show('text', addEndTimes=True)
    {0.0 - 1.0} <music21.note.Note D>
    {32.0 - 33.0} <music21.note.Note C>
    {33.0 - 34.0} <music21.note.Note B>
    ```

    But if we insert something again at the beginning of the stream,
    everything after the first shifted note begins shifting, so the
    C and the B shift even though there is a gap there. Normally
    there’s no gaps in a stream, so this will not be a factor:

    ```python
    >>> st1.insertAndShift(0, note.Note('E'))
    >>> st1.show('text', addEndTimes=True)
    {0.0 - 1.0} <music21.note.Note E>
    {1.0 - 2.0} <music21.note.Note D>
    {33.0 - 34.0} <music21.note.Note C>
    {34.0 - 35.0} <music21.note.Note B>
    ```

    In the single argument form with an object, inserts the element at its stored offset:

    ```python
    >>> n1 = note.Note('C#')
    >>> n1.offset = 30.0
    >>> n2 = note.Note('D#')
    >>> n2.offset = 30.0
    >>> st1 = stream.Stream()
    >>> st1.insertAndShift(n1)
    >>> st1.insertAndShift(n2)  # will shift offset of n1
    >>> n1.getOffsetBySite(st1)
    31.0
    >>> n2.getOffsetBySite(st1)
    30.0
    >>> st1.show('text', addEndTimes=True)
    {30.0 - 31.0} <music21.note.Note D#>
    {31.0 - 32.0} <music21.note.Note C#>
    ```

    ```python
    >>> st2 = stream.Stream()
    >>> st2.insertAndShift(40.0, n1)
    >>> st2.insertAndShift(40.0, n2)
    >>> n1.getOffsetBySite(st2)
    41.0
    ```

    In single argument form with a list, the list should contain pairs that alternate
    offsets and items; the method then, obviously, inserts the items
    at the specified offsets:

    ```python
    >>> n1 = note.Note('G-')
    >>> n2 = note.Note('F-')
    >>> st3 = stream.Stream()
    >>> st3.insertAndShift([1.0, n1, 2.0, n2])
    >>> n1.getOffsetBySite(st3)
    1.0
    >>> n2.getOffsetBySite(st3)
    2.0
    >>> len(st3)
    2
    >>> st3.show('text', addEndTimes=True)
    {1.0 - 2.0} <music21.note.Note G->
    {2.0 - 3.0} <music21.note.Note F->
    ```

    N.B. – using this method on a list assumes that you’ll be inserting
    contiguous objects; you can’t shift things that are separated, as this
    following FAILED example shows.

    ```python
    >>> n1 = note.Note('G', type='half')
    >>> st4 = stream.Stream()
    >>> st4.repeatAppend(n1, 3)
    >>> st4.insertAndShift([2.0, note.Note('e'), 4.0, note.Note('f')])
    >>> st4.show('text')
    {0.0} <music21.note.Note G>
    {2.0} <music21.note.Note E>
    {4.0} <music21.note.Note F>
    {5.0} <music21.note.Note G>
    {7.0} <music21.note.Note G>
    ```

    As an FYI, there is no removeAndShift() function, so the opposite of
    insertAndShift(el) is remove(el, shiftOffsets=True).

Stream.insertIntoNoteOrChord(*offset*, *noteOrChord*, *chordsOnly: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/stream/base.html#Stream.insertIntoNoteOrChord)
:   Insert a Note or Chord into an offset position in this Stream.
    If there is another Note or Chord in this position,
    create a new Note or Chord that combines the pitches of the
    inserted chord. If there is a Rest in this position,
    the Rest is replaced by the Note or Chord. The duration of the
    previously-found chord will remain the same in the new Chord.

    ```python
    >>> n1 = note.Note('D4')
    >>> n1.duration.quarterLength = 2.0
    >>> r1 = note.Rest()
    >>> r1.duration.quarterLength = 2.0
    >>> c1 = chord.Chord(['C4', 'E4'])
    >>> s = stream.Stream()
    >>> s.append(n1)
    >>> s.append(r1)
    >>> s.append(c1)
    >>> s.show('text')
    {0.0} <music21.note.Note D>
    {2.0} <music21.note.Rest half>
    {4.0} <music21.chord.Chord C4 E4>
    ```

    Save the original Streams for later

    ```python
    >>> import copy
    >>> s2 = copy.deepcopy(s)
    >>> s3 = copy.deepcopy(s)
    >>> s4 = copy.deepcopy(s)
    ```

    Notice that the duration of the inserted element is not taken into
    consideration and the original element is not broken up,
    as it would be in chordify(). But Chords and Notes are created:

    ```python
    >>> for i in [0.0, 2.0, 4.0]:
    ...     s.insertIntoNoteOrChord(i, note.Note('F#4'))
    >>> s.show('text')
    {0.0} <music21.chord.Chord D4 F#4>
    {2.0} <music21.note.Note F#>
    {4.0} <music21.chord.Chord C4 E4 F#4>
    ```

    If chordsOnly is set to True then no notes are returned, only chords, but
    untouched notes are left alone:

    ```python
    >>> s2.insert(5.0, note.Note('E##4'))
    >>> for i in [0.0, 2.0, 4.0]:
    ...     s2.insertIntoNoteOrChord(i, note.Note('F#4'), chordsOnly=True)
    >>> s2.show('text')
    {0.0} <music21.chord.Chord D4 F#4>
    {2.0} <music21.chord.Chord F#4>
    {4.0} <music21.chord.Chord C4 E4 F#4>
    {5.0} <music21.note.Note E##>
    ```

    A chord inserted on top of a note always changes the note into a chord:

    ```python
    >>> s2.insertIntoNoteOrChord(5.0, chord.Chord('F#4 G-4'))
    >>> s2.show('text')
    {0.0} <music21.chord.Chord D4 F#4>
    {2.0} <music21.chord.Chord F#4>
    {4.0} <music21.chord.Chord C4 E4 F#4>
    {5.0} <music21.chord.Chord E##4 F#4 G-4>
    ```

    Chords can also be inserted into rests:

    ```python
    >>> s3.getElementsByOffset(2.0).first()
    <music21.note.Rest half>
    >>> s3.insertIntoNoteOrChord(2.0, chord.Chord('C4 E4 G#4'))
    >>> s3.show('text')
    {0.0} <music21.note.Note D>
    {2.0} <music21.chord.Chord C4 E4 G#4>
    {4.0} <music21.chord.Chord C4 E4>
    ```

    Despite the variable name, a rest could be inserted into a noteOrChord.
    It does nothing to existing notes or chords, and just adds a new rest
    afterwards.

    ```python
    >>> s4.show('text', addEndTimes=True)
    {0.0 - 2.0} <music21.note.Note D>
    {2.0 - 4.0} <music21.note.Rest half>
    {4.0 - 5.0} <music21.chord.Chord C4 E4>
    ```

    ```python
    >>> for i in [0.0, 4.0, 6.0]:  # skipping 2.0 for now
    ...     r = note.Rest(type='quarter')
    ...     s4.insertIntoNoteOrChord(i, r)
    >>> r2 = note.Rest(type='quarter')
    >>> s4.insertIntoNoteOrChord(2.0, r)
    >>> s4.show('text', addEndTimes=True)
    {0.0 - 2.0} <music21.note.Note D>
    {2.0 - 4.0} <music21.note.Rest half>
    {4.0 - 5.0} <music21.chord.Chord C4 E4>
    {6.0 - 7.0} <music21.note.Rest quarter>
    ```

    Notice that (1) the original duration and not the new duration is used, unless
    there is no element at that place, and (2) if an element is put into a place where
    no existing element was found, then it will be found in the new Stream, but if it
    is placed on top of an existing element, the original element or a new copy will remain:

    ```python
    >>> r in s4
    True
    >>> r2 in s4
    False
    ```

    If a Stream has more than one note, chord, or rest at that position,
    currently an error is raised. This may change later:

    ```python
    >>> s5 = stream.Stream()
    >>> s5.insert(0, note.Note('C##4'))
    >>> s5.insert(0, note.Note('E--4'))
    >>> s5.insertIntoNoteOrChord(0, note.Note('D4'))
    Traceback (most recent call last):
    music21.exceptions21.StreamException: more than one element found at the specified offset
    ```

Stream.invertDiatonic(*inversionNote: [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/stream/base.html#Stream.invertDiatonic)
:   inverts a stream diatonically around the given note (by default, middle C)

    For pieces where the key signature
    does not change throughout the piece it is MUCH faster than
    for pieces where the key signature changes.

    Here in this test, we put Ciconia’s Quod Jactatur (a single voice
    piece that should have a canon solution: see trecento.quodJactatur)
    into 3 flats (instead of its original 1 flat) in measure 1, but
    into 5 sharps in measure 2 and then invert around F4, creating
    a new piece.

    ```python
    >>> qj = corpus.parse('ciconia/quod_jactatur').parts[0].measures(1, 2)
    >>> qj.id = 'measureExcerpt'
    ```

    ```python
    >>> qj.show('text')
    {0.0} <music21.instrument.Piano 'P1: MusicXML Part: Grand Piano'>
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.layout.SystemLayout>
        {0.0} <music21.clef.Treble8vbClef>
        {0.0} <music21.tempo.MetronomeMark Quarter=120 (playback only)>
        {0.0} <music21.key.Key of F major>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note C>
        {1.5} <music21.note.Note D>
    {2.0} <music21.stream.Measure 2 offset=2.0>
        {0.0} <music21.note.Note E>
        {0.5} <music21.note.Note D>
        {1.0} <music21.note.Note C>
        {1.5} <music21.note.Note D>
    ```

    ```python
    >>> qjFlat = qj.flatten()
    >>> k1 = qjFlat.getElementsByClass(key.KeySignature).first()
    >>> k3flats = key.KeySignature(-3)
    >>> qjFlat.replace(k1, k3flats, allDerived=True)
    >>> qj.getElementsByClass(stream.Measure)[1].insert(0, key.KeySignature(5))
    ```

    ```python
    >>> qj2 = qj.invertDiatonic(note.Note('F4'), inPlace=False)
    >>> qj2.show('text')
    {0.0} <music21.instrument.Piano 'P1: MusicXML Part: Grand Piano'>
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.layout.SystemLayout>
        {0.0} <music21.clef.Treble8vbClef>
        {0.0} <music21.tempo.MetronomeMark Quarter=120 (playback only)>
        {0.0} <music21.key.KeySignature of 3 flats>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note B->
        {1.5} <music21.note.Note A->
    {2.0} <music21.stream.Measure 2 offset=2.0>
        {0.0} <music21.key.KeySignature of 5 sharps>
        {0.0} <music21.note.Note G#>
        {0.5} <music21.note.Note A#>
        {1.0} <music21.note.Note B>
        {1.5} <music21.note.Note A#>
    ```

    * Changed in v5: inPlace is False by default.

Stream.isSequence() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.isSequence)
:   A stream is a sequence if it has no overlaps.

    ```python
    >>> a = stream.Stream()
    >>> for x in [0, 0, 0, 0, 3, 3, 3]:
    ...     n = note.Note('G#')
    ...     n.duration = duration.Duration('whole')
    ...     n.offset = x * 1
    ...     a.insert(n)
    ...
    >>> a.isSequence()
    False
    ```

Stream.isTwelveTone()[[source]](../_modules/music21/stream/base.html#Stream.isTwelveTone)
:   Return true if this Stream only employs twelve-tone equal-tempered pitch values.

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('G#4'))
    >>> s.isTwelveTone()
    True
    >>> s.append(note.Note('G~4'))
    >>> s.isTwelveTone()
    False
    ```

Stream.isWellFormedNotation() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.isWellFormedNotation)
:   Return True if, given the context of this Stream or Stream subclass,
    contains what appears to be well-formed notation. This often means
    the formation of Measures, or a Score that contains Part with Measures.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> s.isWellFormedNotation()
    True
    >>> s.parts[0].isWellFormedNotation()
    True
    >>> s.parts[0].getElementsByClass(stream.Measure).first().isWellFormedNotation()
    True
    ```

    ```python
    >>> s2 = stream.Score()
    >>> m = stream.Measure()
    >>> s2.append(m)
    >>> s2.isWellFormedNotation()
    False
    ```

    ```python
    >>> o = stream.Opus([s])
    >>> o.isWellFormedNotation()
    True
    >>> o2 = stream.Opus([s2])
    >>> o2.isWellFormedNotation()
    False
    ```

    Only Measures and Voices are allowed to contain notes and rests directly:

    ```python
    >>> m.isWellFormedNotation()
    True
    >>> s2.append(note.Rest())
    >>> s2.isWellFormedNotation()
    False
    ```

Stream.iter() → [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[M21ObjType][[source]](../_modules/music21/stream/base.html#Stream.iter)
:   The Stream iterator, used in all for
    loops and similar iteration routines. This method returns the
    specialized `music21.stream.StreamIterator` class, which
    adds necessary Stream-specific features.

    Generally you don’t need this, just iterate over a stream, but it is necessary
    to add custom filters to an iterative search before iterating.

Stream.last() → M21ObjType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.last)
:   Return the last element of a Stream. (Added for compatibility with StreamIterator)
    Or None if the Stream is empty.

    s.last() is the same speed as s[-1], except for not raising an IndexError.

    ```python
    >>> nC = note.Note('C4')
    >>> nD = note.Note('D4')
    >>> s = stream.Stream()
    >>> s.append([nC, nD])
    >>> s.last()
    <music21.note.Note D>
    ```

    ```python
    >>> empty = stream.Stream()
    >>> print(empty.last())
    None
    ```

    * New in v7.

Stream.lyrics(*ignoreBarlines: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipTies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Lyric](moduleNote.html#music21.note.Lyric "music21.note.Lyric") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Lyric](moduleNote.html#music21.note.Lyric "music21.note.Lyric") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[RecursiveLyricList]]]][[source]](../_modules/music21/stream/base.html#Stream.lyrics)
:   Returns a dict of lists of lyric objects (with the keys being
    the lyric numbers) found in self. Each list will have an element for each
    note in the stream (which may be a note.Lyric() or None).
    By default, this method automatically
    recurses through measures, but not other container streams.

    ```python
    >>> s = converter.parse('tinynotation: 4/4 a4 b c d   e f g a', makeNotation=False)
    >>> someLyrics = ['this', 'is', 'a', 'list', 'of', 'eight', 'lyric', 'words']
    >>> for n, lyric in zip(s.notes, someLyrics):
    ...     n.lyric = lyric
    ```

    ```python
    >>> s.lyrics()
    {1: [<music21.note.Lyric number=1 syllabic=single text='this'>, ...,
         <music21.note.Lyric number=1 syllabic=single text='words'>]}
    ```

    ```python
    >>> s.notes[3].lyric = None
    >>> s.lyrics()[1]
    [<music21.note.Lyric number=1 syllabic=single text='this'>, ..., None, ...,
     <music21.note.Lyric number=1 syllabic=single text='words'>]
    ```

    If ignoreBarlines is True, it will behave as if the elements in measures are all
    in a flattened stream (note that this is not stream.flatten()
    as it does not copy the elements)
    together without measure containers. This means that even if recurse is
    False, lyrics() will still essentially recurse through measures.

    ```python
    >>> s.makeMeasures(inPlace=True)
    >>> s.lyrics()[1]
    [<music21.note.Lyric number=1 syllabic=single text='this'>, ..., None, ...,
     <music21.note.Lyric number=1 syllabic=single text='words'>]
    ```

    ```python
    >>> list(s.lyrics(ignoreBarlines=False).keys())
    []
    ```

    If recurse is True, this method will recurse through all container streams and
    build a nested list structure mirroring the hierarchy of the stream.
    Note that if ignoreBarlines is True, measure structure will not be reflected
    in the hierarchy, although if ignoreBarlines is False, it will.

    Note that streams which do not contain any instance of a lyric number will not
    appear anywhere in the final list (not as a [] or otherwise).

    ```python
    >>> scr = stream.Score(s)
    ```

    ```python
    >>> scr.lyrics(ignoreBarlines=False, recurse=True)[1]
    [[[<music21.note.Lyric number=1 syllabic=single text='this'>, <...'is'>, <...'a'>, None],
      [<...'of'>, <...'eight'>, <...'lyric'>, <...'words'>]]]
    ```

    Notice that the measures are nested in the part which is nested in the score.

    ```python
    >>> scr.lyrics(ignoreBarlines=True, recurse=True)[1]
    [[<music21.note.Lyric number=1 syllabic=single text='this'>, <...'is'>, <...'a'>, None,
      <...'of'>, <...'eight'>, <...'lyric'>, <...'words'>]]
    ```

    Notice that this time, the measure structure is ignored.

    ```python
    >>> list(scr.lyrics(ignoreBarlines=True, recurse=False).keys())
    []
    ```

Stream.makeAccidentals(*\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *useKeySignature: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") = True*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *searchKeySignatureByContext: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *tiePitchSet: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/stream/base.html#Stream.makeAccidentals)
:   A method to set and provide accidentals given various conditions and contexts.

    pitchPast is a list of pitches preceding this pitch in this measure.

    pitchPastMeasure is a list of pitches preceding this pitch but in a previous measure.

    otherSimultaneousPitches is a list of other pitches in this simultaneity, for use
    when cautionaryPitchClass is True.

    If useKeySignature is True, a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") will be searched
    for in this Stream or this Stream’s defined contexts. An alternative KeySignature
    can be supplied with this object and used for temporary pitch processing.

    If alteredPitches is a list of modified pitches (Pitches with Accidentals) that
    can be directly supplied to Accidental processing. These are the same values obtained
    from a [`music21.key.KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") object using the
    [`alteredPitches`](moduleKey.html#music21.key.KeySignature.alteredPitches "music21.key.KeySignature.alteredPitches") property.

    If cautionaryPitchClass is True, comparisons to past accidentals are made regardless
    of register. That is, if a past sharp is found two octaves above a present natural,
    a natural sign is still displayed.

    If cautionaryAll is True, all accidentals are shown.

    If overrideStatus is True, this method will ignore any current displayStatus setting
    found on the Accidental. By default this does not happen. If displayStatus is set to
    None, the Accidental’s displayStatus is set.

    If cautionaryNotImmediateRepeat is True, cautionary accidentals will be displayed for
    an altered pitch even if that pitch had already been displayed as altered.

    If tiePitchSet is not None it should be a set of .nameWithOctave strings
    to determine whether following accidentals should be shown because the last
    note of the same pitch had a start or continue tie.

    If searchKeySignatureByContext is True then keySignatures from the context of the
    stream will be used if none found.

    The [`updateAccidentalDisplay()`](modulePitch.html#music21.pitch.Pitch.updateAccidentalDisplay "music21.pitch.Pitch.updateAccidentalDisplay") method is used to determine if
    an accidental is necessary.

    This will assume that the complete Stream is the context of evaluation. For smaller context
    ranges, call this on Measure objects.

    If inPlace is True, this is done in-place; if inPlace is False,
    this returns a modified deep copy.

    * Changed in v6: does not return anything if inPlace is True.
    * Changed in v7: default inPlace is False
    * Changed in v8: altered unisons/octaves in Chords now supply clarifying naturals.

    All arguments are keyword only.

Stream.makeBeams(*\**, *inPlace=False*, *setStemDirections=True*, *failOnNoTimeSignature=False*)[[source]](../_modules/music21/stream/base.html#Stream.makeBeams)
:   Return a new Stream, or modify the Stream in place, with beams applied to all
    notes.

    See [`makeBeams()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.makeBeams "music21.stream.makeNotation.makeBeams").

    * New in v6.7: setStemDirections.
    * New in v7: failOnNoTimeSignature raises StreamException if no TimeSignature
      exists in the stream context from which to make measures.

Stream.makeImmutable()[[source]](../_modules/music21/stream/base.html#Stream.makeImmutable)
:   Clean this Stream: for self and all elements, purge all dead locations
    and remove all non-contained sites. Further, restore all active sites.

Stream.makeMeasures(*meterStream=None*, *refStreamOrTimeRange=None*, *searchContext=False*, *innerBarline=None*, *finalBarline='final'*, *bestClef=False*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.makeMeasures)
:   Return a new stream (or if inPlace=True change in place) this
    Stream so that it has internal measures.

    For more details, see [`makeMeasures()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.makeMeasures "music21.stream.makeNotation.makeMeasures").

Stream.makeMutable(*recurse=True*)[[source]](../_modules/music21/stream/base.html#Stream.makeMutable)

Stream.makeNotation(*\**, *meterStream=None*, *refStreamOrTimeRange=None*, *inPlace=False*, *bestClef=False*, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *useKeySignature: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") = True*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *tiePitchSet: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/stream/base.html#Stream.makeNotation)
:   This method calls a sequence of Stream methods on this Stream to prepare
    notation, including creating voices for overlapped regions, Measures
    if necessary, creating ties, beams, accidentals, and tuplet brackets.

    If inPlace is True, this is done in-place.
    if inPlace is False, this returns a modified deep copy.

    The following additional parameters are documented on
    `makeAccidentals()`:

    ```python
    pitchPast
    pitchPastMeasure
    useKeySignature
    alteredPitches
    cautionaryPitchClass
    cautionaryAll
    overrideStatus
    cautionaryNotImmediateRepeat
    tiePitchSet
    ```

    ```python
    >>> s = stream.Stream()
    >>> n = note.Note('g')
    >>> n.quarterLength = 1.5
    >>> s.repeatAppend(n, 10)
    >>> sMeasures = s.makeNotation()
    >>> len(sMeasures.getElementsByClass(stream.Measure))
    4
    >>> sMeasures.getElementsByClass(stream.Measure).last().rightBarline.type
    'final'
    ```

    * Changed in v7: inPlace=True returns None.

Stream.makeRests(*refStreamOrTimeRange=None*, *fillGaps=False*, *timeRangeFromBarDuration=False*, *inPlace=False*, *hideRests=False*)[[source]](../_modules/music21/stream/base.html#Stream.makeRests)
:   Calls [`makeRests()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.makeRests "music21.stream.makeNotation.makeRests").

    * Changed in v7, inPlace=False by default.

Stream.makeTies(*meterStream=None*, *inPlace=False*, *displayTiedAccidentals=False*, *classFilterList=(<class 'music21.note.GeneralNote'>*, *)*)[[source]](../_modules/music21/stream/base.html#Stream.makeTies)
:   Calls [`makeTies()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.makeTies "music21.stream.makeNotation.makeTies").

    * Changed in v4: inPlace=False by default.
    * New in v.7: classFilterList.

Stream.makeVoices(*\**, *inPlace=False*, *fillGaps=True*)[[source]](../_modules/music21/stream/base.html#Stream.makeVoices)
:   If this Stream has overlapping Notes or Chords, this method will isolate
    all overlaps in unique Voices, and place those Voices in the Stream.

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, note.Note('C4', quarterLength=4))
    >>> s.repeatInsert(note.Note('b-4', quarterLength=0.5), [x * 0.5 for x in list(range(8))])
    >>> s.makeVoices(inPlace=True)
    >>> len(s.voices)
    2
    >>> [n.pitch for n in s.voices[0].notes]
    [<music21.pitch.Pitch C4>]
    >>> [str(n.pitch) for n in s.voices[1].notes]
    ['B-4', 'B-4', 'B-4', 'B-4', 'B-4', 'B-4', 'B-4', 'B-4']
    ```

    * Changed in v7: if fillGaps=True and called on an incomplete measure,
      makes trailing rests in voices. This scenario occurs when parsing MIDI.

Stream.measure(*measureNumber*, *\**, *collect=('Clef', 'TimeSignature', 'Instrument', 'KeySignature')*, *indicesNotNumbers=False*) → [Measure](#music21.stream.base.Measure "music21.stream.base.Measure") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.measure)
:   Given a measure number, return a single
    `Measure` object if the Measure number exists, otherwise return None.

    This method is distinguished from `measures()`
    in that this method returns a single Measure object, not a Stream containing
    one or more Measure objects.

    ```python
    >>> a = corpus.parse('bach/bwv324.xml')
    >>> a.parts[0].measure(3)
    <music21.stream.Measure 3 offset=8.0>
    ```

    See `measures()` for an explanation of collect and
    indicesNotNumbers

    To get the last measure of a piece, use -1 as a measureNumber – this will turn
    on indicesNotNumbers if it is off:

    ```python
    >>> a.parts[0].measure(-1)
    <music21.stream.Measure 9 offset=38.0>
    ```

    Getting a non-existent measure will return None:

    ```python
    >>> print(a.parts[0].measure(99))
    None
    ```

Stream.measureOffsetMap(*classFilterList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Type](https://docs.python.org/3/library/typing.html#typing.Type "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Type](https://docs.python.org/3/library/typing.html#typing.Type "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ('Measure',)*) → [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Measure](#music21.stream.base.Measure "music21.stream.base.Measure")]][[source]](../_modules/music21/stream/base.html#Stream.measureOffsetMap)
:   If this Stream contains Measures, returns an OrderedDict
    whose keys are the offsets of the start of each measure
    and whose values are a list of references
    to the `Measure` objects that start
    at that offset.

    Even in normal music there may be more than
    one Measure starting at each offset because each
    `Part` might define its own Measure.
    However, you are unlikely to encounter such things unless you
    run Score.flatten(retainContainers=True).

    The offsets are always measured relative to the
    calling Stream (self).

    You can specify a classFilterList argument as a list of classes
    to find instead of Measures. But the default will of course
    find Measure objects.

    Example 1: This Bach chorale is in 4/4 without a pickup, so
    as expected, measures are found every 4 offsets, until the
    weird recitation in m. 7 which in our edition lasts 10 beats
    and thus causes a gap in measureOffsetMap from 24.0 to 34.0.

    [![../_images/streamMeasureOffsetMapBWV324.png](../_images/streamMeasureOffsetMapBWV324.png)](../_images/streamMeasureOffsetMapBWV324.png)

    ```python
    >>> chorale = corpus.parse('bach/bwv324.xml')
    >>> alto = chorale.parts['#alto']
    >>> altoMeasures = alto.measureOffsetMap()
    >>> altoMeasures
    OrderedDict([(0.0, [<music21.stream.Measure 1 offset=0.0>]),
                 (4.0, [<music21.stream.Measure 2 offset=4.0>]),
                 (8.0, [<music21.stream.Measure 3 offset=8.0>]),
                 ...
                 (38.0, [<music21.stream.Measure 9 offset=38.0>])])
    >>> list(altoMeasures.keys())
    [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 34.0, 38.0]
    ```

    altoMeasures is a dictionary of the measures
    that are found in the alto part, so we can get
    the measure beginning on offset 4.0 (measure 2)
    and display it (though it’s the only measure
    found at offset 4.0, there might be others as
    in example 2, so we need to call altoMeasures[4.0][0]
    to get this measure.):

    ```python
    >>> altoMeasures[4.0]
    [<music21.stream.Measure 2 offset=4.0>]
    >>> altoMeasures[4.0][0].show('text')
    {0.0} <music21.note.Note D>
    {1.0} <music21.note.Note D#>
    {2.0} <music21.note.Note E>
    {3.0} <music21.note.Note F#>
    ```

    Example 2: How to get all the measures from all parts (not the
    most efficient way, but it works!):

    ```python
    >>> mom = chorale.measureOffsetMap()
    >>> mom
    OrderedDict([(0.0, [<music21.stream.Measure 1 offset=0.0>,
                        <music21.stream.Measure 1 offset=0.0>,
                        <music21.stream.Measure 1 offset=0.0>,
                        <music21.stream.Measure 1 offset=0.0>]),
                  (4.0, [<music21.stream.Measure 2 offset=4.0>,
                         ...])])
    >>> for measure_obj in mom[8.0]:
    ...     print(measure_obj, measure_obj.getContextByClass(stream.Part).id)
    <music21.stream.Measure 3 offset=8.0> Soprano
    <music21.stream.Measure 3 offset=8.0> Alto
    <music21.stream.Measure 3 offset=8.0> Tenor
    <music21.stream.Measure 3 offset=8.0> Bass
    ```

    Changed in v9: classFilterList must be a list or tuple of strings or Music21Objects

Stream.measures(*numberStart*, *numberEnd*, *\**, *collect=('Clef'*, *'TimeSignature'*, *'Instrument'*, *'KeySignature')*, *gatherSpanners=<GatherSpanners.ALL>*, *indicesNotNumbers=False*) → [Stream](#music21.stream.base.Stream "music21.stream.base.Stream")[[Measure](#music21.stream.base.Measure "music21.stream.base.Measure")][[source]](../_modules/music21/stream/base.html#Stream.measures)
:   Get a region of Measures based on a start and end Measure number
    where the boundary numbers are both included.

    That is, a request for measures 4 through 10 will return 7 Measures, numbers 4 through 10.

    Additionally, any number of associated classes can be gathered from the context
    and put into the measure. By default, we collect the Clef, TimeSignature, KeySignature,
    and Instrument so that there is enough context to perform. (See getContextByClass()
    and .previous() for definitions of the context)

    While all elements in the source are the original elements in the extracted region,
    new Measure objects are created and returned.

    ```python
    >>> bachIn = corpus.parse('bach/bwv66.6')
    >>> bachExcerpt = bachIn.parts[0].measures(1, 3)
    >>> len(bachExcerpt.getElementsByClass(stream.Measure))
    3
    ```

    Because bwv66.6 has a pickup measure, and we requested to start at measure 1,
    this is NOT true:

    ```python
    >>> firstExcerptMeasure = bachExcerpt.getElementsByClass(stream.Measure).first()
    >>> firstBachMeasure = bachIn.parts[0].getElementsByClass(stream.Measure).first()
    >>> firstExcerptMeasure is firstBachMeasure
    False
    >>> firstBachMeasure.number
    0
    >>> firstExcerptMeasure.number
    1
    ```

    To get all measures from the beginning, go ahead and always request measure 0 to x,
    there will be no error if there is not a pickup measure.

    ```python
    >>> bachExcerpt = bachIn.parts[0].measures(0, 3)
    >>> excerptNote = bachExcerpt.getElementsByClass(stream.Measure).first().notes.first()
    >>> originalNote = bachIn.parts[0].recurse().notes[0]
    >>> excerptNote is originalNote
    True
    ```

    if indicesNotNumbers is True, then it ignores defined measureNumbers and
    uses 0-indexed measure objects and half-open range. For instance, if you have a piece
    that goes “m1, m2, m3, m4, …” (like a standard piece without pickups, then
    .measures(1, 3, indicesNotNumbers=True) would return measures 2 and 3, because
    it is interpreted as the slice from object with index 1, which is measure 2 (m1 has
    an index of 0) up to but NOT including the object with index 3, which is measure 4.
    IndicesNotNumbers is like a Python-slice.

    ```python
    >>> bachExcerpt2 = bachIn.parts[0].measures(0, 2, indicesNotNumbers=True)
    >>> for m in bachExcerpt2.getElementsByClass(stream.Measure):
    ...     print(m)
    ...     print(m.number)
    <music21.stream.Measure 0 offset=0.0>
    0
    <music21.stream.Measure 1 offset=1.0>
    1
    ```

    If numberEnd=None then it is interpreted as the last measure of the stream:

    ```python
    >>> bachExcerpt3 = bachIn.parts[0].measures(7, None)
    >>> for m in bachExcerpt3.getElementsByClass(stream.Measure):
    ...     print(m)
    <music21.stream.Measure 7 offset=0.0>
    <music21.stream.Measure 8 offset=4.0>
    <music21.stream.Measure 9 offset=8.0>
    ```

    Note that the offsets in the new stream are shifted so that the first measure
    in the excerpt begins at 0.0

    The measure elements are the same objects as the original:

    ```python
    >>> lastExcerptMeasure = bachExcerpt3.getElementsByClass(stream.Measure).last()
    >>> lastOriginalMeasure = bachIn.parts[0].getElementsByClass(stream.Measure).last()
    >>> lastExcerptMeasure is lastOriginalMeasure
    True
    ```

    At the beginning of the Stream returned, before the measures will be some additional
    objects so that the context is properly preserved:

    ```python
    >>> for thing in bachExcerpt3:
    ...     print(thing)
    P1: Soprano: Instrument 1
    <music21.clef.TrebleClef>
    f# minor
    <music21.meter.TimeSignature 4/4>
    <music21.stream.Measure 7 offset=0.0>
    <music21.stream.Measure 8 offset=4.0>
    <music21.stream.Measure 9 offset=8.0>
    ```

    Collecting gets the most recent element in the context of the stream:

    ```python
    >>> bachIn.parts[0].insert(10, key.Key('D-'))
    >>> bachExcerpt4 = bachIn.parts[0].measures(7, None)
    >>> for thing in bachExcerpt4:
    ...     print(thing)
    P1: Soprano: Instrument 1
    <music21.clef.TrebleClef>
    D- major
    ...
    ```

    What is collected is determined by the “collect” iterable. To collect nothing
    send an empty list:

    ```python
    >>> bachExcerpt5 = bachIn.parts[0].measures(8, None, collect=[])
    >>> for thing in bachExcerpt5:
    ...     print(thing)
    <music21.stream.Measure 8 offset=0.0>
    <music21.stream.Measure 9 offset=4.0>
    ```

    If a stream has measure suffixes, then Streams having that suffix or no suffix
    are returned.

    ```python
    >>> p = stream.Part()
    >>> mSuffix3 = stream.Measure(number=3)
    >>> mSuffix4 = stream.Measure(number=4)
    >>> mSuffix4a = stream.Measure(number=4)
    >>> mSuffix4a.numberSuffix = 'a'
    >>> mSuffix4b = stream.Measure(number=4)
    >>> mSuffix4b.numberSuffix = 'b'
    >>> mSuffix5 = stream.Measure(number=5)
    >>> mSuffix5a = stream.Measure(number=5)
    >>> mSuffix5a.numberSuffix = 'a'
    >>> mSuffix6 = stream.Measure(number=6)
    >>> p.append([mSuffix3, mSuffix4, mSuffix4a, mSuffix4b, mSuffix5, mSuffix5a, mSuffix6])
    >>> suffixExcerpt = p.measures('4b', 6)
    >>> suffixExcerpt.show('text')
    {0.0} <music21.stream.Measure 4 offset=0.0>

    {0.0} <music21.stream.Measure 4b offset=0.0>

    {0.0} <music21.stream.Measure 5 offset=0.0>

    {0.0} <music21.stream.Measure 5a offset=0.0>

    {0.0} <music21.stream.Measure 6 offset=0.0>

    >>> suffixExcerpt2 = p.measures(3, '4a')
    >>> suffixExcerpt2.show('text')
    {0.0} <music21.stream.Measure 3 offset=0.0>

    {0.0} <music21.stream.Measure 4 offset=0.0>

    {0.0} <music21.stream.Measure 4a offset=0.0>
    ```

    GatherSpanners can change the output:

    ```python
    >>> from music21.common.enums import GatherSpanners
    >>> beachIn = corpus.parse('beach')
    >>> beachExcerpt = beachIn.measures(3, 4, gatherSpanners=GatherSpanners.ALL)
    >>> len(beachExcerpt.spannerBundle)
    8
    >>> len(beachIn.spannerBundle)
    94
    ```

    * Changed in v7: does not create measures automatically.
    * Changed in v7: If gatherSpanners is True or GatherSpanners.ALL (default),
      then just the spanners pertaining to the requested measure region
      are provided, rather than the entire bundle from the source.

Stream.melodicIntervals(*\*\*skipKeywords*)[[source]](../_modules/music21/stream/base.html#Stream.melodicIntervals)
:   Returns a Stream of [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") objects
    between Notes (and by default, Chords) that follow each other in a stream.
    the offset of the Interval is the offset of the beginning of the interval
    (if two notes are adjacent, then this offset is equal to the offset of
    the second note, but if skipRests is set to True or there is a gap
    in the Stream, then these two numbers
    will be different).

    See `findConsecutiveNotes()` in this class for
    a discussion of what is meant by default for “consecutive notes”, and
    which keywords such as skipChords, skipRests, skipUnisons, etc. can be
    used to change that behavior.

    The interval between a Note and a Chord (or between two chords) is the
    interval to the first pitch of the Chord (pitches[0]) which is usually the lowest.
    For more complex interval calculations,
    run `findConsecutiveNotes()` and then calculate
    your own intervals directly.

    Returns an empty Stream if there are not at least two elements found by
    findConsecutiveNotes.

    ```python
    >>> s1 = converter.parse("tinynotation: 3/4 c4 d' r b b'", makeNotation=False)
    >>> s1.show()
    ```

    [![../_images/streamMelodicIntervals1.png](../_images/streamMelodicIntervals1.png)](../_images/streamMelodicIntervals1.png)

    ```python
    >>> intervalStream1 = s1.melodicIntervals()
    >>> intervalStream1.show('text')
    {1.0} <music21.interval.Interval M9>
    {4.0} <music21.interval.Interval P8>
    ```

    ```python
    >>> M9 = intervalStream1[0]
    >>> M9.noteStart.nameWithOctave, M9.noteEnd.nameWithOctave
    ('C4', 'D5')
    ```

    Using the skip attributes from `findConsecutiveNotes()`,
    we can alter which intervals are reported:

    ```python
    >>> intervalStream2 = s1.melodicIntervals(skipRests=True, skipOctaves=True)
    >>> intervalStream2.show('text')
    {1.0} <music21.interval.Interval M9>
    {2.0} <music21.interval.Interval m-3>
    ```

    ```python
    >>> m3 = intervalStream2[1]
    >>> m3.directedNiceName
    'Descending Minor Third'
    ```

Stream.mergeAttributes(*other: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/stream/base.html#Stream.mergeAttributes)
:   Merge relevant attributes from the Other stream into this one.

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note())
    >>> s.autoSort = False
    >>> s.id = 'hi'
    >>> s2 = stream.Stream()
    >>> s2.mergeAttributes(s)
    >>> s2.autoSort
    False
    >>> s2
    <music21.stream.Stream hi>
    >>> len(s2)
    0
    ```

Stream.mergeElements(*other*, *classFilterList=None*)[[source]](../_modules/music21/stream/base.html#Stream.mergeElements)
:   Given another Stream, store references of each element
    in the other Stream in this Stream. This does not make
    copies of any elements, but simply stores all of them in this Stream.

    Optionally, provide a list of classes to include with the classFilter list.

    This method provides functionality like a shallow copy,
    but manages locations properly, only copies elements,
    and permits filtering by class type.

    ```python
    >>> s1 = stream.Stream()
    >>> s2 = stream.Stream()
    >>> n1 = note.Note('f#')
    >>> n2 = note.Note('g')
    >>> s1.append(n1)
    >>> s1.append(n2)
    >>> s2.mergeElements(s1)
    >>> len(s2)
    2
    >>> s1[0] is s2[0]
    True
    >>> s1[1] is s2[1]
    True
    ```

    ```python
    >>> viola = instrument.Viola()
    >>> trumpet = instrument.Trumpet()
    >>> s1.insert(0, viola)
    >>> s1.insert(0, trumpet)
    >>> s2.mergeElements(s1, classFilterList=('BrassInstrument',))
    >>> len(s2)
    3
    >>> viola in s2
    False
    ```

Stream.metronomeMarkBoundaries(*srcObj=None*)[[source]](../_modules/music21/stream/base.html#Stream.metronomeMarkBoundaries)
:   Return a list of offset start, offset end,
    MetronomeMark triples for all TempoIndication objects found
    in this Stream or a Stream provided by srcObj.

    If no MetronomeMarks are found, or an initial region does not
    have a MetronomeMark, a mark of quarter equal to 120 is provided as default.

    Note that if other TempoIndication objects are defined,
    they will be converted to MetronomeMarks and returned here

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note(), 8)
    >>> s.insert([6, tempo.MetronomeMark(number=240)])
    >>> s.metronomeMarkBoundaries()
    [(0.0, 6.0, <music21.tempo.MetronomeMark animato Quarter=120>),
     (6.0, 8.0, <music21.tempo.MetronomeMark Quarter=240>)]
    ```

Stream.offsetMap(*srcObj=None*)[[source]](../_modules/music21/stream/base.html#Stream.offsetMap)
:   Returns a list where each element is a NamedTuple
    consisting of the ‘offset’ of each element in a stream, the
    ‘endTime’ (that is, the offset plus the duration) and the
    ‘element’ itself. Also contains a ‘voiceIndex’ entry which
    contains the voice number of the element, or None if there
    are no voices.

    ```python
    >>> n1 = note.Note(type='quarter')
    >>> c1 = clef.AltoClef()
    >>> n2 = note.Note(type='half')
    >>> s1 = stream.Stream()
    >>> s1.append([n1, c1, n2])
    >>> om = s1.offsetMap()
    >>> om[2].offset
    1.0
    >>> om[2].endTime
    3.0
    >>> om[2].element is n2
    True
    >>> om[2].voiceIndex
    ```

    Needed for makeMeasures and a few other places.

    The Stream source of elements is self by default,
    unless a srcObj is provided. (this will be removed in v.8)

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note(), 8)
    >>> for om in s.offsetMap():
    ...     om
    OffsetMap(element=<music21.note.Note C>, offset=0.0, endTime=1.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=1.0, endTime=2.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=2.0, endTime=3.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=3.0, endTime=4.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=4.0, endTime=5.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=5.0, endTime=6.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=6.0, endTime=7.0, voiceIndex=None)
    OffsetMap(element=<music21.note.Note C>, offset=7.0, endTime=8.0, voiceIndex=None)
    ```

Stream.playingWhenAttacked(*el*, *elStream=None*)[[source]](../_modules/music21/stream/base.html#Stream.playingWhenAttacked)
:   Given an element (from another Stream) returns the single element
    in this Stream that is sounding while the given element starts.

    If there are multiple elements sounding at the moment it is
    attacked, the method returns the first element of the same class
    as this element, if any. If no element
    is of the same class, then the first element encountered is
    returned. For more complex usages, use allPlayingWhileSounding.

    Returns None if no elements fit the bill.

    The optional elStream is the stream in which el is found.
    If provided, el’s offset
    in that Stream is used. Otherwise, the current offset in
    el is used. It is just
    in case you are paranoid that el.offset might not be what
    you want, because of some fancy manipulation of
    el.activeSite

    ```python
    >>> n1 = note.Note('G#')
    >>> n2 = note.Note('D#')
    >>> s1 = stream.Stream()
    >>> s1.insert(20.0, n1)
    >>> s1.insert(21.0, n2)
    ```

    ```python
    >>> n3 = note.Note('C#')
    >>> s2 = stream.Stream()
    >>> s2.insert(20.0, n3)
    >>> s1.playingWhenAttacked(n3)
    <music21.note.Note G#>
    ```

    ```python
    >>> n3.setOffsetBySite(s2, 20.5)
    >>> s1.playingWhenAttacked(n3)
    <music21.note.Note G#>
    ```

    ```python
    >>> n3.setOffsetBySite(s2, 21.0)
    >>> n3.offset
    21.0
    >>> s1.playingWhenAttacked(n3)
    <music21.note.Note D#>
    ```

    If there is more than one item at the same time in the other stream
    then the first item matching the same class is returned, even if
    another element has a closer offset.

    ```python
    >>> n3.setOffsetBySite(s2, 20.5)
    >>> s1.insert(20.5, clef.BassClef())
    >>> s1.playingWhenAttacked(n3)
    <music21.note.Note G#>
    >>> fc = clef.FClef()  # superclass of BassClef
    >>> s2.insert(20.5, fc)
    >>> s1.playingWhenAttacked(fc)
    <music21.clef.BassClef>
    ```

    But since clefs have zero duration, moving the FClef ever so slightly
    will find the note instead

    ```python
    >>> fc.setOffsetBySite(s2, 20.6)
    >>> s1.playingWhenAttacked(fc)
    <music21.note.Note G#>
    ```

    Optionally, specify the site to get the offset from:

    ```python
    >>> n3.setOffsetBySite(s2, 21.0)
    >>> n3.setOffsetBySite(None, 100)
    >>> n3.activeSite = None
    >>> s1.playingWhenAttacked(n3) is None
    True
    >>> s1.playingWhenAttacked(n3, s2).name
    'D#'
    ```

Stream.plot(*plotFormat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *xValue: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *yValue: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *zValue: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *returnInNotebook: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Stream.plot)
:   Given a method and keyword configuration arguments, create and display a plot.

    Note: plot() requires the Python package matplotlib to be installed.

    For details on arguments this function takes, see
    [User’s Guide, Chapter 22: Graphing](../usersGuide/usersGuide_22_graphing.html#usersguide-22-graphing).

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> thePlot = s.plot('pianoroll')
    ```

    [![../_images/HorizontalBarPitchSpaceOffset.png](../_images/HorizontalBarPitchSpaceOffset.png)](../_images/HorizontalBarPitchSpaceOffset.png)

    By default, a plot is returned in normal Python environments, but not
    in Jupyter notebook/JupyterLab/Google Colab. The
    keyword returnInNotebook if True returns a plot no matter what.

    Changed in v9: Changed default for return in notebook, and added
    :   returnInNotebook keyword based on changes to recent Jupyter and
        similar releases.

Stream.pop(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")[[source]](../_modules/music21/stream/base.html#Stream.pop)
:   Return and remove the object found at the
    user-specified index value. Index values are
    those found in elements and are not necessary offset order.

    ```python
    >>> a = stream.Stream()
    >>> for i in range(12):  # notes C, C#, etc. to B
    ...     a.append(note.Note(i))
    >>> a.pop(0)
    <music21.note.Note C>
    >>> len(a)
    11
    ```

    If nothing is given, then it pops the last thing from the stream.

    ```python
    >>> a.pop()
    <music21.note.Note B>
    >>> len(a)
    10
    ```

Stream.quantize(*quarterLengthDivisors: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = ()*, *processOffsets: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *processDurations: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/stream/base.html#Stream.quantize)
:   Quantize time values in this Stream by snapping offsets
    and/or durations to the nearest multiple of a quarter length value
    given as one or more divisors of 1 quarter length. The quantized
    value found closest to a divisor multiple will be used.

    The quarterLengthDivisors provides a flexible way to provide quantization
    settings. For example, (2,) will snap all events to eighth note grid.
    (4, 3) will snap events to sixteenth notes and eighth note triplets,
    whichever is closer. (4, 6) will snap events to sixteenth notes and
    sixteenth note triplets. If quarterLengthDivisors is not specified then
    defaults.quantizationQuarterLengthDivisors is used. The default is (4, 3).

    processOffsets determines whether the Offsets are quantized.

    processDurations determines whether the Durations are quantized.

    Both are set to True by default. Setting both to False does nothing to the Stream.

    if inPlace is True, then the quantization is done on the Stream itself. If False
    (default) then a new quantized Stream of the same class is returned.

    If recurse is True, then all substreams are also quantized.
    If False (default), then only the highest level of the Stream is quantized.

    * Changed in v7:
      :   + recurse defaults False
          + look-ahead approach to choosing divisors to avoid gaps when processing durations

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 0.49
    >>> s = stream.Stream()
    >>> s.repeatInsert(n, [0.1, 0.49, 0.9])
    >>> nShort = note.Note()
    >>> nShort.quarterLength = 0.26
    >>> s.repeatInsert(nShort, [1.49, 1.76])
    ```

    ```python
    >>> s.quantize((4,), processOffsets=True, processDurations=True, inPlace=True)
    >>> [e.offset for e in s]
    [0.0, 0.5, 1.0, 1.5, 1.75]
    >>> [e.duration.quarterLength for e in s]
    [0.5, 0.5, 0.5, 0.25, 0.25]
    ```

    The error in quantization is set in the editorial attribute for the note in
    two places .offsetQuantizationError and .quarterLengthQuantizationError:

    ```python
    >>> [e.editorial.offsetQuantizationError for e in s.notes]
    [0.1, -0.01, -0.1, -0.01, 0.01]
    >>> [e.editorial.quarterLengthQuantizationError for e in s.notes]
    [-0.01, -0.01, -0.01, 0.01, 0.01]
    ```

    With default quarterLengthDivisors:

    ```python
    >>> s = stream.Stream()
    >>> s.repeatInsert(n, [0.1, 0.49, 0.9])
    >>> nShort = note.Note()
    >>> nShort.quarterLength = 0.26
    >>> s.repeatInsert(nShort, [1.49, 1.76])
    >>> quantized = s.quantize(processOffsets=True, processDurations=True, inPlace=False)
    >>> [e.offset for e in quantized]
    [0.0, 0.5, 1.0, 1.5, 1.75]
    >>> [e.duration.quarterLength for e in quantized]
    [0.5, 0.5, 0.5, 0.25, 0.25]
    ```

    Set recurse=True to quantize elements in substreams such as parts, measures, voices:

    ```python
    >>> myPart = converter.parse('tinynotation: c32 d32 e32 f32')
    >>> myPart.quantize(inPlace=True)
    >>> [e.offset for e in myPart.measure(1).notes]  # no change!
    [0.0, 0.125, 0.25, 0.375]
    ```

    ```python
    >>> myPart.quantize(inPlace=True, recurse=True)
    >>> [e.offset for e in myPart.measure(1).notes]
    [0.0, 0.0, 0.25, Fraction(1, 3)]
    ```

    * New in v7: if both processDurations and processOffsets are True, then
      the next note’s quantized offset is taken into account when quantizing the
      duration of the current note. This is to prevent unnecessary gaps from applying
      different quantization units to adjacent notes:

    ```python
    >>> s2 = stream.Stream()
    >>> nOddLength = note.Note(quarterLength=0.385)
    >>> s2.repeatInsert(nOddLength, [0, 0.5, 1, 1.5])
    >>> s2.show('t', addEndTimes=True)
        {0.0 - 0.385} <music21.note.Note C>
        {0.5 - 0.885} <music21.note.Note C>
        {1.0 - 1.385} <music21.note.Note C>
        {1.5 - 1.885} <music21.note.Note C>
    ```

    Before v.7, this would have yielded four triplet-eighths (separated by 1/6 QL rests):

    ```python
    >>> s2.quantize(processOffsets=True, processDurations=True, inPlace=True)
    >>> s2.show('text', addEndTimes=True)
        {0.0 - 0.5} <music21.note.Note C>
        {0.5 - 1.0} <music21.note.Note C>
        {1.0 - 1.5} <music21.note.Note C>
        {1.5 - 1.8333} <music21.note.Note C>
    ```

Stream.recurse(*\**, *streamsOnly: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *restoreActiveSites=True*, *classFilter=()*, *includeSelf=None*) → [RecursiveIterator](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType][[source]](../_modules/music21/stream/base.html#Stream.recurse)

Stream.recurse(*\**, *streamsOnly: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *restoreActiveSites=True*, *classFilter=()*, *includeSelf=None*) → [RecursiveIterator](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[[Stream](#music21.stream.base.Stream "music21.stream.base.Stream")]
:   .recurse() is a fundamental method of music21 for getting into
    elements contained in a Score, Part, or Measure, where elements such as
    notes are contained in sub-Stream elements.

    Returns an iterator that iterates over a list of Music21Objects
    contained in the Stream, starting with self’s elements (unless
    includeSelf=True in which case, it starts with the element itself),
    and whenever finding a Stream subclass in self,
    that Stream subclass’s elements.

    Here’s an example. Let’s create a simple score.

    ```python
    >>> s = stream.Score(id='mainScore')
    >>> p0 = stream.Part(id='part0')
    >>> p1 = stream.Part(id='part1')
    ```

    ```python
    >>> m01 = stream.Measure(number=1)
    >>> m01.append(note.Note('C', type='whole'))
    >>> m02 = stream.Measure(number=2)
    >>> m02.append(note.Note('D', type='whole'))
    >>> m11 = stream.Measure(number=1)
    >>> m11.append(note.Note('E', type='whole'))
    >>> m12 = stream.Measure(number=2)
    >>> m12.append(note.Note('F', type='whole'))
    ```

    ```python
    >>> p0.append([m01, m02])
    >>> p1.append([m11, m12])
    ```

    ```python
    >>> s.insert(0, p0)
    >>> s.insert(0, p1)
    >>> s.show('text')
    {0.0} <music21.stream.Part part0>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note C>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note D>
    {0.0} <music21.stream.Part part1>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note E>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note F>
    ```

    Now we could assign the .recurse() method to something,
    but that won’t have much effect:

    ```python
    >>> sRecurse = s.recurse()
    >>> sRecurse
    <music21.stream.iterator.RecursiveIterator for Score:mainScore @:0>
    ```

    So, that’s not how we use .recurse(). Instead, use it in a for loop:

    ```python
    >>> for el in s.recurse():
    ...     tup = (el, el.offset, el.activeSite)
    ...     print(tup)
    (<music21.stream.Part part0>, 0.0, <music21.stream.Score mainScore>)
    (<music21.stream.Measure 1 offset=0.0>, 0.0, <music21.stream.Part part0>)
    (<music21.note.Note C>, 0.0, <music21.stream.Measure 1 offset=0.0>)
    (<music21.stream.Measure 2 offset=4.0>, 4.0, <music21.stream.Part part0>)
    (<music21.note.Note D>, 0.0, <music21.stream.Measure 2 offset=4.0>)
    (<music21.stream.Part part1>, 0.0, <music21.stream.Score mainScore>)
    (<music21.stream.Measure 1 offset=0.0>, 0.0, <music21.stream.Part part1>)
    (<music21.note.Note E>, 0.0, <music21.stream.Measure 1 offset=0.0>)
    (<music21.stream.Measure 2 offset=4.0>, 4.0, <music21.stream.Part part1>)
    (<music21.note.Note F>, 0.0, <music21.stream.Measure 2 offset=4.0>)
    ```

    If we specify includeSelf=True then the original stream is also iterated:

    ```python
    >>> for el in s.recurse(includeSelf=True):
    ...     tup = (el, el.offset, el.activeSite)
    ...     print(tup)
    (<music21.stream.Score mainScore>, 0.0, None)
    (<music21.stream.Part part0>, 0.0, <music21.stream.Score mainScore>)
    (<music21.stream.Measure 1 offset=0.0>, 0.0, <music21.stream.Part part0>)
    (<music21.note.Note C>, 0.0, <music21.stream.Measure 1 offset=0.0>)
    ...
    ```

    Notice that like calling .show(‘text’), the offsets are relative to their containers.

    Compare the difference between putting .recurse().notes and .flatten().notes:

    ```python
    >>> for el in s.recurse().notes:
    ...     tup = (el, el.offset, el.activeSite)
    ...     print(tup)
    (<music21.note.Note C>, 0.0, <music21.stream.Measure 1 offset=0.0>)
    (<music21.note.Note D>, 0.0, <music21.stream.Measure 2 offset=4.0>)
    (<music21.note.Note E>, 0.0, <music21.stream.Measure 1 offset=0.0>)
    (<music21.note.Note F>, 0.0, <music21.stream.Measure 2 offset=4.0>)
    ```

    ```python
    >>> for el in s.flatten().notes:
    ...     tup = (el, el.offset, el.activeSite)
    ...     print(tup)
    (<music21.note.Note C>, 0.0, <music21.stream.Score mainScore_flatten>)
    (<music21.note.Note E>, 0.0, <music21.stream.Score mainScore_flatten>)
    (<music21.note.Note D>, 4.0, <music21.stream.Score mainScore_flatten>)
    (<music21.note.Note F>, 4.0, <music21.stream.Score mainScore_flatten>)
    ```

    If you don’t need correct offsets or activeSites, set restoreActiveSites to False.
    Then the last offset/activeSite will be used. It’s a bit of a speedup, but leads to some
    bad code, so use it only in highly optimized situations.

    We’ll also test using multiple classes here. The Stream given is the same as the
    s.flatten().notes stream.

    ```python
    >>> for el in s.recurse(classFilter=('Note', 'Rest'), restoreActiveSites=False):
    ...     tup = (el, el.offset, el.activeSite)
    ...     print(tup)
    (<music21.note.Note C>, 0.0, <music21.stream.Score mainScore_flatten>)
    (<music21.note.Note D>, 4.0, <music21.stream.Score mainScore_flatten>)
    (<music21.note.Note E>, 0.0, <music21.stream.Score mainScore_flatten>)
    (<music21.note.Note F>, 4.0, <music21.stream.Score mainScore_flatten>)
    ```

    So, this is pretty unreliable so don’t use it unless the tiny speedup is worth it.

    The other two attributes are pretty self-explanatory: streamsOnly will put only Streams
    in, while includeSelf will add the initial stream from recursion. If the inclusion or
    exclusion of self is important to you, put it in explicitly.

    ```python
    >>> for el in s.recurse(includeSelf=False, streamsOnly=True):
    ...     tup = (el, el.offset, el.activeSite)
    ...     print(tup)
    (<music21.stream.Part part0>, 0.0, <music21.stream.Score mainScore>)
    (<music21.stream.Measure 1 offset=0.0>, 0.0, <music21.stream.Part part0>)
    (<music21.stream.Measure 2 offset=4.0>, 4.0, <music21.stream.Part part0>)
    (<music21.stream.Part part1>, 0.0, <music21.stream.Score mainScore>)
    (<music21.stream.Measure 1 offset=0.0>, 0.0, <music21.stream.Part part1>)
    (<music21.stream.Measure 2 offset=4.0>, 4.0, <music21.stream.Part part1>)
    ```

    Warning

    Remember that like all iterators, it is dangerous to alter
    the components of the Stream being iterated over during iteration.
    if you need to edit while recursing, list(s.recurse()) is safer.

    * Changed in v5.5: All attributes are keyword only.
    * Changed in v8: removed parameter skipSelf. Use includeSelf instead.

Stream.recurseRepr(*\**, *prefixSpaces=0*, *addBreaks=True*, *addIndent=True*, *addEndTimes=False*, *useMixedNumerals=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.recurseRepr)
:   Used by .show(‘text’) to display a stream’s contents with offsets.

    ```python
    >>> s1 = stream.Stream()
    >>> s2 = stream.Stream()
    >>> s3 = stream.Stream()
    >>> n1 = note.Note()
    >>> s3.append(n1)
    >>> s2.append(s3)
    >>> s1.append(s2)
    >>> post = s1.recurseRepr(addBreaks=False, addIndent=False)
    >>> post
    '{0.0} <music21.stream.Stream ...> / {0.0} <...> / {0.0} <music21.note.Note C>'
    ```

    Made public in v7. Always calls on self.

Stream.remove(*targetOrList: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*, *\**, *shiftOffsets: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/stream/base.html#Stream.remove)
:   Remove an object from this Stream. Additionally, this Stream is
    removed from the object’s sites in [`Sites`](moduleSites.html#music21.sites.Sites "music21.sites.Sites").

    If a list of objects is passed, they will all be removed.
    If shiftOffsets is True, then offsets will be
    corrected after object removal. It is more efficient to pass
    a list of objects than to call remove on
    each object individually if shiftOffsets is True.

    ```python
    >>> import copy
    >>> s = stream.Stream()
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('g#')
    ```

    Copies of an object are not the same as the object

    ```python
    >>> n3 = copy.deepcopy(n2)
    >>> s.insert(10, n1)
    >>> s.insert(5, n2)
    >>> s.remove(n1)
    >>> len(s)
    1
    >>> s.insert(20, n3)
    >>> s.remove(n3)
    >>> [e for e in s] == [n2]
    True
    ```

    No error is raised if the target is not found.

    ```python
    >>> s.remove(n3)
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> c = clef.TrebleClef()
    >>> n1, n2, n3, n4 = note.Note('a'), note.Note('b'), note.Note('c'), note.Note('d')
    >>> n5, n6, n7, n8 = note.Note('e'), note.Note('f'), note.Note('g'), note.Note('a')
    >>> s2.insert(0.0, c)
    >>> s2.append([n1, n2, n3, n4, n5, n6, n7, n8])
    >>> s2.remove(n1, shiftOffsets=True)
    >>> s2.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.note.Note B>
    {1.0} <music21.note.Note C>
    {2.0} <music21.note.Note D>
    {3.0} <music21.note.Note E>
    {4.0} <music21.note.Note F>
    {5.0} <music21.note.Note G>
    {6.0} <music21.note.Note A>
    ```

    ```python
    >>> s2.remove([n3, n6, n4], shiftOffsets=True)
    >>> s2.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.note.Note B>
    {1.0} <music21.note.Note E>
    {2.0} <music21.note.Note G>
    {3.0} <music21.note.Note A>
    ```

    With the recurse=True parameter, we can remove elements deeply nested.
    However, shiftOffsets
    does not work with recurse=True yet.

    ```python
    >>> p1 = stream.Part()
    >>> m1 = stream.Measure(number=1)
    >>> c = clef.BassClef()
    >>> m1.insert(0, c)
    >>> m1.append(note.Note(type='whole'))
    >>> p1.append(m1)
    >>> m2 = stream.Measure(number=2)
    >>> n2 = note.Note('D', type='half')
    >>> m2.append(n2)
    >>> n3 = note.Note(type='half')
    >>> m2.append(n3)
    >>> p1.append(m2)
    >>> p1.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.note.Note C>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note D>
        {2.0} <music21.note.Note C>
    ```

    Without recurse=True:

    ```python
    >>> p1.remove(n2)
    >>> p1.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.note.Note C>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note D>
        {2.0} <music21.note.Note C>
    ```

    With recurse=True:

    ```python
    >>> p1.remove(n2, recurse=True)
    >>> p1.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.note.Note C>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {2.0} <music21.note.Note C>
    ```

    With recurse=True and a list to remove:

    ```python
    >>> p1.remove([c, n3], recurse=True)
    >>> p1.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.note.Note C>
    {4.0} <music21.stream.Measure 2 offset=4.0>
    ```

    Can also remove elements stored at end:

    ```python
    >>> streamWithBarline = stream.Stream(note.Note())
    >>> barline = bar.Barline('final')
    >>> streamWithBarline.storeAtEnd(barline)
    >>> barline in streamWithBarline
    True
    >>> streamWithBarline.remove(barline)
    >>> barline in streamWithBarline
    False
    ```

    * Changed in v5.3: firstMatchOnly removed – impossible to have element
      in stream twice. recurse and shiftOffsets changed to keywordOnly arguments

Stream.removeByClass(*classFilterList*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.removeByClass)
:   Remove all elements from the Stream
    based on one or more classes given
    in a list.

    ```python
    >>> s = stream.Stream()
    >>> s.append(meter.TimeSignature('4/4'))
    >>> s.repeatAppend(note.Note('C'), 8)
    >>> len(s)
    9
    >>> s.removeByClass('GeneralNote')
    >>> len(s)
    1
    >>> len(s.notes)
    0
    ```

    Test that removing from end elements works.

    ```python
    >>> s = stream.Measure()
    >>> s.append(meter.TimeSignature('4/4'))
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s.rightBarline = bar.Barline('final')
    >>> len(s)
    6
    >>> s.removeByClass('Barline')
    >>> len(s)
    5
    ```

Stream.removeByNotOfClass(*classFilterList*)[[source]](../_modules/music21/stream/base.html#Stream.removeByNotOfClass)
:   Remove all elements not of the specified
    class or subclass in the Stream in place.

    ```python
    >>> s = stream.Stream()
    >>> s.append(meter.TimeSignature('4/4'))
    >>> s.repeatAppend(note.Note('C'), 8)
    >>> len(s)
    9
    >>> s.removeByNotOfClass(meter.TimeSignature)
    >>> len(s)
    1
    >>> len(s.notes)
    0
    ```

Stream.repeatAppend(*item*, *numberOfTimes*)[[source]](../_modules/music21/stream/base.html#Stream.repeatAppend)
:   Given an object and a number, run append that many times on
    a deepcopy of the object.
    numberOfTimes should of course be a positive integer.

    ```python
    >>> a = stream.Stream()
    >>> n = note.Note('D--')
    >>> n.duration.type = 'whole'
    >>> a.repeatAppend(n, 10)
    >>> a.show('text')
    {0.0} <music21.note.Note D-->
    {4.0} <music21.note.Note D-->
    {8.0} <music21.note.Note D-->
    {12.0} <music21.note.Note D-->
    ...
    {36.0} <music21.note.Note D-->
    ```

    ```python
    >>> a.duration.quarterLength
    40.0
    >>> a[9].offset
    36.0
    ```

Stream.repeatInsert(*item*, *offsets*)[[source]](../_modules/music21/stream/base.html#Stream.repeatInsert)
:   Given an object, create a deep copy of each object at
    each position specified by the offset list:

    ```python
    >>> a = stream.Stream()
    >>> n = note.Note('G-')
    >>> n.quarterLength = 1
    ```

    ```python
    >>> a.repeatInsert(n, [0, 2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12])
    >>> len(a)
    13
    >>> a[10].offset
    10.0
    ```

Stream.replace(*target: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *replacement: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *allDerived: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.replace)
:   Given a target object, replace it with
    the supplied replacement object.

    Does nothing if target cannot be found. Raises StreamException if replacement
    is already in the stream.

    If allDerived is True (as it is by default), all sites (stream) that
    this stream derives from and also
    have a reference for the replacement will be similarly changed.
    This is useful for altering both a flattened and nested representation.

    ```python
    >>> cSharp = note.Note('C#4')
    >>> s = stream.Stream()
    >>> s.insert(0, cSharp)
    >>> dFlat = note.Note('D-4')
    >>> s.replace(cSharp, dFlat)
    >>> s.show('t')
    {0.0} <music21.note.Note D->
    ```

    If allDerived is True then all streams that this stream comes from get changed
    (but not non-derived streams)

    ```python
    >>> otherStream = stream.Stream()
    >>> otherStream.insert(0, dFlat)
    >>> f = note.Note('F4')
    >>> sf = s.flatten()
    >>> sf is not s
    True
    >>> sf.replace(dFlat, f, allDerived=True)
    >>> sf[0] is f
    True
    >>> s[0] is f
    True
    >>> otherStream[0] is dFlat
    True
    ```

    Note that it does not work the other way: if we made the replacement on s
    then sf, the flattened representation, would not be changed, since s
    does not derive from sf but vice versa.

    With recurse=True, a stream can replace an element that is
    further down in the hierarchy. First let’s set up a
    nested score:

    ```python
    >>> s = stream.Score()
    >>> p = stream.Part(id='part1')
    >>> s.append(p)
    >>> m = stream.Measure()
    >>> p.append(m)
    >>> cSharp = note.Note('C#4')
    >>> m.append(cSharp)
    >>> s.show('text')
    {0.0} <music21.stream.Part part1>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.note.Note C#>
    ```

    Now make a deep-nested replacement

    ```python
    >>> dFlat = note.Note('D-4')
    >>> s.replace(cSharp, dFlat, recurse=True)
    >>> s.show('text')
    {0.0} <music21.stream.Part part1>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.note.Note D->
    ```

    * Changed by v5: allTargetSites renamed to allDerived – only
      searches in derivation chain.
    * Changed in v5.3: firstMatchOnly removed – impossible to have element
      in stream twice. recurse and shiftOffsets changed to keywordOnly arguments
    * Changed in v6: recurse works
    * Changed in v7: raises StreamException if replacement is already in the stream.

Stream.scaleDurations(*amountToScale*, *\**, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.scaleDurations)
:   Scale all durations by a provided scalar. Offsets are not modified.

    To augment or diminish a Stream, see the
    `augmentOrDiminish()` method.

    We do not retain durations in any circumstance;
    if inPlace=False, two deepcopies of each duration are done.

Stream.scaleOffsets(*amountToScale*, *\**, *anchorZero='lowest'*, *anchorZeroRecurse=None*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.scaleOffsets)
:   Scale all offsets by a multiplication factor given
    in amountToScale. Durations are not altered.

    To augment or diminish a Stream,
    see the `augmentOrDiminish()` method.

    The anchorZero parameter determines if and/or where
    the zero offset is established for the set of
    offsets in this Stream before processing.
    Offsets are shifted to make either the lower
    or upper values the new zero; then offsets are scaled;
    then the shifts are removed. Accepted values are None
    (no offset shifting), “lowest”, or “highest”.

    The anchorZeroRecurse parameter determines the
    anchorZero for all embedded Streams, and Streams
    embedded within those Streams. If the lowest offset
    in an embedded Stream is non-zero, setting this value
    to None will allow the space between the start of that
    Stream and the first element to be scaled. If the
    lowest offset in an embedded Stream is non-zero,
    setting this value to ‘lowest’ will not alter the
    space between the start of that Stream and the first
    element to be scaled.

    To shift all the elements in a Stream, see the
    `shiftElements()` method.

    * Changed in v5: inPlace is default False, and anchorZero, anchorZeroRecurse
      and inPlace are keyword only arguments.

Stream.setDerivationMethod(*derivationMethod: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *recurse=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.setDerivationMethod)
:   Sets the .derivation.method for each element in the Stream
    if it has a .derivation object.

    ```python
    >>> import copy
    >>> s = converter.parse('tinyNotation: 2/4 c2 d e f')
    >>> s2 = copy.deepcopy(s)
    >>> s2.recurse().notes[-1].derivation
    <Derivation of <music21.note.Note F> from <music21.note.Note F> via '__deepcopy__'>
    >>> s2.setDerivationMethod('exampleCopy', recurse=True)
    >>> s2.recurse().notes[-1].derivation
    <Derivation of <music21.note.Note F> from <music21.note.Note F> via 'exampleCopy'>
    ```

    Without recurse:

    ```python
    >>> s = converter.parse('tinyNotation: 2/4 c2 d e f')
    >>> s2 = copy.deepcopy(s)
    >>> s2.setDerivationMethod('exampleCopy')
    >>> s2.recurse().notes[-1].derivation
    <Derivation of <music21.note.Note F> from <music21.note.Note F> via '__deepcopy__'>
    ```

Stream.setElementOffset(*element: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [OffsetSpecial](moduleCommonEnums.html#music21.common.enums.OffsetSpecial "music21.common.enums.OffsetSpecial")*)[[source]](../_modules/music21/stream/base.html#Stream.setElementOffset)
:   Sets the Offset for an element that is already in a given stream.

    Set up a note in two different streams at two different offsets:

    ```python
    >>> n = note.Note('B-4')
    >>> s = stream.Stream(id='Stream1')
    >>> s.insert(10, n)
    >>> n.offset
    10.0
    >>> n.activeSite.id
    'Stream1'
    ```

    ```python
    >>> s2 = stream.Stream(id='Stream2')
    >>> s2.insert(30, n)
    >>> n.activeSite.id
    'Stream2'
    ```

    Now change the note’s offset in Stream1:

    ```python
    >>> s.setElementOffset(n, 20.0)
    ```

    This call has the effect of switching the activeSite of n to s.

    ```python
    >>> n.activeSite.id
    'Stream1'
    >>> n.offset
    20.0
    >>> n.getOffsetBySite(s)
    20.0
    ```

    If the element is not in the Stream, raises a StreamException:

    ```python
    >>> n2 = note.Note('D')
    >>> s.setElementOffset(n2, 30.0)
    Traceback (most recent call last):
    music21.exceptions21.StreamException: Cannot set the offset for element
        <music21.note.Note D>, not in Stream <music21.stream.Stream Stream1>.
    ```

    * Changed in v5.5: also sets .activeSite for the element
    * Changed in v6.7: also runs coreElementsChanged()
    * Changed in v7: addElement is removed;
      see `coreSetElementOffset()`

Stream.shiftElements(*offset*, *startOffset=None*, *endOffset=None*, *classFilterList=None*)[[source]](../_modules/music21/stream/base.html#Stream.shiftElements)
:   Add the given offset value to every offset of
    the objects found in the Stream. Objects that are
    specifically placed at the end of the Stream via
    .storeAtEnd() (such as right barlines) are
    not affected.

    If startOffset is given then elements before
    that offset will not be shifted. If endOffset is given
    then all elements at or after this offset will be not be shifted.

    ```python
    >>> a = stream.Stream()
    >>> a.repeatInsert(note.Note('C'), list(range(10)))
    >>> a.shiftElements(30)
    >>> a.lowestOffset
    30.0
    >>> a.shiftElements(-10)
    >>> a.lowestOffset
    20.0
    ```

    Use shiftElements to move elements after a change in
    duration:

    ```python
    >>> st2 = stream.Stream()
    >>> st2.insert(0, note.Note('D4', type='whole'))
    >>> st2.repeatInsert(note.Note('C4'), list(range(4, 8)))
    >>> st2.show('text')
    {0.0} <music21.note.Note D>
    {4.0} <music21.note.Note C>
    {5.0} <music21.note.Note C>
    {6.0} <music21.note.Note C>
    {7.0} <music21.note.Note C>
    ```

    Now make the first note a dotted whole note and shift the rest by two quarters:

    ```python
    >>> firstNote = st2[0]
    >>> firstNoteOldQL = firstNote.quarterLength
    >>> firstNote.duration.dots = 1
    >>> firstNoteNewQL = firstNote.quarterLength
    >>> shiftAmount = firstNoteNewQL - firstNoteOldQL
    >>> shiftAmount
    2.0
    ```

    ```python
    >>> st2.shiftElements(shiftAmount, startOffset=4.0)
    >>> st2.show('text')
    {0.0} <music21.note.Note D>
    {6.0} <music21.note.Note C>
    {7.0} <music21.note.Note C>
    {8.0} <music21.note.Note C>
    {9.0} <music21.note.Note C>
    ```

    A class filter list may be given. It must be an iterable.

    ```python
    >>> st2.insert(7.5, key.Key('F'))
    >>> st2.shiftElements(2/3, startOffset=6.0, endOffset=8.0,
    ...                   classFilterList=[note.Note])
    >>> st2.show('text')
    {0.0} <music21.note.Note D>
    {6.6667} <music21.note.Note C>
    {7.5} <music21.key.Key of F major>
    {7.6667} <music21.note.Note C>
    {8.0} <music21.note.Note C>
    {9.0} <music21.note.Note C>
    ```

Stream.show(*fmt=None*, *app=None*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Stream.show)
:   Displays an object in a format provided by the
    fmt argument or, if not provided, the format set in the user’s Environment

    Valid formats include (but are not limited to):

    ```python
    musicxml
    text
    midi
    lily (or lilypond)
    lily.png
    lily.pdf
    lily.svg
    braille
    vexflow
    musicxml.png
    ```

    N.B. score.write(‘lily’) returns a bare lilypond file,
    score.show(‘lily’) runs it through lilypond and displays it as a png.

    Some formats, including .musicxml, create a copy of the stream, pack it into a well-formed
    score if necessary, and run `makeNotation()`. To
    avoid this when showing .musicxml, use makeNotation=False, an advanced option
    that prioritizes speed but may not guarantee satisfactory notation.

Stream.showVariantAsOssialikePart(*containedPart*, *variantGroups*, *\**, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.showVariantAsOssialikePart)
:   Takes a part within the score and a list of variant groups within that part.
    Puts the variant object
    in a part surrounded by hidden rests to mimic the appearance of an ossia despite limited
    musicXML support for ossia staves. Note that this will ignore variants with .lengthType
    ‘elongation’ and ‘deletion’ as there is no good way to represent ossia staves like those
    by this method.

    ```python
    >>> sPartStr = 'd4 e4 f4 g4   a2 b-4 a4    g4 a8 g8 f4 e4    d2 a2 '
    >>> v1Str =    '              a2. b-8 a8 '
    >>> v2Str =    '                                             d4 f4 a2 '
    ```

    ```python
    >>> sPartStr += "d4 e4 f4 g4    a2 b-4 a4    g4 a8 b-8 c'4 c4    f1"
    ```

    ```python
    >>> sPartStream = converter.parse('tinynotation: 4/4 ' + sPartStr)
    >>> sPartStream.makeMeasures(inPlace=True)  # maybe not necessary?
    >>> v1stream = converter.parse('tinynotation: 4/4 ' + v1Str)
    >>> v2stream = converter.parse('tinynotation: 4/4 ' + v2Str)
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
    >>> v2measure = stream.Measure()
    >>> v2.insert(0.0, v2measure)
    >>> for e in v2stream.notesAndRests:
    ...    v2measure.insert(e.offset, e)
    ```

    ```python
    >>> v3 = variant.Variant()
    >>> v2.replacementDuration = 4.0
    >>> v3.replacementDuration = 4.0
    >>> v1.groups = ['variant1']
    >>> v2.groups = ['variant2']
    >>> v3.groups = ['variant3']
    ```

    ```python
    >>> sPart = stream.Part()
    >>> for e in sPartStream:
    ...    sPart.insert(e.offset, e)
    ```

    ```python
    >>> sPart.insert(4.0, v1)
    >>> sPart.insert(12.0, v2)
    >>> sPart.insert(20.0, v3)  # This is a deletion variant and will be skipped
    >>> s = stream.Score()
    >>> s.insert(0.0, sPart)
    >>> streamWithOssia = s.showVariantAsOssialikePart(sPart,
    ...          ['variant1', 'variant2', 'variant3'], inPlace=False)
    >>> streamWithOssia.show()
    ```

Stream.simultaneousAttacks(*stream2*)[[source]](../_modules/music21/stream/base.html#Stream.simultaneousAttacks)
:   returns an ordered list of offsets where elements are started (attacked)
    at the same time in both self and stream2.

    In this example, we create one stream of Qtr, Half, Qtr, and one of Half, Qtr, Qtr.
    There are simultaneous attacks at offset 0.0 (the beginning) and at offset 3.0,
    but not at 1.0 or 2.0:

    ```python
    >>> st1 = stream.Stream()
    >>> st2 = stream.Stream()
    >>> st1.append([note.Note(type='quarter'),
    ...             note.Note(type='half'),
    ...             note.Note(type='quarter')])
    >>> st2.append([note.Note(type='half'),
    ...             note.Note(type='quarter'),
    ...             note.Note(type='quarter')])
    >>> print(st1.simultaneousAttacks(st2))
    [0.0, 3.0]
    ```

Stream.sliceAtOffsets(*offsetList*, *target=None*, *addTies=True*, *inPlace=False*, *displayTiedAccidentals=False*)[[source]](../_modules/music21/stream/base.html#Stream.sliceAtOffsets)
:   Given a list of quarter lengths, slice and optionally tie all
    Music21Objects crossing these points.

    ```python
    >>> s = stream.Stream()
    >>> n = note.Note()
    >>> n.duration.type = 'whole'
    >>> s.append(n)
    >>> post = s.sliceAtOffsets([1, 2, 3], inPlace=True)
    >>> [(e.offset, e.quarterLength) for e in s]
    [(0.0, 1.0), (1.0, 1.0), (2.0, 1.0), (3.0, 1.0)]
    ```

Stream.sliceByBeat(*target=None*, *addTies=True*, *inPlace=False*, *displayTiedAccidentals=False*)[[source]](../_modules/music21/stream/base.html#Stream.sliceByBeat)
:   Slice all elements in the Stream that have a Duration at
    the offsets determined to be the beat from the local TimeSignature.

    * Changed in v7: return None if inPlace is True

Stream.sliceByGreatestDivisor(*\**, *addTies=True*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.sliceByGreatestDivisor)
:   Slice all [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") objects on all Notes and Rests of this Stream.
    Duration are sliced according to the approximate GCD found in all durations.

Stream.sliceByQuarterLengths(*quarterLengthList*, *\**, *target=None*, *addTies=True*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.sliceByQuarterLengths)
:   Slice all [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") objects on all Notes and Rests
    of this Stream.
    Duration are sliced according to values provided in quarterLengthList list.
    If the sum of these values is less than the Duration, the values are accumulated
    in a loop to try to fill the Duration. If a match cannot be found, an
    Exception is raised.

    If target is None, the entire Stream is processed. Otherwise, only the element
    specified is manipulated.

Stream.sort(*force=False*)[[source]](../_modules/music21/stream/base.html#Stream.sort)
:   Sort this Stream in place by offset, then priority, then
    standard class sort order (e.g., Clefs before KeySignatures before
    TimeSignatures).

    Note that Streams automatically sort themselves unless
    autoSort is set to False (as in the example below)

    If force is True, a sort will be attempted regardless of any other parameters.

    ```python
    >>> n1 = note.Note('A')
    >>> n2 = note.Note('B')
    >>> s = stream.Stream()
    >>> s.autoSort = False
    >>> s.insert(100, n2)
    >>> s.insert(0, n1)  # now a has a lower offset by higher index
    >>> [n.name for n in s]
    ['B', 'A']
    >>> s[0].name
    'B'
    >>> s.sort()
    >>> s[0].name
    'A'
    >>> [n.name for n in s]
    ['A', 'B']
    ```

Stream.sorted()[[source]](../_modules/music21/stream/base.html#Stream.sorted)
:   (TL;DR: you probably do not need to call this method unless you have turned .autoSort to
    off.)

    Returns a new Stream where all the elements are sorted according to offset time, then
    priority, then classSortOrder (so that, for instance, a Clef at offset 0 appears before
    a Note at offset 0).

    If this Stream is not flat, then only the elements directly in the stream itself are sorted.
    To sort all, run myStream.flatten().sorted().

    For instance, here is an unsorted Stream:

    ```python
    >>> s = stream.Stream()
    >>> s.autoSort = False  # if True, sorting is automatic
    >>> s.insert(1, note.Note('D'))
    >>> s.insert(0, note.Note('C'))
    >>> s.show('text')
    {1.0} <music21.note.Note D>
    {0.0} <music21.note.Note C>
    ```

    But a sorted version of the Stream puts the C first:

    ```python
    >>> s.sorted().show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    ```

    While the original stream remains unsorted:

    ```python
    >>> s.show('text')
    {1.0} <music21.note.Note D>
    {0.0} <music21.note.Note C>
    ```

Stream.splitAtDurations(*\**, *recurse=False*) → \_SplitTuple[[source]](../_modules/music21/stream/base.html#Stream.splitAtDurations)
:   Overrides base method [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations")
    so that once each element in the stream having a complex duration is split
    into similar, shorter elements representing each duration component,
    the original element is actually replaced in the stream where it was found
    with those new elements.

    Returns a 1-tuple containing itself, for consistency with the superclass method.

    ```python
    >>> s = stream.Stream()
    >>> s.insert(note.Note(quarterLength=5.0))
    >>> post = s.splitAtDurations()
    >>> post
    (<music21.stream.Stream 0x10955ceb0>,)
    >>> [n.duration for n in s]
    [<music21.duration.Duration 4.0>, <music21.duration.Duration 1.0>]
    ```

    Unless recurse=True, notes in substreams will not be found.

    ```python
    >>> s2 = stream.Score()
    >>> p = stream.Part([note.Note(quarterLength=5)])
    >>> s2.append(p)
    >>> s2.splitAtDurations()
    (<music21.stream.Score 0x10d12f100>,)
    >>> [n.duration for n in s2.recurse().notes]
    [<music21.duration.Duration 5.0>]
    >>> s2.splitAtDurations(recurse=True)
    (<music21.stream.Score 0x10d12f100>,)
    >>> [n.duration for n in s2.recurse().notes]
    [<music21.duration.Duration 4.0>, <music21.duration.Duration 1.0>]
    ```

    recurse=True should not be necessary to find elements in streams
    without substreams, such as a loose Voice:

    ```python
    >>> v = stream.Voice([note.Note(quarterLength=5.5)], id=1)
    >>> v.splitAtDurations()
    (<music21.stream.Voice 1>,)
    >>> [n.duration for n in v.notes]
    [<music21.duration.Duration 4.0>, <music21.duration.Duration 1.5>]
    ```

    But a Voice in a Measure (most common) will not be found without recurse:

    ```python
    >>> m = stream.Measure()
    >>> v2 = stream.Voice([note.Note(quarterLength=5.25)])
    >>> m.insert(v2)
    >>> m.splitAtDurations()
    (<music21.stream.Measure 0 offset=0.0>,)
    >>> [n.duration for n in m.recurse().notes]
    [<music21.duration.Duration 5.25>]
    ```

    For any spanner containing the element being removed, the first or last of the
    replacing components replaces the removed element
    (according to whether it was first or last in the spanner.)

    ```python
    >>> s3 = stream.Stream()
    >>> n1 = note.Note(quarterLength=5)
    >>> n2 = note.Note(quarterLength=5)
    >>> s3.append([n1, n2])
    >>> s3.insert(0, spanner.Slur([n1, n2]))
    >>> post = s3.splitAtDurations()
    >>> s3.spanners.first().getFirst() is n1
    False
    >>> s3.spanners.first().getFirst().duration
    <music21.duration.Duration 4.0>
    >>> s3.spanners.first().getLast().duration
    <music21.duration.Duration 1.0>
    ```

    Does not act on rests where .fullMeasure is True or ‘always’,
    nor when .fullMeasure is ‘auto’ and the duration equals the .barDuration.
    This is because full measure rests are usually represented
    as a single whole rest regardless of their duration.

    ```python
    >>> r = note.Rest(quarterLength=5.0)
    >>> r.fullMeasure = 'auto'
    >>> v = stream.Voice(r)
    >>> m = stream.Measure(v)
    >>> result = m.splitAtDurations(recurse=True)
    >>> list(result[0][note.Rest])
    [<music21.note.Rest 5ql>]
    ```

    Here is a rest that doesn’t fill the measure:

    ```python
    >>> m.insert(0, meter.TimeSignature('6/4'))
    >>> result = m.splitAtDurations(recurse=True)
    >>> list(result[0][note.Rest])
    [<music21.note.Rest whole>, <music21.note.Rest quarter>]
    ```

    But by calling it a full-measure rest, we won’t try to split it:

    ```python
    >>> r2 = note.Rest(quarterLength=5.0)
    >>> r2.fullMeasure = True
    >>> m2 = stream.Measure(r2)
    >>> m2.insert(0, meter.TimeSignature('6/4'))
    >>> result = m2.splitAtDurations()
    >>> list(result[0][note.Rest])
    [<music21.note.Rest 5ql>]
    ```

Stream.splitAtQuarterLength(*quarterLength*, *\**, *retainOrigin=True*, *addTies=True*, *displayTiedAccidentals=False*, *searchContext=True*) → \_SplitTuple[[source]](../_modules/music21/stream/base.html#Stream.splitAtQuarterLength)
:   This method overrides the method on Music21Object to provide
    similar functionality for Streams.

    Most arguments are passed to Music21Object.splitAtQuarterLength.

    * Changed in v7: all but quarterLength are keyword only

Stream.splitByClass(*classObj*, *fx*)[[source]](../_modules/music21/stream/base.html#Stream.splitByClass)
:   Given a stream, get all objects of type classObj and divide them into
    two new streams depending on the results of fx.
    Fx should be a lambda or other function on elements.
    All elements where fx returns “True” go in the first stream.
    All other elements are put in the second stream.

    If classObj is None then all elements are returned. ClassObj
    can also be a list of classes.

    In this example, we will create 50 notes from midi note 30 (two
    octaves and a tritone below middle C) to midi note 80 (an octave
    and a minor sixth above middle C) and add them to a Stream.
    We then create a lambda function to split between those notes
    below middle C (midi note 60) and those above
    (google “lambda functions in Python” for more information on
    what these powerful tools are).

    ```python
    >>> stream1 = stream.Stream()
    >>> for x in range(30, 81):
    ...     n = note.Note()
    ...     n.pitch.midi = x
    ...     stream1.append(n)
    >>> fx = lambda n: n.pitch.midi < 60
    >>> b, c = stream1.splitByClass(note.Note, fx)
    ```

    Stream b now contains all the notes below middle C,
    that is, 30 notes, beginning with F#1 and ending with B3
    while Stream c has the 21 notes from C4 to A-5:

    ```python
    >>> len(b)
    30
    >>> (b[0].nameWithOctave, b[-1].nameWithOctave)
    ('F#1', 'B3')
    >>> len(c)
    21
    >>> (c[0].nameWithOctave, c[-1].nameWithOctave)
    ('C4', 'G#5')
    ```

Stream.storeAtEnd(*itemOrList*, *ignoreSort=False*)[[source]](../_modules/music21/stream/base.html#Stream.storeAtEnd)
:   Inserts an item or items at the end of the Stream,
    stored in the special box (called \_endElements).

    This method is useful for putting things such as
    right bar lines or courtesy clefs that should always
    be at the end of a Stream no matter what else is appended
    to it.

    As sorting is done only by priority and class,
    it cannot avoid setting isSorted to False.

    ```python
    >>> s = stream.Stream()
    >>> b = bar.Repeat()
    >>> s.storeAtEnd(b)
    >>> b in s
    True
    >>> s.elementOffset(b)
    0.0
    >>> s.elementOffset(b, returnSpecial=True)
    <OffsetSpecial.AT_END>
    ```

    Only elements of zero duration can be stored. Otherwise, a
    StreamException is raised.

Stream.stripTies(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *matchByPitch: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.stripTies)

Stream.stripTies(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *matchByPitch: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → StreamType
:   Find all notes that are tied; remove all tied notes,
    then make the first of the tied notes have a duration
    equal to that of all tied constituents. Lastly,
    remove the formerly-tied notes.

    This method can be used on Stream and Stream subclasses.
    When used on a stream containing Part-like substreams, as with many scores,
    `Part`, `Measure`, and other
    Stream subclasses are retained.

    inPlace controls whether the input stream is modified or whether a deep copy
    is made. (New in v7, to conform to the rest of music21, inPlace=True returns None.)

    Presently, this only works if tied notes are sequential in the same voice; ultimately
    this will need to look at .to and .from attributes (if they exist)

    ```python
    >>> a = stream.Stream()
    >>> n = note.Note()
    >>> n.quarterLength = 6
    >>> a.append(n)
    >>> m = a.makeMeasures()
    >>> m.makeTies(inPlace=True)
    >>> len(m.flatten().notes)
    2
    ```

    ```python
    >>> m = m.stripTies()
    >>> len(m.flatten().notes)
    1
    ```

    In cases where notes are manipulated after initial tie creation,
    some chord members might lack ties. This will not prevent merging the tied notes
    if all the pitches match, and matchByPitch=True (default):

    ```python
    >>> c1 = chord.Chord('C4 E4')
    >>> c1.tie = tie.Tie('start')
    ```

    ```python
    >>> c2 = chord.Chord('C4 E4')
    >>> c2.tie = tie.Tie('stop')
    ```

    ```python
    >>> m = stream.Measure()
    >>> m.append([c1, c2])
    ```

    ```python
    >>> c1.add(note.Note('G4'))
    >>> c2.add(note.Note('G4'))
    ```

    ```python
    >>> c2.notes[-1].tie is None
    True
    ```

    ```python
    >>> strippedPitchMatching = m.stripTies()
    >>> len(strippedPitchMatching.flatten().notes)
    1
    ```

    This can be prevented with matchByPitch=False, in which case every note,
    including each chord member, must have “stop” and/or “continue” tie types,
    which was not the case above:

    ```python
    >>> strippedMixedTieTypes = m.stripTies(matchByPitch=False)
    >>> len(strippedMixedTieTypes.flatten().notes)
    2
    ```

    ```python
    >>> c2.notes[0].tie = tie.Tie('stop')
    >>> c2.notes[1].tie = tie.Tie('stop')
    >>> c2.notes[2].tie = tie.Tie('stop')
    >>> strippedUniformTieTypes = m.stripTies(matchByPitch=False)
    >>> len(strippedUniformTieTypes.flatten().notes)
    1
    ```

    Notice the matching happens even after altering the pitches:

    ```python
    >>> c3 = c2.transpose(6)
    >>> otherM = stream.Measure([c1, c3])
    >>> strippedTransposed = otherM.stripTies(matchByPitch=False)
    >>> len(strippedTransposed.flatten().notes)
    1
    ```

    When matchByPitch is True (as it is by default) the following
    behavior defined regarding chords with a tie type “continue”:

    ```python
    >>> c1.notes[0].tie = tie.Tie('continue')
    >>> c1.notes[1].tie = tie.Tie('start')
    >>> c1.notes[2].tie = tie.Tie('start')
    ```

    Continue is accepted here as an ersatz-start:

    ```python
    >>> stripped1 = m.stripTies(matchByPitch=True)
    >>> len(stripped1.flatten().notes)
    1
    ```

    But prepend an element so that it’s considered as a tie continuation:

    ```python
    >>> c0 = chord.Chord('C4 E4 G4')
    >>> c0.tie = tie.Tie('start')
    >>> m2 = stream.Measure()
    >>> m2.append([c0, c1, c2])
    ```

    Now the mixed tie types on c1 will only be connected to c2
    on the permissive option (matchByPitch=True):

    ```python
    >>> stripped2 = m2.stripTies(matchByPitch=True)
    >>> stripped2.elements
    (<music21.chord.Chord C4 E4 G4>,)
    ```

    ```python
    >>> stripped3 = m2.stripTies(matchByPitch=False)
    >>> stripped3.elements
    (<music21.chord.Chord C4 E4 G4>,
     <music21.chord.Chord C4 E4 G4>,
     <music21.chord.Chord C4 E4 G4>)
    ```

    Now correct the tie types on c1 and try the strict option:

    ```python
    >>> c1.notes[0].tie = tie.Tie('continue')
    >>> c1.notes[1].tie = tie.Tie('continue')
    >>> c1.notes[2].tie = tie.Tie('continue')
    >>> stripped4 = m2.stripTies(matchByPitch=False)
    >>> stripped4.elements
    (<music21.chord.Chord C4 E4 G4>,)
    ```

    Now replace the first element with just a single C4 note.
    The following chords will be merged with each other, but not with the single
    note, even on matchByPitch=False.
    (matchByPitch=False is permissive about pitch but strict about cardinality.)

    ```python
    >>> newC = note.Note('C4')
    >>> newC.tie = tie.Tie('start')
    >>> m2.replace(c0, newC)
    >>> stripped5 = m2.stripTies(matchByPitch=False)
    >>> stripped5.elements
    (<music21.note.Note C>, <music21.chord.Chord C4 E4 G4>)
    ```

    * Changed in v7: matchByPitch defaults True

Stream.template(*\**, *fillWithRests=True*, *removeClasses: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *retainVoices=True*, *removeAll=False*, *exemptFromRemove=frozenset({})*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Stream.template)
:   Return a new Stream based on this one, but without the notes and other elements
    but keeping instruments, clefs, keys, etc.

    Classes to remove are specified in removeClasses.

    If this Stream contains measures, return a new Stream
    with new Measures populated with the same characteristics of those found in this Stream.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> sopr = b.parts[0]
    >>> soprEmpty = sopr.template()
    >>> soprEmpty.show('text')
    {0.0} <music21.instrument.Instrument 'P1: Soprano: Instrument 1'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.tempo.MetronomeMark Quarter=96 (playback only)>
        {0.0} <music21.key.Key of f# minor>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Rest quarter>
    {1.0} <music21.stream.Measure 1 offset=1.0>
        {0.0} <music21.note.Rest whole>
    {5.0} <music21.stream.Measure 2 offset=5.0>
        {0.0} <music21.note.Rest whole>
    {9.0} <music21.stream.Measure 3 offset=9.0>
        {0.0} <music21.layout.SystemLayout>
        {0.0} <music21.note.Rest whole>
    {13.0} <music21.stream.Measure 4 offset=13.0>
    ...
    ```

    Really make empty with fillWithRests=False

    ```python
    >>> alto = b.parts[1]
    >>> altoEmpty = alto.template(fillWithRests=False)
    >>> altoEmpty.show('text')
    {0.0} <music21.instrument.Instrument 'P2: Alto: Instrument 2'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.tempo.MetronomeMark Quarter=96 (playback only)>
        {0.0} <music21.key.Key of f# minor>
        {0.0} <music21.meter.TimeSignature 4/4>
    {1.0} <music21.stream.Measure 1 offset=1.0>

    {5.0} <music21.stream.Measure 2 offset=5.0>

    {9.0} <music21.stream.Measure 3 offset=9.0>
        {0.0} <music21.layout.SystemLayout>
    ...
    ```

    removeClasses can be a list or set of classes to remove. By default it is
    [‘GeneralNote’, ‘Dynamic’, ‘Expression’]

    ```python
    >>> tenor = b.parts[2]
    >>> tenorNoClefsSignatures = tenor.template(fillWithRests=False,
    ...       removeClasses=['Clef', 'KeySignature', 'TimeSignature', 'Instrument'])
    >>> tenorNoClefsSignatures.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.tempo.MetronomeMark Quarter=96 (playback only)>
        {0.0} <music21.note.Note A>
        {0.5} <music21.note.Note B>
    {1.0} <music21.stream.Measure 1 offset=1.0>
        {0.0} <music21.note.Note C#>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {5.0} <music21.stream.Measure 2 offset=5.0>
    ...
    ```

    Setting removeAll to True removes everything that is not a Stream:
    (this was removeClasses=True; in v9.9 both removeClasses=True or removeAll=True
    is allowed; in v10 only removeAll=True will be allowed).

    ```python
    >>> bass = b.parts[3]
    >>> bassEmpty = bass.template(fillWithRests=False, removeAll=True)
    >>> bassEmpty.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>

    {1.0} <music21.stream.Measure 1 offset=1.0>

    {5.0} <music21.stream.Measure 2 offset=5.0>

    {9.0} <music21.stream.Measure 3 offset=9.0>

    {13.0} <music21.stream.Measure 4 offset=13.0>

    ...
    ```

    exemptFromRemove should be a set of classes (or class strings) that
    are exempted from removal by removeAll or removeClasses

    ```python
    >>> bass = b.parts[3]
    >>> bassEmpty = bass.template(fillWithRests=False, removeAll=True,
    ...                           exemptFromRemove={meter.TimeSignature})
    >>> bassEmpty[meter.TimeSignature].first()
    <music21.meter.TimeSignature 4/4>
    >>> print(bassEmpty[clef.Clef].first())
    None
    ```

    Here is an example of exerpts of what calling template() with
    default values on the whole score looks like.

    ```python
    >>> b.template().show('text')
    {0.0} <music21.metadata.Metadata object at 0x106151940>
    {0.0} <music21.stream.Part Soprano>
        {0.0} <music21.instrument.Instrument 'P1: Soprano: Instrument 1'>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.tempo.MetronomeMark Quarter=96 (playback only)>
            {0.0} <music21.key.Key of f# minor>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Rest quarter>
        {1.0} <music21.stream.Measure 1 offset=1.0>
            {0.0} <music21.note.Rest whole>
            ...
        {33.0} <music21.stream.Measure 9 offset=33.0>
            {0.0} <music21.note.Rest dotted-half>
            {3.0} <music21.bar.Barline type=final>
    {0.0} <music21.stream.Part Alto>
        {0.0} <music21.instrument.Instrument 'P2: Alto: Instrument 2'>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.tempo.MetronomeMark Quarter=96 (playback only)>
            {0.0} <music21.key.Key of f# minor>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Rest quarter>
        {1.0} <music21.stream.Measure 1 offset=1.0>
            {0.0} <music21.note.Rest whole>
        ...
        {33.0} <music21.stream.Measure 9 offset=33.0>
            {0.0} <music21.note.Rest dotted-half>
            {3.0} <music21.bar.Barline type=final>
    {0.0} <music21.layout.StaffGroup ...>
    ```

    If retainVoices is False (default True) then Voice streams are treated
    differently from all other Streams and are removed. All elements in the
    voice are removed even if they do not match the classList:

    ```python
    >>> p = stream.Part(id='part0')
    >>> m1 = stream.Measure(number=1)
    >>> v1 = stream.Voice(id='voice1')
    >>> v1.insert(0, note.Note('E', quarterLength=4.0))
    >>> v2 = stream.Voice(id='voice2')
    >>> v2.insert(0, note.Note('G', quarterLength=2.0))
    >>> m1.insert(0, v1)
    >>> m1.insert(0, v2)
    >>> m2 = stream.Measure(number=2)
    >>> m2.insert(0, note.Note('D', quarterLength=4.0))
    >>> p.append([m1, m2])
    >>> pt = p.template(retainVoices=False)
    >>> pt.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.note.Rest whole>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Rest whole>
    >>> pt[0][0].quarterLength
    4.0
    ```

    Developer note – if you just want a copy of a Score with new
    Part and Measure objects, but you don’t care that the notes, etc.
    inside are the same objects as the original (i.e., you do not
    plan to manipulate them, or you want the manipulations to
    return to the original objects), using .template() is several
    times faster than a deepcopy of the stream (about 4x faster
    on bwv66.6)

    * Changed in v7: all arguments are keyword only.
    * New in v9.9: added exemptFromRemove
    * Note: in v10: removeClasses cannot be boolean – use removeAll instead

Stream.toSoundingPitch(*\**, *preserveAccidentalDisplay: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *inPlace=False*)[[source]](../_modules/music21/stream/base.html#Stream.toSoundingPitch)
:   If not at sounding pitch, transpose all Pitch
    elements to sounding pitch. The atSoundingPitch property
    is used to determine if transposition is necessary.

    Affected by the presence of Instruments and by Ottava spanners

    ```python
    >>> sc = stream.Score()
    >>> p = stream.Part(id='barisax')
    >>> p.append(instrument.BaritoneSaxophone())
    >>> m = stream.Measure(number=1)
    >>> m.append(note.Note('A4'))
    >>> p.append(m)
    >>> sc.append(p)
    >>> sc.atSoundingPitch = False
    ```

    ```python
    >>> scSounding = sc.toSoundingPitch()
    >>> scSounding.show('text')
    {0.0} <music21.stream.Part barisax>
        {0.0} <music21.instrument.BaritoneSaxophone 'Baritone Saxophone'>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note C>
    ```

    ```python
    >>> scSounding.atSoundingPitch
    True
    >>> scSounding.parts[0].atSoundingPitch
    True
    >>> scSounding.recurse().notes[0].nameWithOctave
    'C3'
    ```

    If ‘atSoundingPitch’ is unknown for this Stream and all of its parent Streams
    then no transposition will take place, and atSoundingPitch will remain unknown
    (this used to raise an exception):

    ```python
    >>> s = stream.Score()
    >>> p = stream.Part(id='partEmpty')
    >>> s.insert(0.0, p)
    >>> p.toSoundingPitch()
    <music21.stream.Part partEmpty>
    >>> s.atSoundingPitch = False
    >>> sp = p.toSoundingPitch()
    >>> sp
    <music21.stream.Part partEmpty>
    >>> sp.atSoundingPitch
    'unknown'
    >>> sp.derivation.origin is p
    True
    ```

    * Changed in v2.0.10: inPlace is False
    * Changed in v5: returns None if inPlace=True
    * Changed in v9: no transposition instead of exception if atSoundingPitch is ‘unknown’

Stream.toWrittenPitch(*\**, *ottavasToSounding: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *preserveAccidentalDisplay: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/stream/base.html#Stream.toWrittenPitch)
:   If not at written pitch, transpose all Pitch elements to
    written pitch. The atSoundingPitch property is used to
    determine if transposition is necessary. Note that if
    ottavasToSounding is True, any notes/chords within
    an Ottava will \_then\_ be transposed to sounding Pitch (this
    is useful for the MusicXML writer, since MusicXML likes
    all pitches to be written pitches, except for those in
    ottavas, which should be transposed to written (by instrument)
    and then transposed to sounding (by ottava).

    ```python
    >>> sc = stream.Score()
    >>> p = stream.Part(id='baritoneSax')
    >>> p.append(instrument.BaritoneSaxophone())
    >>> m = stream.Measure(number=1)
    >>> m.append(note.Note('C3'))
    >>> p.append(m)
    >>> sc.append(p)
    >>> sc.atSoundingPitch = True
    >>> scWritten = sc.toWrittenPitch()
    >>> scWritten.show('text')
    {0.0} <music21.stream.Part baritoneSax>
        {0.0} <music21.instrument.BaritoneSaxophone 'Baritone Saxophone'>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note A>
    >>> scWritten.atSoundingPitch
    False
    >>> scWritten.parts[0].atSoundingPitch
    False
    >>> scWritten.recurse().notes[0].nameWithOctave
    'A4'
    ```

    * Changed in v3: inPlace defaults to False
    * Changed in v5 returns None if inPlace=True
    * Changed in v9: no transposition instead of exception if atSoundingPitch is ‘unknown’

Stream.transferOffsetToElements()[[source]](../_modules/music21/stream/base.html#Stream.transferOffsetToElements)
:   Transfer the offset of this stream to all
    internal elements; then set
    the offset of this stream to zero.

    ```python
    >>> a = stream.Stream()
    >>> a.repeatInsert(note.Note('C'), list(range(10)))
    >>> a.offset = 30
    >>> a.transferOffsetToElements()
    >>> a.lowestOffset
    30.0
    >>> a.offset
    0.0
    >>> a.offset = 20
    >>> a.transferOffsetToElements()
    >>> a.lowestOffset
    50.0
    ```

Stream.transpose(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [music21.interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")*, */*, *\**, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *classFilterList=None*)[[source]](../_modules/music21/stream/base.html#Stream.transpose)
:   Transpose all specified classes in the
    Stream by the
    user-provided value. If the value is an integer, the
    transposition is treated in half steps. If the value is
    a string, any Interval string specification can be
    provided.

    returns a new Stream by default, but if the
    optional “inPlace” key is set to True then
    it modifies pitches in place.

    TODO: for generic interval set accidental by key signature.

    ```python
    >>> aInterval = interval.Interval('d5')
    ```

    ```python
    >>> aStream = corpus.parse('bach/bwv324.xml')
    >>> part = aStream.parts[0]
    >>> [str(p) for p in aStream.parts[0].pitches[:10]]
    ['B4', 'D5', 'B4', 'B4', 'B4', 'B4', 'C5', 'B4', 'A4', 'A4']
    ```

    ```python
    >>> bStream = aStream.parts[0].flatten().transpose('d5')
    >>> [str(p) for p in bStream.pitches[:10]]
    ['F5', 'A-5', 'F5', 'F5', 'F5', 'F5', 'G-5', 'F5', 'E-5', 'E-5']
    ```

    Test that aStream hasn’t been changed:

    ```python
    >>> [str(p) for p in aStream.parts[0].pitches[:10]]
    ['B4', 'D5', 'B4', 'B4', 'B4', 'B4', 'C5', 'B4', 'A4', 'A4']
    ```

    ```python
    >>> cStream = bStream.flatten().transpose('a4')
    >>> [str(p) for p in cStream.pitches[:10]]
    ['B5', 'D6', 'B5', 'B5', 'B5', 'B5', 'C6', 'B5', 'A5', 'A5']
    ```

    ```python
    >>> cStream.flatten().transpose(aInterval, inPlace=True)
    >>> [str(p) for p in cStream.pitches[:10]]
    ['F6', 'A-6', 'F6', 'F6', 'F6', 'F6', 'G-6', 'F6', 'E-6', 'E-6']
    ```

    * Changed in v8: first value is position only, all other values are keyword only

Stream.voicesToParts(*\**, *separateById=False*)[[source]](../_modules/music21/stream/base.html#Stream.voicesToParts)
:   If this Stream defines one or more voices,
    extract each into a Part, returning a Score.

    If this Stream has no voices, return the Stream as a Part within a Score.

    ```python
    >>> c = corpus.parse('demos/two-voices')
    >>> c.show('t')
    {0.0} <music21.text.TextBox 'Music21 Fr...'>
    {0.0} <music21.text.TextBox 'Music21'>
    {0.0} <music21.metadata.Metadata object at 0x109ce1630>
    {0.0} <music21.stream.Part Piano>
        {0.0} <music21.instrument.Instrument 'P1: Piano: '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.layout.PageLayout>
            {0.0} <music21.layout.SystemLayout>
            ...
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.key.Key of D major>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.stream.Voice 3>
                {0.0} <music21.note.Note E>
                ...
                {3.0} <music21.note.Rest quarter>
            {0.0} <music21.stream.Voice 4>
                {0.0} <music21.note.Note F#>
                ...
                {3.5} <music21.note.Note B>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.stream.Voice 3>
                {0.0} <music21.note.Note E>
                ...
                {3.0} <music21.note.Rest quarter>
            {0.0} <music21.stream.Voice 4>
                {0.0} <music21.note.Note E>
                ...
                {3.5} <music21.note.Note A>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.note.Rest whole>
            {4.0} <music21.bar.Barline type=final>
    {0.0} <music21.layout.ScoreLayout>
    ```

    ```python
    >>> ce = c.voicesToParts()
    >>> ce.show('t')
    {0.0} <music21.stream.Part Piano-v0>
        {0.0} <music21.instrument.Instrument 'P1: Piano: '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.key.Key of D major>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note E>
            ...
            {3.0} <music21.note.Rest quarter>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note E>
            ...
            {3.0} <music21.note.Rest quarter>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.note.Rest whole>
            {4.0} <music21.bar.Barline type=final>
    {0.0} <music21.stream.Part Piano-v1>
        {0.0} <music21.instrument.Instrument 'P1: Piano: '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.key.Key of D major>
            ...
            {3.5} <music21.note.Note B>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note E>
            ...
            {3.5} <music21.note.Note A>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.bar.Barline type=final>
    ```

    If separateById is True then all voices with the same id
    will be connected to the same Part, regardless of order
    they appear in the measure.

    Compare the previous output:

    ```python
    >>> p0pitches = ce.parts[0].pitches
    >>> p1pitches = ce.parts[1].pitches
    >>> ' '.join([p.nameWithOctave for p in p0pitches])
    'E4 D#4 D#4 E4 F#4 E4 B3 B3 E4 E4'
    >>> ' '.join([p.nameWithOctave for p in p1pitches])
    'F#2 F#3 E3 E2 D#2 D#3 B2 B3 E2 E3 D3 D2 C#2 C#3 A2 A3'
    ```

    Swap voice ids in first measure:

    ```python
    >>> m0 = c.parts[0].getElementsByClass(stream.Measure).first()
    >>> m0.voices[0].id, m0.voices[1].id
    ('3', '4')
    >>> m0.voices[0].id = '4'
    >>> m0.voices[1].id = '3'
    ```

    Now run voicesToParts with separateById=True

    ```python
    >>> ce = c.voicesToParts(separateById=True)
    >>> p0pitches = ce.parts[0].pitches
    >>> p1pitches = ce.parts[1].pitches
    >>> ' '.join([p.nameWithOctave for p in p0pitches])
    'E4 D#4 D#4 E4 F#4 E2 E3 D3 D2 C#2 C#3 A2 A3'
    >>> ' '.join([p.nameWithOctave for p in p1pitches])
    'F#2 F#3 E3 E2 D#2 D#3 B2 B3 E4 B3 B3 E4 E4'
    ```

    Note that the second and subsequent measure’s pitches were changed
    not the first, because separateById aligns the voices according to
    order first encountered, not by sorting the Ids.

Stream.write(*fmt=None*, *fp=None*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Stream.write)
:   Write out a file of music notation (or an image, etc.) in a given format. If
    fp is specified as a file path then the file will be placed there. If it is not
    given then a temporary file will be created.

    If fmt is not given then the default of your Environment’s ‘writeFormat’ will
    be used. For most people that is musicxml.

    Returns the full path to the file.

    Some formats, including .musicxml, create a copy of the stream, pack it into a well-formed
    score if necessary, and run `makeNotation()`. To
    avoid this when writing .musicxml, use makeNotation=False, an advanced option
    that prioritizes speed but may not guarantee satisfactory notation.

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream") instance variables

Stream.autoSort
:   Boolean describing whether the Stream is automatically sorted by
    offset whenever necessary.

Stream.definesExplicitPageBreaks
:   Boolean that says whether all page breaks in the piece are
    explicitly defined. Only used on musicxml output (maps to the
    musicxml <supports attribute=”new-page”> tag) and only if this is
    the outermost Stream being shown.

Stream.definesExplicitSystemBreaks
:   Boolean that says whether all system breaks in the piece are
    explicitly defined. Only used on musicxml output (maps to the
    musicxml <supports attribute=”new-system”> tag) and only if this is
    the outermost Stream being shown

Stream.isFlat
:   Boolean describing whether this Stream contains embedded
    sub-Streams or Stream subclasses (not flat).

Stream.isSorted
:   Boolean describing whether the Stream is sorted or not.

Stream.recursionType
:   Class variable:

    RecursionType Enum of (ELEMENTS\_FIRST (default), FLATTEN, ELEMENTS\_ONLY)
    that decides whether the stream likely holds relevant
    contexts for the elements in it.

    Define this for a stream class, not an individual object.

    see [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites")

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Measure

class music21.stream.base.Measure(*\*args*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 0*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Measure)
:   A representation of a Measure organized as a Stream.

    All properties of a Measure that are Music21 objects are found as part of
    the Stream’s elements.

    Measure number can be explicitly set with the number keyword:

    ```python
    >>> m4 = stream.Measure(number=4)
    >>> m4
    <music21.stream.Measure 4 offset=0.0>
    >>> m4.number
    4
    ```

    If passed a single integer as an argument, assumes that this int
    is the measure number.

    ```python
    >>> m5 = stream.Measure(5)
    >>> m5
    <music21.stream.Measure 5 offset=0.0>
    ```

    Number can also be a string if there is a suffix:

    ```python
    >>> m4 = stream.Measure(number='4a')
    >>> m4
    <music21.stream.Measure 4a offset=0.0>
    >>> m4.numberSuffix
    'a'
    ```

    Though they have all the features of general streams,
    Measures have specific attributes that allow for setting their number
    and numberSuffix, keep track of whether they have a different clef or
    key or timeSignature than previous measures, allow for padding (and pickups),
    and can be found as a “measure slice” within a score and parts.

[`Measure`](#music21.stream.base.Measure "music21.stream.base.Measure") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Measure`](#music21.stream.base.Measure "music21.stream.base.Measure") read-only properties

Measure.barDuration
:   Return the bar duration, or the Duration specified by the TimeSignature,
    regardless of what elements are found in this Measure or the highest time.
    TimeSignature is found first within the Measure,
    or within a context based search.

    To get the duration of the total length of elements, just use the
    .duration property.

    Here we create a 3/4 measure and “over-stuff” it with five quarter notes.
    barDuration still gives a duration of 3.0, or a dotted quarter note,
    while .duration gives a whole note tied to a quarter.

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.barDuration
    <music21.duration.Duration 3.0>
    >>> m.repeatAppend(note.Note(type='quarter'), 5)
    >>> m.barDuration
    <music21.duration.Duration 3.0>
    >>> m.duration
    <music21.duration.Duration 5.0>
    ```

    The objects returned by barDuration and duration are
    full [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")
    objects, will all the relevant properties:

    ```python
    >>> m.barDuration.fullName
    'Dotted Half'
    >>> m.duration.fullName
    'Whole tied to Quarter (5 total QL)'
    ```

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Measure`](#music21.stream.base.Measure "music21.stream.base.Measure") read/write properties

Measure.leftBarline
:   Get or set the left barline, or the Barline object
    found at offset zero of the Measure. Can be set either with a string
    representing barline style or a bar.Barline() object or None.
    Note that not all bars have
    barline objects here – regular barlines don’t need them.

Measure.rightBarline
:   Get or set the right barline, or the Barline object
    found at the offset equal to the bar duration.

    ```python
    >>> b = bar.Barline('final')
    >>> m = stream.Measure()
    >>> print(m.rightBarline)
    None
    >>> m.rightBarline = b
    >>> m.rightBarline.type
    'final'
    ```

    A string can also be used instead:

    ```python
    >>> c = converter.parse('tinynotation: 3/8 C8 D E F G A B4.')
    >>> c.measure(1).rightBarline = 'light-light'
    >>> c.measure(3).rightBarline = 'light-heavy'
    >>> c.show()
    ```

    [![../_images/stream_barline_demo.png](../_images/stream_barline_demo.png)](../_images/stream_barline_demo.png)

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Measure`](#music21.stream.base.Measure "music21.stream.base.Measure") methods

Measure.barDurationProportion(*barDuration=None*)[[source]](../_modules/music21/stream/base.html#Measure.barDurationProportion)
:   Return a floating point value greater than 0 showing the proportion
    of the bar duration that is filled based on the highest time of
    all elements. 0.0 is empty, 1.0 is filled; 1.5 specifies of an
    overflow of half.

    Bar duration refers to the duration of the Measure as suggested by
    the TimeSignature. This value cannot be determined without a TimeSignature.

    An already-obtained Duration object can be supplied with the barDuration
    optional argument.

    ```python
    >>> import copy
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> n = note.Note()
    >>> n.quarterLength = 1
    >>> m.append(copy.deepcopy(n))
    >>> m.barDurationProportion()
    Fraction(1, 3)
    >>> m.append(copy.deepcopy(n))
    >>> m.barDurationProportion()
    Fraction(2, 3)
    >>> m.append(copy.deepcopy(n))
    >>> m.barDurationProportion()
    1.0
    >>> m.append(copy.deepcopy(n))
    >>> m.barDurationProportion()
    Fraction(4, 3)
    ```

Measure.bestTimeSignature()[[source]](../_modules/music21/stream/base.html#Measure.bestTimeSignature)
:   Given a Measure with elements in it,
    get a TimeSignature that contains all elements.
    Calls meter.bestTimeSignature(self)

    Note: this does not yet accommodate triplets.

    We create a simple stream that should be in 3/4

    ```python
    >>> s = converter.parse('C4 D4 E8 F8', format='tinyNotation', makeNotation=False)
    >>> m = stream.Measure()
    >>> for el in s:
    ...     m.insert(el.offset, el)
    ```

    But there is no TimeSignature!

    ```python
    >>> m.show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    {2.0} <music21.note.Note E>
    {2.5} <music21.note.Note F>
    ```

    So, we get the best Time Signature and put it in the Stream.

    ```python
    >>> ts = m.bestTimeSignature()
    >>> ts
    <music21.meter.TimeSignature 3/4>
    >>> m.timeSignature = ts
    >>> m.show('text')
    {0.0} <music21.meter.TimeSignature 3/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    {2.0} <music21.note.Note E>
    {2.5} <music21.note.Note F>
    ```

    For further details about complex time signatures, etc.
    see meter.bestTimeSignature()

Measure.makeNotation(*inPlace=False*, *\*\*subroutineKeywords*)[[source]](../_modules/music21/stream/base.html#Measure.makeNotation)
:   This method calls a sequence of Stream methods on this
    `Measure` to prepare notation.

    If inPlace is True, this is done in-place; if
    inPlace is False, this returns a modified deep copy.

    ```python
    >>> m = stream.Measure()
    >>> n1 = note.Note('g#')
    >>> n2 = note.Note('g')
    >>> m.append([n1, n2])
    >>> m.makeNotation(inPlace=True)
    >>> m.notes[1].pitch.accidental
    <music21.pitch.Accidental natural>
    ```

Measure.measureNumberWithSuffix()[[source]](../_modules/music21/stream/base.html#Measure.measureNumberWithSuffix)
:   Return the measure .number with the .numberSuffix as a string.

    ```python
    >>> m = stream.Measure()
    >>> m.number = 4
    >>> m.numberSuffix = 'A'
    >>> m.measureNumberWithSuffix()
    '4A'
    ```

    Test that it works as musicxml

    ```python
    >>> xml = musicxml.m21ToXml.GeneralObjectExporter().parse(m)
    >>> print(xml.decode('utf-8'))
    <?xml version="1.0"...?>
    ...
    <part id="...">
        <!--========================= Measure 4 ==========================-->
        <measure implicit="no" number="4A">
    ...
    ```

    Test round tripping:

    ```python
    >>> s2 = converter.parseData(xml)
    >>> print(s2[stream.Measure].first().measureNumberWithSuffix())
    4A
    ```

    Note that we use print here because in parsing the data will become a unicode string.

Measure.mergeAttributes(*other*)[[source]](../_modules/music21/stream/base.html#Measure.mergeAttributes)
:   Given another Measure, configure all non-element attributes of this
    Measure with the attributes of the other Measure. No elements
    will be changed or copied.

    This method is necessary because Measures, unlike some Streams,
    have attributes independent of any stored elements.

    Overrides base.Music21Object.mergeAttributes

    ```python
    >>> m1 = stream.Measure()
    >>> m1.id = 'MyMeasure'
    >>> m1.clefIsNew = True
    >>> m1.number = 2
    >>> m1.numberSuffix = 'b'
    >>> m1.layoutWidth = 200
    ```

    ```python
    >>> m2 = stream.Measure()
    >>> m2.mergeAttributes(m1)
    >>> m2.layoutWidth
    200
    >>> m2.id
    'MyMeasure'
    >>> m2
    <music21.stream.Measure 2b offset=0.0>
    ```

    Try with not another Measure:

    ```python
    >>> m3 = stream.Stream()
    >>> m3.id = 'hello'
    >>> m2.mergeAttributes(m3)
    >>> m2.id
    'hello'
    >>> m2.layoutWidth
    200
    ```

Measure.padAsAnacrusis(*useGaps=True*, *useInitialRests=False*)[[source]](../_modules/music21/stream/base.html#Measure.padAsAnacrusis)
:   Given an incompletely filled Measure, adjust the paddingLeft value to
    represent contained events as shifted to fill the right-most duration of the bar.

    Calling this method will overwrite any previously set paddingLeft value,
    based on the current TimeSignature-derived barDuration attribute.

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> n = note.Note()
    >>> n.quarterLength = 1.0
    >>> m.append(n)
    >>> m.padAsAnacrusis()
    >>> m.paddingLeft
    2.0
    ```

    ```python
    >>> m.timeSignature = meter.TimeSignature('5/4')
    >>> m.padAsAnacrusis()
    >>> m.paddingLeft
    4.0
    ```

    Empty space at the beginning of the measure will not be taken in account:

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> n = note.Note(type='quarter')
    >>> m.insert(2.0, n)
    >>> m.padAsAnacrusis()
    >>> m.paddingLeft
    0.0
    ```

    If useInitialRests is True, then rests at the beginning of the measure
    are removed. This is especially useful for formats that don’t give a
    way to specify a pickup measure (such as tinynotation) or software
    that generates incorrect opening measures. So, to fix the problem before,
    put a rest at the beginning and call useInitialRests:

    ```python
    >>> r = note.Rest(type='half')
    >>> m.insert(0, r)
    >>> m.padAsAnacrusis(useInitialRests=True)
    >>> m.paddingLeft
    2.0
    ```

    And the rest is gone!

    ```python
    >>> m.show('text')
    {0.0} <music21.meter.TimeSignature 3/4>
    {0.0} <music21.note.Note C>
    ```

    Only initial rests count for useInitialRests:

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.append(note.Rest(type='eighth'))
    >>> m.append(note.Rest(type='eighth'))
    >>> m.append(note.Note('C4', type='quarter'))
    >>> m.append(note.Rest(type='eighth'))
    >>> m.append(note.Note('D4', type='eighth'))
    >>> m.show('text')
    {0.0} <music21.meter.TimeSignature 3/4>
    {0.0} <music21.note.Rest eighth>
    {0.5} <music21.note.Rest eighth>
    {1.0} <music21.note.Note C>
    {2.0} <music21.note.Rest eighth>
    {2.5} <music21.note.Note D>
    >>> m.padAsAnacrusis(useInitialRests=True)
    >>> m.paddingLeft
    1.0
    >>> m.show('text')
    {0.0} <music21.meter.TimeSignature 3/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Rest eighth>
    {1.5} <music21.note.Note D>
    ```

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Measure`](#music21.stream.base.Measure "music21.stream.base.Measure") instance variables

Measure.clefIsNew
:   Boolean describing if the Clef is different than the previous Measure.

Measure.keyIsNew
:   Boolean describing if KeySignature is different than the previous Measure.

Measure.layoutWidth
:   A suggestion for layout width, though most rendering systems do not support
    this designation. Use [`SystemLayout`](moduleLayout.html#music21.layout.SystemLayout "music21.layout.SystemLayout")
    objects instead.

Measure.number
:   A number representing the displayed or shown
    Measure number as presented in a written Score.

Measure.numberSuffix
:   If a Measure number has a string annotation, such as “a” or similar,
    this string is stored here. Note that in MusicXML, such
    suffixes often appear as
    prefixes to measure numbers. In music21 (like most measure
    numbering systems), these
    numbers appear as suffixes.

Measure.paddingLeft
:   defines empty space at the front of the measure for purposes of determining
    beat, etc for pickup/anacrusis bars. In 4/4, a
    measure with a one-beat pickup
    note will have a paddingLeft of 3.0.
    (The name comes from the CSS graphical term
    for the amount of padding on the left side of a region.)

Measure.paddingRight
:   defines empty space at the end of the measure for purposes of determining
    whether or not a measure is filled.
    In 4/4, a piece beginning a one-beat pickup
    note will often have a final measure of three beats, instead of four.
    The final
    measure should have a paddingRight of 1.0.
    (The name comes from the CSS graphical term
    for the amount of padding on the right side of a region.)

Measure.showNumber
:   Enum describing if the measure number should be displayed.

Measure.timeSignatureIsNew
:   Boolean describing if the TimeSignature
    is different than the previous Measure.

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Part

class music21.stream.base.Part(*\*args*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Part)
:   A Stream subclass for designating music that is considered a single part.

    When put into a Score object, Part objects are all collected in the Score.parts
    call. Otherwise, they mostly work like generic Streams.

    Generally the hierarchy goes: Score > Part > Measure > Voice, but you are not
    required to stick to this.

    Part groupings (piano braces, etc.) are found in the [music21.layout](moduleLayout.html#modulelayout) module
    in the [`StaffGroup`](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup") Spanner object.

[`Part`](#music21.stream.base.Part "music21.stream.base.Part") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Part`](#music21.stream.base.Part "music21.stream.base.Part") read-only properties

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Part`](#music21.stream.base.Part "music21.stream.base.Part") read/write properties

Part.partAbbreviation
:   Gets or sets a string representing the abbreviated name of this part
    as a whole (not counting instrument changes, etc.).

    It can be set explicitly (or set on parsing) or it
    can take its name from the first [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") object
    encountered in the stream (or within a substream),
    first checking its .partAbbreviation, then checking its .instrumentAbbreviation

    Can also return None.

    ```python
    >>> p = stream.Part()
    >>> p.partAbbreviation is None
    True
    >>> cl = instrument.Clarinet()
    >>> p.insert(0, cl)
    >>> p.partAbbreviation
    'Cl'
    >>> p.remove(cl)
    >>> p.partAbbreviation is None
    True
    >>> p.insert(0, instrument.Flute())
    >>> p.partAbbreviation
    'Fl'
    >>> p.partAbbreviation = 'Rd 1'
    >>> p.partAbbreviation
    'Rd 1'
    ```

    Note that changing an instrument’s .partAbbreviation or .instrumentAbbreviation while it
    is already in the Stream will not automatically update this unless
    .coreElementsChanged() is called or this Stream’s elements are otherwise altered.
    This is because the value is cached so that O(n) searches through the Stream
    do not need to be done every time.

Part.partName
:   Gets or sets a string representing the name of this part
    as a whole (not counting instrument changes, etc.).

    It can be set explicitly (or set on parsing) or it
    can take its name from the first [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") object
    encountered in the stream (or within a substream),
    first checking its .partName, then checking its .instrumentName

    Can also return None.

    ```python
    >>> p = stream.Part()
    >>> p.partName is None
    True
    >>> cl = instrument.Clarinet()
    >>> p.insert(0, cl)
    >>> p.partName
    'Clarinet'
    >>> p.remove(cl)
    >>> p.partName is None
    True
    >>> p.insert(0, instrument.Flute())
    >>> p.partName
    'Flute'
    >>> p.partName = 'Reed 1'
    >>> p.partName
    'Reed 1'
    ```

    Note that changing an instrument’s .partName or .instrumentName while it
    is already in the Stream will not automatically update this unless
    .coreElementsChanged() is called or this Stream’s elements are otherwise altered.
    This is because the value is cached so that O(n) searches through the Stream
    do not need to be done every time.

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Part`](#music21.stream.base.Part "music21.stream.base.Part") methods

Part.makeAccidentals(*\**, *alteredPitches=None*, *cautionaryPitchClass=True*, *cautionaryAll=False*, *inPlace=False*, *overrideStatus=False*, *cautionaryNotImmediateRepeat=True*, *tiePitchSet=None*)[[source]](../_modules/music21/stream/base.html#Part.makeAccidentals)
:   This overridden method of Stream.makeAccidentals
    walks measures to arrive at desired values for keyword arguments
    tiePitchSet and pitchPastMeasure when calling makeAccidentals()
    on each Measure.

    1. Ties across barlines are detected so that accidentals are not
    unnecessarily reiterated. (tiePitchSet)

    2. Pitches appearing on the same step in an immediately preceding measure,
    if foreign to the key signature of that previous measure,
    are printed with cautionary accidentals in the subsequent measure.
    (pitchPastMeasure)

    Most of the logic has been factored out to
    [`makeAccidentalsInMeasureStream()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.makeAccidentalsInMeasureStream "music21.stream.makeNotation.makeAccidentalsInMeasureStream"),
    which is called after managing the inPlace keyword and finding
    measures to iterate.

    * Changed in v7: inPlace defaults False

Part.mergeAttributes(*other*)[[source]](../_modules/music21/stream/base.html#Part.mergeAttributes)
:   Merge relevant attributes from the Other part
    into this one. Key attributes of difference: partName and partAbbreviation.

    TODO: doc test

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Part`](#music21.stream.base.Part "music21.stream.base.Part") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Score

class music21.stream.base.Score(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Score)
:   A Stream subclass for handling music with more than one Part.

    Almost totally optional (the largest containing Stream in a piece could be
    a generic Stream, or a Part, or a Staff). And Scores can be
    embedded in other Scores (in fact, our original thought was to call
    this class a Fragment because of this possibility of continuous
    embedding; though it’s probably better to embed a Score in an Opus),
    but we figure that many people will like calling the largest
    container a Score and that this will become a standard.

[`Score`](#music21.stream.base.Score "music21.stream.base.Score") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Score`](#music21.stream.base.Score "music21.stream.base.Score") read-only properties

Score.parts
:   Return all `Part` objects in a `Score`.

    It filters out all other things that might be in a Score object, such as Metadata
    returning just the Parts.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> s.parts
    <music21.stream.iterator.StreamIterator for Score:bach/bwv66.6.mxl @:0>
    >>> len(s.parts)
    4
    ```

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Score`](#music21.stream.base.Score "music21.stream.base.Score") read/write properties

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Score`](#music21.stream.base.Score "music21.stream.base.Score") methods

Score.expandRepeats(*copySpanners: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Score.expandRepeats)
:   Expand all repeats, as well as all repeat indications
    given by text expressions such as D.C. al Segno.

    This method always returns a new Stream, with deepcopies
    of all contained elements at all level.

    Note that copySpanners is ignored here, as they are always copied.

Score.implode()[[source]](../_modules/music21/stream/base.html#Score.implode)
:   Reduce a polyphonic work into two staves.

    Currently, this is just a synonym for partsToVoices with
    voiceAllocation = 2, and permitOneVoicePerPart = False,
    but someday this will have better methods for finding identical
    parts, etc.

Score.makeNotation(*meterStream=None*, *refStreamOrTimeRange=None*, *inPlace=False*, *bestClef=False*, *\*\*subroutineKeywords*)[[source]](../_modules/music21/stream/base.html#Score.makeNotation)
:   This method overrides the makeNotation method on Stream,
    such that a Score object with one or more Parts or Streams
    that may not contain well-formed notation may be transformed
    and replaced by well-formed notation.

    If inPlace is True, this is done in-place;
    if inPlace is False, this returns a modified deep copy.

Score.measure(*measureNumber*, *collect=(<class 'music21.clef.Clef'>*, *<class 'music21.meter.base.TimeSignature'>*, *<class 'music21.instrument.Instrument'>*, *<class 'music21.key.KeySignature'>)*, *gatherSpanners=<GatherSpanners.ALL>*, *indicesNotNumbers=False*)[[source]](../_modules/music21/stream/base.html#Score.measure)
:   Given a measure number (or measure index, if indicesNotNumbers is True)
    return another Score object which contains multiple parts but each of which has only a
    single `Measure` object if the
    Measure number exists, otherwise returns a score with parts that are empty.

    This method overrides the `measure()` method on Stream to
    allow for finding a single “measure slice” within parts:

    ```python
    >>> bachIn = corpus.parse('bach/bwv324.xml')
    >>> excerpt = bachIn.measure(2)
    >>> excerpt
    <music21.stream.Score bach/bwv324.mxl>
    >>> len(excerpt.parts)
    4
    >>> excerpt.parts[0].show('text')
    {0.0} <music21.instrument.Instrument 'P1: Soprano: '>
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.key.Key of e minor>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.stream.Measure 2 offset=0.0>
        {0.0} <music21.note.Note B>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note B>
        {3.0} <music21.note.Note B>
    ```

    Note that the parts created have all the meta-information outside the measure
    unless this information appears in the measure itself at the beginning:

    ```python
    >>> bachIn.measure(1).parts[0].show('text')
    {0.0} <music21.instrument.Instrument 'P1: Soprano: '>
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.key.Key of e minor>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.layout.SystemLayout>
        {0.0} <music21.note.Note B>
        {2.0} <music21.note.Note D>
    ```

    This way the original measure objects can be returned without being altered.

    The final measure slice of the piece can be obtained with index -1. Example:
    quickly get the last chord of the piece, without needing to run .chordify()
    on the whole piece:

    ```python
    >>> excerpt = bachIn.measure(-1)
    >>> excerptChords = excerpt.chordify()
    >>> excerptChords.show('text')
    {0.0} <music21.instrument.Instrument 'P1: Soprano: '>
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.key.Key of e minor>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.stream.Measure 9 offset=0.0>
        {0.0} <music21.chord.Chord E2 G3 B3 E4>
        {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> lastChord = excerptChords[chord.Chord].last()
    >>> lastChord
    <music21.chord.Chord E2 G3 B3 E4>
    ```

    Note that we still do a .getElementsByClass(chord.Chord) since many pieces end
    with nothing but a rest.

Score.measureOffsetMap(*classFilterList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Type](https://docs.python.org/3/library/typing.html#typing.Type "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Type](https://docs.python.org/3/library/typing.html#typing.Type "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ('Measure',)*) → [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Measure](#music21.stream.base.Measure "music21.stream.base.Measure")]][[source]](../_modules/music21/stream/base.html#Score.measureOffsetMap)
:   This Score method overrides the
    `measureOffsetMap()` method of Stream.
    This creates a map based on all contained Parts in this Score.
    Measures found in multiple Parts with the same offset will be
    appended to the same list.

    If no parts are found in the score, then the normal
    `measureOffsetMap()` routine is called.

    This method is smart and does not assume that all Parts
    have measures with identical offsets.

Score.measures(*numberStart*, *numberEnd*, *collect=('Clef'*, *'TimeSignature'*, *'Instrument'*, *'KeySignature')*, *gatherSpanners=<GatherSpanners.ALL>*, *indicesNotNumbers=False*)[[source]](../_modules/music21/stream/base.html#Score.measures)
:   This method overrides the `measures()`
    method on Stream. This creates a new Score stream that has the same measure
    range for all Parts.

    The collect argument is a list of classes that will be collected; see
    Stream.measures()

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> post = s.measures(3, 5)  # range is inclusive, i.e., [3, 5]
    >>> len(post.parts)
    4
    >>> len(post.parts[0].getElementsByClass(stream.Measure))
    3
    >>> len(post.parts[1].getElementsByClass(stream.Measure))
    3
    ```

Score.partsToVoices(*voiceAllocation: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = 2*, *permitOneVoicePerPart=False*, *setStems=True*)[[source]](../_modules/music21/stream/base.html#Score.partsToVoices)
:   Given a multi-part `Score`,
    return a new Score that combines parts into voices.

    The voiceAllocation parameter sets the maximum number
    of voices per Part.

    The permitOneVoicePerPart parameter, if True, will encode a
    single voice inside a single Part, rather than leaving it as
    a single Part alone, with no internal voices.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> len(s.flatten().notes)
    165
    >>> post = s.partsToVoices(voiceAllocation=4)
    >>> len(post.parts)
    1
    >>> len(post.parts.first().getElementsByClass(stream.Measure).first().voices)
    4
    >>> len(post.flatten().notes)
    165
    ```

Score.sliceByGreatestDivisor(*\**, *addTies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#Score.sliceByGreatestDivisor)

Score.sliceByGreatestDivisor(*\**, *addTies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")
:   Slice all duration of all part by the minimum duration
    that can be summed to each concurrent duration.

    Overrides method defined on Stream.

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") | * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Score`](#music21.stream.base.Score "music21.stream.base.Score") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Opus

class music21.stream.base.Opus(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Opus)
:   A Stream subclass for handling multi-work music encodings.
    Many ABC files, for example, define multiple works or parts within a single file.

    Opus objects can contain multiple Score objects, or even other Opus objects!

[`Opus`](#music21.stream.base.Opus "music21.stream.base.Opus") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Opus`](#music21.stream.base.Opus "music21.stream.base.Opus") read-only properties

Opus.scores
:   Return all `Score` objects
    in an iterator

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Opus`](#music21.stream.base.Opus "music21.stream.base.Opus") read/write properties

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Opus`](#music21.stream.base.Opus "music21.stream.base.Opus") methods

Opus.getNumbers()[[source]](../_modules/music21/stream/base.html#Opus.getNumbers)
:   Return a list of all numbers defined in this Opus.

    ```python
    >>> o = corpus.parse('josquin/oVenusBant')
    >>> o.getNumbers()
    ['1', '2', '3']
    ```

Opus.getScoreByNumber(*opusMatch*)[[source]](../_modules/music21/stream/base.html#Opus.getScoreByNumber)
:   Get Score objects from this Stream by number.
    Performs title search using the
    [`search()`](moduleMetadata.html#music21.metadata.Metadata.search "music21.metadata.Metadata.search") method,
    and returns the first result.

    ```python
    >>> o = corpus.parse('josquin/oVenusBant')
    >>> o.getNumbers()
    ['1', '2', '3']
    >>> s = o.getScoreByNumber(2)
    >>> s.metadata.title
    'O Venus bant'
    >>> s.metadata.alternativeTitle
    'Tenor'
    ```

Opus.getScoreByTitle(*titleMatch*)[[source]](../_modules/music21/stream/base.html#Opus.getScoreByTitle)
:   Get Score objects from this Stream by a title.
    Performs title search using the [`search()`](moduleMetadata.html#music21.metadata.Metadata.search "music21.metadata.Metadata.search") method,
    and returns the first result.

    ```python
    >>> o = corpus.parse('essenFolksong/erk5')
    >>> s = o.getScoreByTitle('Vrienden, kommt alle gaere')
    >>> s.metadata.title
    'Vrienden, kommt alle gaere'
    ```

    Regular expressions work fine

    ```python
    >>> s = o.getScoreByTitle('(.*)kommt(.*)')
    >>> s.metadata.title
    'Vrienden, kommt alle gaere'
    ```

Opus.mergeScores()[[source]](../_modules/music21/stream/base.html#Opus.mergeScores)
:   Some Opus objects represent numerous scores
    that are individual parts of the same work.
    This method will treat each contained Score as a Part,
    merging and returning a single Score with merged Metadata.

    ```python
    >>> o = corpus.parse('josquin/milleRegrets')
    >>> s = o.mergeScores()
    >>> s.metadata.title
    'Mille regrets'
    >>> len(s.parts)
    4
    ```

Opus.show(*fmt=None*, *app=None*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Opus.show)
:   Show an Opus file.

    This method overrides the behavior specified in
    [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") for all
    formats besides explicit lily.x calls. or when running under Jupyter notebook.

Opus.write(*fmt=None*, *fp=None*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Opus.write)
:   Displays an object in a format provided by the fmt argument or, if not
    provided, the format set in the user’s Environment.

    This method overrides the behavior specified in
    [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") for all formats besides explicit
    lily.x calls.

    Individual files are written for each score; returns the last file written.

    ```python
    >>> sc1 = stream.Score()
    >>> sc2 = stream.Score()
    >>> o = stream.Opus()
    >>> o.append([sc1, sc2])
    ```

    #\_DOCS\_SHOW >>> o.write()
    #\_DOCS\_SHOW PosixPath(‘/some/temp/path-2.xml’)

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") | * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Opus`](#music21.stream.base.Opus "music21.stream.base.Opus") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Voice

class music21.stream.base.Voice(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#Voice)
:   A Stream subclass for declaring that all the music in the
    stream belongs to a certain “voice” for analysis or display
    purposes.

    Note that both Finale’s Layers and Voices as concepts are
    considered Voices here.

    Voices have a sort order of 1 greater than time signatures

[`Voice`](#music21.stream.base.Voice "music21.stream.base.Voice") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Voice`](#music21.stream.base.Voice "music21.stream.base.Voice") read-only properties

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Voice`](#music21.stream.base.Voice "music21.stream.base.Voice") read/write properties

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Voice`](#music21.stream.base.Voice "music21.stream.base.Voice") methods

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Voice`](#music21.stream.base.Voice "music21.stream.base.Voice") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SpannerStorage

class music21.stream.base.SpannerStorage(*givenElements=None*, *\**, *client: [spanner.Spanner](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#SpannerStorage)
:   For advanced use. This Stream subclass is only used
    inside a Spanner object to provide object storage
    of connected elements (things the Spanner spans).

    This subclass name can be used to search in an
    object’s .sites and find any and all
    locations that are SpannerStorage objects.

    A client keyword argument must be provided by the Spanner in creation.

    ```python
    >>> stream.SpannerStorage(client=spanner.Slur())
    <music21.stream.SpannerStorage for music21.spanner.Slur>
    ```

    * Changed in v8: spannerParent is renamed client.

[`SpannerStorage`](#music21.stream.base.SpannerStorage "music21.stream.base.SpannerStorage") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpannerStorage`](#music21.stream.base.SpannerStorage "music21.stream.base.SpannerStorage") read-only properties

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SpannerStorage`](#music21.stream.base.SpannerStorage "music21.stream.base.SpannerStorage") read/write properties

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`SpannerStorage`](#music21.stream.base.SpannerStorage "music21.stream.base.SpannerStorage") methods

SpannerStorage.coreSelfActiveSite(*el*)[[source]](../_modules/music21/stream/base.html#SpannerStorage.coreSelfActiveSite)
:   Never set activeSite to spannerStorage

SpannerStorage.coreStoreAtEnd(*element*, *setActiveSite=True*)[[source]](../_modules/music21/stream/base.html#SpannerStorage.coreStoreAtEnd)
:   NB – this is a “core” method. General users should use .storeAtEnd() instead.

    Core method for adding end elements.
    To be called by other methods.

SpannerStorage.replace(*target: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *replacement: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *allDerived: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/base.html#SpannerStorage.replace)
:   Overrides `replace()` in order to check first
    whether replacement already exists in self. If so, delete target from
    self and return; otherwise call the superclass method.

    * New in v7.

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") | * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") | * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`SpannerStorage`](#music21.stream.base.SpannerStorage "music21.stream.base.SpannerStorage") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## VariantStorage

class music21.stream.base.VariantStorage(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#VariantStorage)
:   For advanced use. This Stream subclass is only
    used inside a Variant object to provide object
    storage of connected elements (things the Variant
    defines).

    This subclass name can be used to search in an
    object’s .sites and find any and all
    locations that are VariantStorage objects. It also
    ensures that they are pickled properly as Streams on a non-Stream
    object.

    * Changed in v8: variantParent is removed. Never used.

[`VariantStorage`](#music21.stream.base.VariantStorage "music21.stream.base.VariantStorage") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`VariantStorage`](#music21.stream.base.VariantStorage "music21.stream.base.VariantStorage") read-only properties

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`VariantStorage`](#music21.stream.base.VariantStorage "music21.stream.base.VariantStorage") read/write properties

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`VariantStorage`](#music21.stream.base.VariantStorage "music21.stream.base.VariantStorage") methods

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`VariantStorage`](#music21.stream.base.VariantStorage "music21.stream.base.VariantStorage") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## OffsetMap

class music21.stream.base.OffsetMap(*element*, *offset*, *endTime*, *voiceIndex*)

## BestQuantizationMatch

class music21.stream.base.BestQuantizationMatch(*remainingGap*, *error*, *tick*, *match*, *signedError*, *divisor*)

## PartStaff

class music21.stream.base.PartStaff(*\*args*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#PartStaff)
:   A Part subclass for designating music that is
    represented on a single staff but may only be one
    of many staves for a single part.

[`PartStaff`](#music21.stream.base.PartStaff "music21.stream.base.PartStaff") bases

* [`Part`](#music21.stream.base.Part "music21.stream.base.Part")
* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PartStaff`](#music21.stream.base.PartStaff "music21.stream.base.PartStaff") read-only properties

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PartStaff`](#music21.stream.base.PartStaff "music21.stream.base.PartStaff") read/write properties

Read/write properties inherited from [`Part`](#music21.stream.base.Part "music21.stream.base.Part"):

|  |  |  |
| --- | --- | --- |
| * [`partAbbreviation`](#music21.stream.base.Part.partAbbreviation "music21.stream.base.Part.partAbbreviation") | * [`partName`](#music21.stream.base.Part.partName "music21.stream.base.Part.partName") |  |

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PartStaff`](#music21.stream.base.PartStaff "music21.stream.base.PartStaff") methods

Methods inherited from [`Part`](#music21.stream.base.Part "music21.stream.base.Part"):

|  |  |  |
| --- | --- | --- |
| * [`makeAccidentals()`](#music21.stream.base.Part.makeAccidentals "music21.stream.base.Part.makeAccidentals") | * [`mergeAttributes()`](#music21.stream.base.Part.mergeAttributes "music21.stream.base.Part.mergeAttributes") |  |

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`PartStaff`](#music21.stream.base.PartStaff "music21.stream.base.PartStaff") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## System

class music21.stream.base.System(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/stream/base.html#System)
:   Totally optional and used only in OMR and Capella: a designation that all the
    music in this Stream belongs in a single system.

    The system object has two attributes, systemNumber (which number is it)
    and systemNumbering which says at what point the numbering of
    systems resets. It can be either “Score” (default), “Opus”, or “Page”.

[`System`](#music21.stream.base.System "music21.stream.base.System") bases

* [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`System`](#music21.stream.base.System "music21.stream.base.System") read-only properties

Read-only properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`System`](#music21.stream.base.System "music21.stream.base.System") read/write properties

Read/write properties inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`System`](#music21.stream.base.System "music21.stream.base.System") methods

Methods inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`System`](#music21.stream.base.System "music21.stream.base.System") instance variables

Instance variables inherited from [`Stream`](#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |
