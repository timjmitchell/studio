Source: https://music21.org/music21docs/moduleReference/moduleVoiceLeading.html

# music21.voiceLeading

Objects to represent unique elements in a score that contain special analysis routines
to identify certain aspects of music theory. for use especially with theoryAnalyzer, which will
divide a score up into these segments, returning a list of segments to later analyze

The list of objects included here are:

* [`VoiceLeadingQuartet`](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet") : two by two matrix of notes
* [`iterateAllVoiceLeadingQuartets()`](#music21.voiceLeading.iterateAllVoiceLeadingQuartets "music21.voiceLeading.iterateAllVoiceLeadingQuartets") : yields each VLQ in a piece.
* [`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality")vertical context in a score,
  :   composed of any music21 objects
* [`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet")group of three
  :   contiguous verticality objects
* [`VerticalityTriplet`](#music21.voiceLeading.VerticalityTriplet "music21.voiceLeading.VerticalityTriplet")three verticality objects –
  :   has special features
* [`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment") : n (any number) of music21 objects
* [`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment") : n (any number) of notes
* [`ThreeNoteLinearSegment`](#music21.voiceLeading.ThreeNoteLinearSegment "music21.voiceLeading.ThreeNoteLinearSegment") : three notes in the same part of a score
* [`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment") :
  :   preliminary implementation of n(any number) chords
* [`TwoChordLinearSegment`](#music21.voiceLeading.TwoChordLinearSegment "music21.voiceLeading.TwoChordLinearSegment") : 2 chord objects

## VoiceLeadingQuartet

class music21.voiceLeading.VoiceLeadingQuartet(*v1n1: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = None*, *v1n2: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = None*, *v2n1: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = None*, *v2n2: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = None*, *analyticKey: [Key](moduleKey.html#music21.key.Key "music21.key.Key") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet)
:   An object consisting of four pitches: v1n1, v1n2, v2n1, v2n2
    where v1n1 moves to v1n2 at the same time as
    v2n1 moves to v2n2.
    (v1n1: voice 1(top voice), note 1 (left most note) )

    Necessary for classifying types of voice-leading motion.

    In general, v1 should be the “higher” voice and v2 the “lower” voice
    in order for methods such as .voiceCrossing and isProperResolution
    to make sense. Most routines will work the other way still though.

[`VoiceLeadingQuartet`](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`VoiceLeadingQuartet`](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`VoiceLeadingQuartet`](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet") read/write properties

VoiceLeadingQuartet.key
:   get or set the key of this VoiceLeadingQuartet, for use in theory analysis routines
    such as closesIncorrectly. Can be None

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet('D', 'G', 'B', 'G')
    >>> vlq.key is None
    True
    >>> vlq.key = key.Key('G')
    >>> vlq.key
    <music21.key.Key of G major>
    ```

    Key can also be given as a string:

    ```python
    >>> vlq.key = 'd'
    >>> vlq.key
    <music21.key.Key of d minor>
    ```

    Incorrect keys raise VoiceLeadingQuartetExceptions

VoiceLeadingQuartet.v1n1
:   set note1 for voice 1

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('C', 'D', 'E', 'F')
    >>> vl.v1n1
    <music21.note.Note C>
    ```

VoiceLeadingQuartet.v1n2
:   set note 2 for voice 1

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('C', 'D', 'E', 'F')
    >>> vl.v1n2
    <music21.note.Note D>
    ```

VoiceLeadingQuartet.v2n1
:   set note 1 for voice 2

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('C', 'D', 'E', 'F')
    >>> vl.v2n1
    <music21.note.Note E>
    ```

VoiceLeadingQuartet.v2n2
:   set note 2 for voice 2

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('C', 'D', 'E', 'F')
    >>> vl.v2n2
    <music21.note.Note F>
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`VoiceLeadingQuartet`](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet") methods

VoiceLeadingQuartet.antiParallelMotion(*simpleName=None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.antiParallelMotion)
:   Returns True if the simple interval before is the same as the simple
    interval after and the motion is contrary. if simpleName is
    specified as an Interval object or a string then it only returns
    true if the simpleName of both intervals is the same as simpleName
    (i.e., use to find antiParallel fifths)

    ```python
    >>> n11 = note.Note('C4')
    >>> n12 = note.Note('D3')  # descending 7th
    >>> n21 = note.Note('G4')
    >>> n22 = note.Note('A4')  # ascending 2nd
    >>> vlq1 = voiceLeading.VoiceLeadingQuartet(n11, n12, n21, n22)
    >>> vlq1.antiParallelMotion()
    True
    ```

    ```python
    >>> vlq1.antiParallelMotion('M2')
    False
    ```

    ```python
    >>> vlq1.antiParallelMotion('P5')
    True
    ```

    We can also use interval objects

    ```python
    >>> p5Obj = interval.Interval('P5')
    >>> p8Obj = interval.Interval('P8')
    >>> vlq1.antiParallelMotion(p5Obj)
    True
    ```

    ```python
    >>> p8Obj = interval.Interval('P8')
    >>> vlq1.antiParallelMotion(p8Obj)
    False
    ```

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('G4')
    >>> m2 = note.Note('G3')
    >>> vl2 = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl2.antiParallelMotion()
    False
    ```

VoiceLeadingQuartet.closesIncorrectly() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.closesIncorrectly)
:   TODO(msc): will be renamed to be less dogmatic

    Returns True if the VLQ would be an incorrect closing in
    the style of 16th century Counterpoint (not Bach Chorale style)

    Returns True if closing harmonic interval is a P8 or PU and the interval
    approaching the close is
    6 - 8, 10 - 8, or 3 - U. Must be in contrary motion, and if in minor key,
    has a leading tone resolves to the tonic.

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('C#', 'D', 'E', 'D')
    >>> vl.key = key.Key('d')
    >>> vl.closesIncorrectly()
    False
    >>> vl = voiceLeading.VoiceLeadingQuartet('B3', 'C4', 'G3', 'C2')
    >>> vl.key = key.Key('C')
    >>> vl.closesIncorrectly()
    False
    >>> vl = voiceLeading.VoiceLeadingQuartet('F', 'G', 'D', 'G')
    >>> vl.key = key.Key('g')
    >>> vl.closesIncorrectly()
    True
    >>> vl = voiceLeading.VoiceLeadingQuartet('C#4', 'D4', 'A2', 'D3', analyticKey='D')
    >>> vl.closesIncorrectly()
    True
    ```

VoiceLeadingQuartet.contraryMotion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.contraryMotion)
:   Returns True if both voices move in opposite directions

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('G4')
    >>> m2 = note.Note('G4')
    ```

    No motion, so False:

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.contraryMotion()
    False
    ```

    Oblique motion, so False:

    ```python
    >>> n2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.contraryMotion()
    False
    ```

    Parallel motion, so False

    ```python
    >>> m2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.contraryMotion()
    False
    ```

    Similar motion, so False

    ```python
    >>> m2 = note.Note('A5')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.contraryMotion()
    False
    ```

    Finally, contrary motion, so True!

    ```python
    >>> m2 = note.Note('C4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.contraryMotion()
    True
    ```

VoiceLeadingQuartet.hiddenFifth() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.hiddenFifth)
:   Calls [`hiddenInterval()`](#music21.voiceLeading.VoiceLeadingQuartet.hiddenInterval "music21.voiceLeading.VoiceLeadingQuartet.hiddenInterval")
    by passing a fifth

VoiceLeadingQuartet.hiddenInterval(*thisInterval*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.hiddenInterval)
:   Returns True if there is a hidden interval that matches
    thisInterval.

    N.B. – this method finds ALL hidden intervals,
    not just those that are forbidden under traditional
    common practice counterpoint rules. Takes thisInterval,
    an Interval object.

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('B4')
    >>> m2 = note.Note('D5')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.hiddenInterval(interval.Interval('P5'))
    True
    ```

    ```python
    >>> n1 = note.Note('E4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('B4')
    >>> m2 = note.Note('D5')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.hiddenInterval(interval.Interval('P5'))
    False
    ```

    ```python
    >>> n1 = note.Note('E4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('B4')
    >>> m2 = note.Note('D6')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.hiddenInterval(interval.Interval('P5'))
    False
    ```

VoiceLeadingQuartet.hiddenOctave() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.hiddenOctave)
:   Calls hiddenInterval by passing an octave

VoiceLeadingQuartet.inwardContraryMotion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.inwardContraryMotion)
:   Returns True if both voices move inward by contrary motion

    ```python
    >>> n1 = note.Note('C5')
    >>> n2 = note.Note('B4')
    >>> m1 = note.Note('G4')
    >>> m2 = note.Note('A4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.inwardContraryMotion()
    True
    >>> vl.outwardContraryMotion()
    False
    ```

VoiceLeadingQuartet.isProperResolution() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.isProperResolution)
:   Checks whether the voice-leading quartet resolves correctly according to standard
    counterpoint rules. If the first harmony is dissonant (P4, d5, A4, or m7) it checks
    that these are correctly resolved. If the first harmony is consonant, True is returned.

    The key parameter should be specified to check for motion in the bass from specific
    note degrees. If it is not set, then no checking for scale degrees takes place.

    Currently implements the following resolutions:

    > P4: Top voice must resolve downward.
    >
    > A4: out by contrary motion to a sixth, with chordal seventh resolving
    > :   down to a third in the bass.
    >
    > d5: in by contrary motion to a third, with 7 resolving up to 1 in the bass
    >
    > m7: Resolves to a third with a leap from 5 to 1 in the bass

    We will make the examples shorter with this abbreviation:
    >>> N = note.Note

    ```python
    >>> n1 = note.Note('B-4')
    >>> n2 = note.Note('A4')
    >>> m1 = note.Note('E4')
    >>> m2 = note.Note('F4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # d5 resolves inward
    True
    >>> m2.pitch.name = 'D'
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # d5 resolves outward
    False
    >>> vl.key = 'B-'
    >>> vl.isProperResolution()  # not on scale degrees that need resolution
    True
    ```

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('C4')
    >>> m1 = note.Note('G#3')
    >>> m2 = note.Note('A3')
    >>> k = key.Key('a')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2, k)
    >>> vl.isProperResolution()  # d5 with #7 in minor handled correctly
    True
    ```

    ```python
    >>> n1 = note.Note('E5')
    >>> n2 = note.Note('F5')
    >>> m1 = note.Note('B-4')
    >>> m2 = note.Note('A4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # A4 resolves outward
    True
    >>> m2.pitch.nameWithOctave = 'D5'
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # A4 resolves inward
    False
    >>> vl.key = 'B-'
    >>> vl.isProperResolution()  # A4 not on scale degrees that need resolution
    True
    >>> vl.key = 'F'
    >>> vl.isProperResolution()  # A4 on scale degrees that need resolution
    False
    ```

    ```python
    >>> n1 = note.Note('B-4')
    >>> n2 = note.Note('A4')
    >>> m1 = note.Note('C4')
    >>> m2 = note.Note('F4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # m7
    True
    >>> m2.pitch.nameWithOctave = 'F3'
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # m7 with similar motion
    True
    >>> vl.key = 'B-'
    >>> vl.isProperResolution()  # m7 not on scale degrees that need resolution
    True
    >>> vl.key = 'F'
    >>> vl.isProperResolution()  # m7 on scale degrees that need resolution
    True
    ```

    P4 on the initial harmony must move down.

    ```python
    >>> n1 = note.Note('F5')
    >>> n2 = note.Note('G5')
    >>> m1 = note.Note('C4')
    >>> m2 = note.Note('C4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # P4 must move down or remain static
    False
    >>> n2.step = 'E'
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.isProperResolution()  # P4 can move down by step or leap
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('B-4', 'A4', 'C2', 'F2')
    >>> vl.key = key.Key('F')
    >>> vl.isProperResolution()  # not dissonant, True returned
    True
    ```

VoiceLeadingQuartet.leapNotSetWithStep() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.leapNotSetWithStep)
:   Returns True if there is a leap or skip in once voice then the other voice must
    be a step or unison.
    if neither part skips then False is returned. Returns False if the two voices
    skip thirds in contrary motion.

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('C5')
    >>> m1 = note.Note('B3')
    >>> m2 = note.Note('A3')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.leapNotSetWithStep()
    False
    ```

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('C5')
    >>> m1 = note.Note('B3')
    >>> m2 = note.Note('F3')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.leapNotSetWithStep()
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('E', 'G', 'G', 'E')
    >>> vl.leapNotSetWithStep()
    False
    ```

VoiceLeadingQuartet.motionType(*\**, *allowAntiParallel=False*)[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.motionType)
:   returns the type of motion from the MotionType Enum object
    that exists in this voice leading quartet

    ```python
    >>> for mt in voiceLeading.MotionType:
    ...     print(repr(mt))
    <MotionType.antiParallel: 'Anti-Parallel'>
    <MotionType.contrary: 'Contrary'>
    <MotionType.noMotion: 'No Motion'>
    <MotionType.oblique: 'Oblique'>
    <MotionType.parallel: 'Parallel'>
    <MotionType.similar: 'Similar'>
    ```

    ```python
    >>> n1_d4 = note.Note('D4')
    >>> n2_e4 = note.Note('E4')
    >>> m1_f4 = note.Note('F4')
    >>> m2_b4 = note.Note('B4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1_d4, n2_e4, m1_f4, m2_b4)
    >>> vl.motionType()
    <MotionType.similar: 'Similar'>
    ```

    ```python
    >>> n1_a4 = note.Note('A4')
    >>> n2_c5 = note.Note('C5')
    >>> m1_d4 = note.Note('D4')
    >>> m2_f4 = note.Note('F4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1_a4, n2_c5, m1_d4, m2_f4)
    >>> vl.motionType()
    <MotionType.parallel: 'Parallel'>
    >>> print(vl.motionType())
    MotionType.parallel
    >>> vl.motionType() == 'Parallel'
    True
    ```

    Demonstrations of other motion types.

    Contrary:

    ```python
    >>> n1_d5 = note.Note('D5')   # D5, C5 against D4, F4
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1_d5, n2_c5, m1_d4, m2_f4)
    >>> vl.motionType()
    <MotionType.contrary: 'Contrary'>
    ```

    Oblique:

    ```python
    >>> n1_c5 = note.Note('C5')   # C5, C5 against D4, F4
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1_c5, n2_c5, m1_d4, m2_f4)
    >>> vl.motionType()
    <MotionType.oblique: 'Oblique'>
    ```

    No motion (if I had a dollar for every time I forgot to teach
    that this is not a form of oblique motion):

    ```python
    >>> m1_f4 = note.Note('F4')   # C5, C5 against F4, F4
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1_c5, n2_c5, m1_f4, m2_f4)
    >>> vl.motionType()
    <MotionType.noMotion: 'No Motion'>
    ```

    Anti-parallel motion has to be explicitly enabled to appear:

    ```python
    >>> n1_a5 = note.Note('A5')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1_a5, n2_c5, m1_d4, m2_f4)
    >>> vl.motionType()  # anti-parallel fifths
    <MotionType.contrary: 'Contrary'>
    >>> vl.motionType(allowAntiParallel=True)
    <MotionType.antiParallel: 'Anti-Parallel'>
    ```

    * Changed in v6: anti-parallel motion was supposed to be
      able to be returned in previous versions, but a bug prevented it.
      To preserve backwards compatibility, it must be explicitly enabled.

VoiceLeadingQuartet.noMotion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.noMotion)
:   Returns True if no voice moves in this “voice-leading” moment

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('D4')
    >>> m2 = note.Note('D4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.noMotion()
    True
    >>> n2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.noMotion()
    False
    ```

VoiceLeadingQuartet.obliqueMotion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.obliqueMotion)
:   Returns True if one voice remains the same and another moves. i.e.,
    noMotion must be False if obliqueMotion is True.

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('D4')
    >>> m2 = note.Note('D4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.obliqueMotion()
    False
    >>> n2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.obliqueMotion()
    True
    >>> m2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.obliqueMotion()
    False
    ```

VoiceLeadingQuartet.opensIncorrectly() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.opensIncorrectly)
:   TODO(msc): will be renamed to be less dogmatic

    Returns True if the VLQ would be an incorrect opening in
    the style of 16th century Counterpoint (not Bach Chorale style)

    Returns True if the opening or second harmonic interval is PU, P8, or P5,
    to accommodate an anacrusis.
    also checks to see if opening establishes tonic or dominant harmony (uses
    [`identifyAsTonicOrDominant()`](moduleRoman.html#music21.roman.identifyAsTonicOrDominant "music21.roman.identifyAsTonicOrDominant")

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('D', 'D', 'D', 'F#')
    >>> vl.key = 'D'
    >>> vl.opensIncorrectly()
    False
    >>> vl = voiceLeading.VoiceLeadingQuartet('B', 'A', 'G#', 'A')
    >>> vl.key = 'A'
    >>> vl.opensIncorrectly()
    False
    >>> vl = voiceLeading.VoiceLeadingQuartet('A', 'A', 'F#', 'D')
    >>> vl.key = 'A'
    >>> vl.opensIncorrectly()
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('C#', 'C#', 'D', 'E')
    >>> vl.key = 'A'
    >>> vl.opensIncorrectly()
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet('B', 'B', 'A', 'A')
    >>> vl.key = 'C'
    >>> vl.opensIncorrectly()
    True
    ```

VoiceLeadingQuartet.outwardContraryMotion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.outwardContraryMotion)
:   Returns True if both voices move outward by contrary motion

    ```python
    >>> n1 = note.Note('D5')
    >>> n2 = note.Note('E5')
    >>> m1 = note.Note('G4')
    >>> m2 = note.Note('F4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.outwardContraryMotion()
    True
    >>> vl.inwardContraryMotion()
    False
    ```

VoiceLeadingQuartet.parallelFifth() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.parallelFifth)
:   Returns True if the motion is a parallel or antiparallel Perfect Fifth,
    allowing displacement by an octave (e.g., 5th to a 12th).

    We will make the examples shorter with this abbreviation:

    ```python
    >>> N = note.Note
    ```

    Parallel fifths

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('G4'), N('A4'), N('C4'), N('D4'))
    >>> vlq.parallelFifth()
    True
    ```

    5th -> 12th in similar motion

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('G4'), N('A5'), N('C4'), N('D4'))
    >>> vlq.parallelFifth()
    True
    ```

    5th -> 12th in antiparallel motion

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('G4'), N('A4'), N('C4'), N('D3'))
    >>> vlq.parallelFifth()
    True
    ```

    Note that diminished fifth moving to perfect fifth is not a parallelFifth

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('G4'), N('A4'), N('C#4'), N('D4'))
    >>> vlq.parallelFifth()
    False
    ```

    Nor is P5 moving to d5.

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('G4'), N('Ab4'), N('C4'), N('D4'))
    >>> vlq.parallelFifth()
    False
    ```

VoiceLeadingQuartet.parallelInterval(*thisInterval*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.parallelInterval)
:   Returns True if there is a parallel motion or antiParallel motion of
    this type (thisInterval should be an Interval object)

    ```python
    >>> n11 = note.Note('G4')
    >>> n12a = note.Note('A4')  # ascending 2nd
    ```

    ```python
    >>> n21 = note.Note('C4')
    >>> n22a = note.Note('D4')  # ascending 2nd
    ```

    ```python
    >>> vlq1 = voiceLeading.VoiceLeadingQuartet(n11, n12a, n21, n22a)
    >>> vlq1.parallelInterval(interval.Interval('P5'))
    True
    ```

    ```python
    >>> vlq1.parallelInterval(interval.Interval('P8'))
    False
    ```

    Antiparallel fifths also are True

    ```python
    >>> n22b = note.Note('D3')  # descending 7th
    >>> vlq2 = voiceLeading.VoiceLeadingQuartet(n11, n12a, n21, n22b)
    >>> vlq2.parallelInterval(interval.Interval('P5'))
    True
    ```

    But Antiparallel other interval are not:

    ```python
    >>> N = note.Note
    >>> vlq2a = voiceLeading.VoiceLeadingQuartet(N('C5'), N('C6'), N('C4'), N('C3'))
    >>> vlq2a.parallelInterval(interval.Interval('P5'))
    False
    >>> vlq2a.parallelInterval(interval.Interval('P8'))
    True
    ```

    Non-parallel intervals are, of course, False

    ```python
    >>> n12b = note.Note('B4')  # ascending 3rd
    >>> vlq3 = voiceLeading.VoiceLeadingQuartet(n11, n12b, n21, n22b)
    >>> vlq3.parallelInterval(interval.Interval('P5'))
    False
    ```

VoiceLeadingQuartet.parallelMotion(*requiredInterval=None*, *allowOctaveDisplacement=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.parallelMotion)
:   Returns True if both the first and second intervals are the same sized
    generic interval.

    If requiredInterval is set, returns True only if both intervals are that
    generic or specific interval.

    allowOctaveDisplacement treats motion as parallel even if any of the intervals
    are displaced by octaves, except in the case of unisons and octaves, which
    are always treated as distinct.

    We will make the examples shorter with this abbreviation:
    >>> N = note.Note

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('G4'), N('G4'), N('G3'), N('G3'))
    >>> vl.parallelMotion()  # not even similar motion
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('G4'), N('B4'), N('G3'), N('A3'))
    >>> vl.parallelMotion()  # similar motion, but no kind of parallel
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('G4'), N('G5'), N('G4'), N('G5'))
    >>> vl.parallelMotion()  # parallel unisons
    True
    ```

    ```python
    >>> vl.parallelMotion('P1')
    True
    ```

    octaves never equivalent to unisons

    ```python
    >>> vl.parallelMotion('P8', allowOctaveDisplacement=True)
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('B4'), N('D3'), N('E3'))
    >>> vl.parallelMotion()  # parallel fifths
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('B5'), N('D3'), N('E3'))
    >>> vl.parallelMotion()  # 5th to a 12th
    False
    >>> vl.parallelMotion(allowOctaveDisplacement=True)
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('Bb4'), N('F4'), N('G4'))
    >>> vl.parallelMotion(3)  # parallel thirds ...
    True
    >>> vl.parallelMotion('M3')  # ... but not parallel MAJOR thirds
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('D4'), N('E4'), N('F3'), N('G3'))
    >>> gi = interval.GenericInterval(6)
    >>> vl.parallelMotion(gi)  # these are parallel sixths ...
    True
    ```

    These are also parallel major sixths

    ```python
    >>> i = interval.Interval('M6')
    >>> di = interval.DiatonicInterval('major', 6)
    >>> vl.parallelMotion(i) and vl.parallelMotion(di)
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('D5'), N('E6'), N('F3'), N('G3'))
    >>> vl.parallelMotion(gi)  # octave displacement
    False
    >>> vl.parallelMotion(gi, allowOctaveDisplacement=True)
    True
    ```

