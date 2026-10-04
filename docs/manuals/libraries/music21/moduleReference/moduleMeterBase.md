Source: https://music21.org/music21docs/moduleReference/moduleMeterBase.html

# music21.meter.base

This module defines the `TimeSignature` object,
as well as component objects for defining nested metrical structures,
`MeterTerminal` and `MeterSequence` objects.

## TimeSignature

class music21.meter.base.TimeSignature(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '4/4'*, *divisions=None*, *\*\*keywords*)[[source]](../_modules/music21/meter/base.html#TimeSignature)
:   The TimeSignature object represents time signatures in musical scores
    (4/4, 3/8, 2/4+5/16, Cut, etc.).

    TimeSignatures should be present in the first Measure of each Part
    that they apply to. Alternatively you can put the time signature at the
    front of a Part or at the beginning of a Score, and they will work
    within music21, but they won’t necessarily display properly in MusicXML,
    Lilypond, etc. So best is to create structures where the TimeSignature
    goes in the first Measure of the score, as below:

    ```python
    >>> s = stream.Score()
    >>> p = stream.Part()
    >>> m1 = stream.Measure()
    >>> ts = meter.TimeSignature('3/4')
    >>> m1.insert(0, ts)
    >>> m1.insert(0, note.Note('C#3', type='half'))
    >>> n = note.Note('D3', type='quarter')
    >>> m1.insert(1.0, n)
    >>> m1.number = 1
    >>> p.insert(0, m1)
    >>> s.insert(0, p)
    >>> s.show('t')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.meter.TimeSignature 3/4>
            {0.0} <music21.note.Note C#>
            {1.0} <music21.note.Note D>
    ```

    Basic operations on a TimeSignature object are designed to be very simple.

    ```python
    >>> ts.ratioString
    '3/4'
    ```

    ```python
    >>> ts.numerator
    3
    ```

    ```python
    >>> ts.beatCount
    3
    ```

    ```python
    >>> ts.beatCountName
    'Triple'
    ```

    ```python
    >>> ts.beatDuration.quarterLength
    1.0
    ```

    As an alternative to putting a TimeSignature in a Stream at a specific
    position (offset), it can be assigned to a special property in Measure that
    positions the TimeSignature at the start of a Measure. Notice that when we
    show() the Measure (or if we iterate through it), the TimeSignature
    appears as if it’s in the measure itself:

    ```python
    >>> m2 = stream.Measure()
    >>> m2.number = 2
    >>> ts2 = meter.TimeSignature('2/4')
    >>> m2.timeSignature = ts2
    >>> m2.append(note.Note('E3', type='half'))
    >>> p.append(m2)
    >>> s.show('text')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.meter.TimeSignature 3/4>
            {0.0} <music21.note.Note C#>
            {1.0} <music21.note.Note D>
        {2.0} <music21.stream.Measure 2 offset=2.0>
            {0.0} <music21.meter.TimeSignature 2/4>
            {0.0} <music21.note.Note E>
    ```

    Once a Note has a local TimeSignature, a Note can get its beat position and
    other meter-specific parameters. Remember n, our quarter note at offset
    2.0 of m1, a 3/4 measure? Let’s get its beat:

    ```python
    >>> n.beat
    2.0
    ```

    This feature is more useful if there are more beats:

    ```python
    >>> m3 = stream.Measure()
    >>> m3.timeSignature = meter.TimeSignature('3/4')
    >>> eighth = note.Note(type='eighth')
    >>> m3.repeatAppend(eighth, 6)
    >>> [thisNote.beatStr for thisNote in m3.notes]
    ['1', '1 1/2', '2', '2 1/2', '3', '3 1/2']
    ```

    Now lets change its measure’s TimeSignature and see what happens:

    ```python
    >>> sixEight = meter.TimeSignature('6/8')
    >>> m3.timeSignature = sixEight
    >>> [thisNote.beatStr for thisNote in m3.notes]
    ['1', '1 1/3', '1 2/3', '2', '2 1/3', '2 2/3']
    ```

    TimeSignature(‘6/8’) defaults to fast 6/8:

    ```python
    >>> sixEight.beatCount
    2
    ```

    ```python
    >>> sixEight.beatDuration.quarterLength
    1.5
    ```

    ```python
    >>> sixEight.beatDivisionCountName
    'Compound'
    ```

    Let’s make it slow 6/8 instead:

    ```python
    >>> sixEight.beatCount = 6
    >>> sixEight.beatDuration.quarterLength
    0.5
    ```

    ```python
    >>> sixEight.beatDivisionCountName
    'Simple'
    ```

    Now let’s look at the beatStr for each of the notes in m3:

    ```python
    >>> [thisNote.beatStr for thisNote in m3.notes]
    ['1', '2', '3', '4', '5', '6']
    ```

    As of v7, 3/8 also defaults to fast 3/8, that is, one beat:

    ```python
    >>> meter.TimeSignature('3/8').beatCount
    1
    ```

    TimeSignatures can also use symbols instead of numbers

    ```python
    >>> tsCommon = meter.TimeSignature('c')  # or common
    >>> tsCommon.beatCount
    4
    >>> tsCommon.denominator
    4
    ```

    ```python
    >>> tsCommon.symbol
    'common'
    ```

    ```python
    >>> tsCut = meter.TimeSignature('cut')
    >>> tsCut.beatCount
    2
    >>> tsCut.denominator
    2
    ```

    ```python
    >>> tsCut.symbol
    'cut'
    ```

    For other time signatures, the symbol is ‘’ (not set) or ‘normal’

    ```python
    >>> sixEight.symbol
    ''
    ```

    For complete details on using this object, see
    [User’s Guide Chapter 14: Time Signatures](../usersGuide/usersGuide_14_timeSignatures.html#usersguide-14-timesignatures) and
    [User’s Guide Chapter 55: Advanced Meter](../usersGuide/usersGuide_55_advancedMeter.html#usersguide-55-advancedmeter) and

    That’s it for the simple aspects of TimeSignature objects. You know
    enough to get started now!

    Under the hood, they’re extremely powerful. For musicians, TimeSignatures
    do (at least) three different things:

    * They define where the beats in the measure are and how many there are.
    * They indicate how the notes should be beamed
    * They give a sense of how much accent or weight each note gets, which
      also defines which are important notes and which might be ornaments.

    These three aspects of TimeSignatures are controlled by the
    `beatSequence`,
    `beamSequence`, and
    `accentSequence` properties of the
    TimeSignature. Each of them is an independent
    `MeterSequence` element which might have nested
    properties (e.g., an 11/16 meter might be beamed as {1/4+1/4+{1/8+1/16}}),
    so if you want to change how beats are calculated or beams are generated
    you’ll want to learn more about meter.MeterSequence objects.

    There’s a fourth MeterSequence object inside a TimeSignature, and that is
    the `displaySequence`. That determines
    how the TimeSignature should actually look on paper. Normally this
    MeterSequence is pretty simple. In ‘4/4’ it’s usually just ‘4/4’. But
    if you have the ‘11/16’ time above, you may want to have it displayed as
    ‘2/4+3/16’ or ‘11/16 (2/4+3/16)’. Or you might want the written
    TimeSignature to contradict what the notes imply. All this can be done
    with .displaySequence.

    **Equality**

    For two time signatures to be considered equal,
    they have the same name and internal structure.

    The name is tested by the `symbol`.
    This helps distinguish between ‘Cut’ and ‘2/2’, for example.

    ```python
    >>> tsCut = meter.TimeSignature('Cut')
    >>> ts22 = meter.TimeSignature('2/2')
    >>> tsCut == ts22
    False
    ```

    The internal structure is currently tested simply by the
    `beatCount` and
    `ratioString` attributes.

    The check of `beatCount`
    helps to distinguish the ‘fast’ (2-beat) from ‘slow’ (6-beat)
    versions of 6/8, for example.

    ```python
    >>> fast68 = meter.TimeSignature('fast 6/8')
    >>> slow68 = meter.TimeSignature('slow 6/8')
    >>> fast68 == slow68
    False
    ```

    Complementing this,
    `ratioString`
    provides a check of the internal divsions such that
    ‘2/8+3/8’ is different from ‘3/8+2/8’, for example,
    despite the fact that they could both be written as ‘5/8’.

    ```python
    >>> ts2n3 = meter.TimeSignature('2/8+3/8')
    >>> ts3n2 = meter.TimeSignature('3/8+2/8')
    >>> ts2n3 == ts3n2
    False
    ```

    For a less restrictive test of this, see
    `ratioEqual()`
    which returns True for all cases of ‘5/8’.

    ```python
    >>> ts2n3.ratioEqual(ts3n2)
    True
    ```

    Yes, equality is ever True:

    ```python
    >>> one44 = meter.TimeSignature('4/4')
    >>> another44 = meter.TimeSignature()  # '4/4' by default
    >>> one44 == another44
    True
    ```

[`TimeSignature`](#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") bases

* [`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TimeSignature`](#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") read-only properties

TimeSignature.beatCountName
:   Return the beat count name, or the name given for the number of beat units.
    For example, 2/4 is duple; 9/4 is triple.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatCountName
    'Triple'
    ```

    ```python
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatCountName
    'Duple'
    ```

TimeSignature.beatDivisionCount
:   Return the count of background beat units found within one beat,
    or the number of subdivisions in the beat unit in this TimeSignature.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatDivisionCount
    2
    ```

    ```python
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatDivisionCount
    3
    ```

    ```python
    >>> ts = meter.TimeSignature('15/8')
    >>> ts.beatDivisionCount
    3
    ```

    ```python
    >>> ts = meter.TimeSignature('3/8')
    >>> ts.beatDivisionCount
    1
    ```

    ```python
    >>> ts = meter.TimeSignature('13/8', 13)
    >>> ts.beatDivisionCount
    1
    ```

    * Changed in v7: return 1 instead of a TimeSignatureException.

TimeSignature.beatDivisionCountName
:   Return the beat count name, or the name given for the number of beat units.
    For example, 2/4 is duple; 9/4 is triple.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatDivisionCountName
    'Simple'
    ```

    ```python
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatDivisionCountName
    'Compound'
    ```

    Rare cases of 5-beat divisions return ‘Other’, like this 10/8 divided into
    5/8 + 5/8 with no further subdivisions:

    ```python
    >>> ts = meter.TimeSignature('10/8')
    >>> ts.beatSequence.partition(2)
    >>> ts.beatSequence
    <music21.meter.core.MeterSequence {5/8+5/8}>
    >>> for i, mt in enumerate(ts.beatSequence):
    ...     ts.beatSequence[i] = mt.subdivideByCount(5)
    >>> ts.beatSequence
    <music21.meter.core.MeterSequence {{1/8+1/8+1/8+1/8+1/8}+{1/8+1/8+1/8+1/8+1/8}}>
    >>> ts.beatDivisionCountName
    'Other'
    ```

TimeSignature.beatDivisionDurations
:   Return the beat division, or the durations that make up one beat,
    as a list of [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") objects, if and only if
    the TimeSignature has a uniform beat division for all beats.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatDivisionDurations
    [<music21.duration.Duration 0.5>,
     <music21.duration.Duration 0.5>]
    ```

    ```python
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatDivisionDurations
    [<music21.duration.Duration 0.5>,
     <music21.duration.Duration 0.5>,
     <music21.duration.Duration 0.5>]
    ```

    Value returned of non-uniform beat divisions will change at any time
    after v7.1 to avoid raising an exception.

TimeSignature.beatDuration
:   Return a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object equal to the beat unit
    of this Time Signature, if and only if this TimeSignature has a uniform beat unit.

    Otherwise, raises an exception in v7.1 but will change to returning NaN
    soon fasterwards.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatDuration
    <music21.duration.Duration 1.0>
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatDuration
    <music21.duration.Duration 1.5>
    ```

    ```python
    >>> ts = meter.TimeSignature('7/8')
    >>> ts.beatDuration
    <music21.duration.Duration 0.5>
    ```

    ```python
    >>> ts = meter.TimeSignature('3/8')
    >>> ts.beatDuration
    <music21.duration.Duration 1.5>
    >>> ts.beatCount = 3
    >>> ts.beatDuration
    <music21.duration.Duration 0.5>
    ```

    Cannot do this because of asymmetry

    ```python
    >>> ts = meter.TimeSignature('2/4+3/16')
    >>> ts.beatDuration
    Traceback (most recent call last):
    music21.exceptions21.TimeSignatureException: non-uniform beat unit: [2.0, 0.75]
    ```

    * Changed in v7: return NaN rather than raising Exception in property.

TimeSignature.beatLengthToQuarterLengthRatio
:   Returns 4.0 / denominator. Might seem a bit silly but used often.

    ```python
    >>> a = meter.TimeSignature('3/2')
    >>> a.beatLengthToQuarterLengthRatio
    2.0
    ```

TimeSignature.beatSubDivisionDurations
:   Return a subdivision of the beat division, or a list
    of [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") objects representing each beat division
    divided by two.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatSubDivisionDurations
    [<music21.duration.Duration 0.25>, <music21.duration.Duration 0.25>,
     <music21.duration.Duration 0.25>, <music21.duration.Duration 0.25>]
    ```

    ```python
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatSubDivisionDurations
    [<music21.duration.Duration 0.25>, <music21.duration.Duration 0.25>,
     <music21.duration.Duration 0.25>, <music21.duration.Duration 0.25>,
     <music21.duration.Duration 0.25>, <music21.duration.Duration 0.25>]
    ```

TimeSignature.classification
:   Return the classification of this TimeSignature,
    such as Simple Triple or Compound Quadruple.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.classification
    'Simple Triple'
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.classification
    'Compound Duple'
    >>> ts = meter.TimeSignature('4/32')
    >>> ts.classification
    'Simple Quadruple'
    ```

TimeSignature.quarterLengthToBeatLengthRatio
:   Returns denominator/4.0.

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TimeSignature`](#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") read/write properties

TimeSignature.barDuration
:   Return a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object equal to the
    total length of this TimeSignature.

    ```python
    >>> ts = meter.TimeSignature('5/16')
    >>> ts.barDuration
    <music21.duration.Duration 1.25>
    ```

    ```python
    >>> ts2 = meter.TimeSignature('3/8')
    >>> d = ts2.barDuration
    >>> d.type
    'quarter'
    >>> d.dots
    1
    >>> d.quarterLength
    1.5
    ```

    This can be overridden to create different representations
    or to contradict the meter.

    ```python
    >>> d2 = duration.Duration(1.75)
    >>> ts2.barDuration = d2
    >>> ts2.barDuration
    <music21.duration.Duration 1.75>
    ```

    An uninitialized TimeSignature returns 4.0 for 4/4

    ```python
    >>> meter.TimeSignature().barDuration
    <music21.duration.Duration 4.0>
    ```

TimeSignature.beatCount
:   Return or set the count of beat units, or the number of beats in this TimeSignature.

    When setting beat units, one level of sub-partitions is automatically defined.
    Users can specify beat count values as integers or as lists of durations.
    For more precise configuration of the beat MeterSequence,
    manipulate the .beatSequence attribute directly.

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatCount
    3
    >>> ts.beatDuration.quarterLength
    1.0
    >>> ts.beatCount = [1, 1, 1, 1, 1, 1]
    >>> ts.beatCount
    6
    >>> ts.beatDuration.quarterLength
    0.5
    ```

    Setting a beat-count directly is a simple, high-level way to configure the beatSequence.
    Note that his may not configure lower level partitions correctly,
    and will raise an error if the provided beat count is not supported by the
    overall duration of the .beatSequence MeterSequence.

    ```python
    >>> ts = meter.TimeSignature('6/8')
    >>> ts.beatCount  # default is 2 beats
    2
    >>> ts.beatSequence
    <music21.meter.core.MeterSequence {{1/8+1/8+1/8}+{1/8+1/8+1/8}}>
    >>> ts.beatDivisionCountName
    'Compound'
    >>> ts.beatCount = 6
    >>> ts.beatSequence
    <music21.meter.core.MeterSequence
        {{1/16+1/16}+{1/16+1/16}+{1/16+1/16}+{1/16+1/16}+{1/16+1/16}+{1/16+1/16}}>
    >>> ts.beatDivisionCountName
    'Simple'
    >>> ts.beatCount = 123
    Traceback (most recent call last):
    music21.exceptions21.TimeSignatureException: cannot partition beat with provided value: 123
    ```

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.beatCount = 6
    >>> ts.beatDuration.quarterLength
    0.5
    ```

TimeSignature.denominator
:   Return the denominator of the TimeSignature as a number or set it.

    (for complex TimeSignatures, note that this comes from the .beamSequence
    of the TimeSignature)

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.denominator
    4
    >>> ts.denominator = 8
    >>> ts.ratioString
    '3/8'
    ```

    In this following case, the TimeSignature is silently being converted to 9/8
    to get a single digit denominator:

    ```python
    >>> ts = meter.TimeSignature('2/4+5/8')
    >>> ts.denominator
    8
    ```

TimeSignature.numerator
:   Return the numerator of the TimeSignature as a number.

    Can set the numerator for a simple TimeSignature.
    To set the numerator of a complex TimeSignature, change beatCount.

    (for complex TimeSignatures, note that this comes from the .beamSequence
    of the TimeSignature)

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> ts.numerator
    3
    >>> ts.numerator = 5
    >>> ts
    <music21.meter.TimeSignature 5/4>
    ```

    In this case, the TimeSignature is silently being converted to 9/8
    to get a single digit numerator:

    ```python
    >>> ts = meter.TimeSignature('2/4+5/8')
    >>> ts.numerator
    9
    ```

    Setting a summed time signature’s numerator will change to a
    simple time signature

    ```python
    >>> ts.numerator = 11
    >>> ts
    <music21.meter.TimeSignature 11/8>
    ```

TimeSignature.ratioString
:   Returns or sets a simple string representing the time signature ratio.

    ```python
    >>> threeFour = meter.TimeSignature('3/4')
    >>> threeFour.ratioString
    '3/4'
    ```

    It can also be set to load a new one, but ‘.load()’ is better:

    ```python
    >>> threeFour.ratioString = '5/8'  # now this variable name is dumb!
    >>> threeFour.numerator
    5
    >>> threeFour.denominator
    8
    ```

    ```python
    >>> complexTime = meter.TimeSignature('2/4+3/8')
    >>> complexTime.ratioString
    '2/4+3/8'
    ```

    For advanced users, getting the ratioString is the equivalent of
    [`partitionDisplay`](moduleMeterCore.html#music21.meter.core.MeterSequence.partitionDisplay "music21.meter.core.MeterSequence.partitionDisplay") on the displaySequence:

    ```python
    >>> complexTime.displaySequence.partitionDisplay
    '2/4+3/8'
    ```

TimeSignature.summedNumerator

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TimeSignature`](#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") methods

TimeSignature.averageBeatStrength(*streamIn*, *notesOnly=True*)[[source]](../_modules/music21/meter/base.html#TimeSignature.averageBeatStrength)
:   returns a float of the average beat strength of all objects (or if notesOnly is True
    [default] only the notes) in the Stream specified as streamIn.

    ```python
    >>> s = converter.parse('C4 D4 E8 F8', format='tinyNotation').flatten().notes.stream()
    >>> sixEight = meter.TimeSignature('6/8')
    >>> sixEight.averageBeatStrength(s)
    0.4375
    >>> threeFour = meter.TimeSignature('3/4')
    >>> threeFour.averageBeatStrength(s)
    0.5625
    ```

    If notesOnly is False then test objects will give added
    weight to the beginning of the measure:

    ```python
    >>> sixEight.averageBeatStrength(s, notesOnly=False)
    0.4375
    >>> s.insert(0.0, clef.TrebleClef())
    >>> s.insert(0.0, clef.BassClef())
    >>> sixEight.averageBeatStrength(s, notesOnly=False)
    0.625
    ```

TimeSignature.getAccent(*qLenPos: OffsetQL*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/meter/base.html#TimeSignature.getAccent)
:   Return True or False if the qLenPos is at the start of an accent
    division.

    ```python
    >>> a = meter.TimeSignature('3/4', 3)
    >>> a.accentSequence.partition([2, 1])
    >>> a.accentSequence
    <music21.meter.core.MeterSequence {2/4+1/4}>
    >>> a.getAccent(0.0)
    True
    >>> a.getAccent(1.0)
    False
    >>> a.getAccent(2.0)
    True
    ```

TimeSignature.getAccentWeight(*qLenPos*, *level=0*, *forcePositionMatch=False*, *permitMeterModulus=False*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getAccentWeight)
:   Given a qLenPos, return an accent level. In general, accents are assumed to
    define only a first-level weight.

    If forcePositionMatch is True, an accent will only be returned if the
    provided qLenPos is a near exact match to the provided quarter length. Otherwise,
    half of the minimum quarter length will be provided.

    If permitMeterModulus is True, quarter length positions greater than
    the duration of the Meter will be accepted as the modulus of the total meter duration.

    ```python
    >>> ts1 = meter.TimeSignature('3/4')
    >>> [ts1.getAccentWeight(x) for x in range(3)]
    [1.0, 0.5, 0.5]
    ```

    Calling getAccentWeight on durations beyond the score returns an error:

    ```python
    >>> [ts1.getAccentWeight(x) for x in range(6)]
    Traceback (most recent call last):
    music21.exceptions21.MeterException: cannot access from qLenPos 3.0
        where total duration is 3.0
    ```

    The error is removed if permitMeterModulus is employed:

    ```python
    >>> [ts1.getAccentWeight(x, permitMeterModulus=True) for x in range(6)]
    [1.0, 0.5, 0.5, 1.0, 0.5, 0.5]
    ```

TimeSignature.getBeams(*srcList: stream.Stream | t.Sequence[[base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*, *measureStartOffset: OffsetQL = 0.0*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[beam.Beams](moduleBeam.html#music21.beam.Beams "music21.beam.Beams") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/meter/base.html#TimeSignature.getBeams)
:   Given a qLen position and an iterable of Music21Objects, return a list of Beams objects.

    The iterable can be a list (of elements) or a Stream (preferably flat)
    or a [`StreamIterator`](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator") from which Durations
    and information about note vs. rest will be
    extracted.

    Objects are assumed to be adjoining; offsets are not used, except for
    measureStartOffset()

    Must process a list/Stream at time, because we cannot tell when a beam ends
    unless we see the context of adjoining durations.

    ```python
    >>> a = meter.TimeSignature('2/4', 2)
    >>> a.beamSequence[0] = a.beamSequence[0].subdivide(2)
    >>> a.beamSequence[1] = a.beamSequence[1].subdivide(2)
    >>> a.beamSequence
    <music21.meter.core.MeterSequence {{1/8+1/8}+{1/8+1/8}}>
    >>> b = [note.Note(type='16th') for _ in range(8)]
    >>> c = a.getBeams(b)
    >>> len(c) == len(b)
    True
    >>> print(c)
    [<music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/stop>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/stop>/<music21.beam.Beam 2/stop>>,
     <music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/stop>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/stop>/<music21.beam.Beam 2/stop>>]
    ```

    ```python
    >>> a = meter.TimeSignature('6/8')
    >>> b = [note.Note(type='eighth') for _ in range(6)]
    >>> c = a.getBeams(b)
    >>> print(c)
    [<music21.beam.Beams <music21.beam.Beam 1/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>>,
     <music21.beam.Beams <music21.beam.Beam 1/stop>>,
     <music21.beam.Beams <music21.beam.Beam 1/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>>,
     <music21.beam.Beams <music21.beam.Beam 1/stop>>]
    ```

    ```python
    >>> fourFour = meter.TimeSignature('4/4')
    >>> nList = [note.Note(type=d) for d in ('eighth', 'quarter', 'eighth',
    ...                                      'eighth', 'quarter', 'eighth')]
    >>> beamList = fourFour.getBeams(nList)
    >>> print(beamList)
    [None, None, None, None, None, None]
    ```

    Pickup measure support included by taking in an additional measureStartOffset argument.

    ```python
    >>> twoTwo = meter.TimeSignature('2/2')
    >>> nList = [note.Note(type='eighth') for _ in range(5)]
    >>> beamList = twoTwo.getBeams(nList, measureStartOffset=1.5)
    >>> print(beamList)
    [None,
     <music21.beam.Beams <music21.beam.Beam 1/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>>,
     <music21.beam.Beams <music21.beam.Beam 1/continue>>,
     <music21.beam.Beams <music21.beam.Beam 1/stop>>]
    ```

    Fixed in v.7 – incomplete final measures in 6/8:

    ```python
    >>> sixEight = meter.TimeSignature('6/8')
    >>> nList = [note.Note(type='quarter'), note.Note(type='eighth'), note.Note(type='eighth')]
    >>> beamList = sixEight.getBeams(nList)
    >>> print(beamList)
    [None, None, None]
    ```

    And Measure objects with `paddingRight` set:

    ```python
    >>> twoFour = meter.TimeSignature('2/4')
    >>> m = stream.Measure([note.Note(type='eighth') for _ in range(3)])
    >>> m.paddingRight = 0.5
    >>> twoFour.getBeams(m)
    [<music21.beam.Beams <music21.beam.Beam 1/start>>,
     <music21.beam.Beams <music21.beam.Beam 1/stop>>,
     None]
    ```

TimeSignature.getBeat(*offset*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeat)
:   Given an offset (quarterLength position), get the beat, where beats count from 1

    If you want a fractional number for the beat, see getBeatProportion.

    TODO: In a future version – getBeat will probably do what getBeatProportion does now,
    :   but just with 1 added to it.

    ```python
    >>> a = meter.TimeSignature('3/4', 3)
    >>> a.getBeat(0)
    1
    >>> a.getBeat(2.5)
    3
    >>> a.beatSequence.partition(['3/8', '3/8'])
    >>> a.getBeat(2.5)
    2
    ```

TimeSignature.getBeatDepth(*qLenPos*, *align='quantize'*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeatDepth)
:   Return the number of levels of beat partitioning given a QL into the TimeSignature.
    Note that by default beat partitioning always has a single, top-level partition.

    The align parameter is passed to the `offsetToDepth()`
    method, and can be used to find depths based on start position overlaps.

    ```python
    >>> a = meter.TimeSignature('3/4', 3)
    >>> a.getBeatDepth(0)
    1
    >>> a.getBeatDepth(1)
    1
    >>> a.getBeatDepth(2)
    1
    ```

    ```python
    >>> b = meter.TimeSignature('3/4', 1)
    >>> b.beatSequence[0] = b.beatSequence[0].subdivide(3)
    >>> b.beatSequence[0][0] = b.beatSequence[0][0].subdivide(2)
    >>> b.beatSequence[0][1] = b.beatSequence[0][1].subdivide(2)
    >>> b.beatSequence[0][2] = b.beatSequence[0][2].subdivide(2)
    >>> b.getBeatDepth(0)
    3
    >>> b.getBeatDepth(0.5)
    1
    >>> b.getBeatDepth(1)
    2
    ```

TimeSignature.getBeatDuration(*qLenPos*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeatDuration)
:   Returns a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")
    object representing the length of the beat
    found at qLenPos. For most standard
    meters, you can give qLenPos = 0
    and get the length of any beat in
    the TimeSignature; but the simpler
    `music21.meter.TimeSignature.beatDuration` parameter,
    will do that for you just as well.

    The advantage of this method is that
    it will work for asymmetrical meters, as the second
    example shows.

    Ex. 1: beat duration for 3/4 is always 1.0
    no matter where in the meter you query.

    ```python
    >>> ts1 = meter.TimeSignature('3/4')
    >>> ts1.getBeatDuration(0.5)
    <music21.duration.Duration 1.0>
    >>> ts1.getBeatDuration(2.5)
    <music21.duration.Duration 1.0>
    ```

    Ex. 2: same for 6/8:

    ```python
    >>> ts2 = meter.TimeSignature('6/8')
    >>> ts2.getBeatDuration(2.5)
    <music21.duration.Duration 1.5>
    ```

    Ex. 3: but for a compound meter of 3/8 + 2/8,
    where you ask for the beat duration
    will determine the length of the beat:

    ```python
    >>> ts3 = meter.TimeSignature('3/8+2/8')  # will partition as 2 beat
    >>> ts3.getBeatDuration(0.5)
    <music21.duration.Duration 1.5>
    >>> ts3.getBeatDuration(1.5)
    <music21.duration.Duration 1.0>
    ```

TimeSignature.getBeatOffsets()[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeatOffsets)
:   Return offset positions in a list for the start of each beat,
    assuming this object is found at offset zero.

    ```python
    >>> a = meter.TimeSignature('3/4')
    >>> a.getBeatOffsets()
    [0.0, 1.0, 2.0]
    >>> a = meter.TimeSignature('6/8')
    >>> a.getBeatOffsets()
    [0.0, 1.5]
    ```

TimeSignature.getBeatProgress(*qLenPos*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeatProgress)
:   Given a quarterLength position, get the beat,
    where beats count from 1, and return the
    amount of qLen into this beat the supplied qLenPos
    is.

    ```python
    >>> a = meter.TimeSignature('3/4', 3)
    >>> a.getBeatProgress(0)
    (1, 0)
    >>> a.getBeatProgress(0.75)
    (1, 0.75)
    >>> a.getBeatProgress(1.0)
    (2, 0.0)
    >>> a.getBeatProgress(2.5)
    (3, 0.5)
    ```

    Works for specifically partitioned meters too:

    ```python
    >>> a.beatSequence.partition(['3/8', '3/8'])
    >>> a.getBeatProgress(2.5)
    (2, 1.0)
    ```

TimeSignature.getBeatProportion(*qLenPos*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeatProportion)
:   Given a quarter length position into the meter, return the numerical progress
    through the beat (where beats count from one) with a floating-point or fractional value
    between 0 and 1 appended to this value that gives the proportional progress into the beat.

    For faster, integer values, use simply .getBeat()

    ```python
    >>> ts1 = meter.TimeSignature('3/4')
    >>> ts1.getBeatProportion(0.0)
    1.0
    >>> ts1.getBeatProportion(0.5)
    1.5
    >>> ts1.getBeatProportion(1.0)
    2.0
    ```

    ```python
    >>> ts3 = meter.TimeSignature('3/8+2/8')  # will partition as 2 beat
    >>> ts3.getBeatProportion(0.75)
    1.5
    >>> ts3.getBeatProportion(2.0)
    2.5
    ```

TimeSignature.getBeatProportionStr(*qLenPos*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getBeatProportionStr)
:   Return a string presentation of the beat.

    ```python
    >>> ts1 = meter.TimeSignature('3/4')
    >>> ts1.getBeatProportionStr(0.0)
    '1'
    >>> ts1.getBeatProportionStr(0.5)
    '1 1/2'
    >>> ts1.getBeatProportionStr(1.0)
    '2'
    >>> ts3 = meter.TimeSignature('3/8+2/8')  # will partition as 2 beat
    >>> ts3.getBeatProportionStr(0.75)
    '1 1/2'
    >>> ts3.getBeatProportionStr(2)
    '2 1/2'
    ```

    ```python
    >>> ts4 = meter.TimeSignature('6/8')  # will partition as 2 beat
    ```

TimeSignature.getMeasureOffsetOrMeterModulusOffset(*el*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getMeasureOffsetOrMeterModulusOffset)
:   Return the measure offset based on a Measure, if it exists,
    otherwise based on meter modulus of the TimeSignature.

    ```python
    >>> m = stream.Measure()
    >>> ts1 = meter.TimeSignature('3/4')
    >>> m.insert(0, ts1)
    >>> n1 = note.Note()
    >>> m.insert(2, n1)
    >>> ts1.getMeasureOffsetOrMeterModulusOffset(n1)
    2.0
    ```

    Exceeding the range of the Measure gets a modulus

    ```python
    >>> n2 = note.Note()
    >>> m.insert(4.0, n2)
    >>> ts1.getMeasureOffsetOrMeterModulusOffset(n2)
    1.0
    ```

    Can be applied to Notes in a Stream with a TimeSignature.

    ```python
    >>> ts2 = meter.TimeSignature('5/4')
    >>> s2 = stream.Stream()
    >>> s2.insert(0, ts2)
    >>> n3 = note.Note()
    >>> s2.insert(3, n3)
    >>> ts2.getMeasureOffsetOrMeterModulusOffset(n3)
    3.0
    ```

    ```python
    >>> n4 = note.Note()
    >>> s2.insert(5, n4)
    >>> ts2.getMeasureOffsetOrMeterModulusOffset(n4)
    0.0
    ```

TimeSignature.getOffsetFromBeat(*beat*)[[source]](../_modules/music21/meter/base.html#TimeSignature.getOffsetFromBeat)
:   Given a beat value, convert into an offset position.

    ```python
    >>> ts1 = meter.TimeSignature('3/4')
    >>> ts1.getOffsetFromBeat(1)
    0.0
    >>> ts1.getOffsetFromBeat(2)
    1.0
    >>> ts1.getOffsetFromBeat(3)
    2.0
    >>> ts1.getOffsetFromBeat(3.5)
    2.5
    >>> ts1.getOffsetFromBeat(3.25)
    2.25
    ```

    Get the offset from beat 8/3 (2.6666): give a Fraction, get a Fraction.

    ```python
    >>> from fractions import Fraction
    >>> ts1.getOffsetFromBeat(Fraction(8, 3))
    Fraction(5, 3)
    ```

    ```python
    >>> ts1 = meter.TimeSignature('6/8')
    >>> ts1.getOffsetFromBeat(1)
    0.0
    >>> ts1.getOffsetFromBeat(2)
    1.5
    ```

    Check that 2.5 is 2.5 + (0.5 \* 1.5):

    ```python
    >>> ts1.getOffsetFromBeat(2.5)
    2.25
    ```

    Decimals only need to be pretty close to work.
    (But Fractions are better as demonstrated above)

    ```python
    >>> ts1.getOffsetFromBeat(2.33)
    2.0
    >>> ts1.getOffsetFromBeat(2.66)
    2.5
    ```

    Works for asymmetrical meters as well:

    ```python
    >>> ts3 = meter.TimeSignature('3/8+2/8')  # will partition as 2 beat
    >>> ts3.getOffsetFromBeat(1)
    0.0
    >>> ts3.getOffsetFromBeat(2)
    1.5
    >>> ts3.getOffsetFromBeat(1.66)
    1.0
    >>> ts3.getOffsetFromBeat(2.5)
    2.0
    ```

    Let’s try this on a real piece, a 4/4 chorale with a one beat pickup. Here we get the
    normal offset for beat 4 from the active TimeSignature, but we subtract out
    the pickup length which is in a Measure’s `paddingLeft`
    property, and thus see the distance from the beginning of the measure to beat 4 in
    quarter notes

    ```python
    >>> c = corpus.parse('bwv1.6')
    >>> for m in c.parts.first().getElementsByClass(stream.Measure):
    ...     ts = m.timeSignature or m.getContextByClass(meter.TimeSignature)
    ...     print(m.number, ts.getOffsetFromBeat(4.0) - m.paddingLeft)
    0 0.0
    1 3.0
    2 3.0
    ...
    ```

TimeSignature.load(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *divisions=None*)[[source]](../_modules/music21/meter/base.html#TimeSignature.load)
:   Load up a TimeSignature with a string value.

    ```python
    >>> ts = meter.TimeSignature()
    >>> ts.load('4/4')
    >>> ts
    <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> ts.load('c')
    >>> ts.symbol
    'common'
    ```

    ```python
    >>> ts.load('2/4+3/8')
    >>> ts
    <music21.meter.TimeSignature 2/4+3/8>
    ```

    ```python
    >>> ts.load('fast 6/8')
    >>> ts.beatCount
    2
    >>> ts.load('slow 6/8')
    >>> ts.beatCount
    6
    ```

    Loading destroys all preexisting internal representations

TimeSignature.ratioEqual(*other*)[[source]](../_modules/music21/meter/base.html#TimeSignature.ratioEqual)
:   A basic form of comparison; does not determine if any internal structures are equal; o
    only outermost ratio.

TimeSignature.resetValues(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '4/4'*, *divisions=None*)[[source]](../_modules/music21/meter/base.html#TimeSignature.resetValues)
:   reset all values according to a new value and optionally, the number of
    divisions.

TimeSignature.setAccentWeight(*weights: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *level: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/base.html#TimeSignature.setAccentWeight)
:   Set accent weight, or floating point scalars, for the accent MeterSequence.
    Provide a list of float values; if this list is shorter than the length
    of the MeterSequence, it will be looped; if this list is longer,
    only the relevant values at the beginning will be used.

    If the accent MeterSequence is subdivided, the level of depth to set is given by the
    optional level argument.

    ```python
    >>> a = meter.TimeSignature('4/4', 4)
    >>> len(a.accentSequence)
    4
    >>> a.setAccentWeight([0.8, 0.2])
    >>> a.getAccentWeight(0.0)
    0.8...
    >>> a.getAccentWeight(0.5)
    0.8...
    >>> a.getAccentWeight(1.0)
    0.2...
    >>> a.getAccentWeight(2.5)
    0.8...
    >>> a.getAccentWeight(3.5)
    0.2...
    ```

TimeSignature.setDisplay(*value*, *partitionRequest=None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/base.html#TimeSignature.setDisplay)
:   Set an independent display value for a meter.

    ```python
    >>> a = meter.TimeSignature()
    >>> a.load('3/4')
    >>> a.setDisplay('2/8+2/8+2/8')
    >>> a.displaySequence
    <music21.meter.core.MeterSequence {2/8+2/8+2/8}>
    >>> a.beamSequence
    <music21.meter.core.MeterSequence {{1/8+1/8}+{1/8+1/8}+{1/8+1/8}}>
    >>> a.beatSequence  # a single top-level partition is default for beat
    <music21.meter.core.MeterSequence {{1/8+1/8}+{1/8+1/8}+{1/8+1/8}}>
    >>> a.setDisplay('3/4')
    >>> a.displaySequence
    <music21.meter.core.MeterSequence {3/4}>
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TimeSignature`](#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") instance variables

TimeSignature.accentSequence
:   A `MeterSequence` governing accent partitioning.

TimeSignature.beamSequence
:   A `MeterSequence` governing automatic beaming.

TimeSignature.beatSequence
:   A `MeterSequence` governing beat partitioning.

TimeSignature.displaySequence
:   A `MeterSequence` governing the display of the TimeSignature.

TimeSignature.symbol
:   A string representation of how to display the TimeSignature.
    can be “common”, “cut”, “single-number” (i.e.,
    no denominator), or “normal” or “”.

TimeSignature.symbolizeDenominator
:   If set to True (default is False) then the denominator
    will be displayed as a symbol rather than
    a number. Hindemith uses this in his scores.
    Finale and other MusicXML readers do not support this
    so do not expect proper output yet.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SenzaMisuraTimeSignature

class music21.meter.base.SenzaMisuraTimeSignature(*text=None*)[[source]](../_modules/music21/meter/base.html#SenzaMisuraTimeSignature)
:   A SenzaMisuraTimeSignature represents the absence of a TimeSignature

    It is NOT a TimeSignature subclass, only because it has none of the attributes
    of a TimeSignature.

    ```python
    >>> smts = meter.SenzaMisuraTimeSignature('0')
    >>> smts.text
    '0'
    >>> smts
    <music21.meter.SenzaMisuraTimeSignature 0>
    ```

[`SenzaMisuraTimeSignature`](#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature") bases

* [`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SenzaMisuraTimeSignature`](#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SenzaMisuraTimeSignature`](#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`SenzaMisuraTimeSignature`](#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`SenzaMisuraTimeSignature`](#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TimeSignatureBase

class music21.meter.base.TimeSignatureBase(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *groups: [Groups](moduleBase.html#music21.base.Groups "music21.base.Groups") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sites: [Sites](moduleSites.html#music21.sites.Sites "music21.sites.Sites") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *duration: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *activeSite: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *style: [Style](moduleStyle.html#music21.style.Style "music21.style.Style") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *editorial: [Editorial](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *offset: OffsetQL = 0.0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/meter/base.html#TimeSignatureBase)
:   A base class for TimeSignature and SenzaMisuraTimeSignature to
    inherit from.

[`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TimeSignatureBase`](#music21.meter.base.TimeSignatureBase "music21.meter.base.TimeSignatureBase") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.meter.base.bestTimeSignature(*meas: stream.Stream*) → music21.meter.TimeSignature[[source]](../_modules/music21/meter/base.html#bestTimeSignature)
:   Given a Measure (or any Stream) with elements in it, get a TimeSignature that contains all
    elements.

    Note: this does not yet accommodate triplets.

    ```python
    >>> s = converter.parse('tinynotation: C4 D4 E8 F8').flatten().notes
    >>> m = stream.Measure()
    >>> for el in s:
    ...     m.insert(el.offset, el)
    >>> ts = meter.bestTimeSignature(m)
    >>> ts
    <music21.meter.TimeSignature 3/4>
    ```

    ```python
    >>> s2 = converter.parse('tinynotation: C8. D16 E8 F8. G16 A8').flatten().notes
    >>> m2 = stream.Measure()
    >>> for el in s2:
    ...     m2.insert(el.offset, el)
    >>> ts2 = meter.bestTimeSignature(m2)
    >>> ts2
    <music21.meter.TimeSignature 6/8>
    ```

    ```python
    >>> s3 = converter.parse('C2 D2 E2', format='tinyNotation').flatten().notes
    >>> m3 = stream.Measure()
    >>> for el in s3:
    ...     m3.insert(el.offset, el)
    >>> ts3 = meter.bestTimeSignature(m3)
    >>> ts3
    <music21.meter.TimeSignature 3/2>
    ```

    ```python
    >>> s4 = converter.parse('C8. D16 E8 F8. G16 A8 C4. D4.', format='tinyNotation').flatten().notes
    >>> m4 = stream.Measure()
    >>> for el in s4:
    ...     m4.insert(el.offset, el)
    >>> ts4 = meter.bestTimeSignature(m4)
    >>> ts4
    <music21.meter.TimeSignature 12/8>
    ```

    ```python
    >>> s5 = converter.parse('C4 D2 E4 F2', format='tinyNotation').flatten().notes
    >>> m5 = stream.Measure()
    >>> for el in s5:
    ...     m5.insert(el.offset, el)
    >>> ts5 = meter.bestTimeSignature(m5)
    >>> ts5
    <music21.meter.TimeSignature 6/4>
    ```

    ```python
    >>> s6 = converter.parse('C4 D16.', format='tinyNotation').flatten().notes
    >>> m6 = stream.Measure()
    >>> for el in s6:
    ...     m6.insert(el.offset, el)
    >>> ts6 = meter.bestTimeSignature(m6)
    >>> ts6
    <music21.meter.TimeSignature 11/32>
    ```

    Complex durations (arose in han2.abc, number 445)

    ```python
    >>> m7 = stream.Measure()
    >>> m7.append(note.Note('D', quarterLength=3.5))
    >>> m7.append(note.Note('E', quarterLength=5.5))
    >>> ts7 = meter.bestTimeSignature(m7)
    >>> ts7
    <music21.meter.TimeSignature 9/4>
    ```
