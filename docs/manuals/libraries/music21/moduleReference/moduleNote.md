Source: https://music21.org/music21docs/moduleReference/moduleNote.html

# music21.note

Classes and functions for creating Notes, Rests, and Lyrics.

The [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object is stored within,
and used to configure, [`Note`](#music21.note.Note "music21.note.Note") objects.

## Note

class music21.note.Note(*pitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *nameWithOctave: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/note.html#Note)
:   One of the most important music21 classes, a Note
    stores a single note (that is, not a rest or an unpitched element)
    that can be represented by one or more notational units – so
    for instance a C quarter-note and a D# eighth-tied-to-32nd are both
    a single Note object.

    A Note knows both its total duration and how to express itself as a set of
    tied notes of different lengths. For instance, a note of 2.5 quarters in
    length could be half tied to eighth or dotted quarter tied to quarter.

    The first argument to the Note is the pitch name (with or without
    octave, see the introduction to [`music21.pitch.Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")).
    Further arguments can be specified as keywords (such as type, dots, etc.)
    and are passed to the underlying [`music21.duration.Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") element.

    ```python
    >>> n = note.Note()
    >>> n
    <music21.note.Note C>
    >>> n.pitch
    <music21.pitch.Pitch C4>
    ```

    ```python
    >>> n = note.Note('B-')
    >>> n.name
    'B-'
    >>> n.octave is None
    True
    >>> n.pitch.implicitOctave
    4
    ```

    ```python
    >>> n = note.Note(name='D#')
    >>> n.name
    'D#'
    >>> n = note.Note(nameWithOctave='D#5')
    >>> n.nameWithOctave
    'D#5'
    ```

    Other ways of instantiating a Pitch object, such as by MIDI number or pitch class
    are also possible:

    ```python
    >>> note.Note(64).nameWithOctave
    'E4'
    ```

    All keyword args that are valid for Duration or Pitch objects
    are valid (as well as those for superclasses, NotRest, GeneralNote,
    Music21Object):

    ```python
    >>> n = note.Note(step='C', accidental='sharp', octave=2, id='csharp', type='eighth', dots=2)
    >>> n.nameWithOctave
    'C#2'
    >>> n.duration
    <music21.duration.Duration 0.875>
    ```

    **Equality and ordering**

    Two notes are equal if they pass all the equality tests for NotRest and their
    pitches are equal.

    Attributes that might change based on the wider context
    of a note (such as offset) are not compared. This test does not look at lyrics in
    establishing equality. (It may in the future.)

    ```python
    >>> note.Note('C4') == note.Note('C4')
    True
    ```

    Enharmonics are not equal:

    ```python
    >>> note.Note('D#4') == note.Note('E-4')
    False
    ```

    ```python
    >>> note.Note('C4', type='half') == note.Note('C4', type='quarter')
    False
    ```

    Notes, like pitches, also have an ordering based on their pitches.

    ```python
    >>> highE = note.Note('E5')
    >>> lowF = note.Note('F2')
    >>> otherHighE = note.Note('E5')
    ```

    ```python
    >>> highE > lowF
    True
    >>> highE < lowF
    False
    >>> highE >= otherHighE
    True
    >>> highE <= otherHighE
    True
    ```

    Notice you cannot compare Notes w/ ints or anything that does not have a
    .pitch attribute.

    ```python
    >>> highE < 50
    Traceback (most recent call last):
    TypeError: '<' not supported between instances of 'Note' and 'int'
    ```

    Note also that two objects can be >= and <= without being equal, because
    only pitch-height is being compared in <, <=, >, >= but duration and other
    elements are compared in equality.

    ```python
    >>> otherHighE.duration.type = 'whole'
    ```

    Now otherHighE is != highE

    ```python
    >>> highE == otherHighE
    False
    ```

    But it is both >= and <= it:

    ```python
    >>> highE >= otherHighE
    True
    >>> highE <= otherHighE
    True
    ```

    (The pigeonhole principle police have a bounty out on my head for this.)

[`Note`](#music21.note.Note "music21.note.Note") bases

* [`NotRest`](#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Note`](#music21.note.Note "music21.note.Note") read-only properties

Note.fullName
:   Return the most complete representation of this Note,
    providing duration and pitch information.

    ```python
    >>> n = note.Note('A-', quarterLength=1.5)
    >>> n.fullName
    'A-flat Dotted Quarter Note'
    ```

    ```python
    >>> n = note.Note('E~3', quarterLength=2)
    >>> n.fullName
    'E-half-sharp in octave 3 Half Note'
    ```

    ```python
    >>> n = note.Note('D', quarterLength=0.25)
    >>> n.pitch.microtone = 25
    >>> n.fullName
    'D (+25c) 16th Note'
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Note`](#music21.note.Note "music21.note.Note") read/write properties

Note.name
:   Return or set the pitch name from the [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object.
    See Pitch’s attribute [`name`](modulePitch.html#music21.pitch.Pitch.name "music21.pitch.Pitch.name").

Note.nameWithOctave
:   Return or set the pitch name with octave from the [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object.
    See Pitch’s attribute [`nameWithOctave`](modulePitch.html#music21.pitch.Pitch.nameWithOctave "music21.pitch.Pitch.nameWithOctave").

Note.octave
:   Return or set the octave value from the [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object.
    See [`octave`](modulePitch.html#music21.pitch.Pitch.octave "music21.pitch.Pitch.octave").

Note.pitches
:   Return the single [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object in a tuple.
    This property is designed to provide an interface analogous to
    that found on [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") so that [c.pitches for c in s.notes]
    provides a consistent interface for all objects.

    ```python
    >>> n = note.Note('g#')
    >>> n.nameWithOctave
    'G#'
    >>> n.pitches
    (<music21.pitch.Pitch G#>,)
    ```

    Since this is a Note, not a chord, from the list or tuple,
    only the first one will be used:

    ```python
    >>> n.pitches = [pitch.Pitch('c2'), pitch.Pitch('g2')]
    >>> n.nameWithOctave
    'C2'
    >>> n.pitches
    (<music21.pitch.Pitch C2>,)
    ```

    The value for setting must be a list or tuple:

    ```python
    >>> n.pitches = pitch.Pitch('C4')
    Traceback (most recent call last):
    music21.note.NoteException: cannot set pitches with provided object: C4
    ```

    For setting a single one, use n.pitch instead.

    Don’t use strings, or you will get a string back!

    ```python
    >>> n.pitches = ('C4', 'D4')
    >>> n.pitch
    'C4'
    >>> n.pitch.diatonicNoteNum
    Traceback (most recent call last):
    AttributeError: 'str' object has no attribute 'diatonicNoteNum'
    ```

Note.step
:   Return or set the pitch step from the [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object.
    See [`step`](modulePitch.html#music21.pitch.Pitch.step "music21.pitch.Pitch.step").

Read/write properties inherited from [`NotRest`](#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`notehead`](#music21.note.NotRest.notehead "music21.note.NotRest.notehead") * [`noteheadFill`](#music21.note.NotRest.noteheadFill "music21.note.NotRest.noteheadFill") | * [`noteheadParenthesis`](#music21.note.NotRest.noteheadParenthesis "music21.note.NotRest.noteheadParenthesis") * [`stemDirection`](#music21.note.NotRest.stemDirection "music21.note.NotRest.stemDirection") | * [`storedInstrument`](#music21.note.NotRest.storedInstrument "music21.note.NotRest.storedInstrument") * [`volume`](#music21.note.NotRest.volume "music21.note.NotRest.volume") |

Read/write properties inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") | * [`tie`](#music21.note.GeneralNote.tie "music21.note.GeneralNote.tie") |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Note`](#music21.note.Note "music21.note.Note") methods

Note.pitchChanged()[[source]](../_modules/music21/note.html#Note.pitchChanged)
:   Called by the underlying pitch if something changed there.

Note.transpose(*value*, *\**, *inPlace=False*)[[source]](../_modules/music21/note.html#Note.transpose)
:   Transpose the Note by the user-provided
    value. If the value is an integer, the transposition is treated in half steps.

    If the value is a string, any Interval string specification can be provided.

    ```python
    >>> a = note.Note('g4')
    >>> b = a.transpose('m3')
    >>> b
    <music21.note.Note B->
    >>> aInterval = interval.Interval(-6)
    >>> b = a.transpose(aInterval)
    >>> b
    <music21.note.Note C#>
    ```

    ```python
    >>> c = b.transpose(interval.GenericInterval(2))
    >>> c
    <music21.note.Note D#>
    ```

    ```python
    >>> a.transpose(aInterval, inPlace=True)
    >>> a
    <music21.note.Note C#>
    ```

    If the transposition value is an integer, take the KeySignature or Key context
    into account

    ```python
    >>> s = stream.Stream()
    >>> s.append(key.Key('D'))
    >>> s.append(note.Note('F'))
    >>> s.append(key.Key('b-', 'minor'))
    >>> s.append(note.Note('F'))
    >>> s.show('text')
    {0.0} <music21.key.Key of D major>
    {0.0} <music21.note.Note F>
    {1.0} <music21.key.Key of b- minor>
    {1.0} <music21.note.Note F>
    >>> for n in s.notes:
    ...     n.transpose(1, inPlace=True)
    >>> s.show('text')
    {0.0} <music21.key.Key of D major>
    {0.0} <music21.note.Note F#>
    {1.0} <music21.key.Key of b- minor>
    {1.0} <music21.note.Note G->
    ```

Methods inherited from [`NotRest`](#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`getInstrument()`](#music21.note.NotRest.getInstrument "music21.note.NotRest.getInstrument") | * [`hasVolumeInformation()`](#music21.note.NotRest.hasVolumeInformation "music21.note.NotRest.hasVolumeInformation") |  |

Methods inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.note.GeneralNote.__eq__ "music21.note.GeneralNote.__eq__") * [`addLyric()`](#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") | * [`augmentOrDiminish()`](#music21.note.GeneralNote.augmentOrDiminish "music21.note.GeneralNote.augmentOrDiminish") * [`getGrace()`](#music21.note.GeneralNote.getGrace "music21.note.GeneralNote.getGrace") | * [`insertLyric()`](#music21.note.GeneralNote.insertLyric "music21.note.GeneralNote.insertLyric") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Note`](#music21.note.Note "music21.note.Note") instance variables

Note.isNote
:   Boolean read-only value describing if this Note is a Note (True).

Note.isRest
:   Boolean read-only value describing if this Note is a Rest (False).

Note.pitch
:   A [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object containing all the
    information about the note’s pitch. Many .pitch properties and
    methods are also made Note properties also

Instance variables inherited from [`NotRest`](#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](#music21.note.NotRest.beams "music21.note.NotRest.beams") |  |  |

Instance variables inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`articulations`](#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") * [`expressions`](#music21.note.GeneralNote.expressions "music21.note.GeneralNote.expressions") | * [`isChord`](#music21.note.GeneralNote.isChord "music21.note.GeneralNote.isChord") | * [`lyrics`](#music21.note.GeneralNote.lyrics "music21.note.GeneralNote.lyrics") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Rest

class music21.note.Rest(*length: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *stepShift: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *fullMeasure: t.Literal[True, False, 'auto', 'always'] = 'auto'*, *\*\*keywords*)[[source]](../_modules/music21/note.html#Rest)
:   Rests are represented in music21 as GeneralNote objects that do not have
    a pitch object attached to them. By default, they have length 1.0 (Quarter Rest)

    Calling `notes` on a Stream does not get rests.
    However, the property `notesAndRests` of Streams
    gets rests as well.

    ```python
    >>> r = note.Rest()
    >>> isinstance(r, note.Note)
    False
    >>> r.duration.quarterLength = 2.0
    >>> r.duration.type
    'half'
    ```

    All Rests have the name property ‘rest’:

    ```python
    >>> r.name
    'rest'
    ```

    And their .pitches is an empty tuple

    ```python
    >>> r.pitches
    ()
    ```

    All arguments to Duration are valid in constructing:

    ```python
    >>> r2 = note.Rest(type='whole')
    >>> r2.duration.quarterLength
    4.0
    ```

    Or they can just be specified in without a type, and they’ll be evaluated automatically

    ```python
    >>> r3, r4 = note.Rest('half'), note.Rest(2.0)
    >>> r3 == r4
    True
    >>> r3.duration.quarterLength
    2.0
    ```

    Two rests are considered equal if their durations are equal.

    ```python
    >>> r1 = note.Rest('quarter')
    >>> r2 = note.Rest('quarter')
    >>> r1 == r2
    True
    >>> r1 != r2
    False
    ```

    ```python
    >>> r2.duration.quarterLength = 4/3
    >>> r1 == r2
    False
    ```

    A rest is never equal to a note.

    ```python
    >>> r1 == note.Note()
    False
    ```

    Currently, there are these convenience features, but they are going away
    (They were originally added because isinstance was slow. It is now very fast)
    >>> r.isRest
    True
    >>> r.isNote
    False

[`Rest`](#music21.note.Rest "music21.note.Rest") bases

* [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Rest`](#music21.note.Rest "music21.note.Rest") read-only properties

Rest.fullName
:   Return the most complete representation of this Rest,
    providing duration information.

    ```python
    >>> r = note.Rest(quarterLength=1.5)
    >>> r.fullName
    'Dotted Quarter Rest'
    ```

    ```python
    >>> note.Rest(type='whole').fullName
    'Whole Rest'
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Rest`](#music21.note.Rest "music21.note.Rest") read/write properties

Read/write properties inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") | * [`pitches`](#music21.note.GeneralNote.pitches "music21.note.GeneralNote.pitches") | * [`tie`](#music21.note.GeneralNote.tie "music21.note.GeneralNote.tie") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Rest`](#music21.note.Rest "music21.note.Rest") methods

Methods inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.note.GeneralNote.__eq__ "music21.note.GeneralNote.__eq__") * [`addLyric()`](#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") | * [`augmentOrDiminish()`](#music21.note.GeneralNote.augmentOrDiminish "music21.note.GeneralNote.augmentOrDiminish") * [`getGrace()`](#music21.note.GeneralNote.getGrace "music21.note.GeneralNote.getGrace") | * [`insertLyric()`](#music21.note.GeneralNote.insertLyric "music21.note.GeneralNote.insertLyric") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Rest`](#music21.note.Rest "music21.note.Rest") instance variables

Rest.fullMeasure
:   does this rest last a full measure or if it does, should it display
    itself as whole rest (or breve rest) and centered.

    Options are “auto” (default), False, True, and “always”

    “auto” is the default, where if the rest value happens to match the current
    time signature context (and there is no pickup or other padding),
    then display it as a whole rest, centered, etc. otherwise will display normally.

    False means do not display the rest as full measure whole rest,
    no matter what. This setting is often used by composers in very small time
    signatures such as 1/8, where a whole rest can look incongruous.

    True keeps the set duration, but will always display as a full measure rest
    even if it’s not the length of the measure
    (generally a whole note unless the time signature is very long).

    “always” means that on export, the duration will (EVENTUALLY, not yet!)
    update automatically to match the time signature context and always display
    as a whole rest. “always” does not work yet – functions as True.

    See examples in [`music21.musicxml.m21ToXml.MeasureExporter.restToXml()`](moduleMusicxmlM21ToXml.html#music21.musicxml.m21ToXml.MeasureExporter.restToXml "music21.musicxml.m21ToXml.MeasureExporter.restToXml")

Rest.isNote
:   Boolean read-only value describing if this Rest is a Note (False).

Rest.isRest
:   Boolean read-only value describing if this Rest is a Rest (True, obviously).

Rest.name
:   returns “rest” always. It is here so that you can get
    x.name on all .notesAndRests objects

Rest.stepShift
:   number of lines/spaces to shift the note upwards or downwards for display.

Instance variables inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`articulations`](#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") * [`expressions`](#music21.note.GeneralNote.expressions "music21.note.GeneralNote.expressions") | * [`isChord`](#music21.note.GeneralNote.isChord "music21.note.GeneralNote.isChord") | * [`lyrics`](#music21.note.GeneralNote.lyrics "music21.note.GeneralNote.lyrics") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Unpitched

class music21.note.Unpitched(*displayName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/note.html#Unpitched)
:   A General class of unpitched objects which appear at different places
    on the staff. Examples: percussion notation.

    ```python
    >>> unp = note.Unpitched()
    ```

    Unpitched elements have `displayStep` and `displayOctave`,
    which shows where they should be displayed as if the staff were a
    5-line staff in treble clef, but they do not have pitch
    objects:

    ```python
    >>> unp.displayStep
    'B'
    >>> unp.displayOctave
    4
    >>> unp.displayStep = 'G'
    >>> unp.pitch
    Traceback (most recent call last):
    AttributeError: 'Unpitched' object has no attribute 'pitch...
    ```

    Unpitched elements generally have an instrument object associated with them:

    ```python
    >>> unp.storedInstrument = instrument.Woodblock()
    >>> unp
    <music21.note.Unpitched 'Woodblock'>
    ```

    Two unpitched objects compare the same if their instrument and displayStep and
    displayOctave are equal (and satisfy all the equality requirements of
    their base classes):

    ```python
    >>> unp2 = note.Unpitched()
    >>> unp == unp2
    False
    >>> unp2.displayStep = 'G'
    >>> unp2.storedInstrument = instrument.Woodblock()
    >>> unp == unp2
    True
    >>> unp2.storedInstrument = instrument.Triangle()
    >>> unp == unp2
    False
    ```

[`Unpitched`](#music21.note.Unpitched "music21.note.Unpitched") bases

* [`NotRest`](#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Unpitched`](#music21.note.Unpitched "music21.note.Unpitched") read-only properties

Unpitched.displayName
:   Returns the nameWithOctave of the [`displayPitch()`](#music21.note.Unpitched.displayPitch "music21.note.Unpitched.displayPitch").

    ```python
    >>> unp = note.Unpitched('B2')
    >>> unp.displayName
    'B2'
    ```

Read-only properties inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](#music21.note.GeneralNote.fullName "music21.note.GeneralNote.fullName") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Unpitched`](#music21.note.Unpitched "music21.note.Unpitched") read/write properties

Read/write properties inherited from [`NotRest`](#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`notehead`](#music21.note.NotRest.notehead "music21.note.NotRest.notehead") * [`noteheadFill`](#music21.note.NotRest.noteheadFill "music21.note.NotRest.noteheadFill") | * [`noteheadParenthesis`](#music21.note.NotRest.noteheadParenthesis "music21.note.NotRest.noteheadParenthesis") * [`stemDirection`](#music21.note.NotRest.stemDirection "music21.note.NotRest.stemDirection") | * [`storedInstrument`](#music21.note.NotRest.storedInstrument "music21.note.NotRest.storedInstrument") * [`volume`](#music21.note.NotRest.volume "music21.note.NotRest.volume") |

Read/write properties inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") | * [`pitches`](#music21.note.GeneralNote.pitches "music21.note.GeneralNote.pitches") | * [`tie`](#music21.note.GeneralNote.tie "music21.note.GeneralNote.tie") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Unpitched`](#music21.note.Unpitched "music21.note.Unpitched") methods

Unpitched.displayPitch() → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/note.html#Unpitched.displayPitch)
:   returns a pitch object that is the same as the displayStep and displayOctave.
    it will never have an accidental.

    ```python
    >>> unp = note.Unpitched()
    >>> unp.displayStep = 'E'
    >>> unp.displayOctave = 4
    >>> unp.displayPitch()
    <music21.pitch.Pitch E4>
    ```

Methods inherited from [`NotRest`](#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`getInstrument()`](#music21.note.NotRest.getInstrument "music21.note.NotRest.getInstrument") | * [`hasVolumeInformation()`](#music21.note.NotRest.hasVolumeInformation "music21.note.NotRest.hasVolumeInformation") |  |

Methods inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.note.GeneralNote.__eq__ "music21.note.GeneralNote.__eq__") * [`addLyric()`](#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") | * [`augmentOrDiminish()`](#music21.note.GeneralNote.augmentOrDiminish "music21.note.GeneralNote.augmentOrDiminish") * [`getGrace()`](#music21.note.GeneralNote.getGrace "music21.note.GeneralNote.getGrace") | * [`insertLyric()`](#music21.note.GeneralNote.insertLyric "music21.note.GeneralNote.insertLyric") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Unpitched`](#music21.note.Unpitched "music21.note.Unpitched") instance variables

Instance variables inherited from [`NotRest`](#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](#music21.note.NotRest.beams "music21.note.NotRest.beams") |  |  |

Instance variables inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`articulations`](#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") * [`expressions`](#music21.note.GeneralNote.expressions "music21.note.GeneralNote.expressions") | * [`isChord`](#music21.note.GeneralNote.isChord "music21.note.GeneralNote.isChord") | * [`lyrics`](#music21.note.GeneralNote.lyrics "music21.note.GeneralNote.lyrics") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## NotRest

class music21.note.NotRest(*\**, *beams: [beam.Beams](moduleBeam.html#music21.beam.Beams "music21.beam.Beams") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *storedInstrument: [instrument.Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/note.html#NotRest)
:   Parent class for Note-like objects that are not rests; that is to say
    they have a stem, can be tied, and volume is important.
    Basically, that’s a [`Note`](#music21.note.Note "music21.note.Note") or [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
    (or their subclasses such as [`ChordSymbol`](moduleHarmony.html#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol")), or
    [`Unpitched`](#music21.note.Unpitched "music21.note.Unpitched") object.

    NotRest elements are generally not created on their own. It is a class
    that exists to store common functionality used by Note, Unpitched, and Chord objects.

    ```python
    >>> nr = note.NotRest(storedInstrument=instrument.Ocarina())
    >>> nr.stemDirection = 'up'
    ```

    * Changed in v9: beams is keyword only. Added storedInstrument keyword.

[`NotRest`](#music21.note.NotRest "music21.note.NotRest") bases

* [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`NotRest`](#music21.note.NotRest "music21.note.NotRest") read-only properties

Read-only properties inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](#music21.note.GeneralNote.fullName "music21.note.GeneralNote.fullName") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`NotRest`](#music21.note.NotRest "music21.note.NotRest") read/write properties

NotRest.notehead
:   Get or set the notehead type of this NotRest object.
    Valid notehead type names are found in note.noteheadTypeNames (see below):

    ```python
    >>> note.noteheadTypeNames
    ('arrow down', 'arrow up', 'back slashed', 'circle dot', 'circle-x', 'circled', 'cluster',
     'cross', 'diamond', 'do', 'fa', 'fa up', 'inverted triangle', 'la', 'left triangle',
     'mi', 'none', 'normal', 'other', 're', 'rectangle', 'slash', 'slashed', 'so',
     'square', 'ti', 'triangle', 'x')
    >>> n = note.Note()
    >>> n.notehead = 'diamond'
    >>> n.notehead
    'diamond'
    ```

    ```python
    >>> n.notehead = 'junk'
    Traceback (most recent call last):
    music21.note.NotRestException: not a valid notehead type name: 'junk'
    ```

NotRest.noteheadFill
:   Get or set the note head fill status of this NotRest. Valid note head fill values are
    True, False, or None (meaning default). “yes” and “no” are converted to True
    and False.

    ```python
    >>> n = note.Note()
    >>> n.noteheadFill = 'no'
    >>> n.noteheadFill
    False
    >>> n.noteheadFill = 'filled'
    >>> n.noteheadFill
    True
    ```

    ```python
    >>> n.noteheadFill = 'jelly'
    Traceback (most recent call last):
    music21.note.NotRestException: not a valid notehead fill value: 'jelly'
    ```

NotRest.noteheadParenthesis
:   Get or set the note head parentheses for this Note/Unpitched/Chord object.

    ```python
    >>> n = note.Note()
    >>> n.noteheadParenthesis
    False
    >>> n.noteheadParenthesis = True
    >>> n.noteheadParenthesis
    True
    ```

    ‘yes’ or 1 equate to True; ‘no’ or 0 to False

    ```python
    >>> n.noteheadParenthesis = 'no'
    >>> n.noteheadParenthesis
    False
    ```

    Anything else raises an exception:

    ```python
    >>> n.noteheadParenthesis = 'blah'
    Traceback (most recent call last):
    music21.note.NotRestException: notehead parentheses must be True or False, not 'blah'
    ```

NotRest.stemDirection
:   Get or set the stem direction of this NotRest object.
    Valid stem direction names are found in note.stemDirectionNames (see below).

    ```python
    >>> note.stemDirectionNames
    ('double', 'down', 'noStem', 'none', 'unspecified', 'up')
    >>> n = note.Note()
    ```

    By default, a Note’s stemDirection is ‘unspecified’
    meaning that it is unknown:

    ```python
    >>> n.stemDirection
    'unspecified'
    ```

    ```python
    >>> n.stemDirection = 'noStem'
    >>> n.stemDirection
    'noStem'
    ```

    The alias ‘none’ (the string) is the same as ‘noStem’

    ```python
    >>> n.stemDirection = 'none'
    >>> n.stemDirection
    'noStem'
    ```

    ```python
    >>> n.stemDirection = 'junk'
    Traceback (most recent call last):
    music21.note.NotRestException: not a valid stem direction name: junk
    ```

    Stem direction can be set explicitly to None to remove
    any prior stem information, same as ‘unspecified’:

    ```python
    >>> n.stemDirection = None
    >>> n.stemDirection
    'unspecified'
    ```

NotRest.storedInstrument
:   Get or set the [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") that
    should be used to play this note, overriding whatever
    Instrument object may be active in the Stream. (See
    [`getInstrument()`](#music21.note.NotRest.getInstrument "music21.note.NotRest.getInstrument") for a means of retrieving storedInstrument
    if available before falling back to a context search to find
    the active instrument.)

    ```python
    >>> snare = note.Unpitched()
    >>> snare.storedInstrument = instrument.SnareDrum()
    >>> snare.storedInstrument
    <music21.instrument.SnareDrum 'Snare Drum'>
    >>> snare
    <music21.note.Unpitched 'Snare Drum'>
    ```

NotRest.volume
:   Get and set the [`Volume`](moduleVolume.html#music21.volume.Volume "music21.volume.Volume") object of this object.
    Volume objects are created on demand.

    ```python
    >>> n1 = note.Note()
    >>> n1.volume.velocity = 120
    >>> n2 = note.Note()
    >>> n2.volume = 80  # can directly set a velocity value
    >>> s = stream.Stream()
    >>> s.append([n1, n2])
    >>> [n.volume.velocity for n in s.notes]
    [120, 80]
    ```

Read/write properties inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") | * [`pitches`](#music21.note.GeneralNote.pitches "music21.note.GeneralNote.pitches") | * [`tie`](#music21.note.GeneralNote.tie "music21.note.GeneralNote.tie") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`NotRest`](#music21.note.NotRest "music21.note.NotRest") methods

NotRest.getInstrument(*\**, *returnDefault: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True] = True*) → [instrument.Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")[[source]](../_modules/music21/note.html#NotRest.getInstrument)

NotRest.getInstrument(*\**, *returnDefault: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*) → [instrument.Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   Retrieves the .storedInstrument on this NotRest instance, if any.
    If one is not found, executes a context search (without following
    derivations) to find the closest (i.e., active) instrument in the
    stream hierarchy.

    Returns a default instrument if no instrument is found in the context
    and returnDefault is True (default).

    ```python
    >>> n = note.Note()
    >>> m = stream.Measure([n])
    >>> n.getInstrument(returnDefault=False) is None
    True
    >>> dulcimer = instrument.Dulcimer()
    >>> m.insert(0, dulcimer)
    >>> n.getInstrument() is dulcimer
    True
    ```

    Overridden .storedInstrument is privileged:

    ```python
    >>> picc = instrument.Piccolo()
    >>> n.storedInstrument = picc
    >>> n.getInstrument() is picc
    True
    ```

    Instruments in containing streams ARE found:

    ```python
    >>> n.storedInstrument = None
    >>> m.remove(dulcimer)
    >>> p = stream.Part([m])
    >>> p.insert(0, dulcimer)
    >>> n.getInstrument() is dulcimer
    True
    ```

    But not if the instrument is only found in a derived stream:

    ```python
    >>> derived = p.stripTies()
    >>> p.remove(dulcimer)
    >>> derived.getInstruments().first()
    <music21.instrument.Dulcimer 'Dulcimer'>
    >>> n.getInstrument(returnDefault=False) is None
    True
    ```

    Electing to return a default generic Instrument:

    ```python
    >>> n.getInstrument(returnDefault=True)
    <music21.instrument.Instrument ''>
    ```

NotRest.hasVolumeInformation() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/note.html#NotRest.hasVolumeInformation)
:   Returns bool whether volume was set – saving some time for advanced
    users (such as MusicXML exporters) that only want to look at the volume
    if it is already there.

    ```python
    >>> n = note.Note()
    >>> n.hasVolumeInformation()
    False
    >>> n.volume
     <music21.volume.Volume realized=0.71>
    >>> n.hasVolumeInformation()
    True
    ```

Methods inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.note.GeneralNote.__eq__ "music21.note.GeneralNote.__eq__") * [`addLyric()`](#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") | * [`augmentOrDiminish()`](#music21.note.GeneralNote.augmentOrDiminish "music21.note.GeneralNote.augmentOrDiminish") * [`getGrace()`](#music21.note.GeneralNote.getGrace "music21.note.GeneralNote.getGrace") | * [`insertLyric()`](#music21.note.GeneralNote.insertLyric "music21.note.GeneralNote.insertLyric") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`NotRest`](#music21.note.NotRest "music21.note.NotRest") instance variables

NotRest.beams
:   A [`Beams`](moduleBeam.html#music21.beam.Beams "music21.beam.Beams") object that contains
    information about the beaming of this note.

Instance variables inherited from [`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`articulations`](#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") * [`expressions`](#music21.note.GeneralNote.expressions "music21.note.GeneralNote.expressions") | * [`isChord`](#music21.note.GeneralNote.isChord "music21.note.GeneralNote.isChord") | * [`lyrics`](#music21.note.GeneralNote.lyrics "music21.note.GeneralNote.lyrics") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## GeneralNote

class music21.note.GeneralNote(*\**, *duration: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *lyric: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Lyric](#music21.note.Lyric "music21.note.Lyric") = None*, *\*\*keywords*)[[source]](../_modules/music21/note.html#GeneralNote)
:   A GeneralNote object is the base class object
    for the [`Note`](#music21.note.Note "music21.note.Note"),
    [`Rest`](#music21.note.Rest "music21.note.Rest"), [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"),
    and related objects.

    Keywords can be passed to
    a GeneralNote which are then passed to the
    underlying [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration").
    These keywords might be listed like
    type=’16th’, dots=2 etc. to create a
    double-dotted sixteenth note.

    In almost every circumstance, you should
    create note.Note() or note.Rest() or chord.Chord()
    objects directly, and not use this underlying
    structure.

    ```python
    >>> gn = note.GeneralNote(type='16th', dots=2)
    >>> gn.quarterLength
    0.4375
    ```

    **Equality**

    GeneralNote objects are equal if they pass superclass tests (e.g., their durations are equal),
    and they have the same articulation and expression classes (in any order),
    and their ties are equal.

[`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote") read-only properties

GeneralNote.fullName

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote") read/write properties

GeneralNote.lyric
:   The lyric property can
    be used to get and set a lyric for this
    Note, Chord, or Rest. This is a simplified version of the more general
    [`addLyric()`](#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") method.

    ```python
    >>> a = note.Note('A4')
    >>> a.lyrics
    []
    >>> a.lyric = 'hel-'
    >>> a.lyric
    'hel'
    >>> a.lyrics
    [<music21.note.Lyric number=1 syllabic=begin text='hel'>]
    ```

    Eliminate Lyrics by setting a.lyric to None

    ```python
    >>> a.lyric = None
    >>> a.lyric
    >>> a.lyrics
    []
    ```

    Set multiple lyrics with n separated text:

    ```python
    >>> a.lyric = '1. Hi\n2. Bye'
    >>> a.lyric
    '1. Hi\n2. Bye'
    >>> a.lyrics
    [<music21.note.Lyric number=1 syllabic=single text='1. Hi'>,
     <music21.note.Lyric number=2 syllabic=single text='2. Bye'>]
    ```

    You can also set a lyric with a lyric object directly:

    ```python
    >>> b = note.Note('B5')
    >>> ly = note.Lyric('bon-')
    >>> b.lyric = ly
    >>> b.lyrics
    [<music21.note.Lyric number=1 syllabic=begin text='bon'>]
    >>> b.lyric
    'bon'
    ```

    * Changed in v6.7: added setting to a Lyric object. Removed undocumented
      setting to False instead of setting to None

GeneralNote.pitches
:   Returns an empty tuple. (Useful for iterating over GeneralNotes since they
    include Notes and Chords.)

GeneralNote.tie
:   Return and set a `Tie` object, or None.

    ```python
    >>> n = note.Note()
    >>> n.tie is None
    True
    >>> n.tie = tie.Tie('start')
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote") methods

GeneralNote.\_\_eq\_\_(*other*)[[source]](../_modules/music21/note.html#GeneralNote.__eq__)
:   Define equality for Music21Objects. See main class docs.

GeneralNote.addLyric(*text*, *lyricNumber=None*, *\**, *applyRaw=False*, *lyricIdentifier=None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/note.html#GeneralNote.addLyric)
:   Adds a lyric, or an additional lyric, to a Note, Chord, or Rest’s lyric list.
    If lyricNumber is not None, a specific line of lyric text can be set.
    The lyricIdentifier can also be set.

    ```python
    >>> n1 = note.Note()
    >>> n1.addLyric('hello')
    >>> n1.lyrics[0].text
    'hello'
    >>> n1.lyrics[0].number
    1
    ```

    An added option gives the lyric number, not the list position

    ```python
    >>> n1.addLyric('bye', 3)
    >>> n1.lyrics[1].text
    'bye'
    >>> n1.lyrics[1].number
    3
    >>> for lyr in n1.lyrics:
    ...     print(lyr.text)
    hello
    bye
    ```

    Replace an existing lyric by specifying the same number:

    ```python
    >>> n1.addLyric('ciao', 3)
    >>> n1.lyrics[1].text
    'ciao'
    >>> n1.lyrics[1].number
    3
    ```

    Giving a lyric with a hyphen at either end will set whether it
    is part of a multisyllable word:

    ```python
    >>> n1.addLyric('good-')
    >>> n1.lyrics[2].text
    'good'
    >>> n1.lyrics[2].syllabic
    'begin'
    ```

    This feature can be overridden by specifying the keyword only argument “applyRaw=True”:

    ```python
    >>> n1.addLyric('-5', applyRaw=True)
    >>> n1.lyrics[3].text
    '-5'
    >>> n1.lyrics[3].syllabic
    'single'
    ```

GeneralNote.augmentOrDiminish(*scalar*, *\**, *inPlace=False*)[[source]](../_modules/music21/note.html#GeneralNote.augmentOrDiminish)
:   Given a scalar greater than zero, return a Note with a scaled Duration.
    If inPlace is True, this is done in-place and the method returns None.
    If inPlace is False [default], this returns a modified deepcopy.

    * Changed in v5: inPlace is now False.

    ```python
    >>> n = note.Note('g#')
    >>> n.quarterLength = 3
    >>> n.augmentOrDiminish(2, inPlace=True)
    >>> n.quarterLength
    6.0
    ```

    ```python
    >>> c = chord.Chord(['g#', 'a#', 'd'])
    >>> c.quarterLength = 2
    >>> c.augmentOrDiminish(0.25, inPlace=True)
    >>> c.quarterLength
    0.5
    ```

    ```python
    >>> n = note.Note('g#')
    >>> n.augmentOrDiminish(-1)
    Traceback (most recent call last):
    music21.note.NoteException: scalar must be greater than zero
    ```

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 3
    >>> n2 = n.augmentOrDiminish(1/3, inPlace=False)
    >>> n2.quarterLength
    1.0
    >>> n.quarterLength
    3.0
    ```

GeneralNote.getGrace(*\**, *appoggiatura=False*, *inPlace=False*)[[source]](../_modules/music21/note.html#GeneralNote.getGrace)
:   Return a grace version of this GeneralNote

    ```python
    >>> n = note.Note('G4', quarterLength=2)
    >>> n.duration.quarterLength
    2.0
    >>> n.duration.isGrace
    False
    >>> n.duration
    <music21.duration.Duration 2.0>
    >>> n.duration.type
    'half'
    >>> n.duration.components
    (DurationTuple(type='half', dots=0, quarterLength=2.0),)
    ```

    ```python
    >>> ng = n.getGrace()
    >>> ng.duration.quarterLength
    0.0
    >>> ng.duration.isGrace
    True
    >>> ng.duration
    <music21.duration.GraceDuration unlinked type:half quarterLength:0.0>
    >>> ng.duration.type
    'half'
    >>> ng.duration.components
    (DurationTuple(type='half', dots=0, quarterLength=0.0),)
    ```

    Appoggiaturas are still a work in progress.

    * Changed in v6: corrected spelling of appoggiatura keyword.

    ```python
    >>> ng2 = n.getGrace(appoggiatura=True)
    >>> ng2.duration
    <music21.duration.AppoggiaturaDuration unlinked type:half quarterLength:0.0>
    >>> ng2.duration.slash
    False
    ```

    Set inPlace to True to change the duration element on the Note. This can have
    negative consequences if the Note is in a stream.

    ```python
    >>> r = note.Rest(quarterLength=0.5)
    >>> r.getGrace(inPlace=True)
    >>> r.duration
    <music21.duration.GraceDuration unlinked type:eighth quarterLength:0.0>
    ```

GeneralNote.insertLyric(*text*, *index=0*, *\**, *applyRaw=False*, *identifier=None*)[[source]](../_modules/music21/note.html#GeneralNote.insertLyric)
:   Inserts a lyric into the Note, Chord, or Rest’s lyric list in front of
    the index specified (0 by default), using index + 1 as the inserted lyric’s
    line number. shifts line numbers of all following lyrics in list

    ```python
    >>> n1 = note.Note()
    >>> n1.addLyric('second')
    >>> n1.lyrics
    [<music21.note.Lyric number=1 syllabic=single text='second'>]
    >>> n1.insertLyric('first', 0)
    >>> n1.lyrics
    [<music21.note.Lyric number=1 syllabic=single text='first'>,
     <music21.note.Lyric number=2 syllabic=single text='second'>]
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`GeneralNote`](#music21.note.GeneralNote "music21.note.GeneralNote") instance variables

GeneralNote.articulations
:   a list of articulations such
    as [`Staccato`](moduleArticulations.html#music21.articulations.Staccato "music21.articulations.Staccato"), etc.) that are stored on this Note.

GeneralNote.expressions
:   a list of expressions (such
    as [`Fermata`](moduleExpressions.html#music21.expressions.Fermata "music21.expressions.Fermata"), etc.)
    that are stored on this Note.

GeneralNote.isChord
:   Boolean read-only value describing if this object is a Chord.

GeneralNote.lyrics
:   A list of [`Lyric`](#music21.note.Lyric "music21.note.Lyric") objects.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Lyric

class music21.note.Lyric(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *\**, *applyRaw: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *syllabic: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[None, 'begin', 'single', 'end', 'middle', 'composite'] = None*, *identifier: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/note.html#Lyric)
:   An object representing a single Lyric as part of a note’s .lyrics property.

    The note.lyric property is a simple way of specifying a single lyric, but
    Lyric objects are needed for working with multiple lyrics.

    ```python
    >>> l = note.Lyric(text='hello')
    >>> l
    <music21.note.Lyric number=1 syllabic=single text='hello'>
    ```

    Music21 processes leading and following hyphens intelligently by default.

    ```python
    >>> l2 = note.Lyric(text='hel-')
    >>> l2
    <music21.note.Lyric number=1 syllabic=begin text='hel'>
    ```

    If applyRaw is set to True then hyphens will be treated as actual text,
    and the syllabic will be set to “single”.

    ```python
    >>> l3 = note.Lyric(number=3, text='hel-', applyRaw=True)
    >>> l3
    <music21.note.Lyric number=3 syllabic=single text='hel-'>
    ```

    Lyrics have four properties: text, number, identifier, syllabic (single,
    begin, middle, end, or (not in musicxml) composite)

    ```python
    >>> l3.text
    'hel-'
    ```

    ```python
    >>> l3.number
    3
    ```

    ```python
    >>> l3.syllabic
    'single'
    ```

    Note musicXML only supports one ‘identifier’ attribute which is called
    ‘number’ but which can be a number or a descriptive identifier like
    ‘part2verse1.’ To preserve lyric ordering, music21 stores a number and a
    descriptive identifier separately. The descriptive identifier is by default
    the same as the number, but in cases where a string identifier is present,
    it will be different.

    Both music21 and musicxml support multiple Lyric objects in the same stanza,
    for instance, if there is an elision on a note then multiple lyrics with
    different syllabics can appear on a single note. In music21 these are supported
    by setting .components into a list of Lyric object. For instance in
    the madrigal “Il bianco e dolce cigno”, the “co” and “e” of “bianco e”
    are elided into a single lyric:

    ```python
    >>> bianco = note.Lyric()
    >>> co = note.Lyric('co', syllabic='end')
    >>> e = note.Lyric('e', syllabic='single')
    >>> bianco.components = [co, e]
    >>> bianco.isComposite
    True
    >>> bianco.text
    'co e'
    >>> bianco.syllabic
    'composite'
    >>> e.elisionBefore = '_'
    >>> bianco.text
    'co_e'
    ```

    ```python
    >>> [component.syllabic for component in bianco.components]
    ['end', 'single']
    ```

    Custom elision elements for composite components will be supported later.

    * New in v6.7: composite components, elisionBefore
    * Changed in v8: lyric text can be an empty string, but not None.

[`Lyric`](#music21.note.Lyric "music21.note.Lyric") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Lyric`](#music21.note.Lyric "music21.note.Lyric") read-only properties

Lyric.isComposite
:   Returns True if this Lyric has composite elements,
    for instance, is multiple lyrics placed together.

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

Read-only properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleStyle.html#music21.style.StyleMixin.hasEditorialInformation "music21.style.StyleMixin.hasEditorialInformation") | * [`hasStyleInformation`](moduleStyle.html#music21.style.StyleMixin.hasStyleInformation "music21.style.StyleMixin.hasStyleInformation") |  |

[`Lyric`](#music21.note.Lyric "music21.note.Lyric") read/write properties

Lyric.identifier
:   By default, this is the same as self.number. However, if there is a
    descriptive identifier like ‘part2verse1’, it is stored here and
    will be different from self.number. When converting to musicXML,
    this property will be stored in the lyric ‘number’ attribute which
    can store a number or a descriptive identifier but not both.

    ```python
    >>> l = note.Lyric()
    >>> l.number = 12
    >>> l.identifier
    12
    ```

    ```python
    >>> l.identifier = 'Rainbow'
    >>> l.identifier
    'Rainbow'
    ```

    Default value is the same as default for number, that is, 1:

    ```python
    >>> note.Lyric().identifier
    1
    ```

Lyric.number
:   This stores the number of the lyric (which determines the order
    lyrics appear in the score if there are multiple lyrics). Unlike
    the musicXML lyric number attribute, this value must always be a
    number; lyric order is always stored in this form. Descriptive
    identifiers like ‘part2verse1’ which can be found in the musicXML
    lyric number attribute should be stored in self.identifier.

    Default is 1

    ```python
    >>> l = note.Lyric('Hi')
    >>> l.number
    1
    ```

    ```python
    >>> l.number = 5
    >>> l.number
    5
    >>> l.number = None
    Traceback (most recent call last):
    music21.note.LyricException: Number best be number
    ```

Lyric.rawText
:   returns the text of the syllable with ‘-’ etc.

    ```python
    >>> l = note.Lyric('hel-')
    >>> l.text
    'hel'
    >>> l.rawText
    'hel-'
    ```

    ```python
    >>> l = note.Lyric('lo', syllabic='end')
    >>> l.rawText
    '-lo'
    ```

    ```python
    >>> l = note.Lyric('-ti-')
    >>> l.rawText
    '-ti-'
    ```

    ```python
    >>> l = note.Lyric('bye')
    >>> l.rawText
    'bye'
    ```

    Composite lyrics take their endings from the first and last components:

    ```python
    >>> composite = note.Lyric()
    >>> co = note.Lyric('co', syllabic='end')
    >>> e = note.Lyric('e', syllabic='single')
    >>> e.elisionBefore = '_'
    >>> composite.components = [co, e]
    >>> composite.rawText
    '-co_e'
    >>> e.syllabic = 'middle'
    >>> composite.rawText
    '-co_e-'
    ```

Lyric.syllabic
:   Returns or sets the syllabic property of a lyric.

    ```python
    >>> fragment = note.Lyric('frag', syllabic='begin')
    >>> fragment.syllabic
    'begin'
    >>> fragment.rawText
    'frag-'
    >>> fragment.syllabic = 'end'
    >>> fragment.rawText
    '-frag'
    ```

    Illegal values raise a LyricException

    ```python
    >>> fragment.syllabic = 'slide'
    Traceback (most recent call last):
    music21.note.LyricException: Syllabic value 'slide' is not in
        note.SYLLABIC_CHOICES, namely:
        [None, 'begin', 'single', 'end', 'middle', 'composite']
    ```

Lyric.text
:   Gets or sets the text of the lyric. For composite lyrics, set
    the text of individual components instead of setting the text here.

    ```python
    >>> l = note.Lyric()
    >>> l.text
    ''
    >>> l.text = 'hi'
    >>> l.text
    'hi'
    ```

    Setting the text of a composite lyric wipes out the components:

    ```python
    >>> bianco = note.Lyric()
    >>> co = note.Lyric('co', syllabic='end')
    >>> e = note.Lyric('e', syllabic='single')
    >>> bianco.components = [co, e]
    >>> bianco.isComposite
    True
    >>> bianco.text
    'co e'
    >>> bianco.text = 'co_e'
    >>> bianco.isComposite
    False
    ```

Read/write properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`editorial`](moduleStyle.html#music21.style.StyleMixin.editorial "music21.style.StyleMixin.editorial") | * [`style`](moduleStyle.html#music21.style.StyleMixin.style "music21.style.StyleMixin.style") |  |

[`Lyric`](#music21.note.Lyric "music21.note.Lyric") methods

Lyric.setTextAndSyllabic(*rawText: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *applyRaw: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/note.html#Lyric.setTextAndSyllabic)
:   Given a setting for rawText and applyRaw,
    sets the syllabic type for a lyric based on the rawText. Useful for
    parsing raw text from, say, an OMR score. Or just to quickly set text
    and syllabic.

    ```python
    >>> l = note.Lyric()
    >>> l.setTextAndSyllabic('hel-')
    >>> l.text
    'hel'
    >>> l.syllabic
    'begin'
    >>> l.setTextAndSyllabic('-lo')
    >>> l.text
    'lo'
    >>> l.syllabic
    'end'
    >>> l.setTextAndSyllabic('the')
    >>> l.text
    'the'
    >>> l.syllabic
    'single'
    ```

    If applyRaw is True then this will assume you actually want hyphens
    in the text, and if syllabic is None, sets it to ‘single’

    ```python
    >>> l = note.Lyric()
    >>> l.setTextAndSyllabic('hel-', applyRaw=True)
    >>> l.text
    'hel-'
    >>> l.syllabic
    'single'
    ```

    If applyRaw is True, other syllabic settings except None are retained

    ```python
    >>> l.syllabic = 'begin'
    >>> l.setTextAndSyllabic('-lo', applyRaw=True)
    >>> l.text
    '-lo'
    >>> l.syllabic
    'begin'
    ```

    This method wipes out components.