VoiceLeadingQuartet.parallelOctave() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.parallelOctave)
:   Returns True if the motion is a parallel Perfect Octave.

    (This is a concept so abhorrent we shudder to illustrate it
    with an example, but alas, we must:)

    We will make the examples shorter with this abbreviation:

    ```python
    >>> N = note.Note
    ```

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('C5'), N('D5'), N('C4'), N('D4'))
    >>> vlq.parallelOctave()
    True
    ```

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('C6'), N('D6'), N('C4'), N('D4'))
    >>> vlq.parallelOctave()
    True
    ```

    Or False if the motion is according to the rules of God’s own creation :-)

    ```python
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('C4'), N('D4'), N('C4'), N('D4'))
    >>> vlq.parallelOctave()
    False
    ```

    (P.S., we were joking about parallel octaves being abhorant or out of God’s creation!
    music21 works just as well with popular music and other styles that do not
    have problems with parallel octaves.)

VoiceLeadingQuartet.parallelUnison() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.parallelUnison)
:   Returns True if the motion is a parallel Perfect Unison (and not
    Perfect Octave, etc.)

    We will make the examples shorter with this abbreviation:

    ```python
    >>> N = note.Note
    >>> vlq = voiceLeading.VoiceLeadingQuartet(N('C4'), N('D4'), N('C4'), N('D4'))
    >>> vlq.parallelUnison()
    True
    ```

    ```python
    >>> vlq  = voiceLeading.VoiceLeadingQuartet(N('C5'), N('D5'), N('C4'), N('D4'))
    >>> vlq.parallelUnison()
    False
    ```

