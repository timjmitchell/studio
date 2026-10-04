Source: https://music21.org/music21docs/moduleReference/moduleScale.html

# music21.scale

The various Scale objects provide a bidirectional object representation
of octave repeating and non-octave repeating scales built by network
of [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") objects as modeled
in `IntervalNetwork`.

The main public interface to these resources are subclasses
of [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"), such
as [`MajorScale`](#music21.scale.MajorScale "music21.scale.MajorScale"), [`MinorScale`](#music21.scale.MinorScale "music21.scale.MinorScale"),
and [`MelodicMinorScale`](#music21.scale.MelodicMinorScale "music21.scale.MelodicMinorScale").

More unusual scales are also available, such
as [`OctatonicScale`](#music21.scale.OctatonicScale "music21.scale.OctatonicScale"), [`SieveScale`](#music21.scale.SieveScale "music21.scale.SieveScale"),
and [`RagMarwa`](#music21.scale.RagMarwa "music21.scale.RagMarwa").

All [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") subclasses provide the ability
to get pitches across any range, get a pitch for scale step, get a
scale step for pitch, and, for any given pitch ascend or descend to the
next pitch. In all cases [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects are returned.

```python
>>> sc1 = scale.MajorScale('a')
>>> [str(p) for p in sc1.getPitches('g2', 'g4')]
['G#2', 'A2', 'B2', 'C#3', 'D3', 'E3', 'F#3', 'G#3', 'A3', 'B3', 'C#4', 'D4', 'E4', 'F#4']
```

```python
>>> sc2 = scale.MelodicMinorScale('a')
>>> [str(p) for p in sc2.getPitches('g2', 'g4', direction=scale.Direction.DESCENDING)]
['G4', 'F4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'F3', 'E3', 'D3', 'C3', 'B2', 'A2', 'G2']
```

```python
>>> [str(p) for p in sc2.getPitches('g2', 'g4', direction=scale.Direction.ASCENDING)]
['G#2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F#3', 'G#3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4']
```

## ConcreteScale

class music21.scale.ConcreteScale(*tonic: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#ConcreteScale)
:   A concrete scale is specific scale formation with
    a defined pitch collection (a tonic Pitch) that
    may or may not be bound by specific range. For
    example, a specific Major Scale, such as G
    Major, from G2 to G4.

    This class is can either be used directly or more
    commonly as a base class for all concrete scales.

    Here we treat a diminished triad as a scale:

    ```python
    >>> myScale = scale.ConcreteScale(pitches=['C4', 'E-4', 'G-4', 'A4'])
    >>> myScale.getTonic()
    <music21.pitch.Pitch C4>
    >>> myScale.nextPitch('G-2')
    <music21.pitch.Pitch A2>
    >>> [str(p) for p in myScale.getPitches('E-5', 'G-7')]
    ['E-5', 'G-5', 'A5', 'C6', 'E-6', 'G-6', 'A6', 'C7', 'E-7', 'G-7']
    ```

    A scale that lasts two octaves and uses quarter tones (D~)

    ```python
    >>> complexScale = scale.ConcreteScale(
    ...     pitches=['C#3', 'E-3', 'F3', 'G3', 'B3', 'D~4', 'F#4', 'A4', 'C#5']
    ... )
    >>> complexScale.getTonic()
    <music21.pitch.Pitch C#3>
    >>> complexScale.nextPitch('G3', direction=scale.Direction.DESCENDING)
    <music21.pitch.Pitch F3>
    ```

    ```python
    >>> [str(p) for p in complexScale.getPitches('C3', 'C7')]
    ['C#3', 'E-3', 'F3', 'G3', 'B3', 'D~4', 'F#4',
     'A4', 'C#5', 'E-5', 'F5', 'G5', 'B5', 'D~6', 'F#6', 'A6']
    ```

    Descending form:

    ```python
    >>> [str(p) for p in complexScale.getPitches('C7', 'C5')]
    ['A6', 'F#6', 'D~6', 'B5', 'G5', 'F5', 'E-5', 'C#5']
    ```

    ### Equality

    Two ConcreteScales are the same if they satisfy all general Music21Object
    equality methods and their Abstract scales, their tonics, and their
    boundRanges are the same:

[`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") bases

* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") read-only properties

ConcreteScale.chord
:   Return a Chord object from this harmony over a default range.
    Use the getChord() method if you need greater control over the
    parameters of the chord.

ConcreteScale.isConcrete
:   Return True if the scale is Concrete, that is, it has a defined Tonic.

    ```python
    >>> sc1 = scale.MajorScale('c')
    >>> sc1.isConcrete
    True
    >>> sc2 = scale.MajorScale()
    >>> sc2.isConcrete
    False
    ```

    To be concrete, a Scale must have a
    defined tonic. An abstract Scale is not Concrete

ConcreteScale.name
:   Return or construct the name of this scale

    ```python
    >>> sc = scale.DiatonicScale()  # abstract, as no defined tonic
    >>> sc.name
    'Abstract diatonic'
    ```

ConcreteScale.pitches
:   Get a default pitch list from this scale.

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") read/write properties

ConcreteScale.abstract
:   Return the AbstractScale instance governing this ConcreteScale.

    ```python
    >>> sc1 = scale.MajorScale('d')
    >>> sc2 = scale.MajorScale('b-')
    >>> sc1 == sc2
    False
    >>> sc1.abstract == sc2.abstract
    True
    ```

    Abstract scales can also be set afterwards:

    ```python
    >>> scVague = scale.ConcreteScale()
    >>> scVague.abstract = scale.AbstractDiatonicScale('major')
    >>> scVague.tonic = pitch.Pitch('D')
    >>> [p.name for p in scVague.getPitches()]
    ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']
    ```

    ```python
    >>> scVague.abstract = scale.AbstractOctatonicScale()
    >>> [p.name for p in scVague.getPitches()]
    ['D', 'E', 'F', 'G', 'A-', 'B-', 'C-', 'D-', 'D']
    ```

    * Changed in v6: changing .abstract is now allowed.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") methods

ConcreteScale.\_\_eq\_\_(*other*)[[source]](../_modules/music21/scale.html#ConcreteScale.__eq__)
:   For concrete equality, the stored abstract objects must evaluate as equal,
    as well as local attributes.

    ```python
    >>> sc1 = scale.MajorScale('c')
    >>> sc2 = scale.MajorScale('c')
    >>> sc3 = scale.MinorScale('c')
    >>> sc4 = scale.MajorScale('g')
    >>> sc5 = scale.MajorScale()  # an abstract scale, as no tonic defined
    ```

    ```python
    >>> sc1 == sc2
    True
    >>> sc1 == sc3
    False
    >>> sc1 == sc4
    False
    >>> sc1.abstract == sc4.abstract  # can compare abstract forms
    True
    >>> sc4 == sc5  # implicit abstract comparison
    True
    >>> sc5 == sc2  # implicit abstract comparison
    True
    >>> sc5 == sc3  # implicit abstract comparison
    False
    ```

ConcreteScale.derive(*other*, *comparisonAttribute='pitchClass'*)[[source]](../_modules/music21/scale.html#ConcreteScale.derive)
:   Return the closest-matching [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
    based on the pitch collection provided as a
    `Stream`, a [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"),
    or a list of [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects.

    How the “closest-matching” scale is defined still needs to be
    refined and has changed in the past and will probably change in the future.

    ```python
    >>> sc1 = scale.MajorScale()
    >>> sc1.derive(['C#', 'E', 'G#'])
    <music21.scale.MajorScale B major>
    ```

    ```python
    >>> sc1.derive(['E-', 'B-', 'D'], comparisonAttribute='name')
    <music21.scale.MajorScale B- major>
    ```

ConcreteScale.deriveAll(*other*, *comparisonAttribute='pitchClass'*)[[source]](../_modules/music21/scale.html#ConcreteScale.deriveAll)
:   Return a list of all Scales of the same class as self
    where all the pitches in other are contained.

    Similar to “deriveRanked” but only returns those scales
    no matter how many which contain all the pitches.

    Just returns a list in order.

    If you are working with Diatonic Scales, you will
    probably want to change the comparisonAttribute to name.

    ```python
    >>> sc1 = scale.MajorScale()
    >>> sc1.deriveAll(['C', 'E', 'B'])
    [<music21.scale.MajorScale G major>, <music21.scale.MajorScale C major>]
    ```

    ```python
    >>> [sc.name for sc in sc1.deriveAll(['D-', 'E', 'B'])]
    ['B major', 'A major', 'E major', 'D major', 'C- major']
    ```

    ```python
    >>> sc1.deriveAll(['D-', 'E', 'B'], comparisonAttribute='name')
    []
    ```

    Find all instances of this pentatonic scale in major scales:

    ```python
    >>> scList = sc1.deriveAll(['C#', 'D#', 'F#', 'G#', 'A#'], comparisonAttribute='name')
    >>> [sc.name for sc in scList]
    ['B major', 'F# major', 'C# major']
    ```

ConcreteScale.deriveByDegree(*degree*, *pitchRef*)[[source]](../_modules/music21/scale.html#ConcreteScale.deriveByDegree)
:   Given a scale degree and a pitch, return a
    new [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") that satisfies
    that condition.

    Find a major scale with C as the 7th degree:

    ```python
    >>> sc1 = scale.MajorScale()
    >>> sc1.deriveByDegree(7, 'c')
    <music21.scale.MajorScale D- major>
    ```

    TODO: Does not yet work for directional scales

ConcreteScale.deriveRanked(*other*, *resultsReturned=4*, *comparisonAttribute='pitchClass'*, *removeDuplicates=False*)[[source]](../_modules/music21/scale.html#ConcreteScale.deriveRanked)
:   Return a list of closest-matching [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") objects
    based on this [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"),
    provided as a `Stream`, a [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"),
    or a list of [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects.
    Returned integer values represent the number of matches.

    If you are working with Diatonic Scales, you will probably
    want to change the comparisonAttribute to name.

    ```python
    >>> sc1 = scale.MajorScale()
    >>> sc1.deriveRanked(['C', 'E', 'B'])
    [(3, <music21.scale.MajorScale G major>),
     (3, <music21.scale.MajorScale C major>),
     (2, <music21.scale.MajorScale B major>),
     (2, <music21.scale.MajorScale A major>)]
    ```

    With the default of comparing by pitchClass, D- is fine for B major
    because C# is in the B major scale.

    ```python
    >>> sc1.deriveRanked(['D-', 'E', 'B'])
    [(3, <music21.scale.MajorScale B major>),
     (3, <music21.scale.MajorScale A major>),
     (3, <music21.scale.MajorScale E major>),
     (3, <music21.scale.MajorScale D major>)]
    ```

    Comparing based on enharmonic-sensitive spelling, has fewer hits
    for all of these scales:

    ```python
    >>> sc1.deriveRanked(['D-', 'E', 'B'], comparisonAttribute='name')
    [(2, <music21.scale.MajorScale B major>),
     (2, <music21.scale.MajorScale A major>),
     (2, <music21.scale.MajorScale G major>),
     (2, <music21.scale.MajorScale E major>)]
    ```

    Notice that we check how many of the pitches are in the scale
    and do not de-duplicate pitches.

    ```python
    >>> sc1.deriveRanked(['C', 'E', 'E', 'E', 'B'])
    [(5, <music21.scale.MajorScale G major>),
     (5, <music21.scale.MajorScale C major>),
     (4, <music21.scale.MajorScale B major>),
     (4, <music21.scale.MajorScale A major>)]
    ```

    If removeDuplicates is given, the E’s will get less weight:

    ```python
    >>> sc1.deriveRanked(['C', 'E', 'E', 'E', 'B'], removeDuplicates=True)
    [(3, <music21.scale.MajorScale G major>),
     (3, <music21.scale.MajorScale C major>),
     (2, <music21.scale.MajorScale B major>),
     (2, <music21.scale.MajorScale A major>)]
    ```

    ```python
    >>> sc1.deriveRanked(['C#', 'E', 'G#'])
    [(3, <music21.scale.MajorScale B major>),
     (3, <music21.scale.MajorScale A major>),
     (3, <music21.scale.MajorScale E major>),
     (3, <music21.scale.MajorScale C- major>)]
    ```

    A Concrete Scale created from pitches still has similar
    characteristics to the original.

    Here we create a scale like a Harmonic minor but with flat 2 and sharp 4.

    ```python
    >>> e = scale.ConcreteScale(pitches=['A4', 'B-4', 'C5', 'D#5', 'E5', 'F5', 'G#5', 'A5'])
    ```

    Notice the G# is allowed to be chosen even though we are specifically looking for
    scales with a G natural in them. Once no scale matched all three pitches,
    which scale that matches two pitches is arbitrary.

    ```python
    >>> bestScales = e.deriveRanked(['C', 'E', 'G'], resultsReturned=6)
    >>> bestScales
    [(3, <music21.scale.ConcreteScale E Concrete>),
     (3, <music21.scale.ConcreteScale D- Concrete>),
     (3, <music21.scale.ConcreteScale C# Concrete>),
     (2, <music21.scale.ConcreteScale B Concrete>),
     (2, <music21.scale.ConcreteScale A Concrete>),
     (2, <music21.scale.ConcreteScale G# Concrete>)]
    ```

    ```python
    >>> eConcrete = bestScales[0][1]
    >>> ' '.join([str(p) for p in eConcrete.pitches])
    'E4 F4 G4 A#4 B4 C5 D#5 E5'
    ```

ConcreteScale.findMissing(*other*, *comparisonAttribute='pitchClass'*, *minPitch=None*, *maxPitch=None*, *direction=Direction.ASCENDING*, *alteredDegrees=None*)[[source]](../_modules/music21/scale.html#ConcreteScale.findMissing)
:   Given another object of the forms that extractPitches takes
    (e.g., a `Stream`,
    a [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"),
    a list of [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects),
    return a list of pitches that are found in this Scale but are not
    found in the provided object.

    ```python
    >>> sc1 = scale.MajorScale('g4')
    >>> [str(p) for p in sc1.findMissing(['d'])]
    ['G4', 'A4', 'B4', 'C5', 'E5', 'F#5', 'G5']
    ```

ConcreteScale.getChord(*minPitch=None*, *maxPitch=None*, *direction=Direction.ASCENDING*, *\*\*keywords*) → [music21.chord.Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")[[source]](../_modules/music21/scale.html#ConcreteScale.getChord)
:   Return a realized chord containing all the
    pitches in this scale within a particular
    inclusive range defined by two pitches.

    All keyword arguments are passed on to the
    Chord, permitting specification of
    quarterLength and similar parameters.

ConcreteScale.getDegreeMaxUnique()[[source]](../_modules/music21/scale.html#ConcreteScale.getDegreeMaxUnique)
:   Convenience routine to get this from the AbstractScale.

ConcreteScale.getPitches(*minPitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *direction: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/scale.html#ConcreteScale.getPitches)
:   Return a list of Pitch objects, using a
    deepcopy of a cached version if available.

ConcreteScale.getScalaData()[[source]](../_modules/music21/scale.html#ConcreteScale.getScalaData)
:   Return a configured `ScalaData`
    Object for this scale. It can be used to find interval
    distances in cents between degrees.

ConcreteScale.getScaleDegreeAndAccidentalFromPitch(*pitchTarget*, *direction=Direction.ASCENDING*, *comparisonAttribute='name'*)[[source]](../_modules/music21/scale.html#ConcreteScale.getScaleDegreeAndAccidentalFromPitch)
:   Given a scale (or [`Key`](moduleKey.html#music21.key.Key "music21.key.Key") object) and a pitch, return a two-element
    tuple of the degree of the scale and an accidental (or None) needed to get this
    pitch.

    ```python
    >>> cMaj = key.Key('C')
    >>> cMaj.getScaleDegreeAndAccidentalFromPitch(pitch.Pitch('E'))
    (3, None)
    >>> cMaj.getScaleDegreeAndAccidentalFromPitch(pitch.Pitch('E-'))
    (3, <music21.pitch.Accidental flat>)
    ```

    The Direction of a melodic minor scale is significant

    ```python
    >>> aMin = scale.MelodicMinorScale('a')
    >>> aMin.getScaleDegreeAndAccidentalFromPitch(pitch.Pitch('G'),
    ...                                           direction=scale.Direction.DESCENDING)
    (7, None)
    >>> aMin.getScaleDegreeAndAccidentalFromPitch(pitch.Pitch('G'),
    ...                                           direction=scale.Direction.ASCENDING)
    (7, <music21.pitch.Accidental flat>)
    >>> aMin.getScaleDegreeAndAccidentalFromPitch(pitch.Pitch('G-'),
    ...                                           direction=scale.Direction.ASCENDING)
    (7, <music21.pitch.Accidental double-flat>)
    ```

    Returns (None, None) if for some reason this scale does not have this step
    (a whole-tone scale, for instance)

ConcreteScale.getScaleDegreeFromPitch(*pitchTarget*, *direction=Direction.ASCENDING*, *comparisonAttribute='name'*)[[source]](../_modules/music21/scale.html#ConcreteScale.getScaleDegreeFromPitch)
:   For a given pitch, return the appropriate scale degree.
    If no scale degree is available, None is returned.

    Note: by default it will use a find algorithm that is based on the note’s
    .name not on .pitchClass because this is used so commonly by tonal functions.
    So if it’s important that D# and E- are the same, set the
    comparisonAttribute to pitchClass

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> sc.getScaleDegreeFromPitch('e-2')
    1
    >>> sc.getScaleDegreeFromPitch('d')
    7
    >>> sc.getScaleDegreeFromPitch('d#', comparisonAttribute='name') is None
    True
    >>> sc.getScaleDegreeFromPitch('d#', comparisonAttribute='pitchClass')
    1
    >>> sc.getScaleDegreeFromPitch('e') is None
    True
    >>> sc.getScaleDegreeFromPitch('e', comparisonAttribute='step')
    1
    ```

    ```python
    >>> sc = scale.HarmonicMinorScale('a')
    >>> sc.getScaleDegreeFromPitch('c')
    3
    >>> sc.getScaleDegreeFromPitch('g#')
    7
    >>> sc.getScaleDegreeFromPitch('g') is None
    True
    ```

    ```python
    >>> cMaj = key.Key('C')
    >>> cMaj.getScaleDegreeFromPitch(pitch.Pitch('E-'),
    ...                              direction=scale.Direction.ASCENDING,
    ...                              comparisonAttribute='step')
    3
    ```

ConcreteScale.getTonic()[[source]](../_modules/music21/scale.html#ConcreteScale.getTonic)
:   Return the tonic.

    ```python
    >>> sc = scale.ConcreteScale(tonic='e-4')
    >>> sc.getTonic()
    <music21.pitch.Pitch E-4>
    ```

ConcreteScale.intervalBetweenDegrees(*degreeStart*, *degreeEnd*, *direction=Direction.ASCENDING*, *equateTermini=True*)[[source]](../_modules/music21/scale.html#ConcreteScale.intervalBetweenDegrees)
:   Given two degrees, provide the interval as an interval.Interval object.

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> sc.intervalBetweenDegrees(3, 7)
    <music21.interval.Interval P5>
    ```

ConcreteScale.isNext(*other*, *pitchOrigin*, *direction: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *stepSize=1*, *getNeighbor: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *comparisonAttribute='name'*)[[source]](../_modules/music21/scale.html#ConcreteScale.isNext)
:   Given another pitch, as well as an origin and a direction,
    determine if this other pitch is in the next in the scale.

    ```python
    >>> sc1 = scale.MajorScale('g')
    >>> sc1.isNext('d4', 'c4', scale.Direction.ASCENDING)
    True
    ```

ConcreteScale.match(*other*, *comparisonAttribute='name'*)[[source]](../_modules/music21/scale.html#ConcreteScale.match)
:   Given another object of the forms that extractPitchList can take,
    (e.g., a `Stream`, a [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"),
    a list of [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects),
    return a named dictionary of pitch lists with keys ‘matched’ and ‘notMatched’.

    ```python
    >>> sc1 = scale.MajorScale('g')
    >>> sc2 = scale.MajorScale('d')
    >>> sc3 = scale.MajorScale('a')
    >>> sc4 = scale.MajorScale('e')
    ```

    ```python
    >>> from pprint import pprint as pp
    >>> pp(sc1.match(sc2))
    {'matched': [<music21.pitch.Pitch D4>, <music21.pitch.Pitch E4>,
                 <music21.pitch.Pitch F#4>, <music21.pitch.Pitch G4>,
                 <music21.pitch.Pitch A4>, <music21.pitch.Pitch B4>],
    'notMatched': [<music21.pitch.Pitch C#5>]}
    ```

    ```python
    >>> pp(sc2.match(sc3))
    {'matched': [<music21.pitch.Pitch A4>, <music21.pitch.Pitch B4>,
                 <music21.pitch.Pitch C#5>, <music21.pitch.Pitch D5>,
                 <music21.pitch.Pitch E5>, <music21.pitch.Pitch F#5>],
    'notMatched': [<music21.pitch.Pitch G#5>]}
    ```

    ```python
    >>> pp(sc1.match(sc4))
    {'matched': [<music21.pitch.Pitch E4>, <music21.pitch.Pitch F#4>,
                 <music21.pitch.Pitch A4>, <music21.pitch.Pitch B4>],
     'notMatched': [<music21.pitch.Pitch G#4>,
                    <music21.pitch.Pitch C#5>,
                    <music21.pitch.Pitch D#5>]}
    ```

ConcreteScale.nextPitch(*pitchOrigin=None*, *direction: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = Direction.ASCENDING*, *stepSize=1*, *getNeighbor: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/scale.html#ConcreteScale.nextPitch)
:   Get the next pitch above (or below if direction is Direction.DESCENDING)
    a pitchOrigin or None. If the pitchOrigin is None, the tonic pitch is
    returned. This is useful when starting a chain of iterative calls.

    The direction attribute may be either ascending or descending.
    Default is ascending. Optionally, positive or negative integers
    may be provided as directional stepSize scalars.

    An optional stepSize argument can be used to set the number
    of scale steps that are stepped through. Thus, .nextPitch(stepSize=2)
    will give not the next pitch in the scale, but the next after this one.

    The getNeighbor will return a pitch from the scale
    if pitchOrigin is not in the scale. This value can be
    True, Direction.ASCENDING, or Direction.DESCENDING.

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> print(sc.nextPitch('e-5'))
    F5
    >>> print(sc.nextPitch('e-5', stepSize=2))
    G5
    >>> print(sc.nextPitch('e-6', stepSize=3))
    A-6
    ```

    This uses the getNeighbor attribute to
    find the next note above f#5 in the E-flat
    major scale:

    ```python
    >>> sc.nextPitch('f#5')
    <music21.pitch.Pitch G5>
    ```

    ```python
    >>> sc = scale.HarmonicMinorScale('g')
    >>> sc.nextPitch('g4', scale.Direction.DESCENDING)
    <music21.pitch.Pitch F#4>
    >>> sc.nextPitch('F#4', scale.Direction.DESCENDING)
    <music21.pitch.Pitch E-4>
    >>> sc.nextPitch('E-4', scale.Direction.DESCENDING)
    <music21.pitch.Pitch D4>
    >>> sc.nextPitch('E-4', scale.Direction.ASCENDING, 1)
    <music21.pitch.Pitch F#4>
    >>> sc.nextPitch('E-4', scale.Direction.ASCENDING, 2)
    <music21.pitch.Pitch G4>
    ```

ConcreteScale.pitchFromDegree(*degree: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *minPitch=None*, *maxPitch=None*, *direction: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *equateTermini: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/scale.html#ConcreteScale.pitchFromDegree)
:   Given a scale degree, return a deepcopy of the appropriate pitch.

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> sc.pitchFromDegree(2)
    <music21.pitch.Pitch F4>
    >>> sc.pitchFromDegree(7)
    <music21.pitch.Pitch D5>
    ```

ConcreteScale.pitchesFromScaleDegrees(*degreeTargets*, *minPitch=None*, *maxPitch=None*, *direction=Direction.ASCENDING*)[[source]](../_modules/music21/scale.html#ConcreteScale.pitchesFromScaleDegrees)
:   Given one or more scale degrees, return a list
    of all matches over the entire range.

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> sc.pitchesFromScaleDegrees([3, 7])
    [<music21.pitch.Pitch G4>, <music21.pitch.Pitch D5>]
    >>> [str(p) for p in sc.pitchesFromScaleDegrees([3, 7], 'c2', 'c6')]
    ['D2', 'G2', 'D3', 'G3', 'D4', 'G4', 'D5', 'G5']
    ```

    ```python
    >>> sc = scale.HarmonicMinorScale('a')
    >>> [str(p) for p in sc.pitchesFromScaleDegrees([3, 7], 'c2', 'c6')]
    ['C2', 'G#2', 'C3', 'G#3', 'C4', 'G#4', 'C5', 'G#5', 'C6']
    ```

ConcreteScale.romanNumeral(*degree*)[[source]](../_modules/music21/scale.html#ConcreteScale.romanNumeral)
:   Return a RomanNumeral object built on the specified scale degree.

    ```python
    >>> sc1 = scale.MajorScale('a-4')
    >>> h1 = sc1.romanNumeral(1)
    >>> h1.root()
    <music21.pitch.Pitch A-4>
    ```

    ```python
    >>> h5 = sc1.romanNumeral(5)
    >>> h5.root()
    <music21.pitch.Pitch E-5>
    >>> h5
    <music21.roman.RomanNumeral V in A- major>
    ```

ConcreteScale.show(*fmt=None*, *app=None*, *direction=Direction.ASCENDING*)[[source]](../_modules/music21/scale.html#ConcreteScale.show)
:   Show the scale in a format. Here, prepare scala format
    if requested.

ConcreteScale.solfeg(*pitchTarget=None*, *direction=Direction.ASCENDING*, *variant='music21'*, *chromatic=True*)[[source]](../_modules/music21/scale.html#ConcreteScale.solfeg)
:   Returns the chromatic solfeg (or diatonic if chromatic is False)
    for a given pitch in a given scale.

    The variant method lets one specify either the default music21
    or humdrum solfeg representation
    for altered notes.

    ```python
    >>> eflatMaj = key.Key('E-')
    >>> eflatMaj.solfeg(pitch.Pitch('G'))
    'mi'
    >>> eflatMaj.solfeg('A')
    'fi'
    >>> eflatMaj.solfeg('A', chromatic=False)
    'fa'
    >>> eflatMaj.solfeg(pitch.Pitch('G#'), variant='music21')  # default
    'mis'
    >>> eflatMaj.solfeg(pitch.Pitch('G#'), variant='humdrum')
    'my'
    ```

ConcreteScale.transpose(*value*, *\**, *inPlace=False*)[[source]](../_modules/music21/scale.html#ConcreteScale.transpose)
:   Transpose this Scale by the given interval

    Note: It does not make sense to transpose an abstract scale, since
    it is merely a collection of intervals. Thus,
    only concrete scales can be transposed.

    ```python
    >>> sc1 = scale.MajorScale('C')
    >>> sc2 = sc1.transpose('p5')
    >>> sc2
    <music21.scale.MajorScale G major>
    >>> sc3 = sc2.transpose('p5')
    >>> sc3
    <music21.scale.MajorScale D major>
    ```

    ```python
    >>> sc3.transpose('p5', inPlace=True)
    >>> sc3
    <music21.scale.MajorScale A major>
    ```

ConcreteScale.tune(*streamObj*, *minPitch=None*, *maxPitch=None*, *direction=None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/scale.html#ConcreteScale.tune)
:   Given a Stream object containing Pitches, match all pitch names
    and or pitch space values and replace the target pitch with
    copies of pitches stored in this scale.

    This is always applied recursively to all sub-Streams.

ConcreteScale.write(*fmt=None*, *fp=None*, *direction=Direction.ASCENDING*)[[source]](../_modules/music21/scale.html#ConcreteScale.write)
:   Write the scale in a format.
    Here, prepare scala format if requested.

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractScale

class music21.scale.AbstractScale(*\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractScale)
:   An abstract scale is specific scale formation, but does not have a
    defined pitch collection or pitch reference. For example, all Major
    scales can be represented by an AbstractScale; a ConcreteScale,
    however, is a specific Major Scale, such as G Major.

    These classes provide an interface to, and create and manipulate,
    the stored `IntervalNetwork`
    object. Thus, they are rarely created or manipulated directly by
    most users.

    The AbstractScale additionally stores an \_alteredDegrees dictionary.
    Subclasses can define altered nodes in AbstractScale that are passed
    to the `IntervalNetwork`.

    ### Equality

    Two abstract scales are the same if they have the same class and the
    same tonicDegree and octaveDuplicating attributes and the same intervalNetwork,
    and it satisfies all other music21 superclass attributes.

    ```python
    >>> as1 = scale.AbstractOctatonicScale()
    >>> as2 = scale.AbstractOctatonicScale()
    >>> as1 == as2
    True
    >>> as2.tonicDegree = 5
    >>> as1 == as2
    False
    ```

    ```python
    >>> as1 == scale.AbstractDiatonicScale()
    False
    ```

[`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale") bases

* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale") methods

AbstractScale.buildNetwork()[[source]](../_modules/music21/scale.html#AbstractScale.buildNetwork)
:   Calling the buildNetwork, with or without parameters,
    is main job of the AbstractScale class. This needs to be subclassed by a derived class

AbstractScale.buildNetworkFromPitches(*pitchList*)[[source]](../_modules/music21/scale.html#AbstractScale.buildNetworkFromPitches)
:   Builds the network (list of motions) for an abstract scale
    from a list of pitch.Pitch objects. If
    the concluding note (usually the “octave”) is not given,
    then it’ll be created automatically.

    Here we treat the augmented triad as a scale:

    ```python
    >>> p1 = pitch.Pitch('C4')
    >>> p2 = pitch.Pitch('E4')
    >>> p3 = pitch.Pitch('G#4')
    >>> abstractScale = scale.AbstractScale()
    >>> abstractScale.buildNetworkFromPitches([p1, p2, p3])
    >>> abstractScale.octaveDuplicating
    True
    >>> abstractScale._net
    <music21.scale.intervalNetwork.IntervalNetwork object at 0x...>
    ```

    Now see it return a new “scale” of the augmentedTriad on D5

    ```python
    >>> abstractScale._net.realizePitch('D5')
    [<music21.pitch.Pitch D5>, <music21.pitch.Pitch F#5>,
     <music21.pitch.Pitch A#5>, <music21.pitch.Pitch D6>]
    ```

    It is also possible to use implicit octaves:

    ```python
    >>> abstract_scale = scale.AbstractScale()
    >>> abstract_scale.buildNetworkFromPitches(['C', 'F'])
    >>> abstract_scale.octaveDuplicating
    True
    >>> abstract_scale._net.realizePitch('G')
    [<music21.pitch.Pitch G4>, <music21.pitch.Pitch C5>, <music21.pitch.Pitch G5>]
    ```

static AbstractScale.fixDefaultOctaveForPitchList(*pitchList*)[[source]](../_modules/music21/scale.html#AbstractScale.fixDefaultOctaveForPitchList)
:   Suppose you have a set of octaveless Pitches that you use to make a scale.

    Something like:

    ```python
    >>> pitchListStrs = 'a b c d e f g a'.split()
    >>> pitchList = [pitch.Pitch(p) for p in pitchListStrs]
    ```

    Here’s the problem, between pitchList[1] and pitchList[2] the .implicitOctave
    stays the same, so the .ps drops:

    ```python
    >>> (pitchList[1].implicitOctave, pitchList[2].implicitOctave)
    (4, 4)
    >>> (pitchList[1].ps, pitchList[2].ps)
    (71.0, 60.0)
    ```

    Hence this helper staticmethod that makes it so that for octaveless pitches ONLY, each
    one has a .ps above the previous:

    ```python
    >>> pl2 = scale.AbstractScale.fixDefaultOctaveForPitchList(pitchList)
    >>> (pl2[1].implicitOctave, pl2[2].implicitOctave, pl2[3].implicitOctave)
    (4, 5, 5)
    >>> (pl2[1].ps, pl2[2].ps)
    (71.0, 72.0)
    ```

    Note that the list is modified inPlace:

    ```python
    >>> pitchList is pl2
    True
    >>> pitchList[2] is pl2[2]
    True
    ```

AbstractScale.getDegreeMaxUnique()[[source]](../_modules/music21/scale.html#AbstractScale.getDegreeMaxUnique)
:   Return the maximum number of scale steps, or the number to use as a
    modulus.

AbstractScale.getIntervals(*stepOfPitch=None*, *minPitch=None*, *maxPitch=None*, *direction=Direction.ASCENDING*, *reverse=False*)[[source]](../_modules/music21/scale.html#AbstractScale.getIntervals)
:   Realize the abstract scale as a list of pitch
    objects, given a pitch object, the step of
    that pitch object, and a min and max pitch.

AbstractScale.getNewTonicPitch(*pitchReference*, *nodeName*, *direction=Direction.ASCENDING*, *minPitch=None*, *maxPitch=None*)[[source]](../_modules/music21/scale.html#AbstractScale.getNewTonicPitch)
:   Define a pitch target and a node.

AbstractScale.getPitchFromNodeDegree(*pitchReference*, *nodeName*, *nodeDegreeTarget*, *direction=Direction.ASCENDING*, *minPitch=None*, *maxPitch=None*, *equateTermini=True*)[[source]](../_modules/music21/scale.html#AbstractScale.getPitchFromNodeDegree)
:   Get a pitch for desired scale degree.

AbstractScale.getRealization(*pitchObj*, *stepOfPitch*, *minPitch=None*, *maxPitch=None*, *direction=Direction.ASCENDING*, *reverse=False*)[[source]](../_modules/music21/scale.html#AbstractScale.getRealization)
:   Realize the abstract scale as a list of pitch objects,
    given a pitch object, the step of that pitch object,
    and a min and max pitch.

AbstractScale.getRelativeNodeDegree(*pitchReference*, *nodeName*, *pitchTarget*, *comparisonAttribute='pitchClass'*, *direction=Direction.ASCENDING*)[[source]](../_modules/music21/scale.html#AbstractScale.getRelativeNodeDegree)
:   Expose functionality from
    `IntervalNetwork`, passing on the
    stored alteredDegrees dictionary.

AbstractScale.getScalaData(*direction=Direction.ASCENDING*)[[source]](../_modules/music21/scale.html#AbstractScale.getScalaData)
:   Get the interval sequence as a :class:~music21.scala.ScalaData object
    for a particular scale:

AbstractScale.nextPitch(*pitchReference*, *nodeName*, *pitchOrigin*, *direction: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *stepSize=1*, *getNeighbor: [Direction](moduleScaleIntervalNetwork.html#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/scale.html#AbstractScale.nextPitch)
:   Expose functionality from `IntervalNetwork`,
    passing on the stored alteredDegrees dictionary.

AbstractScale.realizePitchByDegree(*pitchReference*, *nodeId*, *nodeDegreeTargets*, *direction=Direction.ASCENDING*, *minPitch=None*, *maxPitch=None*)[[source]](../_modules/music21/scale.html#AbstractScale.realizePitchByDegree)
:   Given one or more scale degrees, return a list of
    all matches over the entire range.

    See `realizePitchByDegree()`.
    in intervalNetwork.IntervalNetwork.

    Create an abstract pentatonic scale:

    ```python
    >>> pitchList = ['C#4', 'D#4', 'F#4', 'G#4', 'A#4']
    >>> abstractScale = scale.AbstractScale()
    >>> abstractScale.buildNetworkFromPitches([pitch.Pitch(p) for p in pitchList])
    ```

AbstractScale.show(*fmt=None*, *app=None*, *direction=Direction.ASCENDING*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractScale.show)
:   Show the scale in a format. Here, prepare scala format if requested.

AbstractScale.write(*fmt=None*, *fp=None*, *direction=Direction.ASCENDING*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractScale.write)
:   Write the scale in a format. Here, prepare scala format if requested.

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractCyclicalScale

class music21.scale.AbstractCyclicalScale(*mode=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractCyclicalScale)
:   A scale of any size built with an interval list of any form.
    The resulting scale may be non octave repeating.

[`AbstractCyclicalScale`](#music21.scale.AbstractCyclicalScale "music21.scale.AbstractCyclicalScale") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractCyclicalScale`](#music21.scale.AbstractCyclicalScale "music21.scale.AbstractCyclicalScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractCyclicalScale`](#music21.scale.AbstractCyclicalScale "music21.scale.AbstractCyclicalScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractCyclicalScale`](#music21.scale.AbstractCyclicalScale "music21.scale.AbstractCyclicalScale") methods

AbstractCyclicalScale.buildNetwork(*mode*)[[source]](../_modules/music21/scale.html#AbstractCyclicalScale.buildNetwork)
:   Here, mode is the list of intervals.

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractCyclicalScale`](#music21.scale.AbstractCyclicalScale "music21.scale.AbstractCyclicalScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractDiatonicScale

class music21.scale.AbstractDiatonicScale(*mode: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractDiatonicScale)
:   An abstract representation of a Diatonic scale w/ or without mode.

    ```python
    >>> as1 = scale.AbstractDiatonicScale('major')
    >>> as1.type
    'Abstract diatonic'
    >>> as1.mode
    'major'
    >>> as1.octaveDuplicating
    True
    ```

    ### Equality

    AbstractDiatonicScales must satisfy all the characteristics of a
    general AbstractScale but also need to have equal dominantDegrees.

    ```python
    >>> as1 = scale.AbstractDiatonicScale('major')
    >>> as2 = scale.AbstractDiatonicScale('lydian')
    >>> as1 == as2
    False
    ```

    Note that their modes do not need to be the same.
    For instance for the case of major and Ionian which have
    the same networks:

    ```python
    >>> as3 = scale.AbstractDiatonicScale('ionian')
    >>> (as1.mode, as3.mode)
    ('major', 'ionian')
    >>> as1 == as3
    True
    ```

[`AbstractDiatonicScale`](#music21.scale.AbstractDiatonicScale "music21.scale.AbstractDiatonicScale") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractDiatonicScale`](#music21.scale.AbstractDiatonicScale "music21.scale.AbstractDiatonicScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractDiatonicScale`](#music21.scale.AbstractDiatonicScale "music21.scale.AbstractDiatonicScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractDiatonicScale`](#music21.scale.AbstractDiatonicScale "music21.scale.AbstractDiatonicScale") methods

AbstractDiatonicScale.buildNetwork(*mode=None*)[[source]](../_modules/music21/scale.html#AbstractDiatonicScale.buildNetwork)
:   Given subclass dependent parameters, build and assign the IntervalNetwork.

    ```python
    >>> sc = scale.AbstractDiatonicScale()
    >>> sc.buildNetwork('Lydian')  # N.B. case-insensitive name
    >>> [str(p) for p in sc.getRealization('f4', 1, 'f2', 'f6')]
    ['F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3',
     'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4',
     'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5',
     'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6']
    ```

    Unknown modes raise an exception:

    ```python
    >>> sc.buildNetwork('blues-like')
    Traceback (most recent call last):
    music21.scale.ScaleException: Cannot create a
        scale of the following mode: 'blues-like'
    ```

    * Changed in v6: case-insensitive modes

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractDiatonicScale`](#music21.scale.AbstractDiatonicScale "music21.scale.AbstractDiatonicScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractHarmonicMinorScale

class music21.scale.AbstractHarmonicMinorScale(*mode: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractHarmonicMinorScale)
:   A true bidirectional scale that with the augmented
    second to a leading tone.

    This is the only scale to use the “\_alteredDegrees” property.

    mode is not used

[`AbstractHarmonicMinorScale`](#music21.scale.AbstractHarmonicMinorScale "music21.scale.AbstractHarmonicMinorScale") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractHarmonicMinorScale`](#music21.scale.AbstractHarmonicMinorScale "music21.scale.AbstractHarmonicMinorScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractHarmonicMinorScale`](#music21.scale.AbstractHarmonicMinorScale "music21.scale.AbstractHarmonicMinorScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractHarmonicMinorScale`](#music21.scale.AbstractHarmonicMinorScale "music21.scale.AbstractHarmonicMinorScale") methods

AbstractHarmonicMinorScale.buildNetwork()[[source]](../_modules/music21/scale.html#AbstractHarmonicMinorScale.buildNetwork)
:   Calling the buildNetwork, with or without parameters,
    is main job of the AbstractScale class. This needs to be subclassed by a derived class

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractHarmonicMinorScale`](#music21.scale.AbstractHarmonicMinorScale "music21.scale.AbstractHarmonicMinorScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractMelodicMinorScale

class music21.scale.AbstractMelodicMinorScale(*mode: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractMelodicMinorScale)
:   A directional scale.

    mode is not used.

[`AbstractMelodicMinorScale`](#music21.scale.AbstractMelodicMinorScale "music21.scale.AbstractMelodicMinorScale") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractMelodicMinorScale`](#music21.scale.AbstractMelodicMinorScale "music21.scale.AbstractMelodicMinorScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractMelodicMinorScale`](#music21.scale.AbstractMelodicMinorScale "music21.scale.AbstractMelodicMinorScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractMelodicMinorScale`](#music21.scale.AbstractMelodicMinorScale "music21.scale.AbstractMelodicMinorScale") methods

AbstractMelodicMinorScale.buildNetwork()[[source]](../_modules/music21/scale.html#AbstractMelodicMinorScale.buildNetwork)
:   Calling the buildNetwork, with or without parameters,
    is main job of the AbstractScale class. This needs to be subclassed by a derived class

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractMelodicMinorScale`](#music21.scale.AbstractMelodicMinorScale "music21.scale.AbstractMelodicMinorScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractOctatonicScale

class music21.scale.AbstractOctatonicScale(*mode=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractOctatonicScale)
:   Abstract scale representing the two octatonic scales.

[`AbstractOctatonicScale`](#music21.scale.AbstractOctatonicScale "music21.scale.AbstractOctatonicScale") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractOctatonicScale`](#music21.scale.AbstractOctatonicScale "music21.scale.AbstractOctatonicScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractOctatonicScale`](#music21.scale.AbstractOctatonicScale "music21.scale.AbstractOctatonicScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractOctatonicScale`](#music21.scale.AbstractOctatonicScale "music21.scale.AbstractOctatonicScale") methods

AbstractOctatonicScale.buildNetwork(*mode=None*)[[source]](../_modules/music21/scale.html#AbstractOctatonicScale.buildNetwork)
:   Given subclass dependent parameters, build and assign the IntervalNetwork.

    ```python
    >>> sc = scale.AbstractDiatonicScale()
    >>> sc.buildNetwork('lydian')
    >>> [str(p) for p in sc.getRealization('f4', 1, 'f2', 'f6')]
    ['F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3',
     'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4',
     'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5',
     'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6']
    ```

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractOctatonicScale`](#music21.scale.AbstractOctatonicScale "music21.scale.AbstractOctatonicScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractOctaveRepeatingScale

class music21.scale.AbstractOctaveRepeatingScale(*mode=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractOctaveRepeatingScale)
:   A scale of any size built with an interval list
    that assumes octave completion. An additional
    interval to complete the octave will be added
    to the provided intervals. This does not guarantee
    that the octave will be repeated in one octave,
    only the next octave above the last interval will
    be provided.

[`AbstractOctaveRepeatingScale`](#music21.scale.AbstractOctaveRepeatingScale "music21.scale.AbstractOctaveRepeatingScale") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractOctaveRepeatingScale`](#music21.scale.AbstractOctaveRepeatingScale "music21.scale.AbstractOctaveRepeatingScale") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractOctaveRepeatingScale`](#music21.scale.AbstractOctaveRepeatingScale "music21.scale.AbstractOctaveRepeatingScale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractOctaveRepeatingScale`](#music21.scale.AbstractOctaveRepeatingScale "music21.scale.AbstractOctaveRepeatingScale") methods

AbstractOctaveRepeatingScale.buildNetwork(*mode*)[[source]](../_modules/music21/scale.html#AbstractOctaveRepeatingScale.buildNetwork)
:   Here, mode is the list of intervals.

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractOctaveRepeatingScale`](#music21.scale.AbstractOctaveRepeatingScale "music21.scale.AbstractOctaveRepeatingScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractRagAsawari

class music21.scale.AbstractRagAsawari(*\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractRagAsawari)
:   A pseudo raga-scale.

[`AbstractRagAsawari`](#music21.scale.AbstractRagAsawari "music21.scale.AbstractRagAsawari") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractRagAsawari`](#music21.scale.AbstractRagAsawari "music21.scale.AbstractRagAsawari") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractRagAsawari`](#music21.scale.AbstractRagAsawari "music21.scale.AbstractRagAsawari") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractRagAsawari`](#music21.scale.AbstractRagAsawari "music21.scale.AbstractRagAsawari") methods

AbstractRagAsawari.buildNetwork()[[source]](../_modules/music21/scale.html#AbstractRagAsawari.buildNetwork)
:   Calling the buildNetwork, with or without parameters,
    is main job of the AbstractScale class. This needs to be subclassed by a derived class

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractRagAsawari`](#music21.scale.AbstractRagAsawari "music21.scale.AbstractRagAsawari") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractRagMarwa

class music21.scale.AbstractRagMarwa(*\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractRagMarwa)
:   A pseudo raga-scale.

[`AbstractRagMarwa`](#music21.scale.AbstractRagMarwa "music21.scale.AbstractRagMarwa") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractRagMarwa`](#music21.scale.AbstractRagMarwa "music21.scale.AbstractRagMarwa") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractRagMarwa`](#music21.scale.AbstractRagMarwa "music21.scale.AbstractRagMarwa") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractRagMarwa`](#music21.scale.AbstractRagMarwa "music21.scale.AbstractRagMarwa") methods

AbstractRagMarwa.buildNetwork()[[source]](../_modules/music21/scale.html#AbstractRagMarwa.buildNetwork)
:   Calling the buildNetwork, with or without parameters,
    is main job of the AbstractScale class. This needs to be subclassed by a derived class

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractRagMarwa`](#music21.scale.AbstractRagMarwa "music21.scale.AbstractRagMarwa") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AbstractWeightedHexatonicBlues

class music21.scale.AbstractWeightedHexatonicBlues(*\*\*keywords*)[[source]](../_modules/music21/scale.html#AbstractWeightedHexatonicBlues)
:   A dynamic, probabilistic mixture of minor pentatonic and a hexatonic blues scale

[`AbstractWeightedHexatonicBlues`](#music21.scale.AbstractWeightedHexatonicBlues "music21.scale.AbstractWeightedHexatonicBlues") bases

* [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AbstractWeightedHexatonicBlues`](#music21.scale.AbstractWeightedHexatonicBlues "music21.scale.AbstractWeightedHexatonicBlues") read-only properties

Read-only properties inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`isConcrete`](#music21.scale.Scale.isConcrete "music21.scale.Scale.isConcrete") | * [`name`](#music21.scale.Scale.name "music21.scale.Scale.name") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AbstractWeightedHexatonicBlues`](#music21.scale.AbstractWeightedHexatonicBlues "music21.scale.AbstractWeightedHexatonicBlues") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AbstractWeightedHexatonicBlues`](#music21.scale.AbstractWeightedHexatonicBlues "music21.scale.AbstractWeightedHexatonicBlues") methods

AbstractWeightedHexatonicBlues.buildNetwork()[[source]](../_modules/music21/scale.html#AbstractWeightedHexatonicBlues.buildNetwork)
:   Calling the buildNetwork, with or without parameters,
    is main job of the AbstractScale class. This needs to be subclassed by a derived class

Methods inherited from [`AbstractScale`](#music21.scale.AbstractScale "music21.scale.AbstractScale"):

|  |  |  |
| --- | --- | --- |
| * [`buildNetworkFromPitches()`](#music21.scale.AbstractScale.buildNetworkFromPitches "music21.scale.AbstractScale.buildNetworkFromPitches") * [`fixDefaultOctaveForPitchList()`](#music21.scale.AbstractScale.fixDefaultOctaveForPitchList "music21.scale.AbstractScale.fixDefaultOctaveForPitchList") * [`getDegreeMaxUnique()`](#music21.scale.AbstractScale.getDegreeMaxUnique "music21.scale.AbstractScale.getDegreeMaxUnique") * [`getIntervals()`](#music21.scale.AbstractScale.getIntervals "music21.scale.AbstractScale.getIntervals") * [`getNewTonicPitch()`](#music21.scale.AbstractScale.getNewTonicPitch "music21.scale.AbstractScale.getNewTonicPitch") | * [`getPitchFromNodeDegree()`](#music21.scale.AbstractScale.getPitchFromNodeDegree "music21.scale.AbstractScale.getPitchFromNodeDegree") * [`getRealization()`](#music21.scale.AbstractScale.getRealization "music21.scale.AbstractScale.getRealization") * [`getRelativeNodeDegree()`](#music21.scale.AbstractScale.getRelativeNodeDegree "music21.scale.AbstractScale.getRelativeNodeDegree") * [`getScalaData()`](#music21.scale.AbstractScale.getScalaData "music21.scale.AbstractScale.getScalaData") | * [`nextPitch()`](#music21.scale.AbstractScale.nextPitch "music21.scale.AbstractScale.nextPitch") * [`realizePitchByDegree()`](#music21.scale.AbstractScale.realizePitchByDegree "music21.scale.AbstractScale.realizePitchByDegree") * [`show()`](#music21.scale.AbstractScale.show "music21.scale.AbstractScale.show") * [`write()`](#music21.scale.AbstractScale.write "music21.scale.AbstractScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`AbstractWeightedHexatonicBlues`](#music21.scale.AbstractWeightedHexatonicBlues "music21.scale.AbstractWeightedHexatonicBlues") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ChromaticScale

class music21.scale.ChromaticScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#ChromaticScale)
:   A concrete cyclical scale, based on a cycle of half steps.

    ```python
    >>> sc = scale.ChromaticScale('g2')
    >>> [str(p) for p in sc.pitches]
    ['G2', 'A-2', 'A2', 'B-2', 'B2', 'C3', 'C#3', 'D3', 'E-3', 'E3', 'F3', 'F#3', 'G3']
    >>> [str(p) for p in sc.getPitches('g2', 'g6')]
    ['G2', 'A-2', ..., 'F#3', 'G3', 'A-3', ..., 'F#4', 'G4', 'A-4', ..., 'G5', ..., 'F#6', 'G6']
    >>> sc.abstract.getDegreeMaxUnique()
    12
    >>> sc.pitchFromDegree(1)
    <music21.pitch.Pitch G2>
    >>> sc.pitchFromDegree(2)
    <music21.pitch.Pitch A-2>
    >>> sc.pitchFromDegree(3)
    <music21.pitch.Pitch A2>
    >>> sc.pitchFromDegree(8)
    <music21.pitch.Pitch D3>
    >>> sc.pitchFromDegree(12)
    <music21.pitch.Pitch F#3>
    >>> sc.getScaleDegreeFromPitch('g2', comparisonAttribute='pitchClass')
    1
    >>> sc.getScaleDegreeFromPitch('F#6', comparisonAttribute='pitchClass')
    12
    ```

[`ChromaticScale`](#music21.scale.ChromaticScale "music21.scale.ChromaticScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ChromaticScale`](#music21.scale.ChromaticScale "music21.scale.ChromaticScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ChromaticScale`](#music21.scale.ChromaticScale "music21.scale.ChromaticScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ChromaticScale`](#music21.scale.ChromaticScale "music21.scale.ChromaticScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`ChromaticScale`](#music21.scale.ChromaticScale "music21.scale.ChromaticScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## CyclicalScale

class music21.scale.CyclicalScale(*tonic: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *intervalList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#CyclicalScale)
:   A concrete cyclical scale, based on a cycle of intervals.

    ```python
    >>> sc = scale.CyclicalScale('c4', ['P5'])  # can give one list
    >>> sc.pitches
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch G4>]
    >>> [str(p) for p in sc.getPitches('g2', 'g6')]
    ['B-2', 'F3', 'C4', 'G4', 'D5', 'A5', 'E6']
    >>> sc.getScaleDegreeFromPitch('g4')  # as single interval cycle, all are 1
    1
    >>> sc.getScaleDegreeFromPitch('b-2', direction=scale.Direction.BI)
    1
    ```

    No intervalList defaults to a single minor second:

    ```python
    >>> sc2 = scale.CyclicalScale()
    >>> sc2.pitches
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch D-4>]
    ```

[`CyclicalScale`](#music21.scale.CyclicalScale "music21.scale.CyclicalScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`CyclicalScale`](#music21.scale.CyclicalScale "music21.scale.CyclicalScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`CyclicalScale`](#music21.scale.CyclicalScale "music21.scale.CyclicalScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`CyclicalScale`](#music21.scale.CyclicalScale "music21.scale.CyclicalScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`CyclicalScale`](#music21.scale.CyclicalScale "music21.scale.CyclicalScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DiatonicScale

class music21.scale.DiatonicScale(*tonic: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#DiatonicScale)
:   A concrete diatonic scale. Each DiatonicScale
    has one instance of a [`AbstractDiatonicScale`](#music21.scale.AbstractDiatonicScale "music21.scale.AbstractDiatonicScale").

[`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale") methods

DiatonicScale.getDominant()[[source]](../_modules/music21/scale.html#DiatonicScale.getDominant)
:   Return the dominant.

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> sc.getDominant()
    <music21.pitch.Pitch B-4>
    >>> sc = scale.MajorScale('F#')
    >>> sc.getDominant()
    <music21.pitch.Pitch C#5>
    ```

DiatonicScale.getLeadingTone()[[source]](../_modules/music21/scale.html#DiatonicScale.getLeadingTone)
:   Return the leading tone.

    ```python
    >>> sc = scale.MinorScale('c')
    >>> sc.getLeadingTone()
    <music21.pitch.Pitch B4>
    ```

    Note that the leading tone isn’t necessarily
    the same as the 7th scale degree in minor:

    ```python
    >>> sc.pitchFromDegree(7)
    <music21.pitch.Pitch B-4>
    ```

DiatonicScale.getParallelMajor()[[source]](../_modules/music21/scale.html#DiatonicScale.getParallelMajor)
:   Return a concrete relative major scale

    ```python
    >>> sc1 = scale.MinorScale(pitch.Pitch('g'))
    >>> [str(p) for p in sc1.pitches]
    ['G4', 'A4', 'B-4', 'C5', 'D5', 'E-5', 'F5', 'G5']
    ```

    ```python
    >>> sc2 = sc1.getParallelMajor()
    >>> [str(p) for p in sc2.pitches]
    ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5']
    ```

DiatonicScale.getParallelMinor()[[source]](../_modules/music21/scale.html#DiatonicScale.getParallelMinor)
:   Return a parallel minor scale based on this
    concrete scale.

    ```python
    >>> sc1 = scale.MajorScale(pitch.Pitch('a'))
    >>> [str(p) for p in sc1.pitches]
    ['A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G#5', 'A5']
    >>> sc2 = sc1.getParallelMinor()
    >>> [str(p) for p in sc2.pitches]
    ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
    ```

    Running getParallelMinor() again doesn’t change anything

    ```python
    >>> sc3 = sc2.getParallelMinor()
    >>> [str(p) for p in sc3.pitches]
    ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5']
    ```

DiatonicScale.getRelativeMajor()[[source]](../_modules/music21/scale.html#DiatonicScale.getRelativeMajor)
:   Return a concrete relative major scale

    ```python
    >>> sc1 = scale.MinorScale(pitch.Pitch('g'))
    >>> [str(p) for p in sc1.pitches]
    ['G4', 'A4', 'B-4', 'C5', 'D5', 'E-5', 'F5', 'G5']
    ```

    ```python
    >>> sc2 = sc1.getRelativeMajor()
    >>> [str(p) for p in sc2.pitches]
    ['B-4', 'C5', 'D5', 'E-5', 'F5', 'G5', 'A5', 'B-5']
    ```

    Though it’s unlikely you would want to do it,
    getRelativeMajor works on other diatonic scales than
    just Major and Minor.

    ```python
    >>> sc2 = scale.DorianScale('d')
    >>> [str(p) for p in sc2.pitches]
    ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5']
    ```

    ```python
    >>> [str(p) for p in sc2.getRelativeMajor().pitches]
    ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
    ```

DiatonicScale.getRelativeMinor()[[source]](../_modules/music21/scale.html#DiatonicScale.getRelativeMinor)
:   Return a relative minor scale based on this concrete scale.

    ```python
    >>> sc1 = scale.MajorScale(pitch.Pitch('a'))
    >>> [str(p) for p in sc1.pitches]
    ['A4', 'B4', 'C#5', 'D5', 'E5', 'F#5', 'G#5', 'A5']
    >>> sc2 = sc1.getRelativeMinor()
    >>> [str(p) for p in sc2.pitches]
    ['F#5', 'G#5', 'A5', 'B5', 'C#6', 'D6', 'E6', 'F#6']
    ```

DiatonicScale.getTonic()[[source]](../_modules/music21/scale.html#DiatonicScale.getTonic)
:   Return the tonic of the diatonic scale.

    ```python
    >>> sc = scale.MajorScale('e-')
    >>> sc.getTonic()
    <music21.pitch.Pitch E-4>
    >>> sc = scale.MajorScale('F#')
    >>> sc.getTonic()
    <music21.pitch.Pitch F#4>
    ```

    If no tonic has been defined, it will return an Exception.
    (same is true for getDominant, getLeadingTone, etc.)

    ```python
    >>> sc = scale.DiatonicScale()
    >>> sc.getTonic()
    Traceback (most recent call last):
    music21.scale.intervalNetwork.IntervalNetworkException: pitchReference cannot be None
    ```

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DorianScale

class music21.scale.DorianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#DorianScale)
:   A scale built on the Dorian (D-D white-key) mode.

    ```python
    >>> sc = scale.DorianScale(pitch.Pitch('d'))
    >>> [str(p) for p in sc.pitches]
    ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5']
    ```

[`DorianScale`](#music21.scale.DorianScale "music21.scale.DorianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DorianScale`](#music21.scale.DorianScale "music21.scale.DorianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DorianScale`](#music21.scale.DorianScale "music21.scale.DorianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DorianScale`](#music21.scale.DorianScale "music21.scale.DorianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`DorianScale`](#music21.scale.DorianScale "music21.scale.DorianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HarmonicMinorScale

class music21.scale.HarmonicMinorScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HarmonicMinorScale)
:   The harmonic minor collection, realized as a scale.

    (The usage of this collection as a scale, is quite ahistorical for
    Western European classical music, but it is common in other parts of the
    world, but where the term “HarmonicMinor” would not be appropriate).

    ```python
    >>> sc = scale.HarmonicMinorScale('e4')
    >>> [str(p) for p in sc.pitches]
    ['E4', 'F#4', 'G4', 'A4', 'B4', 'C5', 'D#5', 'E5']
    >>> sc.getTonic()
    <music21.pitch.Pitch E4>
    >>> sc.getDominant()
    <music21.pitch.Pitch B4>
    >>> sc.pitchFromDegree(1)  # scale degree 1 is treated as lowest
    <music21.pitch.Pitch E4>
    ```

    ```python
    >>> sc = scale.HarmonicMinorScale()
    >>> sc
    <music21.scale.HarmonicMinorScale Abstract harmonic minor>
    >>> sc.deriveRanked(['C', 'E', 'G'], comparisonAttribute='name')
    [(3, <music21.scale.HarmonicMinorScale F harmonic minor>),
     (3, <music21.scale.HarmonicMinorScale E harmonic minor>),
     (2, <music21.scale.HarmonicMinorScale B harmonic minor>),
     (2, <music21.scale.HarmonicMinorScale A harmonic minor>)]
    ```

    Note that G and D are also equally good as B and A, but the system arbitrarily
    chooses among ties.

[`HarmonicMinorScale`](#music21.scale.HarmonicMinorScale "music21.scale.HarmonicMinorScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HarmonicMinorScale`](#music21.scale.HarmonicMinorScale "music21.scale.HarmonicMinorScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HarmonicMinorScale`](#music21.scale.HarmonicMinorScale "music21.scale.HarmonicMinorScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HarmonicMinorScale`](#music21.scale.HarmonicMinorScale "music21.scale.HarmonicMinorScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HarmonicMinorScale`](#music21.scale.HarmonicMinorScale "music21.scale.HarmonicMinorScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HypoaeolianScale

class music21.scale.HypoaeolianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HypoaeolianScale)
:   A hypoaeolian scale

    ```python
    >>> sc = scale.HypoaeolianScale(pitch.Pitch('a'))
    >>> [str(p) for p in sc.pitches]
    ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
    ```

    ```python
    >>> sc = scale.HypoaeolianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['G3', 'A-3', 'B-3', 'C4', 'D4', 'E-4', 'F4', 'G4']
    ```

[`HypoaeolianScale`](#music21.scale.HypoaeolianScale "music21.scale.HypoaeolianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HypoaeolianScale`](#music21.scale.HypoaeolianScale "music21.scale.HypoaeolianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HypoaeolianScale`](#music21.scale.HypoaeolianScale "music21.scale.HypoaeolianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HypoaeolianScale`](#music21.scale.HypoaeolianScale "music21.scale.HypoaeolianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HypoaeolianScale`](#music21.scale.HypoaeolianScale "music21.scale.HypoaeolianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HypodorianScale

class music21.scale.HypodorianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HypodorianScale)
:   A hypodorian scale: a dorian scale where the given pitch is scale degree 4.

    ```python
    >>> sc = scale.HypodorianScale(pitch.Pitch('d'))
    >>> [str(p) for p in sc.pitches]
    ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4']
    >>> sc = scale.HypodorianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['G3', 'A3', 'B-3', 'C4', 'D4', 'E-4', 'F4', 'G4']
    ```

[`HypodorianScale`](#music21.scale.HypodorianScale "music21.scale.HypodorianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HypodorianScale`](#music21.scale.HypodorianScale "music21.scale.HypodorianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HypodorianScale`](#music21.scale.HypodorianScale "music21.scale.HypodorianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HypodorianScale`](#music21.scale.HypodorianScale "music21.scale.HypodorianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HypodorianScale`](#music21.scale.HypodorianScale "music21.scale.HypodorianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HypolocrianScale

class music21.scale.HypolocrianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HypolocrianScale)
:   A hypolocrian scale

    ```python
    >>> sc = scale.HypolocrianScale(pitch.Pitch('b'))
    >>> [str(p) for p in sc.pitches]
    ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    ```

    ```python
    >>> sc = scale.HypolocrianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['G-3', 'A-3', 'B-3', 'C4', 'D-4', 'E-4', 'F4', 'G-4']
    ```

[`HypolocrianScale`](#music21.scale.HypolocrianScale "music21.scale.HypolocrianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HypolocrianScale`](#music21.scale.HypolocrianScale "music21.scale.HypolocrianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HypolocrianScale`](#music21.scale.HypolocrianScale "music21.scale.HypolocrianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HypolocrianScale`](#music21.scale.HypolocrianScale "music21.scale.HypolocrianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HypolocrianScale`](#music21.scale.HypolocrianScale "music21.scale.HypolocrianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HypolydianScale

class music21.scale.HypolydianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HypolydianScale)
:   A hypolydian scale

    ```python
    >>> sc = scale.HypolydianScale(pitch.Pitch('f'))
    >>> [str(p) for p in sc.pitches]
    ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    >>> sc = scale.HypolydianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4', 'G4']
    ```

[`HypolydianScale`](#music21.scale.HypolydianScale "music21.scale.HypolydianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HypolydianScale`](#music21.scale.HypolydianScale "music21.scale.HypolydianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HypolydianScale`](#music21.scale.HypolydianScale "music21.scale.HypolydianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HypolydianScale`](#music21.scale.HypolydianScale "music21.scale.HypolydianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HypolydianScale`](#music21.scale.HypolydianScale "music21.scale.HypolydianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HypomixolydianScale

class music21.scale.HypomixolydianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HypomixolydianScale)
:   A hypomixolydian scale

    ```python
    >>> sc = scale.HypomixolydianScale(pitch.Pitch('g'))
    >>> [str(p) for p in sc.pitches]
    ['D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5']
    >>> sc = scale.HypomixolydianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['G3', 'A3', 'B-3', 'C4', 'D4', 'E4', 'F4', 'G4']
    ```

[`HypomixolydianScale`](#music21.scale.HypomixolydianScale "music21.scale.HypomixolydianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HypomixolydianScale`](#music21.scale.HypomixolydianScale "music21.scale.HypomixolydianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HypomixolydianScale`](#music21.scale.HypomixolydianScale "music21.scale.HypomixolydianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HypomixolydianScale`](#music21.scale.HypomixolydianScale "music21.scale.HypomixolydianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HypomixolydianScale`](#music21.scale.HypomixolydianScale "music21.scale.HypomixolydianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HypophrygianScale

class music21.scale.HypophrygianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#HypophrygianScale)
:   A hypophrygian scale

    ```python
    >>> sc = scale.HypophrygianScale(pitch.Pitch('e'))
    >>> sc.abstract.octaveDuplicating
    True
    >>> [str(p) for p in sc.pitches]
    ['B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
    >>> sc.getTonic()
    <music21.pitch.Pitch E4>
    >>> sc.getDominant()
    <music21.pitch.Pitch A4>
    >>> sc.pitchFromDegree(1)  # scale degree 1 is treated as lowest
    <music21.pitch.Pitch B3>
    ```

[`HypophrygianScale`](#music21.scale.HypophrygianScale "music21.scale.HypophrygianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HypophrygianScale`](#music21.scale.HypophrygianScale "music21.scale.HypophrygianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HypophrygianScale`](#music21.scale.HypophrygianScale "music21.scale.HypophrygianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HypophrygianScale`](#music21.scale.HypophrygianScale "music21.scale.HypophrygianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HypophrygianScale`](#music21.scale.HypophrygianScale "music21.scale.HypophrygianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## LocrianScale

class music21.scale.LocrianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#LocrianScale)
:   A so-called “locrian” scale

    ```python
    >>> sc = scale.LocrianScale(pitch.Pitch('b'))
    >>> [str(p) for p in sc.pitches]
    ['B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5']
    ```

    ```python
    >>> sc = scale.LocrianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['C4', 'D-4', 'E-4', 'F4', 'G-4', 'A-4', 'B-4', 'C5']
    ```

[`LocrianScale`](#music21.scale.LocrianScale "music21.scale.LocrianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LocrianScale`](#music21.scale.LocrianScale "music21.scale.LocrianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LocrianScale`](#music21.scale.LocrianScale "music21.scale.LocrianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`LocrianScale`](#music21.scale.LocrianScale "music21.scale.LocrianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`LocrianScale`](#music21.scale.LocrianScale "music21.scale.LocrianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## LydianScale

class music21.scale.LydianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#LydianScale)
:   A Lydian scale (that is, the F-F white-key scale; does not have the
    probability of B- emerging as in a historical Lydian collection).

    ```python
    >>> sc = scale.LydianScale(pitch.Pitch('f'))
    >>> [str(p) for p in sc.pitches]
    ['F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5']
    ```

    ```python
    >>> sc = scale.LydianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['C4', 'D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C5']
    ```

[`LydianScale`](#music21.scale.LydianScale "music21.scale.LydianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LydianScale`](#music21.scale.LydianScale "music21.scale.LydianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LydianScale`](#music21.scale.LydianScale "music21.scale.LydianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`LydianScale`](#music21.scale.LydianScale "music21.scale.LydianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`LydianScale`](#music21.scale.LydianScale "music21.scale.LydianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MajorScale

class music21.scale.MajorScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#MajorScale)
:   A Major Scale

    ```python
    >>> sc = scale.MajorScale(pitch.Pitch('d'))
    >>> sc.pitchFromDegree(7).name
    'C#'
    ```

[`MajorScale`](#music21.scale.MajorScale "music21.scale.MajorScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MajorScale`](#music21.scale.MajorScale "music21.scale.MajorScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MajorScale`](#music21.scale.MajorScale "music21.scale.MajorScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MajorScale`](#music21.scale.MajorScale "music21.scale.MajorScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`MajorScale`](#music21.scale.MajorScale "music21.scale.MajorScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MelodicMinorScale

class music21.scale.MelodicMinorScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#MelodicMinorScale)
:   A melodic minor scale, which is not the same ascending or descending

    ```python
    >>> sc = scale.MelodicMinorScale('e4')
    ```

[`MelodicMinorScale`](#music21.scale.MelodicMinorScale "music21.scale.MelodicMinorScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MelodicMinorScale`](#music21.scale.MelodicMinorScale "music21.scale.MelodicMinorScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MelodicMinorScale`](#music21.scale.MelodicMinorScale "music21.scale.MelodicMinorScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MelodicMinorScale`](#music21.scale.MelodicMinorScale "music21.scale.MelodicMinorScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`MelodicMinorScale`](#music21.scale.MelodicMinorScale "music21.scale.MelodicMinorScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MinorScale

class music21.scale.MinorScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#MinorScale)
:   A natural minor scale, or the Aeolian mode.

    ```python
    >>> sc = scale.MinorScale(pitch.Pitch('g'))
    >>> [str(p) for p in sc.pitches]
    ['G4', 'A4', 'B-4', 'C5', 'D5', 'E-5', 'F5', 'G5']
    ```

[`MinorScale`](#music21.scale.MinorScale "music21.scale.MinorScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MinorScale`](#music21.scale.MinorScale "music21.scale.MinorScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MinorScale`](#music21.scale.MinorScale "music21.scale.MinorScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MinorScale`](#music21.scale.MinorScale "music21.scale.MinorScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`MinorScale`](#music21.scale.MinorScale "music21.scale.MinorScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MixolydianScale

class music21.scale.MixolydianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#MixolydianScale)
:   A mixolydian scale

    ```python
    >>> sc = scale.MixolydianScale(pitch.Pitch('g'))
    >>> [str(p) for p in sc.pitches]
    ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']
    ```

    ```python
    >>> sc = scale.MixolydianScale(pitch.Pitch('c'))
    >>> [str(p) for p in sc.pitches]
    ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B-4', 'C5']
    ```

[`MixolydianScale`](#music21.scale.MixolydianScale "music21.scale.MixolydianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MixolydianScale`](#music21.scale.MixolydianScale "music21.scale.MixolydianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MixolydianScale`](#music21.scale.MixolydianScale "music21.scale.MixolydianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MixolydianScale`](#music21.scale.MixolydianScale "music21.scale.MixolydianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`MixolydianScale`](#music21.scale.MixolydianScale "music21.scale.MixolydianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## OctatonicScale

class music21.scale.OctatonicScale(*tonic=None*, *mode=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#OctatonicScale)
:   A concrete Octatonic scale in one of two modes

[`OctatonicScale`](#music21.scale.OctatonicScale "music21.scale.OctatonicScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OctatonicScale`](#music21.scale.OctatonicScale "music21.scale.OctatonicScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OctatonicScale`](#music21.scale.OctatonicScale "music21.scale.OctatonicScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`OctatonicScale`](#music21.scale.OctatonicScale "music21.scale.OctatonicScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`OctatonicScale`](#music21.scale.OctatonicScale "music21.scale.OctatonicScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## OctaveRepeatingScale

class music21.scale.OctaveRepeatingScale(*tonic=None*, *intervalList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#OctaveRepeatingScale)
:   A concrete cyclical scale, based on a cycle of intervals.

    ```python
    >>> sc = scale.OctaveRepeatingScale('c4', ['m3', 'M3'])
    >>> sc.pitches
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch E-4>,
     <music21.pitch.Pitch G4>, <music21.pitch.Pitch C5>]
    >>> [str(p) for p in sc.getPitches('g2', 'g6')]
    ['G2', 'C3', 'E-3', 'G3', 'C4', 'E-4', 'G4', 'C5', 'E-5', 'G5', 'C6', 'E-6', 'G6']
    >>> sc.getScaleDegreeFromPitch('c4')
    1
    >>> sc.getScaleDegreeFromPitch('e-')
    2
    ```

    No intervalList defaults to a single minor second:

    ```python
    >>> sc2 = scale.OctaveRepeatingScale()
    >>> sc2.pitches
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch D-4>, <music21.pitch.Pitch C5>]
    ```

[`OctaveRepeatingScale`](#music21.scale.OctaveRepeatingScale "music21.scale.OctaveRepeatingScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OctaveRepeatingScale`](#music21.scale.OctaveRepeatingScale "music21.scale.OctaveRepeatingScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OctaveRepeatingScale`](#music21.scale.OctaveRepeatingScale "music21.scale.OctaveRepeatingScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`OctaveRepeatingScale`](#music21.scale.OctaveRepeatingScale "music21.scale.OctaveRepeatingScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`OctaveRepeatingScale`](#music21.scale.OctaveRepeatingScale "music21.scale.OctaveRepeatingScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PhrygianScale

class music21.scale.PhrygianScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#PhrygianScale)
:   A Phrygian scale (E-E white key)

    ```python
    >>> sc = scale.PhrygianScale(pitch.Pitch('e'))
    >>> [str(p) for p in sc.pitches]
    ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5']
    ```

[`PhrygianScale`](#music21.scale.PhrygianScale "music21.scale.PhrygianScale") bases

* [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale")
* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PhrygianScale`](#music21.scale.PhrygianScale "music21.scale.PhrygianScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PhrygianScale`](#music21.scale.PhrygianScale "music21.scale.PhrygianScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PhrygianScale`](#music21.scale.PhrygianScale "music21.scale.PhrygianScale") methods

Methods inherited from [`DiatonicScale`](#music21.scale.DiatonicScale "music21.scale.DiatonicScale"):

|  |  |  |
| --- | --- | --- |
| * [`getDominant()`](#music21.scale.DiatonicScale.getDominant "music21.scale.DiatonicScale.getDominant") * [`getLeadingTone()`](#music21.scale.DiatonicScale.getLeadingTone "music21.scale.DiatonicScale.getLeadingTone") * [`getParallelMajor()`](#music21.scale.DiatonicScale.getParallelMajor "music21.scale.DiatonicScale.getParallelMajor") | * [`getParallelMinor()`](#music21.scale.DiatonicScale.getParallelMinor "music21.scale.DiatonicScale.getParallelMinor") * [`getRelativeMajor()`](#music21.scale.DiatonicScale.getRelativeMajor "music21.scale.DiatonicScale.getRelativeMajor") | * [`getRelativeMinor()`](#music21.scale.DiatonicScale.getRelativeMinor "music21.scale.DiatonicScale.getRelativeMinor") * [`getTonic()`](#music21.scale.DiatonicScale.getTonic "music21.scale.DiatonicScale.getTonic") |

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") | * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`PhrygianScale`](#music21.scale.PhrygianScale "music21.scale.PhrygianScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RagAsawari

class music21.scale.RagAsawari(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#RagAsawari)
:   A concrete pseudo-raga scale.

    ```python
    >>> sc = scale.RagAsawari('c2')
    >>> [str(p) for p in sc.pitches]
    ['C2', 'D2', 'F2', 'G2', 'A-2', 'C3']
    >>> [str(p) for p in sc.getPitches(direction=scale.Direction.DESCENDING)]
    ['C3', 'B-2', 'A-2', 'G2', 'F2', 'E-2', 'D2', 'C2']
    ```

[`RagAsawari`](#music21.scale.RagAsawari "music21.scale.RagAsawari") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RagAsawari`](#music21.scale.RagAsawari "music21.scale.RagAsawari") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RagAsawari`](#music21.scale.RagAsawari "music21.scale.RagAsawari") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RagAsawari`](#music21.scale.RagAsawari "music21.scale.RagAsawari") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`RagAsawari`](#music21.scale.RagAsawari "music21.scale.RagAsawari") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RagMarwa

class music21.scale.RagMarwa(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#RagMarwa)
:   A concrete pseudo-raga scale.

    ```python
    >>> sc = scale.RagMarwa('c2')
    ```

    this gets a pitch beyond the terminus b/c of descending form max

    ```python
    >>> [str(p) for p in sc.pitches]
    ['C2', 'D-2', 'E2', 'F#2', 'A2', 'B2', 'A2', 'C3', 'D-3']
    ```

[`RagMarwa`](#music21.scale.RagMarwa "music21.scale.RagMarwa") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RagMarwa`](#music21.scale.RagMarwa "music21.scale.RagMarwa") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RagMarwa`](#music21.scale.RagMarwa "music21.scale.RagMarwa") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RagMarwa`](#music21.scale.RagMarwa "music21.scale.RagMarwa") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`RagMarwa`](#music21.scale.RagMarwa "music21.scale.RagMarwa") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ScalaScale

class music21.scale.ScalaScale(*tonic=None*, *scalaString=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#ScalaScale)
:   A scale created from a Scala scale .scl file. Any file
    in the Scala archive can be given by name. Additionally, a file
    path to a Scala .scl file, or a raw string representation, can be used.

    ```python
    >>> sc = scale.ScalaScale('g4', 'mbira banda')
    >>> [str(p) for p in sc.pitches]
    ['G4', 'A4(-15c)', 'B4(-11c)', 'C#5(-7c)', 'D~5(+6c)', 'E5(+14c)', 'F~5(+1c)', 'G#5(+2c)']
    ```

    If only a single string is given, and it’s too long to be a tonic,
    or it ends in .scl, assume it’s the name of a scala scale and
    set the tonic to C4

    ```python
    >>> sc = scale.ScalaScale('pelog_9')
    >>> [str(p) for p in sc.pitches]
    ['C4', 'C#~4(-17c)', 'D~4(+17c)', 'F~4(-17c)',
     'F#~4(+17c)', 'G#4(-0c)', 'A~4(-17c)', 'C5(-0c)']
    ```

    If no scale with that name can be found then it raises an exception:

    ```python
    >>> sc = scale.ScalaScale('badFileName.scl')
    Traceback (most recent call last):
    music21.scale.ScaleException: Could not find a file named badFileName.scl in the scala database
    ```

[`ScalaScale`](#music21.scale.ScalaScale "music21.scale.ScalaScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScalaScale`](#music21.scale.ScalaScale "music21.scale.ScalaScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScalaScale`](#music21.scale.ScalaScale "music21.scale.ScalaScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ScalaScale`](#music21.scale.ScalaScale "music21.scale.ScalaScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`ScalaScale`](#music21.scale.ScalaScale "music21.scale.ScalaScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Scale

class music21.scale.Scale(*\*\*keywords*)[[source]](../_modules/music21/scale.html#Scale)
:   Generic base class for all scales, both abstract and concrete.

    ```python
    >>> s = scale.Scale()
    >>> s.type
    'Scale'
    >>> s.name  # default same as type.
    'Scale'
    >>> s.isConcrete
    False
    ```

    Not a useful class on its own. See its subclasses.

[`Scale`](#music21.scale.Scale "music21.scale.Scale") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Scale`](#music21.scale.Scale "music21.scale.Scale") read-only properties

Scale.isConcrete
:   To be concrete, a Scale must have a defined tonic.
    An abstract Scale is not Concrete, nor is a Concrete scale
    without a defined tonic. Thus, it is always false.

Scale.name
:   Return or construct the name of this scale

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Scale`](#music21.scale.Scale "music21.scale.Scale") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Scale`](#music21.scale.Scale "music21.scale.Scale") methods

static Scale.extractPitchList(*other*, *comparisonAttribute='nameWithOctave'*, *removeDuplicates=True*)[[source]](../_modules/music21/scale.html#Scale.extractPitchList)
:   Utility function and staticmethod

    Given a data format as “other” (a ConcreteScale, Chord, Stream, List of Pitches,
    or single Pitch),
    extract all unique Pitches using comparisonAttribute to test for them.

    ```python
    >>> pStrList = ['A4', 'D4', 'E4', 'F-4', 'D4', 'D5', 'A', 'D#4']
    >>> pList = [pitch.Pitch(p) for p in pStrList]
    >>> nList = [note.Note(p) for p in pStrList]
    >>> s = stream.Stream()
    >>> for n in nList:
    ...     s.append(n)
    ```

    Here we only remove the second ‘D4’ because the default comparison is nameWithOctave

    ```python
    >>> [str(p) for p in scale.Scale.extractPitchList(pList)]
    ['A4', 'D4', 'E4', 'F-4', 'D5', 'A4', 'D#4']
    ```

    Note that octaveless notes like the ‘A’ get a default octave. In general,
    it is better to work with octave-possessing pitches.

    Now we remove the F-4, D5, and A also because we are working with
    comparisonAttribute=pitchClass.
    Note that we’re using a Stream as other now:

    ```python
    >>> [str(p) for p in scale.Scale.extractPitchList(s, comparisonAttribute='pitchClass')]
    ['A4', 'D4', 'E4', 'D#4']
    ```

    Now let’s get rid of all but one diatonic D
    by using [`step()`](modulePitch.html#music21.pitch.Pitch.step "music21.pitch.Pitch.step") as our
    comparisonAttribute. Note that we can just give a list of
    strings as well, and they become [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects. Oh, we will also
    show that extractPitchList works on any scale:

    ```python
    >>> sc = scale.Scale()
    >>> [str(p) for p in sc.extractPitchList(pStrList, comparisonAttribute='step')]
    ['A4', 'D4', 'E4', 'F-4']
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Scale`](#music21.scale.Scale "music21.scale.Scale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SieveScale

class music21.scale.SieveScale(*tonic=None*, *sieveString='2@0'*, *eld: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 1*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#SieveScale)
:   A scale created from a Xenakis sieve logical string, based on the
    [`Sieve`](moduleSieve.html#music21.sieve.Sieve "music21.sieve.Sieve") object definition. The complete period of the
    sieve is realized as intervals and used to create a scale.

    ```python
    >>> sc = scale.SieveScale('c4', '3@0')
    >>> sc.pitches
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch E-4>]
    >>> sc = scale.SieveScale('d4', '3@0')
    >>> sc.pitches
    [<music21.pitch.Pitch D4>, <music21.pitch.Pitch F4>]
    >>> sc = scale.SieveScale('c2', '(-3@2 & 4) | (-3@1 & 4@1) | (3@2 & 4@2) | (-3 & 4@3)')
    >>> [str(p) for p in sc.pitches]
    ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3']
    ```

[`SieveScale`](#music21.scale.SieveScale "music21.scale.SieveScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SieveScale`](#music21.scale.SieveScale "music21.scale.SieveScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SieveScale`](#music21.scale.SieveScale "music21.scale.SieveScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`SieveScale`](#music21.scale.SieveScale "music21.scale.SieveScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`SieveScale`](#music21.scale.SieveScale "music21.scale.SieveScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WeightedHexatonicBlues

class music21.scale.WeightedHexatonicBlues(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#WeightedHexatonicBlues)
:   A concrete scale based on a dynamic mixture of a minor pentatonic
    and the hexatonic blues scale.

[`WeightedHexatonicBlues`](#music21.scale.WeightedHexatonicBlues "music21.scale.WeightedHexatonicBlues") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WeightedHexatonicBlues`](#music21.scale.WeightedHexatonicBlues "music21.scale.WeightedHexatonicBlues") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WeightedHexatonicBlues`](#music21.scale.WeightedHexatonicBlues "music21.scale.WeightedHexatonicBlues") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WeightedHexatonicBlues`](#music21.scale.WeightedHexatonicBlues "music21.scale.WeightedHexatonicBlues") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`WeightedHexatonicBlues`](#music21.scale.WeightedHexatonicBlues "music21.scale.WeightedHexatonicBlues") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WholeToneScale

class music21.scale.WholeToneScale(*tonic=None*, *\*\*keywords*)[[source]](../_modules/music21/scale.html#WholeToneScale)
:   A concrete whole-tone scale.

    ```python
    >>> sc = scale.WholeToneScale('g2')
    >>> [str(p) for p in sc.pitches]
    ['G2', 'A2', 'B2', 'C#3', 'D#3', 'E#3', 'G3']
    >>> [str(p) for p in sc.getPitches('g2', 'g5')]
    ['G2', 'A2', 'B2', 'C#3', 'D#3', 'E#3', 'G3', 'A3', 'B3', 'C#4',
     'D#4', 'E#4', 'G4', 'A4', 'B4', 'C#5', 'D#5', 'E#5', 'G5']
    >>> sc.abstract.getDegreeMaxUnique()
    6
    >>> sc.pitchFromDegree(1)
    <music21.pitch.Pitch G2>
    >>> sc.pitchFromDegree(2)
    <music21.pitch.Pitch A2>
    >>> sc.pitchFromDegree(6)
    <music21.pitch.Pitch E#3>
    >>> sc.getScaleDegreeFromPitch('g2', comparisonAttribute='pitchClass')
    1
    >>> sc.getScaleDegreeFromPitch('F6', comparisonAttribute='pitchClass')
    6
    ```

[`WholeToneScale`](#music21.scale.WholeToneScale "music21.scale.WholeToneScale") bases

* [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale")
* [`Scale`](#music21.scale.Scale "music21.scale.Scale")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WholeToneScale`](#music21.scale.WholeToneScale "music21.scale.WholeToneScale") read-only properties

Read-only properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`chord`](#music21.scale.ConcreteScale.chord "music21.scale.ConcreteScale.chord") * [`isConcrete`](#music21.scale.ConcreteScale.isConcrete "music21.scale.ConcreteScale.isConcrete") | * [`name`](#music21.scale.ConcreteScale.name "music21.scale.ConcreteScale.name") | * [`pitches`](#music21.scale.ConcreteScale.pitches "music21.scale.ConcreteScale.pitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WholeToneScale`](#music21.scale.WholeToneScale "music21.scale.WholeToneScale") read/write properties

Read/write properties inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`abstract`](#music21.scale.ConcreteScale.abstract "music21.scale.ConcreteScale.abstract") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WholeToneScale`](#music21.scale.WholeToneScale "music21.scale.WholeToneScale") methods

Methods inherited from [`ConcreteScale`](#music21.scale.ConcreteScale "music21.scale.ConcreteScale"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.ConcreteScale.__eq__ "music21.scale.ConcreteScale.__eq__") * [`derive()`](#music21.scale.ConcreteScale.derive "music21.scale.ConcreteScale.derive") * [`deriveAll()`](#music21.scale.ConcreteScale.deriveAll "music21.scale.ConcreteScale.deriveAll") * [`deriveByDegree()`](#music21.scale.ConcreteScale.deriveByDegree "music21.scale.ConcreteScale.deriveByDegree") * [`deriveRanked()`](#music21.scale.ConcreteScale.deriveRanked "music21.scale.ConcreteScale.deriveRanked") * [`findMissing()`](#music21.scale.ConcreteScale.findMissing "music21.scale.ConcreteScale.findMissing") * [`getChord()`](#music21.scale.ConcreteScale.getChord "music21.scale.ConcreteScale.getChord") * [`getDegreeMaxUnique()`](#music21.scale.ConcreteScale.getDegreeMaxUnique "music21.scale.ConcreteScale.getDegreeMaxUnique") * [`getPitches()`](#music21.scale.ConcreteScale.getPitches "music21.scale.ConcreteScale.getPitches") | * [`getScalaData()`](#music21.scale.ConcreteScale.getScalaData "music21.scale.ConcreteScale.getScalaData") * [`getScaleDegreeAndAccidentalFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch "music21.scale.ConcreteScale.getScaleDegreeAndAccidentalFromPitch") * [`getScaleDegreeFromPitch()`](#music21.scale.ConcreteScale.getScaleDegreeFromPitch "music21.scale.ConcreteScale.getScaleDegreeFromPitch") * [`getTonic()`](#music21.scale.ConcreteScale.getTonic "music21.scale.ConcreteScale.getTonic") * [`intervalBetweenDegrees()`](#music21.scale.ConcreteScale.intervalBetweenDegrees "music21.scale.ConcreteScale.intervalBetweenDegrees") * [`isNext()`](#music21.scale.ConcreteScale.isNext "music21.scale.ConcreteScale.isNext") * [`match()`](#music21.scale.ConcreteScale.match "music21.scale.ConcreteScale.match") * [`nextPitch()`](#music21.scale.ConcreteScale.nextPitch "music21.scale.ConcreteScale.nextPitch") | * [`pitchFromDegree()`](#music21.scale.ConcreteScale.pitchFromDegree "music21.scale.ConcreteScale.pitchFromDegree") * [`pitchesFromScaleDegrees()`](#music21.scale.ConcreteScale.pitchesFromScaleDegrees "music21.scale.ConcreteScale.pitchesFromScaleDegrees") * [`romanNumeral()`](#music21.scale.ConcreteScale.romanNumeral "music21.scale.ConcreteScale.romanNumeral") * [`show()`](#music21.scale.ConcreteScale.show "music21.scale.ConcreteScale.show") * [`solfeg()`](#music21.scale.ConcreteScale.solfeg "music21.scale.ConcreteScale.solfeg") * [`transpose()`](#music21.scale.ConcreteScale.transpose "music21.scale.ConcreteScale.transpose") * [`tune()`](#music21.scale.ConcreteScale.tune "music21.scale.ConcreteScale.tune") * [`write()`](#music21.scale.ConcreteScale.write "music21.scale.ConcreteScale.write") |

Methods inherited from [`Scale`](#music21.scale.Scale "music21.scale.Scale"):

|  |  |  |
| --- | --- | --- |
| * [`extractPitchList()`](#music21.scale.Scale.extractPitchList "music21.scale.Scale.extractPitchList") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") | * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`WholeToneScale`](#music21.scale.WholeToneScale "music21.scale.WholeToneScale") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |
