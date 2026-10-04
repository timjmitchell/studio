Source: https://music21.org/music21docs/moduleReference/moduleKey.html

# music21.key

This module defines objects for representing key signatures as well as key
areas. The [`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature") is used in
`Measure` objects for defining notated key signatures.

The [`Key`](#music21.key.Key "music21.key.Key") object is a fuller representation not just of
a key signature but also of the key of a region.

## KeySignature

class music21.key.KeySignature(*sharps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 0*, *\*\*keywords*)[[source]](../_modules/music21/key.html#KeySignature)
:   A KeySignature object specifies the signature to be used for a piece; it normally
    takes one argument: an int giving the number of sharps,
    or, if negative, the number of flats.

    If you are starting with the name of a key, see the [`Key`](#music21.key.Key "music21.key.Key") object.

    ```python
    >>> A = key.KeySignature(3)
    >>> A
    <music21.key.KeySignature of 3 sharps>
    ```

    ```python
    >>> Eflat = key.KeySignature(-3)
    >>> Eflat
    <music21.key.KeySignature of 3 flats>
    ```

    If you want to get a real Key, then use the [`Key`](#music21.key.Key "music21.key.Key") object instead:

    ```python
    >>> illegal = key.KeySignature('c#')
    Traceback (most recent call last):
    music21.key.KeySignatureException: Cannot get a KeySignature from this
        "number" of sharps: 'c#'; did you mean to use a key.Key() object instead?
    ```

    ```python
    >>> legal = key.Key('c#')
    >>> legal.sharps
    4
    >>> legal
    <music21.key.Key of c# minor>
    ```

    To set a non-traditional Key Signature, create a KeySignature object
    with sharps=None, and then set the alteredPitches list:

    ```python
    >>> unusual = key.KeySignature(sharps=None)
    >>> unusual.alteredPitches = ['E-', 'G#']
    >>> unusual
    <music21.key.KeySignature of pitches: [E-, G#]>
    >>> unusual.isNonTraditional
    True
    ```

    To set a pitch as displayed in a particular octave, create a non-traditional
    KeySignature and then set pitches with octaves:

    ```python
    >>> unusual = key.KeySignature(sharps=None)
    >>> unusual.alteredPitches = ['F#4']
    >>> unusual
    <music21.key.KeySignature of pitches: [F#4]>
    ```

    If the accidental applies to all octaves but is being displayed differently
    then you are done, but if you want them to apply only to the octave displayed
    in then set .accidentalsApplyOnlyToOctave to True:

    ```python
    >>> unusual.accidentalsApplyOnlyToOctave
    False
    >>> unusual.accidentalsApplyOnlyToOctave = True
    ```

    **Equality**

    Two KeySignatures are equal if they pass all super().\_\_eq\_\_ checks and
    their sharps are equal. Currently, non-standard key signatures are not
    checked (this may change).

    ```python
    >>> sharp2 = key.KeySignature(2)
    >>> flat4 = key.KeySignature(-4)
    >>> sharp2 == flat4
    False
    >>> sharp2 == key.KeySignature(2)
    True
    ```

    * Changed in v7: sharps defaults to 0 (key of no flats/sharps)
      rather than None for nontraditional keys.

[`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature") read-only properties

KeySignature.isNonTraditional
:   Returns bool if this is a non-traditional KeySignature:

    ```python
    >>> g = key.KeySignature(3)
    >>> g.isNonTraditional
    False
    ```

    ```python
    >>> g = key.KeySignature(sharps=None)
    >>> g.alteredPitches = [pitch.Pitch('E`')]
    >>> g.isNonTraditional
    True
    ```

    ```python
    >>> g
    <music21.key.KeySignature of pitches: [E`]>
    ```

    ```python
    >>> g.accidentalByStep('E')
    <music21.pitch.Accidental half-flat>
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature") read/write properties

KeySignature.alteredPitches
:   Return or set a list of music21.pitch.Pitch objects that are altered by this
    KeySignature. That is, all Pitch objects that will receive an accidental.

    ```python
    >>> a = key.KeySignature(3)
    >>> a.alteredPitches
    [<music21.pitch.Pitch F#>, <music21.pitch.Pitch C#>, <music21.pitch.Pitch G#>]
    >>> b = key.KeySignature(1)
    >>> b.alteredPitches
    [<music21.pitch.Pitch F#>]
    ```

    ```python
    >>> c = key.KeySignature(9)
    >>> [str(p) for p in c.alteredPitches]
    ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#', 'F##', 'C##']
    ```

    ```python
    >>> d = key.KeySignature(-3)
    >>> d.alteredPitches
    [<music21.pitch.Pitch B->, <music21.pitch.Pitch E->, <music21.pitch.Pitch A->]
    ```

    ```python
    >>> e = key.KeySignature(-1)
    >>> e.alteredPitches
    [<music21.pitch.Pitch B->]
    ```

    ```python
    >>> f = key.KeySignature(-6)
    >>> [str(p) for p in f.alteredPitches]
    ['B-', 'E-', 'A-', 'D-', 'G-', 'C-']
    ```

    ```python
    >>> g = key.KeySignature(-8)
    >>> [str(p) for p in g.alteredPitches]
    ['B-', 'E-', 'A-', 'D-', 'G-', 'C-', 'F-', 'B--']
    ```

    Non-standard, non-traditional key signatures can set their own
    altered pitches cache.

    ```python
    >>> nonTrad = key.KeySignature(sharps=None)
    >>> nonTrad.alteredPitches = ['B-', 'F#', 'E-', 'G#']
    >>> nonTrad.alteredPitches
    [<music21.pitch.Pitch B->,
     <music21.pitch.Pitch F#>,
     <music21.pitch.Pitch E->,
     <music21.pitch.Pitch G#>]
    ```

KeySignature.sharps
:   Get or set the number of sharps. If the number is negative
    then it sets the number of flats. Equivalent to musicxml’s ‘fifths’
    attribute.

    ```python
    >>> ks1 = key.KeySignature(2)
    >>> ks1.sharps
    2
    >>> ks1.sharps = -4
    >>> ks1
    <music21.key.KeySignature of 4 flats>
    ```

    Can be set to None for a non-traditional key signature

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature") methods

KeySignature.accidentalByStep(*step: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['C', 'D', 'E', 'F', 'G', 'A', 'B']*) → [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/key.html#KeySignature.accidentalByStep)
:   Given a step (C, D, E, F, etc.) return the accidental
    for that note in this key (using the natural minor for minor)
    or None if there is none.

    ```python
    >>> g = key.KeySignature(1)
    >>> g.accidentalByStep('F')
    <music21.pitch.Accidental sharp>
    >>> g.accidentalByStep('G') is None
    True
    ```

    ```python
    >>> f = key.KeySignature(-1)
    >>> bbNote = note.Note('B-5')
    >>> f.accidentalByStep(bbNote.step)
    <music21.pitch.Accidental flat>
    ```

    Fix a wrong note in F-major:

    ```python
    >>> wrongBNote = note.Note('B#4')
    >>> if f.accidentalByStep(wrongBNote.step) != wrongBNote.pitch.accidental:
    ...    wrongBNote.pitch.accidental = f.accidentalByStep(wrongBNote.step)
    >>> wrongBNote
    <music21.note.Note B->
    ```

    Set all notes to the correct notes for a key using the
    note’s Key Context. Before:

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(key.KeySignature(4))  # E-major or C-sharp-minor
    >>> s1.append(note.Note('C', type='half'))
    >>> s1.append(note.Note('E-', type='half'))
    >>> s1.append(key.KeySignature(-4))  # A-flat-major or F-minor
    >>> s1.append(note.Note('A', type='whole'))
    >>> s1.append(note.Note('F#', type='whole'))
    >>> s1.show()
    ```

    [![../_images/keyAccidentalByStep_Before.png](../_images/keyAccidentalByStep_Before.png)](../_images/keyAccidentalByStep_Before.png)

    After:

    ```python
    >>> for n in s1.notes:
    ...    n.pitch.accidental = n.getContextByClass(key.KeySignature).accidentalByStep(n.step)
    >>> s1.show()
    ```

    [![../_images/keyAccidentalByStep.png](../_images/keyAccidentalByStep.png)](../_images/keyAccidentalByStep.png)

KeySignature.asKey(*mode: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *tonic: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/key.html#KeySignature.asKey)
:   Return a key.Key object representing this KeySignature object as a key in the
    given mode or in the given tonic. If mode is None, and tonic is not provided,
    major is assumed. If both mode and tonic are provided, the tonic is ignored.

    ```python
    >>> ks = key.KeySignature(2)
    >>> ks.asKey()
    <music21.key.Key of D major>
    >>> ks.asKey(mode='minor')
    <music21.key.Key of b minor>
    ```

    If mode is None, an attempt is made to solve for the mode:

    ```python
    >>> ks.asKey(tonic='A')
    <music21.key.Key of A mixolydian>
    ```

    But will raise KeyException if an impossible solution is requested:

    ```python
    >>> ks.asKey(tonic='D#')
    Traceback (most recent call last):
    music21.key.KeyException: Could not solve for mode from sharps=2, tonic=D#
    ```

    Ionian and Aeolian are supplied instead of major or minor when deriving mode in this way:

    ```python
    >>> ks2 = key.KeySignature()
    >>> ks2.asKey()
    <music21.key.Key of C major>
    >>> ks2.asKey(tonic='C')
    <music21.key.Key of C ionian>
    ```

    * New in v7: tonic argument to solve for mode.

KeySignature.getScale(*mode='major'*)[[source]](../_modules/music21/key.html#KeySignature.getScale)
:   Return a [`music21.scale.Scale`](moduleScale.html#music21.scale.Scale "music21.scale.Scale") object (or, actually, a subclass such as
    [`MajorScale`](moduleScale.html#music21.scale.MajorScale "music21.scale.MajorScale") or [`MinorScale`](moduleScale.html#music21.scale.MinorScale "music21.scale.MinorScale")) that is
    representative of this key signature and mode.

    Raises KeySignatureException if mode is not in [None, ‘major’, ‘minor’].

    ```python
    >>> ks = key.KeySignature(3)
    >>> ks
    <music21.key.KeySignature of 3 sharps>
    >>> ks.getScale('major')
    <music21.scale.MajorScale A major>
    >>> ks.getScale('minor')
    <music21.scale.MinorScale F# minor>
    ```

KeySignature.transpose(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [GenericInterval](moduleInterval.html#music21.interval.GenericInterval "music21.interval.GenericInterval")*, *\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/key.html#KeySignature.transpose)

KeySignature.transpose(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [GenericInterval](moduleInterval.html#music21.interval.GenericInterval "music21.interval.GenericInterval")*, *\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   Transpose the KeySignature by the user-provided value.
    If the value is an integer, the transposition is treated
    in half steps. If the value is a string, any Interval string
    specification can be provided. Alternatively, a
    [`music21.interval.Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object can be supplied.

    ```python
    >>> a = key.KeySignature(2)
    >>> a
    <music21.key.KeySignature of 2 sharps>
    >>> a.asKey('major')
    <music21.key.Key of D major>
    ```

    ```python
    >>> b = a.transpose('p5')
    >>> b
    <music21.key.KeySignature of 3 sharps>
    >>> b.asKey('major')
    <music21.key.Key of A major>
    >>> b.sharps
    3
    ```

    ```python
    >>> c = b.transpose('-m2')
    >>> c.asKey('major')
    <music21.key.Key of G# major>
    >>> c.sharps
    8
    ```

    ```python
    >>> d = c.transpose('-a3')
    >>> d.asKey('major')
    <music21.key.Key of E- major>
    >>> d.sharps
    -3
    ```

    Transposition by semitone (or other chromatic interval)

    ```python
    >>> c = key.KeySignature(0)
    >>> dFlat = c.transpose(1)
    >>> dFlat
    <music21.key.KeySignature of 5 flats>
    >>> d = dFlat.transpose(1)
    >>> d
    <music21.key.KeySignature of 2 sharps>
    >>> eFlat = d.transpose(1)
    >>> eFlat
    <music21.key.KeySignature of 3 flats>
    ```

KeySignature.transposePitchFromC(*p: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *\**, *inPlace=False*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/key.html#KeySignature.transposePitchFromC)
:   Takes a pitch in C major and transposes it so that it has
    the same step position in the current key signature.

    Example: B is the leading tone in C major, so given
    a key signature of 3 flats, get the leading tone in E-flat major:

    ```python
    >>> ks = key.KeySignature(-3)
    >>> p1 = pitch.Pitch('B')
    >>> p2 = ks.transposePitchFromC(p1)
    >>> p2.name
    'D'
    ```

    Original pitch is unchanged:

    ```python
    >>> p1.name
    'B'
    ```

    ```python
    >>> ks2 = key.KeySignature(2)
    >>> p2 = ks2.transposePitchFromC(p1)
    >>> p2.name
    'C#'
    ```

    For out of scale pitches the relationship still works; note also that
    original octave is preserved.

    ```python
    >>> p3 = pitch.Pitch('G-4')
    >>> p4 = ks.transposePitchFromC(p3)
    >>> p4.nameWithOctave
    'B--4'
    ```

    If inPlace is True then the original pitch is
    modified and nothing is returned.

    ```python
    >>> p5 = pitch.Pitch('C5')
    >>> ks.transposePitchFromC(p5, inPlace=True)
    >>> p5.nameWithOctave
    'E-5'
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Key

class music21.key.Key(*tonic: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") = 'C'*, *mode=None*, *\*\*keywords*)[[source]](../_modules/music21/key.html#Key)
:   Note that a key is a sort of hypothetical/conceptual object.
    It probably has a scale (or scales) associated with it and a [`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature"),
    but not necessarily.

    A Key object has all the attributes of a KeySignature and all the attributes of a
    [`DiatonicScale`](moduleScale.html#music21.scale.DiatonicScale "music21.scale.DiatonicScale").

    ```python
    >>> cm = key.Key('c')  # lowercase = c minor.
    >>> cm
    <music21.key.Key of c minor>
    >>> cm.mode
    'minor'
    >>> cm.tonic
    <music21.pitch.Pitch C>
    ```

    ```python
    >>> cm.sharps
    -3
    >>> cm.pitchFromDegree(3)
    <music21.pitch.Pitch E-4>
    >>> cm.pitchFromDegree(7)
    <music21.pitch.Pitch B-4>
    ```

    ```python
    >>> cSharpMaj = key.Key('C#')  # uppercase = C# major
    >>> cSharpMaj
    <music21.key.Key of C# major>
    >>> cSharpMaj.sharps
    7
    ```

    ```python
    >>> fFlatMaj = key.Key('F-')
    >>> fFlatMaj
    <music21.key.Key of F- major>
    >>> fFlatMaj.sharps
    -8
    >>> fFlatMaj.accidentalByStep('B')
    <music21.pitch.Accidental double-flat>
    ```

    ```python
    >>> eDor = key.Key('E', 'dorian')
    >>> eDor
    <music21.key.Key of E dorian>
    >>> eDor.sharps
    2
    >>> eDor.pitches
    [<music21.pitch.Pitch E4>,
     <music21.pitch.Pitch F#4>,
     <music21.pitch.Pitch G4>,
     <music21.pitch.Pitch A4>,
     <music21.pitch.Pitch B4>,
     <music21.pitch.Pitch C#5>,
     <music21.pitch.Pitch D5>,
     <music21.pitch.Pitch E5>]
    ```

    If you prefer not to use uppercase and lowercase to distinguish major and minor,
    the shorthand of CM or Cm can also be used:

    ```python
    >>> key.Key('EM')
    <music21.key.Key of E major>
    >>> key.Key('F#m')
    <music21.key.Key of f# minor>
    ```

    **Equality**

    Two Keys are equal if their tonics’ names are equal, their sharps are equal,
    and their modes are equal (and they pass all superclass tests)

    ```python
    >>> k = key.Key(pitch.Pitch('C4'))
    >>> k2 = key.Key(pitch.Pitch('C5'))
    >>> k == k2
    True
    >>> k.mode = 'minor'
    >>> k == k2
    False
    ```

    * Changed in v8: keys now compare equal regardless of the octave of their tonics.

[`Key`](#music21.key.Key "music21.key.Key") bases

* [`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature")
* [`DiatonicScale`](moduleScale.html#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](moduleScale.html#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Key`](#music21.key.Key "music21.key.Key") read-only properties

Key.parallel
:   if the Key is major or minor, return the parallel minor or major.

    Otherwise, just returns self – this is the best way to not have random crashes
    in the middle of large datasets.

    ```python
    >>> k = key.Key('D')
    >>> k
    <music21.key.Key of D major>
    >>> k.parallel
    <music21.key.Key of d minor>
    >>> k.parallel.parallel
    <music21.key.Key of D major>
    ```

    ```python
    >>> key.Key('D', 'dorian').parallel
    <music21.key.Key of D dorian>
    ```

Key.relative
:   if the Key is major or minor, return the relative minor or major.

    Otherwise, just returns self – this is the best way to not have random crashes
    in the middle of large datasets.

    Note that this uses .sharps as a speedup, so if that has been changed, there
    will be a problem:

    ```python
    >>> k = key.Key('E-')
    >>> k
    <music21.key.Key of E- major>
    >>> k.relative
    <music21.key.Key of c minor>
    >>> k.relative.relative
    <music21.key.Key of E- major>
    ```

    ```python
    >>> key.Key('D', 'dorian').relative
    <music21.key.Key of D dorian>
    ```

Key.tonicPitchNameWithCase
:   Return the pitch name as a string with the proper case (upper = major; lower = minor)

    Useful, but simple:

    ```python
    >>> k = key.Key('c#')
    >>> k.tonicPitchNameWithCase
    'c#'
    >>> k = key.Key('B')
    >>> k.tonicPitchNameWithCase
    'B'
    >>> k.mode = 'minor'
    >>> k.tonicPitchNameWithCase
    'b'
    ```

    Anything else will return the default (capital)

    ```python
    >>> k.mode = 'dorian'
    >>> k.tonicPitchNameWithCase
    'B'
    ```

Read-only properties inherited from [`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature"):

|  |  |  |
| --- | --- | --- |
| * [`isNonTraditional`](#music21.key.KeySignature.isNonTraditional "music21.key.KeySignature.isNonTraditional") |  |  |

Read-only properties inherited from [`ConcreteScale`](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](moduleScale.html#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](moduleScale.html#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](moduleScale.html#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](moduleScale.html#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Key`](#music21.key.Key "music21.key.Key") read/write properties

Read/write properties inherited from [`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature"):

|  |  |  |
| --- | --- | --- |
| * [`alteredPitches`](#music21.key.KeySignature.alteredPitches "music21.key.KeySignature.alteredPitches") | * [`sharps`](#music21.key.KeySignature.sharps "music21.key.KeySignature.sharps") |  |

Read/write properties inherited from [`ConcreteScale`](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](moduleScale.html#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Key`](#music21.key.Key "music21.key.Key") methods

Key.\_\_eq\_\_(*other*)[[source]](../_modules/music21/key.html#Key.__eq__)
:   Define equality for Music21Objects. See main class docs.

Key.deriveByDegree(*degree*, *pitchRef*)[[source]](../_modules/music21/key.html#Key.deriveByDegree)
:   Given a degree and pitchReference derive a new
    Key object that has the same mode but a different tonic

    Example: What minor key has scale degree 3 as B-flat?

    ```python
    >>> minorKey = key.Key(mode='minor')
    >>> newMinor = minorKey.deriveByDegree(3, 'B-')
    >>> newMinor
    <music21.key.Key of g minor>
    ```

    Note that in minor, the natural form is used:

    ```python
    >>> minorKey.deriveByDegree(7, 'E')
    <music21.key.Key of f# minor>
    >>> minorKey.deriveByDegree(6, 'G')
    <music21.key.Key of b minor>
    ```

    To use the harmonic form, change .abstract on the key to
    another abstract scale:

    ```python
    >>> minorKey.abstract = scale.AbstractHarmonicMinorScale()
    >>> minorKey.deriveByDegree(7, 'E')
    <music21.key.Key of f minor>
    >>> minorKey.deriveByDegree(6, 'G')
    <music21.key.Key of b minor>
    ```

    Currently because of a limitation in bidirectional scale
    searching, melodic minor scales cannot be used as abstracts
    for deriving by degree.

    * New in v6: preserve mode in key.Key.deriveByDegree

Key.tonalCertainty(*method='correlationCoefficient'*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/key.html#Key.tonalCertainty)
:   Provide a measure of tonal ambiguity for Key
    determined with one of many methods.

    The correlationCoefficient assumes that the
    alternateInterpretations list has
    been filled from the use of a KeyWeightKeyAnalysis subclass.

    ```python
    >>> littlePiece = converter.parse("tinyNotation: 4/4 c4 d e f g a b c' e' g' e' c'")
    >>> k = littlePiece.analyze('key')
    >>> k
    <music21.key.Key of C major>
    >>> k.tonalCertainty()
    1.1648...
    ```

    Three most likely alternateInterpretations:

    ```python
    >>> k.alternateInterpretations[0:3]
    [<music21.key.Key of a minor>, <music21.key.Key of F major>, <music21.key.Key of d minor>]
    >>> k.correlationCoefficient
    0.9068...
    >>> k.alternateInterpretations[0].correlationCoefficient
    0.7778...
    ```

    least likely interpretation:

    ```python
    >>> k.alternateInterpretations[-1]
    <music21.key.Key of F# major>
    ```

    Note that this method only exists if the key has come from an analysis method. Otherwise
    it raises a KeySignatureException

    ```python
    >>> k2 = key.Key('b-')
    >>> k2.tonalCertainty()
    Traceback (most recent call last):
    music21.key.KeySignatureException: cannot process ambiguity without a
        list of .alternateInterpretations
    ```

    ```python
    >>> k2.alternateInterpretations
    []
    ```

Key.transpose(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [GenericInterval](moduleInterval.html#music21.interval.GenericInterval "music21.interval.GenericInterval")*, *\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/key.html#Key.transpose)

Key.transpose(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [GenericInterval](moduleInterval.html#music21.interval.GenericInterval "music21.interval.GenericInterval")*, *\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   Transpose the Key by the user-provided value.
    If the value is an integer, the transposition is treated
    in half steps. If the value is a string, any Interval string
    specification can be provided. Alternatively, a
    [`music21.interval.Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object can be supplied.

    ```python
    >>> dMajor = key.Key('D')
    >>> dMajor
    <music21.key.Key of D major>
    ```

    ```python
    >>> aMaj = dMajor.transpose('p5')
    >>> aMaj
    <music21.key.Key of A major>
    >>> aMaj.sharps
    3
    >>> aMaj.tonic
    <music21.pitch.Pitch A>
    >>> aMaj.mode
    'major'
    ```

    inPlace=True works here and returns None while changing the Key itself.

    ```python
    >>> changingKey = key.Key('g')
    >>> changingKey
    <music21.key.Key of g minor>
    >>> changingKey.sharps
    -2
    >>> changingKey.transpose('m-3', inPlace=True)
    >>> changingKey
    <music21.key.Key of e minor>
    >>> changingKey.sharps
    1
    ```

    ```python
    >>> changingKey.transpose(1, inPlace=True)
    >>> changingKey
    <music21.key.Key of f minor>
    >>> changingKey.sharps
    -4
    >>> changingKey.transpose(1, inPlace=True)
    >>> changingKey
    <music21.key.Key of f# minor>
    >>> changingKey.transpose(1, inPlace=True)
    >>> changingKey
    <music21.key.Key of g minor>
    >>> changingKey.transpose(1, inPlace=True)
    >>> changingKey
    <music21.key.Key of g# minor>
    ```

Methods inherited from [`KeySignature`](#music21.key.KeySignature "music21.key.KeySignature"):

|  |  |  |
| --- | --- | --- |
| * [`accidentalByStep()`](#music21.key.KeySignature.accidentalByStep "music21.key.KeySignature.accidentalByStep") * [`asKey()`](#music21.key.KeySignature.asKey "music21.key.KeySignature.asKey") | * [`getScale()`](#music21.key.KeySignature.getScale "music21.key.KeySignature.getScale") | * [`transposePitchFromC()`](#music21.key.KeySignature.transposePitchFromC "music21.key.KeySignature.transposePitchFromC") |

Methods inherited from [`DiatonicScale`](moduleScale.html#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](moduleScale.html#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](moduleScale.html#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](moduleScale.html#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](moduleScale.html#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](moduleScale.html#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](moduleScale.html#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](moduleScale.html#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`derive()`](moduleScale.html#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](moduleScale.html#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveRanked()`](moduleScale.html#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](moduleScale.html#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](moduleScale.html#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](moduleScale.html#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](moduleScale.html#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](moduleScale.html#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](moduleScale.html#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](moduleScale.html#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](moduleScale.html#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](moduleScale.html#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](moduleScale.html#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](moduleScale.html#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](moduleScale.html#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](moduleScale.html#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](moduleScale.html#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](moduleScale.html#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](moduleScale.html#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`tune()`](moduleScale.html#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](moduleScale.html#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](moduleScale.html#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](moduleScale.html#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Key`](#music21.key.Key "music21.key.Key") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.key.convertKeyStringToMusic21KeyString(*textString*)[[source]](../_modules/music21/key.html#convertKeyStringToMusic21KeyString)
:   Utility function to change strings in the form of “Eb” to
    “E-” (for E-flat major) and leaves alone proper music21 strings
    (like “E-” or “f#”). A little bit complex because of parsing
    bb as B-flat minor and Bb as B-flat major.

    ```python
    >>> key.convertKeyStringToMusic21KeyString('Eb')
    'E-'
    >>> key.convertKeyStringToMusic21KeyString('f#')
    'f#'
    >>> key.convertKeyStringToMusic21KeyString('bb')
    'b-'
    >>> key.convertKeyStringToMusic21KeyString('Bb')
    'B-'
    >>> key.convertKeyStringToMusic21KeyString('b#')
    'b#'
    >>> key.convertKeyStringToMusic21KeyString('c')
    'c'
    >>> key.convertKeyStringToMusic21KeyString('Bbb')
    'B--'
    >>> key.convertKeyStringToMusic21KeyString('bbb')
    'b--'
    >>> key.convertKeyStringToMusic21KeyString('Ebb')
    'E--'
    ```

music21.key.pitchToSharps(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *mode: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/key.html#pitchToSharps)
:   Given a pitch string or [`music21.pitch.Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") or
    [`music21.note.Note`](moduleNote.html#music21.note.Note "music21.note.Note") object,
    return the number of sharps found in that mode.

    The mode parameter can be ‘major’, ‘minor’, or most
    of the common church/jazz modes (‘dorian’, ‘mixolydian’, etc.)
    including Locrian.

    If mode is omitted or not found, the default mode is major.

    (extra points to anyone who can find the earliest reference to
    the Locrian mode in print. David Cohen and I (MSAC) have been
    looking for this for years).

    ```python
    >>> key.pitchToSharps('c')
    0
    >>> key.pitchToSharps('c', 'minor')
    -3
    >>> key.pitchToSharps('a', 'minor')
    0
    >>> key.pitchToSharps('d')
    2
    >>> key.pitchToSharps('e-')
    -3
    >>> key.pitchToSharps('a')
    3
    >>> key.pitchToSharps('e', 'minor')
    1
    >>> key.pitchToSharps('f#', 'major')
    6
    >>> key.pitchToSharps('g-', 'major')
    -6
    >>> key.pitchToSharps('c#')
    7
    >>> key.pitchToSharps('g#')
    8
    >>> key.pitchToSharps('e', 'dorian')
    2
    >>> key.pitchToSharps('d', 'dorian')
    0
    >>> key.pitchToSharps('g', 'mixolydian')
    0
    >>> key.pitchToSharps('e-', 'lydian')
    -2
    >>> key.pitchToSharps('e-', 'lydian')
    -2
    >>> key.pitchToSharps('a', 'phrygian')
    -1
    >>> key.pitchToSharps('e', 'phrygian')
    0
    >>> key.pitchToSharps('f#')
    6
    >>> key.pitchToSharps(note.Note('f-'))
    -8
    >>> key.pitchToSharps(pitch.Pitch('f--'))
    -15
    >>> key.pitchToSharps('f--', 'locrian')
    -20
    >>> key.pitchToSharps('a', 'ionian')
    3
    >>> key.pitchToSharps('a', 'aeolian')
    0
    ```

    But quarter tones don’t work:

    ```python
    >>> key.pitchToSharps('C~')
    Traceback (most recent call last):
    music21.key.KeyException: Cannot determine sharps for quarter-tone keys! silly!
    ```

music21.key.sharpsToPitch(*sharpCount*)[[source]](../_modules/music21/key.html#sharpsToPitch)
:   Given a positive/negative number of sharps, return a Pitch
    object set to the appropriate major key value.

    ```python
    >>> key.sharpsToPitch(1)
    <music21.pitch.Pitch G>
    >>> key.sharpsToPitch(2)
    <music21.pitch.Pitch D>
    >>> key.sharpsToPitch(-2)
    <music21.pitch.Pitch B->
    >>> key.sharpsToPitch(-6)
    <music21.pitch.Pitch G->
    ```

    Note that these are [`music21.pitch.Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects not just names:

    ```python
    >>> k1 = key.sharpsToPitch(6)
    >>> k1
    <music21.pitch.Pitch F#>
    >>> k1.step
    'F'
    >>> k1.accidental
    <music21.pitch.Accidental sharp>
    ```