VoiceLeadingQuartet.parallelUnisonOrOctave() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.parallelUnisonOrOctave)
:   Returns True if the VoiceLeadingQuartet has motion by parallel
    octave or parallel unison

    ```python
    >>> voiceLeading.VoiceLeadingQuartet(
    ...     note.Note('C4'),
    ...     note.Note('D4'),
    ...     note.Note('C3'),
    ...     note.Note('D3')
    ...     ).parallelUnisonOrOctave()
    True
    ```

    ```python
    >>> voiceLeading.VoiceLeadingQuartet(
    ...     note.Note('C4'),
    ...     note.Note('D4'),
    ...     note.Note('C4'),
    ...     note.Note('D4')
    ...     ).parallelUnisonOrOctave()
    True
    ```

VoiceLeadingQuartet.similarMotion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.similarMotion)
:   Returns True if the two voices both move in the same direction.
    Parallel Motion will also return true, as it is a special case of
    similar motion. If there is no motion, returns False.

    ```python
    >>> n1 = note.Note('G4')
    >>> n2 = note.Note('G4')
    >>> m1 = note.Note('G4')
    >>> m2 = note.Note('G4')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.similarMotion()
    False
    >>> n2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.similarMotion()
    False
    >>> m2.octave = 5
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.similarMotion()
    True
    >>> m2 = note.Note('A5')
    >>> vl = voiceLeading.VoiceLeadingQuartet(n1, n2, m1, m2)
    >>> vl.similarMotion()
    True
    ```

