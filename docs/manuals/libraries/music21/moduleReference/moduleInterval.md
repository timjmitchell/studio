Source: https://music21.org/music21docs/moduleReference/moduleInterval.html

# music21.interval

This module defines various types of interval objects.
Fundamental classes are [`Interval`](#music21.interval.Interval "music21.interval.Interval"),
[`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval"),
and [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval").

## Interval

class music21.interval.Interval(*arg0: t.Union[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), [note.Note](moduleNote.html#music21.note.Note "music21.note.Note"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] = None*, *arg1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, */*, *\**, *diatonic: [DiatonicInterval](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *chromatic: [ChromaticInterval](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchStart: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchEnd: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *noteStart: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *noteEnd: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/interval.html#Interval)
:   An Interval class that encapsulates both
    [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") and
    [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") objects all in one model.

    The interval is specified either as named arguments, a
    [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") and
    a [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval"),
    or two [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects
    (or `Pitch` objects),
    from which both a ChromaticInterval and DiatonicInterval are derived.

    ```python
    >>> p1 = pitch.Pitch('c3')
    >>> p2 = pitch.Pitch('c5')
    >>> aInterval = interval.Interval(pitchStart=p1, pitchEnd=p2)
    >>> aInterval
    <music21.interval.Interval P15>
    >>> aInterval.name
    'P15'
    >>> aInterval.pitchStart is p1
    True
    >>> aInterval.pitchEnd is p2
    True
    ```

    Reduce to less than an octave:

    ```python
    >>> aInterval.simpleName
    'P1'
    ```

    Reduce to no more than an octave:

    ```python
    >>> aInterval.semiSimpleName
    'P8'
    ```

    An interval can also be specified directly:

    ```python
    >>> aInterval = interval.Interval('m3')
    >>> aInterval
    <music21.interval.Interval m3>
    >>> aInterval = interval.Interval('M3')
    >>> aInterval
    <music21.interval.Interval M3>
    ```

    ```python
    >>> aInterval = interval.Interval('p5')
    >>> aInterval
    <music21.interval.Interval P5>
    >>> aInterval.isChromaticStep
    False
    >>> aInterval.isDiatonicStep
    False
    >>> aInterval.isStep
    False
    ```

    Some ways of creating half-steps.

    ```python
    >>> aInterval = interval.Interval('half')
    >>> aInterval
    <music21.interval.Interval m2>
    >>> aInterval.isChromaticStep
    True
    >>> aInterval.isDiatonicStep
    True
    >>> aInterval.isStep
    True
    ```

    ```python
    >>> aInterval = interval.Interval('-h')
    >>> aInterval
    <music21.interval.Interval m-2>
    >>> aInterval.directedName
    'm-2'
    >>> aInterval.name
    'm2'
    ```

    A single int is treated as a number of half-steps:

    ```python
    >>> aInterval = interval.Interval(4)
    >>> aInterval
    <music21.interval.Interval M3>
    ```

    ```python
    >>> aInterval = interval.Interval(7)
    >>> aInterval
    <music21.interval.Interval P5>
    ```

    If giving a starting pitch, an ending pitch has to be specified.

    ```python
    >>> aInterval = interval.Interval(pitchStart=p1)
    Traceback (most recent call last):
    ValueError: either both the starting and the ending pitch (or note) must be given
        or neither can be given. You cannot have one without the other.
    ```

    An Interval can be constructed from a DiatonicInterval and ChromaticInterval
    object (or just one):

    ```python
    >>> diaInterval = interval.DiatonicInterval('major', 'third')
    >>> chrInterval = interval.ChromaticInterval(4)
    >>> fullInterval = interval.Interval(diatonic=diaInterval, chromatic=chrInterval)
    >>> fullInterval
    <music21.interval.Interval M3>
    ```

    ```python
    >>> fullInterval = interval.Interval(diatonic=diaInterval)
    >>> fullInterval.semitones
    4
    >>> fullInterval = interval.Interval(chromatic=chrInterval)
    >>> fullInterval.diatonic.name
    'M3'
    >>> fullInterval.implicitDiatonic
    True
    ```

    Two Intervals are the same if their Chromatic and Diatonic intervals
    are the same.

    ```python
    >>> aInt = interval.Interval('P4')
    >>> bInt = interval.Interval(
    ...        diatonic=interval.DiatonicInterval('P', 4),
    ...        chromatic=interval.ChromaticInterval(5),
    ...        )
    >>> aInt == bInt
    True
    ```

    N.B. that interval.Interval(‘A4’) != ‘A4’

    ```python
    >>> interval.Interval('A4') == 'A4'
    False
    ```

    More demonstrations using pitches:

    ```python
    >>> aPitch = pitch.Pitch('c4')
    >>> bPitch = pitch.Pitch('g5')
    >>> aInterval = interval.Interval(aPitch, bPitch)
    >>> aInterval
    <music21.interval.Interval P12>
    >>> bInterval = interval.Interval(pitchStart=aPitch, pitchEnd=bPitch)
    >>> aInterval.niceName == bInterval.niceName
    True
    ```

    ```python
    >>> aPitch = pitch.Pitch('c#4')
    >>> bPitch = pitch.Pitch('f-5')
    >>> cInterval = interval.Interval(aPitch, bPitch)
    >>> cInterval
    <music21.interval.Interval dd11>
    ```

    ```python
    >>> cPitch = pitch.Pitch('e#4')
    >>> dPitch = pitch.Pitch('f-4')
    >>> dInterval = interval.Interval(cPitch, dPitch)
    >>> dInterval
    <music21.interval.Interval dd2>
    ```

    ```python
    >>> ePitch = pitch.Pitch('e##4')
    >>> fPitch = pitch.Pitch('f--4')
    >>> dInterval = interval.Interval(ePitch, fPitch)
    >>> dInterval
    <music21.interval.Interval dddd2>
    ```

    ```python
    >>> gPitch = pitch.Pitch('c--4')
    >>> hPitch = pitch.Pitch('c##4')
    >>> iInterval = interval.Interval(gPitch, hPitch)
    >>> iInterval
    <music21.interval.Interval AAAA1>
    ```

    ```python
    >>> interval.Interval(pitch.Pitch('e##4'), pitch.Pitch('f--5'))
    <music21.interval.Interval dddd9>
    ```

    * Changed in v8:
      - Pitches are emphasized over notes.
      - It is not possible to create an interval with a name and a pitchStart/noteStart
      and automatically get a pitchEnd/noteEnd in the process. Set them later.
      - Incompatible keywords raise ValueError not IntervalException.
      - An empty instantiation gives a P1 interval.

[`Interval`](#music21.interval.Interval "music21.interval.Interval") bases

* [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Interval`](#music21.interval.Interval "music21.interval.Interval") read-only properties

Interval.cents
:   Return the cents from the chromatic interval, where 100 cents = a half-step

    ```python
    >>> aInterval = interval.Interval('M3')
    >>> aInterval.cents
    400.0
    ```

    ```python
    >>> p1 = pitch.Pitch('C4')
    >>> p2 = pitch.Pitch('D4')
    >>> p2.microtone = 30
    >>> microtoneInterval = interval.Interval(pitchStart=p1, pitchEnd=p2)
    >>> microtoneInterval.cents
    230.0
    ```

Interval.complement
:   Return a new [`Interval`](#music21.interval.Interval "music21.interval.Interval") object that is the
    complement of this Interval.

    ```python
    >>> aInterval = interval.Interval('M3')
    >>> bInterval = aInterval.complement
    >>> bInterval
    <music21.interval.Interval m6>
    ```

    ```python
    >>> cInterval = interval.Interval('A2')
    >>> dInterval = cInterval.complement
    >>> dInterval
    <music21.interval.Interval d7>
    ```

Interval.directedName

Interval.directedNiceName

Interval.directedSimpleName

Interval.directedSimpleNiceName

Interval.direction

Interval.generic
:   Returns the [`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") object
    associated with this Interval

    ```python
    >>> interval.Interval('P5').generic
    <music21.interval.GenericInterval 5>
    ```

Interval.intervalClass
:   Return the interval class from the chromatic interval,
    that is, the lesser of the number of half-steps in the
    simpleInterval or its complement.

    ```python
    >>> aInterval = interval.Interval('M3')
    >>> aInterval.intervalClass
    4
    ```

    ```python
    >>> bInterval = interval.Interval('m6')
    >>> bInterval.intervalClass
    4
    ```

    Empty intervals return 0:

    ```python
    >>> interval.Interval().intervalClass
    0
    ```

    * Changed in v6.5: empty intervals return 0

Interval.isChromaticStep

Interval.isDiatonicStep

Interval.isSkip

Interval.isStep

Interval.name
:   Return the simple name of the interval, ignoring direction:

    ```python
    >>> interval.Interval('Descending Perfect Fourth').name
    'P4'
    ```

Interval.niceName
:   ```python
    >>> interval.Interval('m3').niceName
    'Minor Third'
    ```

Interval.semiSimpleName

Interval.semiSimpleNiceName

Interval.semitones

Interval.simpleName

Interval.simpleNiceName

Interval.specificName

Interval.specifier

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Interval`](#music21.interval.Interval "music21.interval.Interval") read/write properties

Interval.noteEnd
:   Return or set the Note that pitchEnd is attached to. For
    backwards compatibility

Interval.noteStart
:   Return or set the Note that pitchStart is attached to. For
    backwards compatibility

Interval.pitchEnd
:   Set the
    end pitch to a new value; this will adjust
    the value of the start pitch (pitchStart).

    ```python
    >>> aInterval = interval.Interval('M3')
    >>> aInterval.pitchEnd = pitch.Pitch('E4')
    >>> aInterval.pitchStart.nameWithOctave
    'C4'
    ```

    ```python
    >>> aInterval = interval.Interval('m2')
    >>> aInterval.pitchEnd = pitch.Pitch('A#3')
    >>> aInterval.pitchStart.nameWithOctave
    'G##3'
    ```

    ```python
    >>> p1 = pitch.Pitch('G#3')
    >>> p2 = pitch.Pitch('C3')
    >>> aInterval = interval.Interval(p1, p2)
    >>> aInterval.directedName  # downward augmented fifth
    'A-5'
    >>> aInterval.pitchEnd = pitch.Pitch('C4')
    >>> aInterval.pitchStart.nameWithOctave
    'G#4'
    ```

    ```python
    >>> aInterval = interval.Interval('M3')
    >>> aInterval.pitchEnd = pitch.Pitch('A-3')
    >>> aInterval.pitchStart.nameWithOctave
    'F-3'
    ```

Interval.pitchStart
:   Get the start pitch or set it a new value.
    Setting this will adjust the value of the end pitch (pitchEnd).

    ```python
    >>> maj3 = interval.Interval('M3')
    >>> maj3.pitchStart = pitch.Pitch('c4')
    >>> maj3.pitchEnd.nameWithOctave
    'E4'
    ```

    ```python
    >>> p1 = pitch.Pitch('c3')
    >>> p2 = pitch.Pitch('g#3')
    >>> a5 = interval.Interval(p1, p2)
    >>> a5.name
    'A5'
    ```

    ```python
    >>> a5.pitchStart = pitch.Pitch('g4')
    >>> a5.pitchEnd.nameWithOctave
    'D#5'
    ```

    ```python
    >>> descM3 = interval.Interval('-M3')
    >>> descM3.pitchStart = pitch.Pitch('c4')
    >>> descM3.pitchEnd.nameWithOctave
    'A-3'
    ```

    ```python
    >>> descM2 = interval.Interval('M-2')
    >>> descM2.pitchStart = pitch.Pitch('A#3')
    >>> descM2.pitchEnd.nameWithOctave
    'G#3'
    ```

    Implicit diatonic intervals do not need to
    follow the diatonic directed name:

    ```python
    >>> halfStep = interval.Interval('h')
    >>> halfStep.directedName
    'm2'
    >>> halfStep.implicitDiatonic
    True
    >>> halfStep.pitchStart = pitch.Pitch('F-3')
    >>> halfStep.pitchEnd.nameWithOctave
    'F3'
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Interval`](#music21.interval.Interval "music21.interval.Interval") methods

Interval.\_\_eq\_\_(*other*)[[source]](../_modules/music21/interval.html#Interval.__eq__)
:   True if .diatonic and .chromatic are equal.

    ```python
    >>> a = interval.Interval('a4')
    >>> b = interval.Interval('d5')
    >>> c = interval.Interval('m3')
    >>> d = interval.Interval('d5')
    >>> a == b
    False
    >>> b == d
    True
    >>> a == c
    False
    >>> b in [a, c, d]
    True
    ```

    Now, of course, this makes sense:

    ```python
    >>> a == 'hello'
    False
    ```

    But note well that this is also a False expression:

    ```python
    >>> a == 'a4'
    False
    ```

Interval.isConsonant() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/interval.html#Interval.isConsonant)
:   returns True if the pitches are a major or
    minor third or sixth or perfect fifth or unison.

    These rules define all common-practice consonances
    (and earlier back to about 1300 all imperfect consonances)

    ```python
    >>> i1 = interval.Interval(note.Note('C'), note.Note('E'))
    >>> i1.isConsonant()
    True
    >>> i1 = interval.Interval(note.Note('B-'), note.Note('C'))
    >>> i1.isConsonant()
    False
    ```

Interval.reverse()[[source]](../_modules/music21/interval.html#Interval.reverse)
:   Return a reversed version of this interval.
    If [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects are stored as
    pitchStart and pitchEnd, these pitches are reversed.

    ```python
    >>> p1 = pitch.Pitch('c3')
    >>> p2 = pitch.Pitch('g3')
    >>> intvP5 = interval.Interval(pitchStart=p1, pitchEnd=p2)
    >>> intvP5
    <music21.interval.Interval P5>
    >>> revInterval = intvP5.reverse()
    >>> revInterval
    <music21.interval.Interval P-5>
    >>> revInterval.pitchStart is intvP5.pitchEnd
    True
    ```

    ```python
    >>> m3 = interval.Interval('m3')
    >>> m3.reverse()
    <music21.interval.Interval m-3>
    ```

Interval.transposePitch(*p: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *\**, *reverse=False*, *maxAccidental: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 4*, *inPlace=False*)[[source]](../_modules/music21/interval.html#Interval.transposePitch)
:   Given a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object, return a new,
    transposed Pitch, that is transformed
    according to this Interval. This is the main public interface to all
    transposition routines found on higher-level objects.

    The maxAccidental parameter sets an integer number of half step
    alterations that will be accepted in the transposed pitch before it
    is simplified. For example,
    a value of 2 will permit double sharps but not triple sharps. The
    maxAccidental default is 4, because music21 does not support quintuple
    sharps/flats. Set to None to try anyhow.

    ```python
    >>> p1 = pitch.Pitch('A#4')
    >>> i = interval.Interval('m3')
    >>> p2 = i.transposePitch(p1)
    >>> p2
    <music21.pitch.Pitch C#5>
    >>> p2 = i.transposePitch(p1, reverse=True)
    >>> p2
    <music21.pitch.Pitch F##4>
    >>> i.transposePitch(p1, reverse=True, maxAccidental=1)
    <music21.pitch.Pitch G4>
    ```

    Pitch objects without octaves are transposed also into
    objects without octaves. This might make them appear to be
    lower than the original even if transposed up:

    ```python
    >>> anyA = pitch.Pitch('A')
    >>> anyC = i.transposePitch(anyA)
    >>> anyC
    <music21.pitch.Pitch C>
    >>> anyC.ps < anyA.ps  # !!
    True
    ```

    If inPlace is True then function is done in place and no pitch is returned.

    ```python
    >>> p1 = pitch.Pitch('A4')
    >>> i = interval.Interval('m3')
    >>> i.transposePitch(p1, inPlace=True)
    >>> p1
    <music21.pitch.Pitch C5>
    ```

    Note that reverse=True is only there for historical reasons;
    it is the same as i.reverse().transposePitch(x) and that format
    will be much faster when calling many times.

    * Changed in v6: inPlace parameter added. Reverse and maxAccidental
      changed to keyword only.

Methods inherited from [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase"):

|  |  |  |
| --- | --- | --- |
| * [`transposeNote()`](#music21.interval.IntervalBase.transposeNote "music21.interval.IntervalBase.transposeNote") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Interval`](#music21.interval.Interval "music21.interval.Interval") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ChromaticInterval

class music21.interval.ChromaticInterval(*semitones: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0*, *\*\*keywords*)[[source]](../_modules/music21/interval.html#ChromaticInterval)
:   Chromatic interval class. Unlike a [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval"),
    this IntervalBase subclass treats interval spaces in half-steps.
    So Major 3rd and Diminished 4th are the same.

    Two ChromaticIntervals are equal if their size and direction are equal.

    ```python
    >>> aInterval = interval.ChromaticInterval(-14)
    >>> aInterval.semitones
    -14
    >>> aInterval.undirected
    14
    >>> aInterval.mod12
    10
    >>> aInterval.intervalClass
    2
    >>> aInterval.isChromaticStep
    False
    >>> aInterval.isStep
    False
    ```

    ```python
    >>> aInterval = interval.ChromaticInterval(1)
    >>> aInterval.isChromaticStep
    True
    >>> aInterval.isStep
    True
    ```

[`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") bases

* [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") read-only properties

ChromaticInterval.cents
:   Return the number of cents in a ChromaticInterval:

    ```python
    >>> dime = interval.ChromaticInterval(0.1)
    >>> dime.cents
    10.0
    ```

ChromaticInterval.directed
:   A synonym for .semitones

    ```python
    >>> tritoneDown = interval.ChromaticInterval(-6)
    >>> tritoneDown.directed
    -6
    ```

ChromaticInterval.direction
:   Returns an enum of the direction:

    ```python
    >>> interval.ChromaticInterval(-3).direction
    <Direction.DESCENDING: -1>
    ```

    note that the number can be helpful for multiplication:

    ```python
    >>> interval.ChromaticInterval(-3).direction * 9
    -9
    ```

ChromaticInterval.intervalClass

ChromaticInterval.isChromaticStep

ChromaticInterval.isStep

ChromaticInterval.mod12
:   The number of semitones within an octave using modulo arithmatic.

    (see [`simpleUndirected()`](#music21.interval.ChromaticInterval.simpleUndirected "music21.interval.ChromaticInterval.simpleUndirected")
    for a similar method that puts musical
    intuition above mathematical intuition)

    ```python
    >>> interval.ChromaticInterval(15).mod12
    3
    >>> interval.ChromaticInterval(-4).mod12
    8
    >>> interval.ChromaticInterval(-16).mod12
    8
    ```

ChromaticInterval.simpleDirected
:   The number of semitones within an octave while preserving direction.

    ```python
    >>> interval.ChromaticInterval(15).simpleDirected
    3
    >>> interval.ChromaticInterval(-4).simpleDirected
    -4
    >>> interval.ChromaticInterval(-16).simpleDirected
    -4
    ```

ChromaticInterval.simpleUndirected
:   The number of semitones within an octave while ignoring direction.

    (see [`mod12()`](#music21.interval.ChromaticInterval.mod12 "music21.interval.ChromaticInterval.mod12")
    for a similar method that puts mathematical
    intuition above musical intuition)

    ```python
    >>> interval.ChromaticInterval(15).simpleUndirected
    3
    >>> interval.ChromaticInterval(-4).simpleUndirected
    4
    >>> interval.ChromaticInterval(-16).simpleUndirected
    4
    ```

ChromaticInterval.undirected
:   The absolute value of the number of semitones:

    ```python
    >>> tritoneDown = interval.ChromaticInterval(-6)
    >>> tritoneDown.undirected
    6
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") methods

ChromaticInterval.\_\_eq\_\_(*other*)[[source]](../_modules/music21/interval.html#ChromaticInterval.__eq__)
:   True if number of semitones is the same.

    ```python
    >>> a = interval.ChromaticInterval(-14)
    >>> b = interval.ChromaticInterval(14)
    >>> c = interval.ChromaticInterval(-14)
    >>> d = interval.ChromaticInterval(7)
    >>> e = interval.ChromaticInterval(2)
    ```

    ```python
    >>> a == b
    False
    >>> a == c
    True
    >>> a == d
    False
    >>> b == e
    False
    ```

    Intervals do not equal numbers:

    ```python
    >>> interval.ChromaticInterval(7) == 7
    False
    ```

ChromaticInterval.getDiatonic() → [DiatonicInterval](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval")[[source]](../_modules/music21/interval.html#ChromaticInterval.getDiatonic)
:   Given a ChromaticInterval, return a [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval")
    object of the same size.

    While there is more than one Generic Interval for any given chromatic
    interval, this is needed to permit easy chromatic specification of
    Interval objects. Augmented or diminished intervals are never returned
    except for the interval of 6 which returns a diminished fifth, not
    augmented fourth.

    ```python
    >>> aInterval = interval.ChromaticInterval(5)
    >>> aInterval.getDiatonic()
    <music21.interval.DiatonicInterval P4>
    ```

    ```python
    >>> aInterval = interval.ChromaticInterval(6)
    >>> aInterval.getDiatonic()
    <music21.interval.DiatonicInterval d5>
    ```

    ```python
    >>> aInterval = interval.ChromaticInterval(7)
    >>> aInterval.getDiatonic()
    <music21.interval.DiatonicInterval P5>
    ```

    ```python
    >>> aInterval = interval.ChromaticInterval(11)
    >>> aInterval.getDiatonic()
    <music21.interval.DiatonicInterval M7>
    ```

ChromaticInterval.reverse() → [ChromaticInterval](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval")[[source]](../_modules/music21/interval.html#ChromaticInterval.reverse)
:   Return an inverted [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval"),
    that is, reversing the direction.

    ```python
    >>> aInterval = interval.ChromaticInterval(-14)
    >>> aInterval.reverse()
    <music21.interval.ChromaticInterval 14>
    ```

    ```python
    >>> aInterval = interval.ChromaticInterval(3)
    >>> aInterval.reverse()
    <music21.interval.ChromaticInterval -3>
    ```

ChromaticInterval.transposePitch(*p: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *\**, *inPlace=False*)[[source]](../_modules/music21/interval.html#ChromaticInterval.transposePitch)
:   Given a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object, return a new,
    transposed Pitch, that is transformed
    according to this ChromaticInterval.

    Because [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") object
    do not take into account diatonic spelling,
    the new Pitch is simplified to the most common intervals. See
    [`simplifyEnharmonic()`](modulePitch.html#music21.pitch.Pitch.simplifyEnharmonic "music21.pitch.Pitch.simplifyEnharmonic") with `mostCommon = True`
    to see the results.

    ```python
    >>> tritone = interval.ChromaticInterval(6)
    >>> p = pitch.Pitch('E#4')
    >>> p2 = tritone.transposePitch(p)
    >>> p2
    <music21.pitch.Pitch B4>
    >>> p3 = tritone.transposePitch(p2)
    >>> p3
    <music21.pitch.Pitch F5>
    ```

    If no octave number is given then octaves “wrap around” and thus even
    after transposing upward, you could end up with a pitch that is
    displayed as lower than the original:

    ```python
    >>> p4 = pitch.Pitch('B')
    >>> p4.ps
    71.0
    >>> p5 = tritone.transposePitch(p4)
    ```

    Since the octave on p4 was implicit, the ps here wraps around

    ```python
    >>> p5.ps
    65.0
    ```

    Afterward, the spelling of the new pitch will always be inferred.

    ```python
    >>> p4.spellingIsInferred
    False
    >>> p5.spellingIsInferred
    True
    ```

    Can be done inPlace as well:

    ```python
    >>> p = pitch.Pitch('E#4')
    >>> tritone.transposePitch(p, inPlace=True)
    >>> p
    <music21.pitch.Pitch B4>
    >>> p.spellingIsInferred
    True
    ```

    * Changed in v6: added inPlace

Methods inherited from [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase"):

|  |  |  |
| --- | --- | --- |
| * [`transposeNote()`](#music21.interval.IntervalBase.transposeNote "music21.interval.IntervalBase.transposeNote") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DiatonicInterval

class music21.interval.DiatonicInterval(*specifier: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 'P'*, *generic: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [GenericInterval](#music21.interval.GenericInterval "music21.interval.GenericInterval") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 1*, *\*\*keywords*)[[source]](../_modules/music21/interval.html#DiatonicInterval)
:   A class representing a diatonic interval. Two required arguments are a string specifier
    (such as perfect, major, or minor) and generic, either an int
    of an interval size (such as 2, 2nd, or second) or a
    [`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") object.

    Two DiatonicIntervals are the same if their GenericIntervals
    are the same and their specifiers are the same and they should be
    if their directions are the same, but this is not checked yet.

    The specifier is an enumeration/Specifier object.

    The generic is an integer or GenericInterval instance.

    ```python
    >>> unison = interval.DiatonicInterval(interval.Specifier.PERFECT, 1)
    >>> unison
    <music21.interval.DiatonicInterval P1>
    >>> unison.simpleName
    'P1'
    >>> unison.specifier
    <Specifier.PERFECT>
    >>> unison.generic
    <music21.interval.GenericInterval 1>
    >>> unison.direction
    <Direction.OBLIQUE: 0>
    ```

    The first value can be a string:

    ```python
    >>> major3a = interval.DiatonicInterval('major', 3)
    >>> major3a.simpleName
    'M3'
    >>> major3a.niceName
    'Major Third'
    >>> major3a.semiSimpleName
    'M3'
    >>> major3a.directedSimpleName
    'M3'
    >>> major3a.mod7inversion
    'm6'
    ```

    Or the first attribute can be a string abbreviation
    (not case sensitive, except Major vs. minor):

    ```python
    >>> major3b = interval.DiatonicInterval('M', 3)
    >>> major3b.niceName
    'Major Third'
    ```

    A string can be given for the second argument (generic interval):

    ```python
    >>> major3c = interval.DiatonicInterval('major', 'third')
    >>> major3c.niceName
    'Major Third'
    ```

    ```python
    >>> p8 = interval.DiatonicInterval('perfect', 'octave')
    >>> p8.niceName
    'Perfect Octave'
    ```

    ```python
    >>> genericTenth = interval.GenericInterval(10)
    >>> minor10 = interval.DiatonicInterval('m', genericTenth)
    >>> minor10.mod7
    'm3'
    >>> minor10.isDiatonicStep
    False
    >>> minor10.isStep
    False
    ```

    ```python
    >>> aInterval = interval.DiatonicInterval('major', 2)
    >>> aInterval.isDiatonicStep
    True
    >>> aInterval.isStep
    True
    ```

    ```python
    >>> augAscending = interval.DiatonicInterval('augmented', 1)
    >>> augAscending
    <music21.interval.DiatonicInterval A1>
    >>> augAscending.isDiatonicStep
    False
    >>> augAscending.isStep  # TODO: should this be True???
    False
    >>> augAscending.directedNiceName
    'Ascending Augmented Unison'
    ```

    For Augmented Unisons, the diatonic interval is ascending while the .generic is oblique:

    ```python
    >>> augAscending.direction
    <Direction.ASCENDING: 1>
    >>> augAscending.generic.direction
    <Direction.OBLIQUE: 0>
    ```

    ```python
    >>> dimDescending = augAscending.reverse()
    >>> dimDescending
    <music21.interval.DiatonicInterval d1>
    >>> dimDescending.directedNiceName
    'Descending Diminished Unison'
    >>> dimDescending.direction
    <Direction.DESCENDING: -1>
    ```

    This raises an error:

    ```python
    >>> interval.DiatonicInterval('Perfect', -1)
    Traceback (most recent call last):
    music21.interval.IntervalException: There is no such thing as a descending Perfect Unison
    ```

[`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") bases

* [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") read-only properties

DiatonicInterval.cents
:   Return the number of cents in this interval. Returns a float,
    always assuming an equal-tempered presentation.

    ```python
    >>> i = interval.DiatonicInterval('minor', 'second')
    >>> i.niceName
    'Minor Second'
    >>> i.cents
    100.0
    ```

DiatonicInterval.directedName
:   The name of the interval in abbreviated form with direction.

    ```python
    >>> interval.DiatonicInterval('Minor', -6).directedName
    'm-6'
    ```

DiatonicInterval.directedNiceName
:   The name of the interval in full form with direction.

    ```python
    >>> interval.DiatonicInterval('P', 11).directedNiceName
    'Ascending Perfect Eleventh'
    >>> interval.DiatonicInterval('Diminished', 'Descending Octave').directedNiceName
    'Descending Diminished Octave'
    ```

DiatonicInterval.directedSemiSimpleName
:   The name of the interval in abbreviated form with direction, reduced to one octave,
    except for octaves themselves

    ```python
    >>> interval.DiatonicInterval('Minor', -14).directedSemiSimpleName
    'm-7'
    >>> interval.DiatonicInterval('P', 'Octave').directedSemiSimpleName
    'P8'
    ```

DiatonicInterval.directedSemiSimpleNiceName
:   The name of the interval in full form with direction.

    ```python
    >>> interval.DiatonicInterval('P', 11).directedSemiSimpleNiceName
    'Ascending Perfect Fourth'
    >>> interval.DiatonicInterval('Diminished', 'Descending Octave').directedSemiSimpleNiceName
    'Descending Diminished Octave'
    ```

DiatonicInterval.directedSimpleName
:   The name of the interval in abbreviated form with direction, reduced to one octave

    ```python
    >>> interval.DiatonicInterval('Minor', -14).directedSimpleName
    'm-7'
    ```

DiatonicInterval.directedSimpleNiceName
:   The name of the interval, reduced to within an octave, in full form with direction.

    ```python
    >>> interval.DiatonicInterval('P', 11).directedNiceName
    'Ascending Perfect Eleventh'
    >>> interval.DiatonicInterval('Diminished', 'Descending Octave').directedNiceName
    'Descending Diminished Octave'
    ```

DiatonicInterval.direction
:   The direction of the DiatonicInterval:

    ```python
    >>> interval.DiatonicInterval('Augmented', 'Twelfth').direction
    <Direction.ASCENDING: 1>
    ```

    ```python
    >>> interval.DiatonicInterval('M', -2).direction
    <Direction.DESCENDING: -1>
    ```

    ```python
    >>> interval.DiatonicInterval('P', 1).direction
    <Direction.OBLIQUE: 0>
    ```

    In the absence of other evidence, assumes that augmented unisons are
    ascending and diminished unisons are descending:

    ```python
    >>> interval.DiatonicInterval('d', 1).direction
    <Direction.DESCENDING: -1>
    ```

    ```python
    >>> interval.DiatonicInterval('A', 1).direction
    <Direction.ASCENDING: 1>
    ```

    Note that in the case of non-perfect unisons/primes, the .generic.direction
    will be OBLIQUE while the diatonic direction may be ASCENDING, DESCENDING,
    or OBLIQUE.

    ```python
    >>> interval.DiatonicInterval('A', 1).generic.direction
    <Direction.OBLIQUE: 0>
    ```

DiatonicInterval.isDiatonicStep
:   Same as GenericInterval.isDiatonicStep and .isStep

    ```python
    >>> interval.DiatonicInterval('M', 2).isDiatonicStep
    True
    >>> interval.DiatonicInterval('P', 5).isDiatonicStep
    False
    ```

DiatonicInterval.isSkip
:   Same as GenericInterval.isSkip

    ```python
    >>> interval.DiatonicInterval('M', 2).isSkip
    False
    >>> interval.DiatonicInterval('P', 5).isSkip
    True
    ```

DiatonicInterval.isStep
:   Same as GenericInterval.isStep and .isDiatonicStep

    ```python
    >>> interval.DiatonicInterval('M', 2).isStep
    True
    >>> interval.DiatonicInterval('P', 5).isStep
    False
    ```

DiatonicInterval.mod7
:   Return this interval as string of a specifier followed by a number 1-7,
    representing a diatonic interval within an octave,
    but unlike simpleDirected or simpleUndirected, turns descending
    seconds into sevenths, etc.

    For instance, going down a minor second from C
    would give a B, which is the same as going up a major seventh to B.

    This method gives a string representing a diatonic interval that
    will reach the same note as this DiatonicInterval but within an octave
    up from the basic note.

    ```python
    >>> interval.DiatonicInterval('m', -2).mod7
    'M7'
    >>> interval.DiatonicInterval('m', 2).mod7
    'm2'
    >>> interval.DiatonicInterval('M', 9).mod7
    'M2'
    >>> interval.DiatonicInterval('Perfect', 'Unison').mod7
    'P1'
    >>> interval.DiatonicInterval('Perfect', 'Descending Octave').mod7
    'P1'
    >>> interval.DiatonicInterval(interval.Specifier.AUGMENTED, -4).mod7
    'd5'
    ```

    See [`music21.chord.Chord.semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep") for a place
    this is used.

DiatonicInterval.mod7inversion
:   Return an inversion of the interval within an octave, losing
    direction. Returns as a string.

    ```python
    >>> interval.DiatonicInterval('M', 2).mod7inversion
    'm7'
    >>> interval.DiatonicInterval('A', 4).mod7inversion
    'd5'
    >>> interval.DiatonicInterval('P', 1).mod7inversion
    'P8'
    ```

    Everything is within an octave:

    ```python
    >>> interval.DiatonicInterval('M', 9).mod7inversion
    'm7'
    ```

    Direction is lost:

    ```python
    >>> interval.DiatonicInterval('d', -3).mod7inversion
    'A6'
    ```

DiatonicInterval.name
:   The name of the interval in abbreviated form without direction.

    ```python
    >>> interval.DiatonicInterval('Perfect', 'Fourth').name
    'P4'
    >>> interval.DiatonicInterval(interval.Specifier.MAJOR, -6).name
    'M6'
    ```

DiatonicInterval.niceName
:   Return the full form of the name of a Diatonic interval

    ```python
    >>> interval.DiatonicInterval('P', 4).niceName
    'Perfect Fourth'
    ```

DiatonicInterval.perfectable
:   Is the generic component of this interval able to be made perfect?
    That is, is this a type of unison, fourth, fifth, or octave (or larger
    component).

    Note that this does not ask if THIS interval is perfect. A diminished
    fifth is not perfect, but as a fifth it is perfectable.

    An augmented seventh sounds like a perfect octave but no seventh can
    ever be perfect.

    ```python
    >>> interval.DiatonicInterval('M', 2).perfectable
    False
    >>> interval.DiatonicInterval('P', 12).perfectable
    True
    >>> interval.DiatonicInterval('A', 12).perfectable
    True
    ```

DiatonicInterval.semiSimpleName
:   Return the name of a Diatonic interval removing octaves except that
    octaves (and double octaves) themselves are 8 instead of 1

    ```python
    >>> interval.DiatonicInterval('Augmented', 'Twelfth').semiSimpleName
    'A5'
    >>> interval.DiatonicInterval('Diminished', 'Descending Octave').semiSimpleName
    'd8'
    ```

DiatonicInterval.semiSimpleNiceName
:   Return the full name of a Diatonic interval removing octaves except that
    octaves (and double octaves) themselves are 8 instead of 1

    ```python
    >>> interval.DiatonicInterval('Augmented', 'Twelfth').semiSimpleNiceName
    'Augmented Fifth'
    >>> interval.DiatonicInterval('Diminished', 'Descending Octave').semiSimpleNiceName
    'Diminished Octave'
    ```

DiatonicInterval.simpleName
:   Return the name of a Diatonic interval removing octaves

    ```python
    >>> interval.DiatonicInterval('Augmented', 'Twelfth').simpleName
    'A5'
    ```

DiatonicInterval.simpleNiceName
:   Return the full name of a Diatonic interval, simplifying octaves

    ```python
    >>> interval.DiatonicInterval('d', 14).simpleNiceName
    'Diminished Seventh'
    ```

DiatonicInterval.specificName
:   Same as .specifier.niceName – the nice name of the specifier alone

    ```python
    >>> p12 = interval.DiatonicInterval('P', -12)
    >>> p12.specificName
    'Perfect'
    ```

DiatonicInterval.specifierAbbreviation
:   Returns the abbreviation for the specifier.

    ```python
    >>> i = interval.Interval('M-10')
    >>> d = i.diatonic
    >>> d.specifierAbbreviation
    'M'
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") methods

DiatonicInterval.\_\_eq\_\_(*other*)[[source]](../_modules/music21/interval.html#DiatonicInterval.__eq__)
:   True if generic, specifier, and direction are the same.

    ```python
    >>> a = interval.DiatonicInterval('major', 3)
    >>> b = interval.DiatonicInterval('minor', 3)
    >>> c = interval.DiatonicInterval('major', 3)
    >>> d = interval.DiatonicInterval('diminished', 4)
    >>> a == b
    False
    >>> a == c
    True
    >>> a == d
    False
    >>> e = interval.DiatonicInterval('d', 4)
    >>> d == e
    True
    ```

    Intervals do not compare to strings:

    ```python
    >>> e == 'd4'
    False
    ```

DiatonicInterval.getChromatic() → [ChromaticInterval](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval")[[source]](../_modules/music21/interval.html#DiatonicInterval.getChromatic)
:   Return a [`music21.interval.ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval")
    based on the size of this Interval.

    ```python
    >>> aInterval = interval.DiatonicInterval('major', 'third')
    >>> aInterval.niceName
    'Major Third'
    >>> aInterval.getChromatic()
    <music21.interval.ChromaticInterval 4>
    ```

    ```python
    >>> aInterval = interval.DiatonicInterval('augmented', -5)
    >>> aInterval.niceName
    'Augmented Fifth'
    >>> aInterval.getChromatic()
    <music21.interval.ChromaticInterval -8>
    ```

    ```python
    >>> aInterval = interval.DiatonicInterval('minor', 'second')
    >>> aInterval.niceName
    'Minor Second'
    >>> aInterval.getChromatic()
    <music21.interval.ChromaticInterval 1>
    ```

DiatonicInterval.reverse() → [DiatonicInterval](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval")[[source]](../_modules/music21/interval.html#DiatonicInterval.reverse)
:   Return a [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") that is
    an inversion of this Interval.

    ```python
    >>> aInterval = interval.DiatonicInterval('major', 3)
    >>> aInterval.reverse().directedName
    'M-3'
    ```

    ```python
    >>> aInterval = interval.DiatonicInterval('augmented', 5)
    >>> aInterval.reverse().directedName
    'A-5'
    ```

    (Ascending) Augmented Unisons reverse to (Descending)
    Diminished Unisons and vice versa

    ```python
    >>> aug1 = interval.DiatonicInterval('augmented', 1)
    >>> aug1.direction
    <Direction.ASCENDING: 1>
    >>> aug1.directedName
    'A1'
    >>> dimUnison = aug1.reverse()
    >>> dimUnison.directedName
    'd1'
    >>> dimUnison.directedNiceName
    'Descending Diminished Unison'
    ```

DiatonicInterval.transposePitch(*p: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *\**, *inPlace=False*)[[source]](../_modules/music21/interval.html#DiatonicInterval.transposePitch)
:   Calls transposePitch from a full interval object.

    This is not particularly optimized since it
    requires creating both a ChromaticInterval
    object and a full Interval object. But it’s here for completeness.

    ```python
    >>> di = interval.DiatonicInterval('P', 11)
    >>> p = pitch.Pitch('C#4')
    >>> di.transposePitch(p)
    <music21.pitch.Pitch F#5>
    ```

    Previous pitch was unchanged. inPlace=True changes that.

    ```python
    >>> p
    <music21.pitch.Pitch C#4>
    >>> di.transposePitch(p, inPlace=True)
    >>> p
    <music21.pitch.Pitch F#5>
    ```

    * Changed in v6: added inPlace

Methods inherited from [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase"):

|  |  |  |
| --- | --- | --- |
| * [`transposeNote()`](#music21.interval.IntervalBase.transposeNote "music21.interval.IntervalBase.transposeNote") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") instance variables

DiatonicInterval.generic
:   A [`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") enum representing the general interval.

DiatonicInterval.specifier
:   A [`Specifier`](#music21.interval.Specifier "music21.interval.Specifier") enum representing the Quality of the interval.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Direction

class music21.interval.Direction(*\*values*)[[source]](../_modules/music21/interval.html#Direction)

## GenericInterval

class music21.interval.GenericInterval(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'Unison'*, *\*\*keywords*)[[source]](../_modules/music21/interval.html#GenericInterval)
:   A GenericInterval is an interval such as Third, Seventh, Octave, or Tenth.
    Constructor takes an integer or string specifying the interval and direction.

    The interval is not specified in half-steps, but in numeric values
    derived from interval names:
    a Third is 3; a Seventh is 7, etc. String values for interval names (‘3rd’ or ‘third’)
    are generally accepted, but discouraged since not every one will work.

    staffDistance: the number of lines or spaces apart, eg:

    > E.g. C4 to C4 = 0; C4 to D4 = 1; C4 to B3 = -1

    Two generic intervals are the equal if their size and direction are the same.

    ```python
    >>> gi = interval.GenericInterval(8)
    >>> gi
    <music21.interval.GenericInterval 8>
    ```

    ```python
    >>> third = interval.GenericInterval(3)
    >>> third.directed
    3
    >>> third.direction
    <Direction.ASCENDING: 1>
    >>> third.perfectable
    False
    >>> third.staffDistance
    2
    ```

    We can also specify intervals from strings:

    ```python
    >>> third = interval.GenericInterval('Third')
    >>> third
    <music21.interval.GenericInterval 3>
    >>> third.directed
    3
    ```

    or like this:

    ```python
    >>> thirdDown = interval.GenericInterval('Descending Third')
    >>> thirdDown
    <music21.interval.GenericInterval -3>
    >>> thirdDown.directed
    -3
    ```

    A lot of tools for working with large intervals

    ```python
    >>> twelfthDown = interval.GenericInterval(-12)
    >>> twelfthDown.niceName
    'Twelfth'
    >>> twelfthDown.perfectable
    True
    >>> twelfthDown.staffDistance
    -11
    >>> twelfthDown.mod7
    4
    >>> twelfthDown.directed
    -12
    >>> twelfthDown.undirected
    12
    ```

    ```python
    >>> complement12 = twelfthDown.complement()
    >>> complement12.niceName
    'Fourth'
    >>> complement12.staffDistance
    3
    ```

    Note this illegal interval:

    ```python
    >>> zeroth = interval.GenericInterval(0)
    Traceback (most recent call last):
    music21.interval.IntervalException: The Zeroth is not an interval
    ```

    However, this is okay:

    ```python
    >>> descendingUnison = interval.GenericInterval(-1)
    >>> descendingUnison.direction
    <Direction.DESCENDING: -1>
    >>> descendingUnison.directed
    -1
    >>> descendingUnison.undirected
    1
    ```

    This is because we don’t yet know what type of unison this is: is it
    a Perfect Unison or an Augmented Unison (or Augmented Prime as some prefer)?
    Thus, the illegal check will be moved to a higher level Interval object.

    A second is a step:

    ```python
    >>> second = interval.GenericInterval(2)
    >>> second.isDiatonicStep
    True
    >>> second.isStep
    True
    ```

    A third is not:

    ```python
    >>> third = interval.GenericInterval(-3)
    >>> third.isDiatonicStep
    False
    >>> third.isStep
    False
    ```

    Intervals more than three octaves use numbers with abbreviations instead of names

    ```python
    >>> threeOctaveSecond = interval.GenericInterval(23)
    >>> threeOctaveSecond.niceName
    '23rd'
    ```

    ```python
    >>> threeOctaveThird = interval.GenericInterval(24)
    >>> threeOctaveThird.niceName
    '24th'
    >>> threeOctaveThird.isDiatonicStep
    False
    >>> threeOctaveThird.isStep
    False
    >>> threeOctaveThird.simpleNiceName
    'Third'
    ```

    * Changed in v6: large intervals get abbreviations

[`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") bases

* [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") read-only properties

GenericInterval.direction
:   Returns a Direction Enum value for the direction of this interval:

    ```python
    >>> interval.GenericInterval('Descending Fifth').direction
    <Direction.DESCENDING: -1>
    ```

    ```python
    >>> interval.GenericInterval('Unison').direction
    <Direction.OBLIQUE: 0>
    ```

    ```python
    >>> interval.GenericInterval(4).direction
    <Direction.ASCENDING: 1>
    ```

GenericInterval.isDiatonicStep
:   Return True if this interval is a step (a second).
    A synonym for isStep for generic intervals.

    ```python
    >>> interval.GenericInterval(-2).isDiatonicStep
    True
    >>> interval.GenericInterval(1).isDiatonicStep
    False
    >>> interval.GenericInterval(9).isDiatonicStep
    False
    ```

    Note that Unisons are neither steps nor skips.

GenericInterval.isSkip
:   Returns True if the undirected interval is bigger than a second.

    ```python
    >>> interval.GenericInterval('Octave').isSkip
    True
    >>> interval.GenericInterval('Descending 2nd').isSkip
    False
    >>> interval.GenericInterval(1).isSkip
    False
    ```

    Note that Unisons are neither steps nor skips.

GenericInterval.isStep
:   Return True if this interval is a step (a second).
    A synonym for isDiatonicStep for generic intervals.

    ```python
    >>> interval.GenericInterval(2).isStep
    True
    >>> interval.GenericInterval(1).isStep
    False
    >>> interval.GenericInterval(-9).isStep
    False
    ```

GenericInterval.isUnison
:   Returns True if this interval is a Unison.

    Note that Unisons are neither steps nor skips.

GenericInterval.mod7
:   Return this interval as a number 1-7, that is, within an octave,
    but unlike simpleDirected or simpleUndirected, turn descending
    seconds into sevenths, etc. Used for calculating step names.

    For instance, going down a step from C, or GenericInterval(-2),
    would give a B, which is the same as GenericInterval(7) (not counting
    octaves), but going up a step from C, or GenericInterval(2) is D, which
    is the same as going up a 9th.

    ```python
    >>> interval.GenericInterval(-2).mod7
    7
    >>> interval.GenericInterval(2).mod7
    2
    >>> interval.GenericInterval(9).mod7
    2
    >>> interval.GenericInterval('Unison').mod7
    1
    >>> interval.GenericInterval('Descending Octave').mod7
    1
    >>> interval.GenericInterval(15).mod7
    1
    ```

    See [`music21.chord.Chord.semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep") for a place
    this is used.

GenericInterval.mod7inversion
:   Return the inversion of this interval within an octave.
    For instance, seconds become sevenths, octaves become unisons,
    and vice versa.

    All are undirected intervals.

    ```python
    >>> interval.GenericInterval(4).mod7inversion
    5
    >>> interval.GenericInterval('Descending Octave').mod7inversion
    1
    >>> interval.GenericInterval(9).mod7inversion
    7
    ```

GenericInterval.niceName
:   Return the niceName as a string for this Interval

    ```python
    >>> interval.GenericInterval(4).niceName
    'Fourth'
    >>> interval.GenericInterval(-12).niceName
    'Twelfth'
    >>> interval.GenericInterval(3).niceName
    'Third'
    ```

    Extremely large intervals get displayed as abbreviations

    ```python
    >>> interval.GenericInterval(44).niceName
    '44th'
    ```

    * Changed in v6: large numbers get the ‘th’ or ‘rd’ etc. suffix

GenericInterval.octaves
:   Return the number of octaves with direction.

    ```python
    >>> interval.GenericInterval(5).octaves
    0
    >>> interval.GenericInterval('Descending Ninth').octaves
    -1
    >>> interval.GenericInterval(8).octaves
    1
    >>> interval.GenericInterval(-15).octaves
    -2
    ```

GenericInterval.perfectable
:   Returns True if the interval might represent a perfect interval,
    that is, it is a Generic 4th, 5th, or unison/octave

    ```python
    >>> interval.GenericInterval(4).perfectable
    True
    >>> interval.GenericInterval(-12).perfectable
    True
    >>> interval.GenericInterval(3).perfectable
    False
    ```

GenericInterval.semiSimpleDirected
:   Return the same as semiSimpleUndirected but with descending intervals
    as a negative number

    ```python
    >>> interval.GenericInterval('Descending Ninth').semiSimpleDirected
    -2
    >>> interval.GenericInterval(8).semiSimpleDirected
    8
    >>> interval.GenericInterval(-15).semiSimpleDirected
    -8
    >>> interval.GenericInterval(-8).semiSimpleDirected
    -8
    ```

GenericInterval.semiSimpleNiceName
:   Return the niceName as a string for this Interval’s semiSimple form

    ```python
    >>> interval.GenericInterval(4).semiSimpleNiceName
    'Fourth'
    >>> interval.GenericInterval(-12).semiSimpleNiceName
    'Fifth'
    >>> interval.GenericInterval(8).semiSimpleNiceName
    'Octave'
    ```

GenericInterval.semiSimpleUndirected
:   Same as simpleUndirected, but allows octaves and double octaves, etc.
    to remain 8, which is useful for a
    number of parallel octave vs. unison routines.

    ```python
    >>> interval.GenericInterval('Descending Ninth').semiSimpleUndirected
    2
    >>> interval.GenericInterval(8).semiSimpleUndirected
    8
    >>> interval.GenericInterval(-15).semiSimpleUndirected
    8
    ```

GenericInterval.simpleDirected
:   Return the directed distance within an octave

    ```python
    >>> interval.GenericInterval('Descending Ninth').simpleDirected
    -2
    >>> interval.GenericInterval(8).simpleDirected
    1
    >>> interval.GenericInterval(-8).simpleDirected
    1
    ```

GenericInterval.simpleNiceName
:   Return the niceName as a string for this Interval’s simple form

    ```python
    >>> interval.GenericInterval(4).simpleNiceName
    'Fourth'
    >>> interval.GenericInterval(-12).simpleNiceName
    'Fifth'
    >>> interval.GenericInterval(8).simpleNiceName
    'Unison'
    ```

GenericInterval.simpleUndirected
:   Return the undirected distance within an octave

    ```python
    >>> interval.GenericInterval('Descending Ninth').simpleUndirected
    2
    >>> interval.GenericInterval(8).simpleUndirected
    1
    ```

GenericInterval.staffDistance
:   Return the number of spaces/stafflines that this
    interval represents. A unison is 0, an ascending second is 1,
    a descending third is -2, etc.

    Useful for interval arithmetic

    ```python
    >>> interval.GenericInterval('Ascending Third').staffDistance
    2
    >>> interval.GenericInterval(-8).staffDistance
    -7
    >>> interval.GenericInterval(1).staffDistance
    0
    ```

GenericInterval.undirected
:   Returns the absolute value of self.directed. Read-only

    ```python
    >>> sixthDown = interval.GenericInterval(-6)
    >>> sixthDown.undirected
    6
    ```

GenericInterval.undirectedOctaves
:   Returns the number of octaves (without direction) for an interval

    ```python
    >>> interval.GenericInterval(5).undirectedOctaves
    0
    >>> interval.GenericInterval('Descending Ninth').undirectedOctaves
    1
    >>> interval.GenericInterval(8).undirectedOctaves
    1
    >>> interval.GenericInterval(-15).undirectedOctaves
    2
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") read/write properties

GenericInterval.directed
:   Synonym for self.value

    ```python
    >>> sixthDown = interval.GenericInterval(-6)
    >>> sixthDown.directed
    -6
    >>> sixthDown.directed = 2
    >>> sixthDown.value
    2
    ```

GenericInterval.value
:   The size of this interval as an integer. Synonym for self.directed

    ```python
    >>> interval.GenericInterval('Descending Sixth').value
    -6
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") methods

GenericInterval.\_\_eq\_\_(*other*)[[source]](../_modules/music21/interval.html#GenericInterval.__eq__)
:   True if value and direction are the same.

    ```python
    >>> a = interval.GenericInterval('Third')
    >>> b = interval.GenericInterval(-3)
    >>> c = interval.GenericInterval(3)
    >>> d = interval.GenericInterval(6)
    >>> a == b
    False
    >>> a == a == c
    True
    >>> b == c
    False
    >>> a != d
    True
    >>> a in [b, c, d]
    True
    ```

    ```python
    >>> a == ''
    False
    >>> a is None
    False
    ```

GenericInterval.complement() → [GenericInterval](#music21.interval.GenericInterval "music21.interval.GenericInterval")[[source]](../_modules/music21/interval.html#GenericInterval.complement)
:   Returns a new GenericInterval object where 3rds are 6ths, etc.

    ```python
    >>> third = interval.GenericInterval('Third')
    >>> third.complement()
    <music21.interval.GenericInterval 6>
    ```

    Note that currently direction is lost after a complement relationship:

    ```python
    >>> fourth = interval.GenericInterval(-4)
    >>> fourthComp = fourth.complement()
    >>> fourthComp
    <music21.interval.GenericInterval 5>
    >>> fourthComp.directed
    5
    ```

    Called more than once, this may return the exact identical object:

    ```python
    >>> fourthComp.complement() is fourthComp.complement()
    True
    ```

GenericInterval.getDiatonic(*specifier: [Specifier](#music21.interval.Specifier "music21.interval.Specifier") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [DiatonicInterval](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval")[[source]](../_modules/music21/interval.html#GenericInterval.getDiatonic)
:   Given a specifier, return a [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval") object.

    Specifier should be provided as an interval.Specifier enumeration or
    a string name, such as ‘dd’, ‘M’, or ‘perfect’.

    ```python
    >>> third = interval.GenericInterval('Third')
    >>> third.getDiatonic(interval.Specifier.MAJOR)
    <music21.interval.DiatonicInterval M3>
    >>> third.getDiatonic('minor')
    <music21.interval.DiatonicInterval m3>
    >>> third.getDiatonic('d')
    <music21.interval.DiatonicInterval d3>
    >>> third.getDiatonic(interval.Specifier.TRPAUG)
    <music21.interval.DiatonicInterval AAA3>
    ```

    Old in, specifier values are also allowed

    ```python
    >>> third.getDiatonic(2)
    <music21.interval.DiatonicInterval M3>
    ```

    ```python
    >>> fifth = interval.GenericInterval('fifth')
    >>> fifth.getDiatonic('perfect')
    <music21.interval.DiatonicInterval P5>
    ```

    ```python
    >>> fifth.getDiatonic('major')
    Traceback (most recent call last):
    music21.interval.IntervalException: Cannot create a 'Major Fifth'
    ```

GenericInterval.reverse() → [GenericInterval](#music21.interval.GenericInterval "music21.interval.GenericInterval")[[source]](../_modules/music21/interval.html#GenericInterval.reverse)
:   Returns a new GenericInterval object that is inverted.

    ```python
    >>> aInterval = interval.GenericInterval('Third')
    >>> aInterval.reverse()
    <music21.interval.GenericInterval -3>
    ```

    ```python
    >>> aInterval = interval.GenericInterval(-13)
    >>> aInterval.direction
    <Direction.DESCENDING: -1>
    >>> aInterval.reverse()
    <music21.interval.GenericInterval 13>
    ```

    Unisons invert to unisons

    ```python
    >>> aInterval = interval.GenericInterval(1)
    >>> aInterval.reverse()
    <music21.interval.GenericInterval 1>
    ```

GenericInterval.transposePitch(*p: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *\**, *inPlace=False*)[[source]](../_modules/music21/interval.html#GenericInterval.transposePitch)
:   transpose a pitch, retaining the accidental if any.

    ```python
    >>> aPitch = pitch.Pitch('g4')
    >>> genericFifth = interval.GenericInterval(5)
    >>> bPitch = genericFifth.transposePitch(aPitch)
    >>> bPitch
    <music21.pitch.Pitch D5>
    ```

    If inPlace is True then applied to the current pitch:

    ```python
    >>> gPitch = pitch.Pitch('g4')
    >>> genericFifth = interval.GenericInterval(5)
    >>> genericFifth.transposePitch(gPitch, inPlace=True)
    >>> gPitch
    <music21.pitch.Pitch D5>
    ```

    A generic interval transformation retains accidentals:

    ```python
    >>> a2 = pitch.Pitch('B-')
    >>> cPitch = genericFifth.transposePitch(a2)
    >>> cPitch
    <music21.pitch.Pitch F->
    >>> a2.octave == cPitch.octave
    True
    ```

    Can be done inPlace as well, in which case, nothing is returned:

    ```python
    >>> gSharp = pitch.Pitch('g#4')
    >>> genericFifth = interval.GenericInterval(5)
    >>> genericFifth.transposePitch(gSharp, inPlace=True)
    >>> gSharp
    <music21.pitch.Pitch D#5>
    ```

GenericInterval.transposePitchKeyAware(*p: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *k: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/interval.html#GenericInterval.transposePitchKeyAware)
:   Transposes a pitch while remaining aware of its key context,
    for modal transposition:

    If k is None, works the same as .transposePitch:

    ```python
    >>> aPitch = pitch.Pitch('g4')
    >>> genericFifth = interval.GenericInterval(5)
    >>> bPitch = genericFifth.transposePitchKeyAware(aPitch, None)
    >>> bPitch
    <music21.pitch.Pitch D5>
    ```

    But if a key or keySignature (such as one from .getContextByClass(key.KeySignature))
    is given, then the fun begins:

    ```python
    >>> fis = pitch.Pitch('F#4')
    >>> e = pitch.Pitch('E')
    >>> gMaj = key.Key('G')
    >>> genericStep = interval.GenericInterval('second')
    >>> genericStep.transposePitchKeyAware(fis, gMaj)
    <music21.pitch.Pitch G4>
    >>> genericStep.transposePitchKeyAware(e, gMaj)
    <music21.pitch.Pitch F#>
    ```

    If a pitch already has an accidental that contradicts the current
    key, the difference between that pitch and the new key is applied
    to the new pitch:

    ```python
    >>> fNat = pitch.Pitch('F4')
    >>> genericStep.transposePitchKeyAware(fNat, gMaj)
    <music21.pitch.Pitch G-4>
    ```

    inPlace should work:

    ```python
    >>> genericStep.transposePitchKeyAware(fis, gMaj, inPlace=True)
    >>> fis
    <music21.pitch.Pitch G4>
    ```

    This is used for Stream.transpose when a GenericInterval is given:

    ```python
    >>> s = converter.parse('tinyNotation: 4/4 d4 e f f# g1 a-4 g b- a c1')
    >>> s.measure(1).insert(0, key.Key('G'))
    >>> s.measure(3).insert(0, key.Key('c'))
    >>> s2 = s.transpose(interval.GenericInterval(2))
    >>> s2.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.key.Key of G major>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note F#>
        {2.0} <music21.note.Note G->
        {3.0} <music21.note.Note G>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note A>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.key.Key of c minor>
        {0.0} <music21.note.Note B->
        {1.0} <music21.note.Note A->
        {2.0} <music21.note.Note C>
        {3.0} <music21.note.Note B>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note D>
        {4.0} <music21.bar.Barline type=final>
    ```

    Does not take into account harmonic or melodic minor.

Methods inherited from [`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase"):

|  |  |  |
| --- | --- | --- |
| * [`transposeNote()`](#music21.interval.IntervalBase.transposeNote "music21.interval.IntervalBase.transposeNote") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## IntervalBase

class music21.interval.IntervalBase(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *groups: [Groups](moduleBase.html#music21.base.Groups "music21.base.Groups") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sites: [Sites](moduleSites.html#music21.sites.Sites "music21.sites.Sites") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *duration: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *activeSite: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *style: [Style](moduleStyle.html#music21.style.Style "music21.style.Style") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *editorial: [Editorial](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *offset: OffsetQL = 0.0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/interval.html#IntervalBase)
:   General base class for inheritance.

[`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase") methods

abstractmethod IntervalBase.reverse()[[source]](../_modules/music21/interval.html#IntervalBase.reverse)
:   IntervalBase does not know how to do this, so it must be overridden in
    derived classes.

IntervalBase.transposeNote(*note1: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*) → [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")[[source]](../_modules/music21/interval.html#IntervalBase.transposeNote)
:   Uses self.transposePitch to do the same to a note.

    ```python
    >>> n1 = note.Note('C#4', quarterLength=2.0)
    >>> i = interval.Interval('d5')
    >>> n2 = i.transposeNote(n1)
    >>> n2
    <music21.note.Note G>
    >>> n2.pitch
    <music21.pitch.Pitch G4>
    >>> n2.duration.type
    'half'
    ```

abstractmethod IntervalBase.transposePitch(*pitch1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *\**, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/interval.html#IntervalBase.transposePitch)
:   IntervalBase does not know how to do this, so it must be overridden in
    derived classes.

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`IntervalBase`](#music21.interval.IntervalBase "music21.interval.IntervalBase") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Specifier

class music21.interval.Specifier(*\*values*)[[source]](../_modules/music21/interval.html#Specifier)
:   An enumeration for “specifiers” such as Major, Minor, etc.
    that has some special properties.

    ```python
    >>> from music21.interval import Specifier
    >>> Specifier.PERFECT
    <Specifier.PERFECT>
    ```

    Value numbers are arbitrary and just there for backwards compatibility
    with pre v6 work:

    ```python
    >>> Specifier.PERFECT.value
    1
    >>> Specifier.PERFECT.name
    'PERFECT'
    ```

    ```python
    >>> str(Specifier.PERFECT)
    'P'
    >>> str(Specifier.MINOR)
    'm'
    >>> str(Specifier.DBLDIM)
    'dd'
    >>> Specifier.DBLDIM.niceName
    'Doubly-Diminished'
    ```

## Functions

music21.interval.notesToChromatic(*n1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *n2: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*) → [ChromaticInterval](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval")[[source]](../_modules/music21/interval.html#notesToChromatic)
:   Given two [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects,
    returns a [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") object.

    Works equally well with [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects.

    ```python
    >>> aNote = note.Note('c4')
    >>> bNote = note.Note('g#5')
    >>> interval.notesToChromatic(aNote, bNote)
    <music21.interval.ChromaticInterval 20>
    ```

    ```python
    >>> aPitch = pitch.Pitch('c#4')
    >>> bPitch = pitch.Pitch('f-5')
    >>> bInterval = interval.notesToChromatic(aPitch, bPitch)
    >>> bInterval
    <music21.interval.ChromaticInterval 15>
    ```

music21.interval.intervalsToDiatonic(*gInt: [GenericInterval](#music21.interval.GenericInterval "music21.interval.GenericInterval")*, *cInt: [ChromaticInterval](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval")*) → [DiatonicInterval](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval")[[source]](../_modules/music21/interval.html#intervalsToDiatonic)
:   Given a [`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") and
    a [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") object,
    return a [`DiatonicInterval`](#music21.interval.DiatonicInterval "music21.interval.DiatonicInterval").

    ```python
    >>> aInterval = interval.GenericInterval('descending fifth')
    >>> bInterval = interval.ChromaticInterval(-7)
    >>> cInterval = interval.intervalsToDiatonic(aInterval, bInterval)
    >>> cInterval
    <music21.interval.DiatonicInterval P5>
    ```

music21.interval.intervalFromGenericAndChromatic(*gInt: [GenericInterval](#music21.interval.GenericInterval "music21.interval.GenericInterval") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *cInt: [ChromaticInterval](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [Interval](#music21.interval.Interval "music21.interval.Interval")[[source]](../_modules/music21/interval.html#intervalFromGenericAndChromatic)
:   Given a [`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") and a
    [`ChromaticInterval`](#music21.interval.ChromaticInterval "music21.interval.ChromaticInterval") object, return
    a full [`Interval`](#music21.interval.Interval "music21.interval.Interval").

    ```python
    >>> aInterval = interval.GenericInterval('descending fifth')
    >>> bInterval = interval.ChromaticInterval(-8)
    >>> cInterval = interval.intervalFromGenericAndChromatic(aInterval, bInterval)
    >>> cInterval
    <music21.interval.Interval A-5>
    ```

    ```python
    >>> cInterval.name
    'A5'
    >>> cInterval.directedName
    'A-5'
    >>> cInterval.directedNiceName
    'Descending Augmented Fifth'
    ```

    ```python
    >>> interval.intervalFromGenericAndChromatic(3, 4)
    <music21.interval.Interval M3>
    >>> interval.intervalFromGenericAndChromatic(3, 3)
    <music21.interval.Interval m3>
    ```

    ```python
    >>> interval.intervalFromGenericAndChromatic(5, 6)
    <music21.interval.Interval d5>
    >>> interval.intervalFromGenericAndChromatic(5, 5)
    <music21.interval.Interval dd5>
    >>> interval.intervalFromGenericAndChromatic(-2, -2)
    <music21.interval.Interval M-2>
    ```

    ```python
    >>> interval.intervalFromGenericAndChromatic(1, 0.5)
    <music21.interval.Interval A1 (-50c)>
    ```

music21.interval.add(*intervalList*)[[source]](../_modules/music21/interval.html#add)
:   Add a list of intervals and return the composite interval
    Intervals can be Interval objects or just strings.

    (Currently not particularly efficient for large lists)

    ```python
    >>> A2 = interval.Interval('A2')
    >>> P5 = interval.Interval('P5')
    ```

    ```python
    >>> interval.add([A2, P5])
    <music21.interval.Interval A6>
    >>> interval.add([P5, 'm2'])
    <music21.interval.Interval m6>
    >>> interval.add(['W', 'W', 'H', 'W', 'W', 'W', 'H'])
    <music21.interval.Interval P8>
    ```

    Direction does matter:

    ```python
    >>> interval.add([P5, 'P-4'])
    <music21.interval.Interval M2>
    ```

music21.interval.convertDiatonicNumberToStep(*dn: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['C', 'D', 'E', 'F', 'G', 'A', 'B'], [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/interval.html#convertDiatonicNumberToStep)
:   Convert a diatonic number to a step name (without accidental) and an octave integer.
    The lowest C on a Bösendorfer Imperial Grand is assigned 1 the D above it is 2,
    E is 3, etc. See pitch.diatonicNoteNum for more details

    ```python
    >>> interval.convertDiatonicNumberToStep(15)
    ('C', 2)
    >>> interval.convertDiatonicNumberToStep(23)
    ('D', 3)
    >>> interval.convertDiatonicNumberToStep(0)
    ('B', -1)
    >>> interval.convertDiatonicNumberToStep(1)
    ('C', 0)
    ```

    Extremely high and absurdly low numbers also produce “notes”.

    ```python
    >>> interval.convertDiatonicNumberToStep(2100)
    ('B', 299)
    >>> interval.convertDiatonicNumberToStep(-19)
    ('D', -3)
    ```

music21.interval.convertGeneric(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/interval.html#convertGeneric)
:   Convert an interval specified in terms of its name (second, third)
    into an integer. If integers are passed, assume they are correct.

    ```python
    >>> interval.convertGeneric(3)
    3
    >>> interval.convertGeneric('third')
    3
    >>> interval.convertGeneric('3rd')
    3
    >>> interval.convertGeneric('octave')
    8
    >>> interval.convertGeneric('twelfth')
    12
    >>> interval.convertGeneric('descending twelfth')
    -12
    >>> interval.convertGeneric(12)
    12
    >>> interval.convertGeneric(-12)
    -12
    >>> interval.convertGeneric(1)
    1
    ```

    ```python
    >>> interval.convertGeneric(None)
    Traceback (most recent call last):
    music21.interval.IntervalException: Cannot get a direction from None.
    ```

    Strings are not the same as numbers:

    ```python
    >>> interval.convertGeneric('1')
    Traceback (most recent call last):
    music21.interval.IntervalException: Cannot convert '1' to an interval.
    ```

    But this works:

    ```python
    >>> interval.convertGeneric('1st')
    1
    ```

music21.interval.convertSemitoneToSpecifierGeneric(*count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Specifier](#music21.interval.Specifier "music21.interval.Specifier"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/interval.html#convertSemitoneToSpecifierGeneric)
:   Given a number of semitones, return a default diatonic specifier, and
    a number that can be used as a GenericInterval

    ```python
    >>> interval.convertSemitoneToSpecifierGeneric(0)
    (<Specifier.PERFECT>, 1)
    >>> interval.convertSemitoneToSpecifierGeneric(-2)
    (<Specifier.MAJOR>, -2)
    >>> interval.convertSemitoneToSpecifierGeneric(1)
    (<Specifier.MINOR>, 2)
    >>> interval.convertSemitoneToSpecifierGeneric(7)
    (<Specifier.PERFECT>, 5)
    >>> interval.convertSemitoneToSpecifierGeneric(11)
    (<Specifier.MAJOR>, 7)
    >>> interval.convertSemitoneToSpecifierGeneric(12)
    (<Specifier.PERFECT>, 8)
    >>> interval.convertSemitoneToSpecifierGeneric(13)
    (<Specifier.MINOR>, 9)
    >>> interval.convertSemitoneToSpecifierGeneric(-15)
    (<Specifier.MINOR>, -10)
    >>> interval.convertSemitoneToSpecifierGeneric(24)
    (<Specifier.PERFECT>, 15)
    ```

    Note that the tritone is given as diminished fifth, not augmented fourth:

    ```python
    >>> interval.convertSemitoneToSpecifierGeneric(6)
    (<Specifier.DIMINISHED>, 5)
    ```

    Microtones are rounded here:

    ```python
    >>> interval.convertSemitoneToSpecifierGeneric(0.4)
    (<Specifier.PERFECT>, 1)
    >>> interval.convertSemitoneToSpecifierGeneric(0.6)
    (<Specifier.MINOR>, 2)
    ```

music21.interval.convertSemitoneToSpecifierGenericMicrotone(*count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Specifier](#music21.interval.Specifier "music21.interval.Specifier"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][[source]](../_modules/music21/interval.html#convertSemitoneToSpecifierGenericMicrotone)
:   Given a number of semitones (positive or negative),
    return a default diatonic specifier and cent offset.

    ```python
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(2.5)
    (<Specifier.MAJOR>, 2, 50.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(-2.5)
    (<Specifier.MINOR>, -3, 50.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(-2.25)
    (<Specifier.MAJOR>, -2, -25.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(-1.0)
    (<Specifier.MINOR>, -2, 0.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(2.25)
    (<Specifier.MAJOR>, 2, 25.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(1.0)
    (<Specifier.MINOR>, 2, 0.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(1.75)
    (<Specifier.MAJOR>, 2, -25.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(1.9)
    (<Specifier.MAJOR>, 2, -10.0...)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(0.25)
    (<Specifier.PERFECT>, 1, 25.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(12.25)
    (<Specifier.PERFECT>, 8, 25.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(24.25)
    (<Specifier.PERFECT>, 15, 25.0)
    >>> interval.convertSemitoneToSpecifierGenericMicrotone(23.75)
    (<Specifier.PERFECT>, 15, -25.0)
    ```

music21.interval.convertStaffDistanceToInterval(*staffDist*)[[source]](../_modules/music21/interval.html#convertStaffDistanceToInterval)
:   Returns an integer of the generic interval number
    (P5 = 5, M3 = 3, minor 3 = 3 also) etc. from the given staff distance.

    ```python
    >>> interval.convertStaffDistanceToInterval(3)
    4
    >>> interval.convertStaffDistanceToInterval(7)
    8
    >>> interval.convertStaffDistanceToInterval(0)
    1
    >>> interval.convertStaffDistanceToInterval(-1)
    -2
    ```

music21.interval.getAbsoluteHigherNote(*note1: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")[[source]](../_modules/music21/interval.html#getAbsoluteHigherNote)

music21.interval.getAbsoluteHigherNote(*note1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")
:   Given two [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") or [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects,
    returns the higher element based on sounding pitch.
    If both sounding pitches are the same, returns the first element given.

    ```python
    >>> aNote = note.Note('c#3')
    >>> bNote = note.Note('d--3')
    >>> interval.getAbsoluteHigherNote(aNote, bNote)
    <music21.note.Note C#>
    ```

music21.interval.getAbsoluteLowerNote(*note1: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")[[source]](../_modules/music21/interval.html#getAbsoluteLowerNote)

music21.interval.getAbsoluteLowerNote(*note1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")
:   Given two [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") or [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects, returns
    the lower element based on actual pitch.
    If both pitches are the same, returns the first element given.

    ```python
    >>> aNote = pitch.Pitch('c#3')
    >>> bNote = pitch.Pitch('d--3')
    >>> interval.getAbsoluteLowerNote(aNote, bNote)
    <music21.pitch.Pitch D--3>
    ```

music21.interval.getWrittenHigherNote(*note1: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")[[source]](../_modules/music21/interval.html#getWrittenHigherNote)

music21.interval.getWrittenHigherNote(*note1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")
:   Given two [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") or [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects,
    this function returns the higher element based on diatonic note
    numbers. If the diatonic numbers are
    the same, returns the sounding higher element,
    or the first element if that is also the same.

    ```python
    >>> cis = pitch.Pitch('C#')
    >>> deses = pitch.Pitch('D--')
    >>> higher = interval.getWrittenHigherNote(cis, deses)
    >>> higher is deses
    True
    ```

    ```python
    >>> aPitch = pitch.Pitch('c#3')
    >>> bPitch = pitch.Pitch('d-3')
    >>> interval.getWrittenHigherNote(aPitch, bPitch)
    <music21.pitch.Pitch D-3>
    ```

    ```python
    >>> aNote = note.Note('c#3')
    >>> bNote = note.Note('c3')
    >>> interval.getWrittenHigherNote(aNote, bNote) is aNote
    True
    ```

music21.interval.getWrittenLowerNote(*note1: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")[[source]](../_modules/music21/interval.html#getWrittenLowerNote)

music21.interval.getWrittenLowerNote(*note1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *note2: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")
:   Given two [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") or [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects,
    returns the lower element based on diatonic note
    number. If the diatonic number is
    the same returns the sounding lower element,
    or the first element if sounding pitch is also the same.

    ```python
    >>> aNote = pitch.Pitch('C#3')
    >>> bNote = pitch.Pitch('D--3')
    >>> interval.getWrittenLowerNote(aNote, bNote)
    <music21.pitch.Pitch C#3>
    ```

    ```python
    >>> aNote = pitch.Pitch('C#3')
    >>> bNote = pitch.Pitch('D-3')
    >>> interval.getWrittenLowerNote(aNote, bNote)
    <music21.pitch.Pitch C#3>
    ```

    Both elements should be pitches or notes – if note2 is lower and not the same class
    as note1 raises a ValueError:

    ```python
    >>> aNote = pitch.Pitch('C#4')
    >>> bNote = note.Note('C#3')
    >>> interval.getWrittenLowerNote(aNote, bNote)
    Traceback (most recent call last):
    ValueError: note1 <music21.pitch.Pitch C#4>
        and note2 <music21.note.Note C#> must both be notes or pitches
    ```

music21.interval.intervalToPythagoreanRatio(*intervalObj: [Interval](#music21.interval.Interval "music21.interval.Interval")*) → [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/interval.html#intervalToPythagoreanRatio)
:   Returns the interval ratio in pythagorean tuning, always as a Fraction object.

    ```python
    >>> iList = [interval.Interval(name) for name in ('P4', 'P5', 'M7', 'm23')]
    >>> iList
    [<music21.interval.Interval P4>,
     <music21.interval.Interval P5>,
     <music21.interval.Interval M7>,
     <music21.interval.Interval m23>]
    ```

    ```python
    >>> [interval.intervalToPythagoreanRatio(i) for i in iList]
    [Fraction(4, 3), Fraction(3, 2), Fraction(243, 128), Fraction(2048, 243)]
    ```

    Throws an exception if no ratio can be found, such as for quarter tones.

    ```python
    >>> p1, p2 = pitch.Pitch('C1'), pitch.Pitch('C1')
    >>> p2.accidental = 'half-sharp'
    ```

    ```python
    >>> fiftyCent = interval.Interval(p1, p2)
    >>> fiftyCent
    <music21.interval.Interval A1 (-50c)>
    ```

    ```python
    >>> interval.intervalToPythagoreanRatio(fiftyCent)
    Traceback (most recent call last):
    music21.interval.IntervalException: Could not find a pythagorean ratio for
        <music21.interval.Interval A1 (-50c)>.
    ```

music21.interval.notesToGeneric(*n1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *n2: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*) → [GenericInterval](#music21.interval.GenericInterval "music21.interval.GenericInterval")[[source]](../_modules/music21/interval.html#notesToGeneric)
:   Given two [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects,
    returns a [`GenericInterval`](#music21.interval.GenericInterval "music21.interval.GenericInterval") object.

    Works equally well with [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects

    ```python
    >>> aNote = note.Note('c4')
    >>> bNote = note.Note('g5')
    >>> aInterval = interval.notesToGeneric(aNote, bNote)
    >>> aInterval
    <music21.interval.GenericInterval 12>
    ```

    ```python
    >>> aPitch = pitch.Pitch('c#4')
    >>> bPitch = pitch.Pitch('f-5')
    >>> bInterval = interval.notesToGeneric(aPitch, bPitch)
    >>> bInterval
    <music21.interval.GenericInterval 11>
    ```

music21.interval.notesToInterval(*n1*, *n2*) → [Interval](#music21.interval.Interval "music21.interval.Interval")[[source]](../_modules/music21/interval.html#notesToInterval)
:   Soon to be DEPRECATED: Call Interval Directly

    Given two [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects, returns an
    [`Interval`](#music21.interval.Interval "music21.interval.Interval") object. The same
    functionality is available by calling the Interval class
    with two Notes as arguments.

    ```python
    >>> aNote = note.Note('c4')
    >>> bNote = note.Note('g5')
    >>> aInterval = interval.notesToInterval(aNote, bNote)
    >>> aInterval
    <music21.interval.Interval P12>
    ```

music21.interval.parseSpecifier(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Specifier](#music21.interval.Specifier "music21.interval.Specifier")*) → [Specifier](#music21.interval.Specifier "music21.interval.Specifier")[[source]](../_modules/music21/interval.html#parseSpecifier)
:   Given an integer or a string representing a “specifier” (major, minor,
    perfect, diminished, etc.), return the Specifier.

    ```python
    >>> interval.parseSpecifier('p')
    <Specifier.PERFECT>
    >>> interval.parseSpecifier('P')
    <Specifier.PERFECT>
    >>> interval.parseSpecifier('M')
    <Specifier.MAJOR>
    >>> interval.parseSpecifier('major')
    <Specifier.MAJOR>
    >>> interval.parseSpecifier('m')
    <Specifier.MINOR>
    >>> interval.parseSpecifier('Augmented')
    <Specifier.AUGMENTED>
    >>> interval.parseSpecifier('a')
    <Specifier.AUGMENTED>
    ```

    This is not very useful, but they are there for completeness:

    ```python
    >>> interval.parseSpecifier(interval.Specifier.MAJOR)
    <Specifier.MAJOR>
    ```

    This is the same as calling a Specifier by value:

    ```python
    >>> interval.parseSpecifier(3)
    <Specifier.MINOR>
    ```

    Why? Because of this:

    ```python
    >>> interval.Specifier.MINOR.value
    3
    ```

    Unparsable strings raise an IntervalException:

    ```python
    >>> interval.parseSpecifier('Zebra')
    Traceback (most recent call last):
    music21.interval.IntervalException: Cannot find a match for value: 'Zebra'
    ```

    Illegal intervals raise a ValueError:

    ```python
    >>> interval.parseSpecifier(None)
    Traceback (most recent call last):
    ValueError: Value None must be int, str, or Specifier
    ```

music21.interval.subtract(*intervalList*)[[source]](../_modules/music21/interval.html#subtract)
:   Starts with the first interval and subtracts the
    following intervals from it:

    ```python
    >>> interval.subtract(['P5', 'M3'])
    <music21.interval.Interval m3>
    >>> interval.subtract(['P4', 'd3'])
    <music21.interval.Interval A2>
    ```

    ```python
    >>> m2Object = interval.Interval('m2')
    >>> interval.subtract(['M6', 'm2', m2Object])
    <music21.interval.Interval AA4>
    >>> interval.subtract(['P4', 'M-2'])
    <music21.interval.Interval P5>
    >>> interval.subtract(['A2', 'A2'])
    <music21.interval.Interval P1>
    >>> interval.subtract(['A1', 'P1'])
    <music21.interval.Interval A1>
    ```

    ```python
    >>> interval.subtract(['P8', 'P1'])
    <music21.interval.Interval P8>
    >>> interval.subtract(['P8', 'd2'])
    <music21.interval.Interval A7>
    >>> interval.subtract(['P8', 'A1'])
    <music21.interval.Interval d8>
    ```

    ```python
    >>> a = interval.subtract(['P5', 'A5'])
    >>> a.niceName
    'Diminished Unison'
    >>> a.directedNiceName
    'Descending Diminished Unison'
    >>> a.chromatic.semitones
    -1
    ```

music21.interval.transposeNote(*note1: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *intervalString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Interval](#music21.interval.Interval "music21.interval.Interval")*) → [note.Note](moduleNote.html#music21.note.Note "music21.note.Note")[[source]](../_modules/music21/interval.html#transposeNote)
:   To be deprecated: call n.transpose(intervalString) directly.

    Given a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") and
    an interval string (such as ‘P5’) or an Interval object,
    return a new Note object at the appropriate pitch level.

    ```python
    >>> aNote = note.Note('c4')
    >>> bNote = interval.transposeNote(aNote, 'p5')
    >>> bNote
    <music21.note.Note G>
    >>> bNote.pitch
    <music21.pitch.Pitch G4>
    ```

    ```python
    >>> aNote = note.Note('f#4')
    >>> bNote = interval.transposeNote(aNote, 'm2')
    >>> bNote
    <music21.note.Note G>
    ```

music21.interval.transposePitch(*pitch1: [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *interval1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Interval](#music21.interval.Interval "music21.interval.Interval")*, *\**, *inPlace=False*) → [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/interval.html#transposePitch)
:   DEPRECATED: call p.transpose(interval1) directly

    Given a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")
    and a [`Interval`](#music21.interval.Interval "music21.interval.Interval") object (Not another class such
    as ChromaticInterval) or a string such as ‘P5’ or a number such as 6 (=tritone),
    return a new Pitch object at the appropriate pitch level.

    ```python
    >>> aPitch = pitch.Pitch('C4')
    >>> P5 = interval.Interval('P5')
    >>> bPitch = interval.transposePitch(aPitch, P5)
    >>> bPitch
    <music21.pitch.Pitch G4>
    >>> bInterval = interval.Interval('P-5')
    >>> cPitch = interval.transposePitch(aPitch, bInterval)
    >>> cPitch
    <music21.pitch.Pitch F3>
    ```

    Pitches with implicit octaves should work,

    ```python
    >>> dPitch = pitch.Pitch('G')
    >>> ePitch = interval.transposePitch(dPitch, P5)
    >>> ePitch
    <music21.pitch.Pitch D>
    ```

    Can be done inPlace as well

    ```python
    >>> C4 = pitch.Pitch('C4')
    >>> interval.transposePitch(C4, P5, inPlace=True)
    >>> C4
    <music21.pitch.Pitch G4>
    ```

    * Changed in v6: added inPlace parameter