VoiceLeadingQuartet.voiceCrossing() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.voiceCrossing)
:   Returns True if either note in V1 is lower than the simultaneous note in V2.

    We will make the examples shorter with this abbreviation:

    ```python
    >>> N = note.Note
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('A4'), N('G4'), N('G4'))
    >>> vl.voiceCrossing()  # nothing crossed
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('F4'), N('G4'), N('G4'))
    >>> vl.voiceCrossing()  # second interval is crossed
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('F4'), N('A4'), N('G4'), N('G4'))
    >>> vl.voiceCrossing()  # first interval crossed
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('F4'), N('F4'), N('G4'), N('G4'))
    >>> vl.voiceCrossing()  # both crossed
    True
    ```

VoiceLeadingQuartet.voiceOverlap() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#VoiceLeadingQuartet.voiceOverlap)
:   Returns True if the second note in V1 is lower than the first in V2, or
    if the second note in V2 is higher than the first note in V1.

    We will make the examples shorter with this abbreviation:
    >>> N = note.Note

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('B4'), N('F4'), N('G4'))
    >>> vl.voiceOverlap()  # no overlap
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('B4'), N('F4'), N('A4'))
    >>> vl.voiceOverlap()  # Motion to the SAME note is not considered overlap
    False
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('C4'), N('F4'), N('Bb4'))
    >>> vl.voiceOverlap()  # V2 overlaps V1
    True
    ```

    ```python
    >>> vl = voiceLeading.VoiceLeadingQuartet(N('A4'), N('E4'), N('F4'), N('D4'))
    >>> vl.voiceOverlap()  # V1 overlaps V2
    True
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`VoiceLeadingQuartet`](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet") instance variables

VoiceLeadingQuartet.hIntervals
:   A two-element list of the two melodic intervals present,
    v1n1 to v1n2 and v2n1 to v2n2.

VoiceLeadingQuartet.vIntervals
:   A two-element list of the two harmonic intervals present,
    vn1n1 to v2n1 and v1n2 to v2n2.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ThreeNoteLinearSegment

class music21.voiceLeading.ThreeNoteLinearSegment(*noteListOrN1=None*, *n2=None*, *n3=None*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment)
:   An object consisting of three sequential notes

    The middle tone in a ThreeNoteLinearSegment can
    be classified using methods enclosed in this class
    to identify it as types of embellishing tones. Further
    methods can be used on the entire stream to identify these
    as non-harmonic.

    Accepts a sequence of strings, pitches, or notes.

    ```python
    >>> ex = voiceLeading.ThreeNoteLinearSegment('C#4', 'D4', 'E-4')
    >>> ex.n1
    <music21.note.Note C#>
    >>> ex.n2
    <music21.note.Note D>
    >>> ex.n3
    <music21.note.Note E->
    ```

    ```python
    >>> ex = voiceLeading.ThreeNoteLinearSegment(note.Note('A4'),note.Note('D4'),'F5')
    >>> ex.n1
    <music21.note.Note A>
    >>> ex.n2
    <music21.note.Note D>
    >>> ex.n3
    <music21.note.Note F>
    >>> ex.iLeftToRight
    <music21.interval.Interval m6>
    ```

    ```python
    >>> ex.iLeft
    <music21.interval.Interval P-5>
    >>> ex.iRight
    <music21.interval.Interval m10>
    ```

    if no octave specified, default octave of 4 is assumed

    ```python
    >>> ex2 = voiceLeading.ThreeNoteLinearSegment('a', 'b', 'c')
    >>> ex2.n1
    <music21.note.Note A>
    >>> defaults.pitchOctave
    4
    ```

[`ThreeNoteLinearSegment`](#music21.voiceLeading.ThreeNoteLinearSegment "music21.voiceLeading.ThreeNoteLinearSegment") bases

* [`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ThreeNoteLinearSegment`](#music21.voiceLeading.ThreeNoteLinearSegment "music21.voiceLeading.ThreeNoteLinearSegment") read-only properties

ThreeNoteLinearSegment.iLeft
:   get the interval between the left-most note and the middle note
    (read-only property)

    ```python
    >>> tnls = voiceLeading.ThreeNoteLinearSegment('A', 'B', 'G')
    >>> tnls.iLeft
    <music21.interval.Interval M2>
    ```

ThreeNoteLinearSegment.iLeftToRight
:   get the interval between the left-most note and the right-most note
    (read-only property)

    ```python
    >>> tnls = voiceLeading.ThreeNoteLinearSegment('C', 'E', 'G')
    >>> tnls.iLeftToRight
    <music21.interval.Interval P5>
    ```

ThreeNoteLinearSegment.iRight
:   get the interval between the middle note and the right-most note
    (read-only property)

    ```python
    >>> tnls = voiceLeading.ThreeNoteLinearSegment('A', 'B', 'G')
    >>> tnls.iRight
    <music21.interval.Interval M-3>
    ```

Read-only properties inherited from [`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment"):

|  |  |  |
| --- | --- | --- |
| * [`melodicIntervals`](#music21.voiceLeading.NNoteLinearSegment.melodicIntervals "music21.voiceLeading.NNoteLinearSegment.melodicIntervals") | * [`noteList`](#music21.voiceLeading.NNoteLinearSegment.noteList "music21.voiceLeading.NNoteLinearSegment.noteList") |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ThreeNoteLinearSegment`](#music21.voiceLeading.ThreeNoteLinearSegment "music21.voiceLeading.ThreeNoteLinearSegment") read/write properties

ThreeNoteLinearSegment.n1
:   get or set the first note (left-most) in the segment

ThreeNoteLinearSegment.n2
:   get or set the middle note in the segment

ThreeNoteLinearSegment.n3
:   get or set the last note (right-most) in the segment

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ThreeNoteLinearSegment`](#music21.voiceLeading.ThreeNoteLinearSegment "music21.voiceLeading.ThreeNoteLinearSegment") methods

ThreeNoteLinearSegment.couldBeChromaticNeighborTone() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment.couldBeChromaticNeighborTone)
:   returns True if and only if noteToAnalyze could be a chromatic neighbor tone, that is,
    the left and right notes are identical while the middle is a chromatic step up or down

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'D3', 'C3').couldBeChromaticNeighborTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'D-3', 'C3').couldBeChromaticNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C#3', 'D3', 'C#3').couldBeChromaticNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C#3', 'D3', 'D-3').couldBeChromaticNeighborTone()
    False
    ```

ThreeNoteLinearSegment.couldBeChromaticPassingTone()[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment.couldBeChromaticPassingTone)
:   A note could a chromatic passing tone (and therefore a passing tone in general)
    if the generic interval between the previous and the current is -2, 1, or 2;
    the generic interval between the current and next is -2, 1, 2; the two generic
    intervals multiply to -2 or 2 (if 4 then it’s a diatonic interval; if 1 then
    not a passing tone; i.e, C -> C# -> C## is not a chromatic passing tone);
    AND between each of the notes there is a chromatic interval of 1 or -1 and
    multiplied together it is 1. (i.e.: C -> D– -> D- is not a chromatic passing tone).

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'C4', 'C#4').couldBeChromaticPassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'C4', 'C#4').couldBeChromaticPassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'B#3', 'C#4').couldBeChromaticPassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'D-4', 'C#4').couldBeChromaticPassingTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'C##4', 'C#4').couldBeChromaticPassingTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('C#4', 'C4', 'C##4').couldBeChromaticPassingTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('D--4', 'C4', 'D-4').couldBeChromaticPassingTone()
    False
    ```

ThreeNoteLinearSegment.couldBeDiatonicNeighborTone() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment.couldBeDiatonicNeighborTone)
:   Returns True if and only if noteToAnalyze could be a diatonic neighbor tone, that is,
    the left and right notes are identical while the middle is a diatonic step up or down

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'D3', 'C3').couldBeDiatonicNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'C#3', 'C3').couldBeDiatonicNeighborTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'D-3', 'C3').couldBeDiatonicNeighborTone()
    False
    ```

ThreeNoteLinearSegment.couldBeDiatonicPassingTone()[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment.couldBeDiatonicPassingTone)
:   A note could be a diatonic passing tone (and therefore a passing tone in general)
    if the generic interval between the previous and the current is 2 or -2;
    same for the next; and both move in the same direction
    (that is, the two intervals multiplied by each other are 4, not -4).

    ```python
    >>> tls = voiceLeading.ThreeNoteLinearSegment('B3', 'C4', 'C#4')
    >>> tls.couldBeDiatonicPassingTone()
    False
    ```

    ```python
    >>> tls = voiceLeading.ThreeNoteLinearSegment('C3', 'D3', 'E3')
    >>> tls.couldBeDiatonicPassingTone()
    True
    ```

ThreeNoteLinearSegment.couldBeNeighborTone()[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment.couldBeNeighborTone)
:   checks if noteToAnalyze could be a neighbor tone, either a diatonic neighbor tone
    or a chromatic neighbor tone. Does NOT check if tone is non-harmonic.

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('E3', 'F3', 'E3').couldBeNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('B-4', 'C5', 'B-4').couldBeNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('B4', 'C5', 'B4').couldBeNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('G4', 'F#4', 'G4').couldBeNeighborTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('E-3', 'F3', 'E-4').couldBeNeighborTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'D3', 'E3').couldBeNeighborTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('A3', 'C3', 'D3').couldBeNeighborTone()
    False
    ```

ThreeNoteLinearSegment.couldBePassingTone() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/voiceLeading.html#ThreeNoteLinearSegment.couldBePassingTone)
:   checks if the two intervals are steps and if these steps
    are moving in the same direction. Returns True if the tone is
    identified as either a chromatic passing tone or a diatonic passing
    tone. Only major and minor diatonic passing tones are recognized (not
    pentatonic or scales beyond twelve-notes). Does NOT check if tone is non-harmonic.

    Accepts pitch or note objects; method is dependent on octave information

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('C#4', 'D4', 'E-4').couldBePassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'D3', 'E3').couldBePassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('E-3', 'F3', 'G-3').couldBePassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C3', 'C3', 'C3').couldBePassingTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('A3', 'C3', 'D3').couldBePassingTone()
    False
    ```

    Directionality must be maintained

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('B##3', 'C4', 'D--4').couldBePassingTone()
    False
    ```

    If no octave is given then .\_defaultOctave is used. This is generally octave 4

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('C', 'D', 'E').couldBePassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C4', 'D', 'E').couldBePassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('C5', 'D', 'E').couldBePassingTone()
    False
    ```

    Method returns True if either a chromatic passing tone or a diatonic passing
    tone is identified. Spelling of the pitch does matter!

    ```python
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'C4', 'B##3').couldBePassingTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('A##3', 'C4', 'E---4').couldBePassingTone()
    False
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'C4', 'D-4').couldBePassingTone()
    True
    >>> voiceLeading.ThreeNoteLinearSegment('B3', 'C4', 'C#4').couldBePassingTone()
    True
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ThreeNoteLinearSegment`](#music21.voiceLeading.ThreeNoteLinearSegment "music21.voiceLeading.ThreeNoteLinearSegment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Verticality

class music21.voiceLeading.Verticality(*contentDict: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#Verticality)
:   DEPRECATED in v7 in favor of tree.verticality.Verticality

    A Verticality (previously called “vertical slice”)
    object provides more accessible information about
    vertical moments in a score. A Verticality is
    instantiated by passing in a dictionary of
    the form {partNumber: [ music21Objects ] }

    Verticalities are useful to provide direct and easy access to objects in a part.
    A list of Verticalities, although similar to the list of chords from a chordified score,
    provides easier access to part number
    information and identity of objects in the score. Plus, the objects in a
    Verticality point directly
    to the objects in the score, so modifying a Verticality taken from a
    score is the same as modifying the elements
    of the Verticality in the score directly.

    ```python
    >>> vs1 = voiceLeading.Verticality({0: [note.Note('A4'), harmony.ChordSymbol('Cm')],
    ...                                 1: [note.Note('F2')]})
    >>> vs1.getObjectsByClass(note.Note)
    [<music21.note.Note A>, <music21.note.Note F>]
    >>> vs1.getObjectsByPart(0, note.Note)
    <music21.note.Note A>
    ```

[`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality") read-only properties

Verticality.objects
:   return a list of all the music21 objects in the Verticality

    ```python
    >>> vs1 = voiceLeading.Verticality({0: [harmony.ChordSymbol('C'), note.Note('A4'),],
    ...                                 1: [note.Note('C')]})
    >>> vs1.objects
    [<music21.harmony.ChordSymbol C>, <music21.note.Note A>, <music21.note.Note C>]
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality") read/write properties

Verticality.color
:   sets the color of each element in the Verticality

    ```python
    >>> vs1 = voiceLeading.Verticality({1:note.Note('C'), 2:harmony.ChordSymbol('D')})
    >>> vs1.color = 'blue'
    >>> [(x, x.style.color) for x in vs1.objects]
    [(<music21.note.Note C>, 'blue'), (<music21.harmony.ChordSymbol D>, 'blue')]
    ```

Verticality.lyric
:   sets each object on the Verticality to have the passed in lyric

    ```python
    >>> h = voiceLeading.Verticality({1: note.Note('C'), 2: harmony.ChordSymbol('C')})
    >>> h.lyric = 'Verticality 1'
    >>> h.getStream().flatten().getElementsByClass(note.Note).first().lyric
    'Verticality 1'
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality") methods

Verticality.changeDurationOfAllObjects(*newQuarterLength*)[[source]](../_modules/music21/voiceLeading.html#Verticality.changeDurationOfAllObjects)
:   changes the duration of all objects in Verticality

    ```python
    >>> n1 =  note.Note('C4')
    >>> n1.quarterLength = 1
    >>> n2 =  note.Note('G4')
    >>> n2.quarterLength = 2
    >>> cs = harmony.ChordSymbol('C')
    >>> cs.quarterLength = 4
    >>> vs1 = voiceLeading.Verticality({0:n1, 1:n2, 2:cs})
    >>> vs1.changeDurationOfAllObjects(1.5)
    >>> [x.quarterLength for x in vs1.objects]
    [1.5, 1.5, 1.5]
    ```

    Note: capitalization of function changed in v5.7

Verticality.getChord()[[source]](../_modules/music21/voiceLeading.html#Verticality.getChord)
:   extracts all simultaneously sounding pitches (from chords, notes, harmony objects, etc.)
    and returns
    as a chord. Pretty much returns the Verticality to a chordified output.

    ```python
    >>> N = note.Note
    >>> vs1 = voiceLeading.Verticality({0:N('A4'), 1:chord.Chord(['B', 'C', 'A']), 2:N('A')})
    >>> vs1.getChord()
    <music21.chord.Chord A4 B C A A>
    >>> voiceLeading.Verticality({0:N('A3'),
    ...                           1:chord.Chord(['F3', 'D4', 'A4']),
    ...                           2:harmony.ChordSymbol('Am')}).getChord()
    <music21.chord.Chord A3 F3 D4 A4 A2 C3 E3>
    ```

Verticality.getLongestDuration()[[source]](../_modules/music21/voiceLeading.html#Verticality.getLongestDuration)
:   returns the longest duration that exists among all elements

    ```python
    >>> n1 =  note.Note('C4')
    >>> n1.quarterLength = 1
    >>> n2 =  note.Note('G4')
    >>> n2.quarterLength = 2
    >>> cs = harmony.ChordSymbol('C')
    >>> cs.quarterLength = 4
    >>> vs1 = voiceLeading.Verticality({0:n1, 1:n2, 2:cs})
    >>> vs1.getLongestDuration()
    4.0
    ```

Verticality.getObjectsByClass(*classFilterList*, *partNums=None*)[[source]](../_modules/music21/voiceLeading.html#Verticality.getObjectsByClass)
:   returns a list of all objects in the Verticality of a type contained
    in the classFilterList. Optionally
    specify part numbers to only search for matching objects

    ```python
    >>> N = note.Note
    >>> vs1 = voiceLeading.Verticality({0: [N('A4'), harmony.ChordSymbol('C')],
    ...                                 1: [N('C')],
    ...                                 2: [N('B'), N('F#')]})
    >>> vs1.getObjectsByClass('Note')
    [<music21.note.Note A>, <music21.note.Note C>,
     <music21.note.Note B>, <music21.note.Note F#>]
    >>> vs1.getObjectsByClass('Note', [1, 2])
    [<music21.note.Note C>, <music21.note.Note B>, <music21.note.Note F#>]
    ```

Verticality.getObjectsByPart(*partNum*, *classFilterList=None*)[[source]](../_modules/music21/voiceLeading.html#Verticality.getObjectsByPart)
:   returns the list of music21 objects associated with a given part number
    (if more than one). returns
    the single object if only one. Optionally specify which
    type of objects to return with classFilterList

    ```python
    >>> vs1 = voiceLeading.Verticality({0: [note.Note('A4'), harmony.ChordSymbol('C')],
    ...                                 1: [note.Note('C')]})
    >>> vs1.getObjectsByPart(0, classFilterList=['Harmony'])
    <music21.harmony.ChordSymbol C>
    >>> vs1.getObjectsByPart(0)
    [<music21.note.Note A>, <music21.harmony.ChordSymbol C>]
    >>> vs1.getObjectsByPart(1)
    <music21.note.Note C>
    ```

Verticality.getShortestDuration()[[source]](../_modules/music21/voiceLeading.html#Verticality.getShortestDuration)
:   returns the smallest quarterLength that exists among all elements

    ```python
    >>> n1 =  note.Note('C4')
    >>> n1.quarterLength = 1
    >>> n2 =  note.Note('G4')
    >>> n2.quarterLength = 2
    >>> cs = harmony.ChordSymbol('C')
    >>> cs.quarterLength = 4
    >>> vs1 = voiceLeading.Verticality({0:n1, 1:n2, 2:cs})
    >>> vs1.getShortestDuration()
    1.0
    ```

Verticality.getStream()[[source]](../_modules/music21/voiceLeading.html#Verticality.getStream)
:   returns a stream representation of this Verticality. Correct key, meter, and time
    signatures will be included if they are found in the context of the first part

    ```python
    >>> vs1 = voiceLeading.Verticality({0: [harmony.ChordSymbol('C'), note.Note('A4'),],
    ...                                 1: [note.Note('C')]})
    >>> vsStream = vs1.getStream()
    >>> vsStream.show('text')
    {0.0} <music21.stream.Part part-0>
        {0.0} <music21.harmony.ChordSymbol C>
        {0.0} <music21.note.Note A>
    {0.0} <music21.stream.Part part-1>
        {0.0} <music21.note.Note C>
    ```

    How many notes are there anywhere in the hierarchy?

    ```python
    >>> len(vsStream[note.Note])
    2
    >>> len(vsStream[harmony.Harmony])
    1
    ```

Verticality.getVerticalityOffset(*\**, *leftAlign=True*)[[source]](../_modules/music21/voiceLeading.html#Verticality.getVerticalityOffset)
:   returns the overall offset of the Verticality. Typically, this would just be the
    offset of each object in the Verticality,
    and each object would have the same offset.
    However, if the duration of one object in the slice is different from
    the duration of another,
    and that other starts after the first, but the first is still sounding, then the
    offsets would be
    different. In this case, specify leftAlign=True to return the lowest valued-offset
    of all the objects
    in the Verticality. If you prefer the offset of the right-most starting object,
    then specify leftAlign=False

    ```python
    >>> s = stream.Score()
    >>> n1 = note.Note('A4', quarterLength=1.0)
    >>> s.append(n1)
    >>> n1.offset
    0.0
    >>> n2 = note.Note('F2', quarterLength =0.5)
    >>> s.append(n2)
    >>> n2.offset
    1.0
    >>> vs = voiceLeading.Verticality({0:n1, 1: n2})
    >>> vs.getObjectsByClass(note.Note)
    [<music21.note.Note A>, <music21.note.Note F>]
    ```

    ```python
    >>> vs.getVerticalityOffset(leftAlign=True)
    0.0
    >>> vs.getVerticalityOffset(leftAlign=False)
    1.0
    ```

    * Changed in v8: renamed getVerticalityOffset to not conflict with
      :   .offset property. Made leftAlign keyword only

Verticality.isConsonant()[[source]](../_modules/music21/voiceLeading.html#Verticality.isConsonant)
:   evaluates whether this Verticality moment is consonant or dissonant
    according to the common-practice
    consonance rules. Method generates chord of all simultaneously sounding pitches, then calls
    `isConsonant()`

    ```python
    >>> V = voiceLeading.Verticality
    >>> N = note.Note
    >>> V({0: N('A4'), 1: N('B4'), 2: N('A4')}).isConsonant()
    False
    >>> V({0: N('A4'), 1: N('B4'), 2: N('C#4')}).isConsonant()
    False
    >>> V({0: N('C3'), 1: N('G5'), 2: chord.Chord(['C3', 'E4', 'G5'])}).isConsonant()
    True
    >>> V({0: N('A3'), 1: N('B3'), 2: N('C4')}).isConsonant()
    False
    >>> V({0: N('C1'), 1: N('C2'), 2: N('C3'),
    ...    3: N('G1'), 4: N('G2'), 5: N('G3')}).isConsonant()
    True
    >>> V({0: N('A3'), 1: harmony.ChordSymbol('Am')}).isConsonant()
    True
    ```

Verticality.makeAllLargestDuration()[[source]](../_modules/music21/voiceLeading.html#Verticality.makeAllLargestDuration)
:   locates the largest duration of all elements in the Verticality
    and assigns this duration
    to each element

    ```python
    >>> n1 =  note.Note('C4')
    >>> n1.quarterLength = 1
    >>> n2 =  note.Note('G4')
    >>> n2.quarterLength = 2
    >>> cs = harmony.ChordSymbol('C')
    >>> cs.quarterLength = 4
    >>> vs1 = voiceLeading.Verticality({0:n1, 1:n2, 2:cs})
    >>> vs1.makeAllLargestDuration()
    >>> [x.quarterLength for x in vs1.objects]
    [4.0, 4.0, 4.0]
    ```

Verticality.makeAllSmallestDuration()[[source]](../_modules/music21/voiceLeading.html#Verticality.makeAllSmallestDuration)
:   locates the smallest duration of all elements in the Verticality
    and assigns this duration
    to each element

    ```python
    >>> n1 =  note.Note('C4')
    >>> n1.quarterLength = 1
    >>> n2 =  note.Note('G4')
    >>> n2.quarterLength = 2
    >>> cs = harmony.ChordSymbol('C')
    >>> cs.quarterLength = 4
    >>> vs1 = voiceLeading.Verticality({0:n1, 1:n2, 2:cs})
    >>> vs1.makeAllSmallestDuration()
    >>> [x.quarterLength for x in vs1.objects]
    [1.0, 1.0, 1.0]
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality") instance variables

Verticality.contentDict
:   Dictionary representing contents of Verticalities.
    the keys of the dictionary
    are the part numbers and the element at each key is a list of
    music21 objects (allows for multiple voices
    in a single part)

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## VerticalityNTuplet

class music21.voiceLeading.VerticalityNTuplet(*listOfVerticalities=()*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#VerticalityNTuplet)
:   a collection of n number of Verticalities. These objects are useful when
    analyzing counterpoint
    motion and music theory elements such as passing tones

[`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MotionType

class music21.voiceLeading.MotionType(*\*values*)[[source]](../_modules/music21/voiceLeading.html#MotionType)

## NChordLinearSegment

class music21.voiceLeading.NChordLinearSegment(*chordList=()*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#NChordLinearSegment)

[`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment") bases

* [`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment") read-only properties

NChordLinearSegment.chordList
:   Returns a list of all chord symbols in this linear segment.
    Modifying the list does not change the linear segment.

    ```python
    >>> n = voiceLeading.NChordLinearSegment([harmony.ChordSymbol('Am'),
    ...                                       harmony.ChordSymbol('F7'),
    ...                                       harmony.ChordSymbol('G9')])
    >>> n.chordList
    [<music21.harmony.ChordSymbol Am>,
     <music21.harmony.ChordSymbol F7>,
     <music21.harmony.ChordSymbol G9>]
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## NNoteLinearSegment

class music21.voiceLeading.NNoteLinearSegment(*noteList=()*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#NNoteLinearSegment)
:   a list of n notes strung together in a sequence
    noteList = [note1, note2, note3, …, note-n ] Once this
    object is created with a noteList, the noteList may not
    be changed

    ```python
    >>> n = voiceLeading.NNoteLinearSegment(['A', 'C', 'D'])
    >>> n.noteList
    [<music21.note.Note A>, <music21.note.Note C>, <music21.note.Note D>]
    ```

[`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment") read-only properties

NNoteLinearSegment.melodicIntervals
:   calculates the melodic intervals and returns them as a list,
    with the interval at 0 being the interval between the first and second note.

    ```python
    >>> linSeg = voiceLeading.NNoteLinearSegment([note.Note('A'), note.Note('B'),
    ...            note.Note('C'), note.Note('D')])
    >>> linSeg.melodicIntervals
    [<music21.interval.Interval M2>,
     <music21.interval.Interval M-7>,
     <music21.interval.Interval M2>]
    ```

NNoteLinearSegment.noteList
:   Read-only property – returns a copy of the list of notes in the
    linear segment.

    ```python
    >>> n = voiceLeading.NNoteLinearSegment(['A', 'B5', 'C', 'F#'])
    >>> n.noteList
    [<music21.note.Note A>, <music21.note.Note B>,
     <music21.note.Note C>, <music21.note.Note F#>]
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`NNoteLinearSegment`](#music21.voiceLeading.NNoteLinearSegment "music21.voiceLeading.NNoteLinearSegment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## NObjectLinearSegment

class music21.voiceLeading.NObjectLinearSegment(*objectList=()*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#NObjectLinearSegment)

[`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TwoChordLinearSegment

class music21.voiceLeading.TwoChordLinearSegment(*chordList=()*, *chord2=None*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#TwoChordLinearSegment)

[`TwoChordLinearSegment`](#music21.voiceLeading.TwoChordLinearSegment "music21.voiceLeading.TwoChordLinearSegment") bases

* [`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment")
* [`NObjectLinearSegment`](#music21.voiceLeading.NObjectLinearSegment "music21.voiceLeading.NObjectLinearSegment")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TwoChordLinearSegment`](#music21.voiceLeading.TwoChordLinearSegment "music21.voiceLeading.TwoChordLinearSegment") read-only properties

Read-only properties inherited from [`NChordLinearSegment`](#music21.voiceLeading.NChordLinearSegment "music21.voiceLeading.NChordLinearSegment"):

|  |  |  |
| --- | --- | --- |
| * [`chordList`](#music21.voiceLeading.NChordLinearSegment.chordList "music21.voiceLeading.NChordLinearSegment.chordList") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TwoChordLinearSegment`](#music21.voiceLeading.TwoChordLinearSegment "music21.voiceLeading.TwoChordLinearSegment") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TwoChordLinearSegment`](#music21.voiceLeading.TwoChordLinearSegment "music21.voiceLeading.TwoChordLinearSegment") methods

TwoChordLinearSegment.bassInterval()[[source]](../_modules/music21/voiceLeading.html#TwoChordLinearSegment.bassInterval)
:   returns the chromatic interval between the basses of the two chord symbols

    ```python
    >>> h = voiceLeading.TwoChordLinearSegment(harmony.ChordSymbol('C/E'),
    ...                                        harmony.ChordSymbol('G'))
    >>> h.bassInterval()
    <music21.interval.ChromaticInterval 3>
    ```

TwoChordLinearSegment.rootInterval()[[source]](../_modules/music21/voiceLeading.html#TwoChordLinearSegment.rootInterval)
:   returns the chromatic interval between the roots of the two chord symbols

    ```python
    >>> h = voiceLeading.TwoChordLinearSegment([harmony.ChordSymbol('C'),
    ...                                         harmony.ChordSymbol('G')])
    >>> h.rootInterval()
    <music21.interval.ChromaticInterval 7>
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TwoChordLinearSegment`](#music21.voiceLeading.TwoChordLinearSegment "music21.voiceLeading.TwoChordLinearSegment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## VerticalityTriplet

class music21.voiceLeading.VerticalityTriplet(*listOfVerticalities=()*, *\*\*keywords*)[[source]](../_modules/music21/voiceLeading.html#VerticalityTriplet)
:   a collection of three Verticalities

[`VerticalityTriplet`](#music21.voiceLeading.VerticalityTriplet "music21.voiceLeading.VerticalityTriplet") bases

* [`VerticalityNTuplet`](#music21.voiceLeading.VerticalityNTuplet "music21.voiceLeading.VerticalityNTuplet")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`VerticalityTriplet`](#music21.voiceLeading.VerticalityTriplet "music21.voiceLeading.VerticalityTriplet") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`VerticalityTriplet`](#music21.voiceLeading.VerticalityTriplet "music21.voiceLeading.VerticalityTriplet") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`VerticalityTriplet`](#music21.voiceLeading.VerticalityTriplet "music21.voiceLeading.VerticalityTriplet") methods

VerticalityTriplet.hasNeighborTone(*partNumToIdentify*, *unaccentedOnly=False*)[[source]](../_modules/music21/voiceLeading.html#VerticalityTriplet.hasNeighborTone)
:   return true if this Verticality triplet contains a neighbor tone
    music21 currently identifies neighbor tones by analyzing both horizontal motion
    and vertical motion.
    It first checks to see if the note could be a neighbor tone based on the notes
    linearly adjacent to it.
    It then checks to see if the note’s vertical context is dissonant,
    while the Verticalities
    to the left and right are consonant

    partNum is the part (starting with 0) to identify the passing tone
    for use on 3 Verticalities (3-tuplet)

    ```python
    >>> vs1 = voiceLeading.Verticality({0:note.Note('E-4'), 1: note.Note('C3')})
    >>> vs2 = voiceLeading.Verticality({0:note.Note('E-4'), 1: note.Note('B2')})
    >>> vs3 = voiceLeading.Verticality({0:note.Note('C5'), 1: note.Note('C3')})
    >>> vt = voiceLeading.VerticalityTriplet([vs1, vs2, vs3])
    >>> vt.hasNeighborTone(1)
    True
    ```

VerticalityTriplet.hasPassingTone(*partNumToIdentify*, *unaccentedOnly=False*)[[source]](../_modules/music21/voiceLeading.html#VerticalityTriplet.hasPassingTone)
:   return true if this Verticality triplet contains a passing tone
    music21 currently identifies passing tones by analyzing both horizontal motion
    and vertical motion.
    It first checks to see if the note could be a passing tone based on the notes
    linearly adjacent to it.
    It then checks to see if the note’s vertical context is dissonant, while the
    Verticalities
    to the left and right are consonant

    partNum is the part (starting with 0) to identify the passing tone

    ```python
    >>> vs1 = voiceLeading.Verticality({0:note.Note('A4'), 1:note.Note('F2')})
    >>> vs2 = voiceLeading.Verticality({0:note.Note('B-4'), 1:note.Note('F2')})
    >>> vs3 = voiceLeading.Verticality({0:note.Note('C5'), 1:note.Note('E2')})
    >>> vt = voiceLeading.VerticalityTriplet([vs1, vs2, vs3])
    >>> vt.hasPassingTone(0)
    True
    >>> vt.hasPassingTone(1)
    False
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`VerticalityTriplet`](#music21.voiceLeading.VerticalityTriplet "music21.voiceLeading.VerticalityTriplet") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.voiceLeading.getVerticalityFromObject(*music21Obj*, *scoreObjectIsFrom*, *classFilterList=None*)[[source]](../_modules/music21/voiceLeading.html#getVerticalityFromObject)
:   returns the [`Verticality`](#music21.voiceLeading.Verticality "music21.voiceLeading.Verticality") object given a score,
    and a music21 object within this score
    (under development)

    ```python
    >>> c = corpus.parse('bach/bwv66.6')
    >>> n1 = c.flatten().getElementsByClass(note.Note).first()
    >>> voiceLeading.getVerticalityFromObject(n1, c)
    <music21.voiceLeading.Verticality
        contentDict={0: [<music21.instrument.Instrument 'P1: Soprano: Instrument 1'>,
                         <music21.clef.TrebleClef>,
                         <music21.tempo.MetronomeMark Quarter=96 (playback only)>,
                         <music21.key.Key of f# minor>,
                         <music21.meter.TimeSignature 4/4>,
                         <music21.note.Note C#>],
              1: [<music21.instrument.Instrument 'P2: Alto: Instrument 2'>,
                  <music21.clef.TrebleClef>,
                  <music21.tempo.MetronomeMark Quarter=96 (playback only)>,
                  <music21.key.Key of f# minor>,
                  <music21.meter.TimeSignature 4/4>,
                  <music21.note.Note E>],
              2: [<music21.instrument.Instrument 'P3: Tenor: Instrument 3'>,
                  <music21.clef.BassClef>,
                  <music21.tempo.MetronomeMark Quarter=96 (playback only)>,
                  <music21.key.Key of f# minor>,
                  <music21.meter.TimeSignature 4/4>,
                  <music21.note.Note A>],
              3: [<music21.instrument.Instrument 'P4: Bass: Instrument 4'>,
                  <music21.clef.BassClef>,
                  <music21.tempo.MetronomeMark Quarter=96 (playback only)>,
                  <music21.key.Key of f# minor>,
                  <music21.meter.TimeSignature 4/4>,
                  <music21.note.Note A>]}>
    ```

    for getting things at the beginning of scores, probably better to use a classFilterList:

    ```python
    >>> voiceLeading.getVerticalityFromObject(n1, c,
    ...                      classFilterList=[note.Note, chord.Chord, note.Rest])
    <music21.voiceLeading.Verticality contentDict={0: [<music21.note.Note C#>],
              1: [<music21.note.Note E>],
              2: [<music21.note.Note A>],
              3: [<music21.note.Note A>]}>
    ```

music21.voiceLeading.iterateAllVoiceLeadingQuartets(*s: stream.Stream*, *\**, *includeRests: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *includeOblique: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *includeNoMotion: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *reverse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → Generator[[VoiceLeadingQuartet](#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/voiceLeading.html#iterateAllVoiceLeadingQuartets)
:   Iterate through all VoiceLeading quartets in a Stream (generally a Score),
    yielding a generator of VoiceLeadingQuartets. N.B. does not yet support Streams with
    Chords in them.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> for vlq in voiceLeading.iterateAllVoiceLeadingQuartets(b):
    ...     print(vlq.v1n1.measureNumber,
    ...           vlq.v1n1.getContextByClass(stream.Part).id,
    ...           vlq.v2n1.getContextByClass(stream.Part).id,
    ...           vlq)
    0 Soprano Tenor <music21.voiceLeading.VoiceLeadingQuartet v1n1=B4, v1n2=A4, v2n1=B3, v2n2=C#4>
    0 Soprano Bass <music21.voiceLeading.VoiceLeadingQuartet v1n1=B4, v1n2=A4, v2n1=G#3, v2n2=F#3>
    0 Tenor Bass <music21.voiceLeading.VoiceLeadingQuartet v1n1=B3, v1n2=C#4, v2n1=G#3, v2n2=F#3>
    1 Soprano Alto <music21.voiceLeading.VoiceLeadingQuartet v1n1=A4, v1n2=B4, v2n1=F#4, v2n2=E4>
    1 Soprano Tenor <music21.voiceLeading.VoiceLeadingQuartet v1n1=A4, v1n2=B4, v2n1=C#4, v2n2=B3>
    1 Soprano Bass <music21.voiceLeading.VoiceLeadingQuartet v1n1=A4, v1n2=B4, v2n1=F#3, v2n2=G#3>
    1 Alto Tenor <music21.voiceLeading.VoiceLeadingQuartet v1n1=F#4, v1n2=E4, v2n1=C#4, v2n2=B3>
    1 Alto Bass <music21.voiceLeading.VoiceLeadingQuartet v1n1=F#4, v1n2=E4, v2n1=F#3, v2n2=G#3>
    ...
    ```
