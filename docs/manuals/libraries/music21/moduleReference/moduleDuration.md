Source: https://music21.org/music21docs/moduleReference/moduleDuration.html

# music21.duration

The duration module contains [`Duration`](#music21.duration.Duration "music21.duration.Duration") objects
(among other objects and functions). Duration objects are a fundamental
component of [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") and all Music21Objects, such as
`TimeSignature` objects.

Containers such as `Stream` and
`Score` also have durations which are equal to the
position of the ending of the last object in the Stream.

Music21 Durations are almost always measured in Quarter Notes, so an eighth
note has a duration of 0.5. Different Duration-like objects support objects
such as grace notes which take no duration on the page, have a short (but real)
duration when played, and have a duration-type representation when performed.

Example usage:

```python
>>> d = duration.Duration()
>>> d.quarterLength = 0.5
>>> d.type
'eighth'
```

```python
>>> d.type = 'whole'
>>> d.quarterLength
4.0
```

```python
>>> d.quarterLength = 0.166666666
>>> d.type
'16th'
```

```python
>>> d.tuplets[0].numberNotesActual
3
```

```python
>>> d.tuplets[0].numberNotesNormal
2
```

## Duration

class music21.duration.Duration(*typeOrDuration: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | OffsetQLIn | [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, */*, *\**, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *dots: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *durationTuple: [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *components: Iterable[[DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *client: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/duration.html#Duration)
:   Durations are one of the most important objects in music21. A Duration
    represents a span of musical time measurable in terms of quarter notes (or
    in advanced usage other units). For instance, “57 quarter notes” or “dotted
    half tied to quintuplet sixteenth note” or simply “quarter note.”

    A Duration object is made of one or more immutable DurationTuple objects stored on the
    components list. A Duration created by setting quarterLength sets the attribute
    [`expressionIsInferred`](#music21.duration.Duration.expressionIsInferred "music21.duration.Duration.expressionIsInferred") to True, which indicates that callers
    (such as [`splitElementsToCompleteTuplets()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.splitElementsToCompleteTuplets "music21.stream.makeNotation.splitElementsToCompleteTuplets"))
    can express this Duration using another combination of components that sums to the
    quarterLength. Otherwise, expressionIsInferred is set to False, indicating that
    components are not allowed to mutate.

    Multiple DurationTuples in a single Duration may be used to express tied
    notes, or may be used to split duration across barlines or beam groups.
    Some Duration objects are not expressible as a single notation unit.

    Duration objects are not Music21Objects.

    If a single argument is passed to Duration() and it is a string, then it is
    assumed to be a type, such as ‘half’, ‘eighth’, or ‘16th’, etc. If that
    single argument is a number then it is assumed to be a quarterLength (2 for
    half notes, 0.5 for eighth notes, 0.75 for dotted eighth notes, 0.333333333
    for a triplet eighth, etc.). If one or more named arguments are passed
    then the Duration() is configured according to those arguments. Supported
    arguments are ‘type’, ‘dots’, ‘quarterLength’, or ‘components’.

    Example 1: a triplet eighth configured by quarterLength:

    ```python
    >>> d = duration.Duration(0.333333333)
    >>> d.type
    'eighth'
    ```

    ```python
    >>> d.tuplets
    (<music21.duration.Tuplet 3/2/eighth>,)
    ```

    Example 2: A Duration made up of multiple
    [`music21.duration.DurationTuple`](#music21.duration.DurationTuple "music21.duration.DurationTuple") objects automatically configured by
    the specified quarterLength.

    ```python
    >>> d2 = duration.Duration(0.625)
    >>> d2.type
    'complex'
    ```

    ```python
    >>> d2.components
    (DurationTuple(type='eighth', dots=0, quarterLength=0.5),
     DurationTuple(type='32nd', dots=0, quarterLength=0.125))
    ```

    ```python
    >>> d2.expressionIsInferred
    True
    ```

    Example 3: A Duration configured by keywords.

    ```python
    >>> d3 = duration.Duration(type='half', dots=2)
    >>> d3.quarterLength
    3.5
    >>> d3.expressionIsInferred
    False
    ```

[`Duration`](#music21.duration.Duration "music21.duration.Duration") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Duration`](#music21.duration.Duration "music21.duration.Duration") read-only properties

Duration.fullName
:   Return the most complete representation of this Duration, providing
    dots, type, tuplet, and quarter length representation.

    ```python
    >>> d = duration.Duration(quarterLength=1.5)
    >>> d.fullName
    'Dotted Quarter'
    ```

    ```python
    >>> d = duration.Duration(type='half')
    >>> d.fullName
    'Half'
    ```

    ```python
    >>> d = duration.Duration(quarterLength=1.25)
    >>> d.fullName
    'Quarter tied to 16th (1 1/4 total QL)'
    ```

    ```python
    >>> d = duration.Duration(quarterLength=0.333333)
    >>> d.fullName
    'Eighth Triplet (1/3 QL)'
    ```

    ```python
    >>> d = duration.Duration(quarterLength=0.666666)
    >>> d.fullName
    'Quarter Triplet (2/3 QL)'
    ```

    ```python
    >>> d = duration.Duration(quarterLength=0.571428)
    >>> d.fullName
    'Quarter Septuplet (4/7 QL)'
    ```

    ```python
    >>> d = duration.Duration(quarterLength=0)
    >>> d.fullName
    'Zero Duration (0 total QL)'
    ```

Duration.isComplex
:   Returns True if this Duration has more than one DurationTuple object on
    the component list. That is to say if it’s a single Duration that
    need multiple tied noteheads to represent.

    ```python
    >>> aDur = duration.Duration()
    >>> aDur.quarterLength = 1.375
    >>> aDur.isComplex
    True
    ```

    ```python
    >>> len(aDur.components)
    2
    ```

    ```python
    >>> aDur.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),
     DurationTuple(type='16th', dots=1, quarterLength=0.375))
    ```

    ```python
    >>> cDur = duration.Duration()
    >>> cDur.quarterLength = 0.25
    >>> cDur.isComplex
    False
    ```

    ```python
    >>> len(cDur.components)
    1
    ```

Duration.ordinal
:   Get the ordinal value of the Duration, where whole is 4,
    half is 5, etc.

    ```python
    >>> d = duration.Duration()
    >>> d.quarterLength = 2.0
    >>> d.ordinal
    5
    >>> d.type = '16th'
    >>> d.ordinal
    8
    ```

    Complex values have an ordinal of the string ‘complex’. This might
    change to NaN in a later version.

    ```python
    >>> d.quarterLength = 2.5
    >>> d.ordinal
    'complex'
    ```

    Zero durations have an ordinal of None

    ```python
    >>> d2 = duration.Duration(0.0)
    >>> print(d2.ordinal)
    None
    ```

Duration.quarterLengthNoTuplets
:   Returns the quarter length of the duration without taking into account triplets.

    Does not cache.

    ```python
    >>> d = duration.Duration(1/3)
    >>> d.quarterLengthNoTuplets
    0.5
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Duration`](#music21.duration.Duration "music21.duration.Duration") read/write properties

Duration.components
:   Returns or sets a tuple of the component DurationTuples of this
    Duration object

    ```python
    >>> d = duration.Duration(1.0)
    >>> d.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),)
    ```

    Tuplets do not have the tuplet in their components.

    ```python
    >>> d = duration.Duration(1/3)
    >>> d.components
    (DurationTuple(type='eighth', dots=0, quarterLength=0.5),)
    ```

    With a complex duration it becomes clearer why multiple components are needed.
    Here is a duration that cannot be expressed as a single note.

    ```python
    >>> d = duration.Duration(1.25)
    >>> d.type
    'complex'
    >>> d.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),
     DurationTuple(type='16th', dots=0, quarterLength=0.25))
    ```

    But it can be expressed another way and will output in that way in MusicXML
    and other readers:

    ```python
    >>> component0 = duration.DurationTuple(type='eighth', dots=0, quarterLength=0.5)
    >>> component1 = duration.DurationTuple(type='eighth', dots=1, quarterLength=0.75)
    >>> d.components = [component0, component1]
    ```

    It is allowed but not advised to set components that do not add up
    to the current (pre-tuplet) quarterLength. In which case the quarterLength
    will be adjusted:

    ```python
    >>> d.components = [component0]
    >>> d
    <music21.duration.Duration 0.5>
    >>> d.type
    'eighth'
    ```

Duration.dotGroups
:   Dot groups are a convenience for transcribing medieval music.
    They represent dotted-dotted notes (written one above another).
    For instance a half note with dotGroups = (1, 1) represents a dotted half note that
    is itself dotted. Worth 9 eighth notes (dotted-half tied to dotted-quarter). It
    is not the same as a double-dotted half note, which is only worth 7 eighth notes.

    ```python
    >>> a = duration.Duration()
    >>> a.type = 'half'
    >>> a.dotGroups
    (0,)
    >>> a.dots = 1
    ```

    ```python
    >>> a.dotGroups = (1, 1)
    >>> a.quarterLength
    4.5
    ```

Duration.dots
:   Returns or sets the number of dots in the Duration
    if it is a simple Duration.

    For returning only the number of dots on the first component is returned for
    complex durations. (Previously it could return None
    if it was not a simple duration which led to some
    terribly difficult to find errors.)

    ```python
    >>> a = duration.Duration()
    >>> a.type = 'quarter'
    >>> a.dots = 1
    >>> a.quarterLength
    1.5
    >>> a.dots = 2
    >>> a.quarterLength
    1.75
    ```

    If a duration is complex then setting dots has the effect of
    setting the number of dots to value on every component.

    ```python
    >>> DT = duration.durationTupleFromTypeDots
    >>> complexDuration = duration.Duration()
    >>> complexDuration.addDurationTuple(DT('half', 0))
    >>> complexDuration.addDurationTuple(DT('eighth', 2))
    >>> complexDuration.type
    'complex'
    >>> complexDuration.quarterLength
    2.875
    ```

    In a complex duration, the number of dots comes from the first component:

    ```python
    >>> complexDuration.dots
    0
    ```

    But if set, applies to all components:

    ```python
    >>> complexDuration.dots = 1
    >>> complexDuration.components
    (DurationTuple(type='half', dots=1, quarterLength=3.0),
     DurationTuple(type='eighth', dots=1, quarterLength=0.75))
    >>> complexDuration.quarterLength
    3.75
    ```

    Dots can go pretty high.

    ```python
    >>> d = duration.Duration('half')
    >>> d.quarterLength
    2.0
    >>> d.dots = 5
    >>> d.quarterLength
    3.9375
    >>> d.dots = 10
    >>> d.quarterLength
    3.998046875
    ```

    Infinite dots gives an Easter egg:

    ```python
    >>> from math import inf
    >>> d.type = 'half'
    >>> d.dots = inf
    >>> d.quarterLength
    4.0
    >>> d.dots
    0
    >>> d.type
    'whole'
    ```

Duration.linked
:   Gets or sets the .linked property – if linked (default) then type, dots, tuplets are
    always coherent with quarterLength. If not, then they are separate.

    ```python
    >>> d = duration.Duration(0.5)
    >>> d.linked
    True
    ```

    Linked durations change other values when one changes:

    ```python
    >>> d.type = '16th'
    >>> d.quarterLength
    0.25
    ```

    Unlinked values do not:

    ```python
    >>> d.linked = False
    >>> d.type = 'half'
    >>> d.quarterLength
    0.25
    ```

Duration.quarterLength
:   Returns the quarter note length or Sets the quarter note length to
    the specified value. May be expressed as a float or Fraction.

    Currently (if the value is different from what is already stored)
    this wipes out any existing components, not preserving their type.
    So if you’ve set up Duration(1.5) as 3-eighth notes, setting
    Duration to 1.75 will NOT dot the last eighth note, but instead
    give you a single double-dotted half note.

    ```python
    >>> a = duration.Duration()
    >>> a.quarterLength = 3.5
    >>> a.quarterLength
    3.5
    ```

    ```python
    >>> for thisUnit in a.components:
    ...    print(thisUnit.quarterLength, thisUnit.type, thisUnit.dots)
    3.5 half 2
    ```

    A duration of 2.5 quarter notes has to be represented as more than one
    component.

    ```python
    >>> b = duration.Duration()
    >>> b.quarterLength = 2.5
    >>> b.quarterLength
    2.5
    ```

    ```python
    >>> for thisUnit in b.components:
    ...    print(thisUnit.quarterLength, thisUnit.type, thisUnit.dots)
    2.0 half 0
    0.5 eighth 0
    ```

    Note that integer values of quarter lengths get
    silently converted to floats (internally opFracs):

    ```python
    >>> c = duration.Duration()
    >>> c.quarterLength = 5
    >>> c.quarterLength
    5.0
    >>> c.type  # complex because 5 quarters cannot be expressed as a single note.
    'complex'
    ```

    Float values will be converted to fractions if they are inexpressible exactly
    as floats:

    ```python
    >>> d = duration.Duration()
    >>> d.quarterLength = 1/3
    >>> d.quarterLength
    Fraction(1, 3)
    ```

Duration.tuplets
:   Return a tuple of Tuplet objects.
    Setting tuplets will inform the client (Note) that the duration has changed.

Duration.type
:   Get or set the type of the Duration.

    ```python
    >>> a = duration.Duration()
    >>> a.type = 'half'
    >>> a.quarterLength
    2.0
    ```

    ```python
    >>> a.type= '16th'
    >>> a.quarterLength
    0.25
    ```

[`Duration`](#music21.duration.Duration "music21.duration.Duration") methods

Duration.\_\_eq\_\_(*other*)[[source]](../_modules/music21/duration.html#Duration.__eq__)
:   Two durations are the same if their type, dots, tuplets, and
    quarterLength are all the same.

    ```python
    >>> aDur = duration.Duration('quarter')
    >>> bDur = duration.Duration('16th')
    >>> cDur = duration.Duration('16th')
    >>> aDur == bDur
    False
    >>> aDur != bDur
    True
    ```

    ```python
    >>> cDur == bDur
    True
    ```

    ```python
    >>> dDur = duration.Duration(0.0)
    >>> eDur = duration.Duration(0.0)
    >>> dDur == eDur
    True
    ```

    ```python
    >>> tupDur1 = duration.Duration(2 / 3)
    >>> tupDur2 = duration.Duration(2 / 3)
    >>> tupDur1 == tupDur2
    True
    ```

    ```python
    >>> graceDur1 = tupDur1.getGraceDuration()
    >>> graceDur1 == tupDur1
    False
    >>> graceDur2 = tupDur2.getGraceDuration()
    >>> graceDur1 == graceDur2
    True
    ```

    Link status must be the same:

    ```python
    >>> tupDur1.linked = False
    >>> tupDur1 == tupDur2
    False
    ```

Duration.addDurationTuple(*dur: [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [Duration](#music21.duration.Duration "music21.duration.Duration") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *\**, *\_skipInform=False*)[[source]](../_modules/music21/duration.html#Duration.addDurationTuple)
:   Add a DurationTuple or a Duration’s components to this Duration.
    Does not simplify the Duration. For instance, adding two
    quarter notes results in two tied quarter notes, not one half note.
    See consolidate below for more info on how to do that.

    ```python
    >>> a = duration.Duration('quarter')
    >>> b = duration.durationTupleFromTypeDots('quarter', 0)
    >>> a.addDurationTuple(b)
    >>> a.quarterLength
    2.0
    >>> a.type
    'complex'
    ```

Duration.aggregateTupletMultiplier() → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Duration.aggregateTupletMultiplier)
:   Returns the multiple of all the tuplet multipliers as an opFrac.

    This method is needed for MusicXML time-modification among other
    places.

    No tuplets:

    ```python
    >>> complexDur = duration.Duration('eighth')
    >>> complexDur.aggregateTupletMultiplier()
    1.0
    ```

    With tuplets:

    ```python
    >>> complexDur.appendTuplet(duration.Tuplet())
    >>> complexDur.aggregateTupletMultiplier()
    Fraction(2, 3)
    ```

    Nested tuplets are possible…

    ```python
    >>> tup2 = duration.Tuplet()
    >>> tup2.setRatio(5, 4)
    >>> complexDur.appendTuplet(tup2)
    >>> complexDur.aggregateTupletMultiplier()
    Fraction(8, 15)
    ```

Duration.appendTuplet(*newTuplet: [Tuplet](#music21.duration.Tuplet "music21.duration.Tuplet")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Duration.appendTuplet)
:   Adds a new Tuplet to a Duration, sets the Tuplet’s .frozen state to True,
    and then informs the client (Note) that the duration has changed.

    ```python
    >>> tup = duration.Tuplet(3, 2)
    >>> d = duration.Duration(1.0)
    >>> d.appendTuplet(tup)
    >>> d.quarterLength
    Fraction(2, 3)
    >>> t2 = duration.Tuplet(5, 4)
    >>> d.appendTuplet(t2)
    >>> d.quarterLength
    Fraction(8, 15)
    >>> tup.frozen
    True
    ```

Duration.augmentOrDiminish(*amountToScale*, *retainComponents=False*)[[source]](../_modules/music21/duration.html#Duration.augmentOrDiminish)
:   Given a number greater than zero, creates a new Duration object
    after
    multiplying the current quarterLength of the
    duration by the number and resets the components
    for the duration (by default).

    Returns a new duration that has
    the new length.

    ```python
    >>> aDur = duration.Duration()
    >>> aDur.quarterLength = 1.5  # dotted quarter
    >>> cDur = aDur.augmentOrDiminish(2)
    >>> cDur.quarterLength
    3.0
    >>> cDur.type
    'half'
    >>> cDur.dots
    1
    ```

    aDur is not changed:

    ```python
    >>> aDur
    <music21.duration.Duration 1.5>
    ```

    A complex duration that cannot be expressed as a single notehead (component)

    ```python
    >>> bDur = duration.Duration()
    >>> bDur.quarterLength = 2.125  # requires components
    >>> bDur.quarterLength
    2.125
    >>> len(bDur.components)
    2
    >>> bDur.components
    (DurationTuple(type='half', dots=0, quarterLength=2.0),
     DurationTuple(type='32nd', dots=0, quarterLength=0.125))
    ```

    By default, when augmenting or diminishing, we will delete any
    unusual components or tuplets:

    ```python
    >>> dDur = duration.Duration(1.5)
    >>> dDur.appendTuplet(duration.Tuplet(3, 2))
    >>> dDur
    <music21.duration.Duration 1.0>
    >>> dDur.dots
    1
    >>> dDur.tuplets
    (<music21.duration.Tuplet 3/2>,)
    ```

    ```python
    >>> eDur = dDur.augmentOrDiminish(2)
    >>> eDur
    <music21.duration.Duration 2.0>
    >>> eDur.dots
    0
    >>> eDur.tuplets
    ()
    ```

    ```python
    >>> eRetain = dDur.augmentOrDiminish(2, retainComponents=True)
    >>> eRetain
    <music21.duration.Duration 2.0>
    >>> eRetain.dots
    1
    >>> eRetain.tuplets
    (<music21.duration.Tuplet 3/2>,)
    ```

    ```python
    >>> fDur = duration.Duration(1.0)
    >>> fDur.addDurationTuple(duration.DurationTuple('quarter', 0, 1.0))
    >>> fDur
    <music21.duration.Duration 2.0>
    >>> fDur.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),
     DurationTuple(type='quarter', dots=0, quarterLength=1.0))
    ```

    ```python
    >>> gDur = fDur.augmentOrDiminish(0.5)
    >>> gDur.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),)
    ```

    ```python
    >>> gRetain = fDur.augmentOrDiminish(0.5, retainComponents=True)
    >>> gRetain.components
    (DurationTuple(type='eighth', dots=0, quarterLength=0.5),
     DurationTuple(type='eighth', dots=0, quarterLength=0.5))
    ```

    Negative values raise ValueError:

    ```python
    >>> fDur.augmentOrDiminish(-1)
    Traceback (most recent call last):
    ValueError: amountToScale must be greater than zero
    ```

Duration.clear() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Duration.clear)
:   Permit all components to be removed.
    This is needed for resetting to zero duration.

    ```python
    >>> a = duration.Duration()
    >>> a.quarterLength = 6
    >>> a.type
    'whole'
    >>> a.components
    (DurationTuple(type='whole', dots=1, quarterLength=6.0),)
    ```

    ```python
    >>> a.clear()
    ```

    ```python
    >>> a.dots
    0
    >>> a.components
    ()
    >>> a.type
    'zero'
    >>> a.quarterLength
    0.0
    ```

Duration.componentIndexAtQtrPosition(*quarterPosition*)[[source]](../_modules/music21/duration.html#Duration.componentIndexAtQtrPosition)
:   returns the index number of the duration component sounding at
    the given quarter position.

    Note that for 0 and the last value, the object is returned.

    ```python
    >>> components = []
    >>> components.append(duration.Duration('quarter'))
    >>> components.append(duration.Duration('quarter'))
    >>> components.append(duration.Duration('quarter'))
    ```

    ```python
    >>> a = duration.Duration()
    >>> a.components = components
    >>> a.quarterLength
    3.0
    >>> a.componentIndexAtQtrPosition(0.5)
    0
    >>> a.componentIndexAtQtrPosition(1.5)
    1
    >>> a.componentIndexAtQtrPosition(2.5)
    2
    ```

    this is odd behavior:

    e.g. given d1, d2, d3 as 3 quarter notes and
    self.components = [d1, d2, d3]

    then

    self.componentIndexAtQtrPosition(1.5) == d2
    self.componentIndexAtQtrPosition(2.0) == d3
    self.componentIndexAtQtrPosition(2.5) == d3

    Currently sometimes returns the component itself. Changing in v7.

Duration.componentStartTime(*componentIndex: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Duration.componentStartTime)
:   For a valid component index value, this returns the quarter note offset
    at which that component would start.

    This does not handle fractional arguments.

    ```python
    >>> components = []
    >>> qdt = duration.DurationTuple('quarter', 0, 1.0)
    >>> components.append(qdt)
    >>> components.append(qdt)
    >>> components.append(qdt)
    ```

    ```python
    >>> a = duration.Duration()
    >>> a.components = components
    >>> a.quarterLength
    3.0
    >>> a.componentStartTime(0)
    0.0
    >>> a.componentStartTime(1)
    1.0
    >>> a.componentStartTime(3)
    Traceback (most recent call last):
    IndexError: invalid component index value 3 submitted;
                value must be an integer between 0 and 2
    ```

Duration.consolidate()[[source]](../_modules/music21/duration.html#Duration.consolidate)
:   Given a Duration with multiple components, consolidate into a single
    Duration. This can only be based on quarterLength; this is
    destructive: information is lost from components.

    This cannot be done for all Durations, as DurationTuples cannot express all durations

    ```python
    >>> a = duration.Duration(1)
    >>> a.addDurationTuple(duration.DurationTuple('half', 0, 2.0))
    >>> a.addDurationTuple(duration.DurationTuple('quarter', 0, 1.0))
    >>> a.quarterLength
    4.0
    >>> len(a.components)
    3
    >>> a.type
    'complex'
    ```

    After consolidate:

    ```python
    >>> a.consolidate()
    >>> a.quarterLength
    4.0
    >>> len(a.components)
    1
    ```

    It gains a type!

    ```python
    >>> a.type
    'whole'
    ```

    If the type cannot be expressed then the type is inexpressible

    ```python
    >>> a = duration.Duration(1)
    >>> a.addDurationTuple(duration.DurationTuple('half', 0, 2.0))
    >>> a.addDurationTuple(duration.DurationTuple('half', 0, 2.0))
    >>> a.quarterLength
    5.0
    >>> len(a.components)
    3
    >>> a.type
    'complex'
    ```

    After consolidate:

    ```python
    >>> a.consolidate()
    >>> a.quarterLength
    5.0
    >>> len(a.components)
    1
    >>> a.components
    (DurationTuple(type='inexpressible', dots=0, quarterLength=5.0),)
    ```

    It gains a type!

    ```python
    >>> a.type
    'inexpressible'
    ```

    For an ‘inexpressible’ duration, the opposite of consolidate is
    to set the duration’s quarterLength to itself. It won’t necessarily
    return to the original components, but it will usually
    create something that can be notated.

    ```python
    >>> a.quarterLength = a.quarterLength
    >>> a.type
    'complex'
    >>> a.components
    (DurationTuple(type='whole', dots=0, quarterLength=4.0),
     DurationTuple(type='quarter', dots=0, quarterLength=1.0))
    ```

Duration.currentComponents()[[source]](../_modules/music21/duration.html#Duration.currentComponents)
:   Advanced Method:

    returns the current components WITHOUT running the component updater.

    Needed by some internal methods. Components are made on the fly.

    ```python
    >>> d = duration.Duration(1.25)
    >>> d.currentComponents()
    ()
    ```

    Like in quantum physics, an observation affects the state:

    ```python
    >>> d.type
    'complex'
    >>> d.currentComponents()
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),
     DurationTuple(type='16th', dots=0, quarterLength=0.25))
    ```

    Generally, just look at .components

    ```python
    >>> d = duration.Duration(1.25)
    >>> d.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),
     DurationTuple(type='16th', dots=0, quarterLength=0.25))
    ```

Duration.getGraceDuration(*appoggiatura=False*) → [GraceDuration](#music21.duration.GraceDuration "music21.duration.GraceDuration") | [AppoggiaturaDuration](#music21.duration.AppoggiaturaDuration "music21.duration.AppoggiaturaDuration")[[source]](../_modules/music21/duration.html#Duration.getGraceDuration)
:   Return a deepcopy of this Duration as a GraceDuration instance with the same types.

    ```python
    >>> d = duration.Duration(1.25)
    >>> d
    <music21.duration.Duration 1.25>
    >>> d.components
    (DurationTuple(type='quarter', dots=0, quarterLength=1.0),
     DurationTuple(type='16th', dots=0, quarterLength=0.25))
    ```

    ```python
    >>> gd = d.getGraceDuration()
    >>> gd
    <music21.duration.GraceDuration unlinked type:complex quarterLength:0.0>
    >>> gd.quarterLength
    0.0
    >>> gd.components
    (DurationTuple(type='quarter', dots=0, quarterLength=0.0),
     DurationTuple(type='16th', dots=0, quarterLength=0.0))
    ```

    d is unchanged.

    ```python
    >>> d.quarterLength
    1.25
    ```

Duration.informClient() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Duration.informClient)
:   A method that tells the client that something has changed.

    Call informSites({‘changedAttribute’: ‘duration’, ‘quarterLength’: quarterLength})
    on any call that changes the quarterLength, so that the client can make a change.

    Returns False if there was no need to inform the client (like nothing has changed)
    or if .client is None. Otherwise returns True.

Duration.sliceComponentAtPosition(*quarterPosition*)[[source]](../_modules/music21/duration.html#Duration.sliceComponentAtPosition)
:   Given a quarter position within a component, divide that
    component into two components.

    ```python
    >>> d = duration.Duration()
    >>> d.clear()  # need to remove default
    >>> components = []
    ```

    ```python
    >>> d.addDurationTuple(duration.Duration('quarter'))
    >>> d.addDurationTuple(duration.Duration('quarter'))
    >>> d.addDurationTuple(duration.Duration('quarter'))
    >>> d.quarterLength
    3.0
    >>> d.sliceComponentAtPosition(0.5)
    >>> d.quarterLength
    3.0
    >>> len(d.components)
    4
    >>> d.components[0].type
    'eighth'
    >>> d.components[1].type
    'eighth'
    >>> d.components[2].type
    'quarter'
    ```

Duration.splitDotGroups(*\**, *inPlace=False*)[[source]](../_modules/music21/duration.html#Duration.splitDotGroups)
:   splits a dotGroup-duration (of 1 component) into a new duration of two
    components. Returns a new duration

    Probably does not handle properly tuplets of dot-groups.
    Never seen one, so probably okay.

    ```python
    >>> d1 = duration.Duration(type='half')
    >>> d1.dotGroups = (1, 1)
    >>> d1.quarterLength
    4.5
    >>> d2 = d1.splitDotGroups()
    >>> d2.components
    (DurationTuple(type='half', dots=1, quarterLength=3.0),
     DurationTuple(type='quarter', dots=1, quarterLength=1.5))
    >>> d2.quarterLength
    4.5
    ```

    Here’s how a system that does not support dotGroups can still display
    the notes accurately. N.B. MusicXML does this automatically, so
    no need.

    ```python
    >>> n1 = note.Note()
    >>> n1.duration = d1
    >>> n1.duration = n1.duration.splitDotGroups()
    >>> n1.duration.components
    (DurationTuple(type='half', dots=1, quarterLength=3.0),
     DurationTuple(type='quarter', dots=1, quarterLength=1.5))
    ```

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('9/8'))
    >>> s1.append(n1)
    >>> s1.show('lily.png')
    .. image:: images/duration_splitDotGroups.*
    ```

    ```python
    >>> n2 = note.Note()
    >>> n2.duration.type = 'quarter'
    >>> n2.duration.dotGroups = (1, 1)
    >>> n2.quarterLength
    2.25
    >>> n2.show()  # generates a dotted-quarter tied to dotted-eighth
    >>> n2.duration.splitDotGroups(inPlace=True)
    >>> n2.duration.dotGroups
    (1,)
    >>> n2.duration.components
    (DurationTuple(type='quarter', dots=1, quarterLength=1.5),
     DurationTuple(type='eighth', dots=1, quarterLength=0.75))
    ```

    ```python
    >>> n2 = note.Note()
    >>> n2.duration.type = 'quarter'
    >>> n2.duration.dotGroups = (1, 1, 1)
    >>> n2.quarterLength
    3.375
    >>> dSplit = n2.duration.splitDotGroups()
    >>> dSplit.quarterLength
    3.375
    >>> dSplit.components
    (DurationTuple(type='quarter', dots=1, quarterLength=1.5),
     DurationTuple(type='eighth', dots=1, quarterLength=0.75),
     DurationTuple(type='eighth', dots=1, quarterLength=0.75),
     DurationTuple(type='16th', dots=1, quarterLength=0.375))
    ```

    Does NOT handle tuplets etc.

[`Duration`](#music21.duration.Duration "music21.duration.Duration") instance variables

Duration.client
:   A duration’s “client” is the object that holds this
    duration as a property. It is informed whenever the duration changes.

    ```python
    >>> n = note.Note('C#5', type='whole')
    >>> d = n.duration
    >>> d.client is n
    True
    ```

Duration.expressionIsInferred
:   Boolean indicating whether this duration was created from a
    number rather than a type and thus can be changed to another
    expression. For instance the duration of 0.5 is generally
    an eighth note, but in the middle of a triplet group might be
    better written as a dotted-eighth triplet. If expressionIsInferred
    is True then music21 can change it according to complex. If
    False, then the type, dots, and tuplets are considered immutable.

    ```python
    >>> d = duration.Duration(0.5)
    >>> d.expressionIsInferred
    True
    ```

    ```python
    >>> d = duration.Duration('eighth')
    >>> d.expressionIsInferred
    False
    ```

## Tuplet

class music21.duration.Tuplet(*numberNotesActual: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 3*, *numberNotesNormal: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 2*, *durationActual: [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [Duration](#music21.duration.Duration "music21.duration.Duration") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *durationNormal: [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [Duration](#music21.duration.Duration "music21.duration.Duration") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *tupletId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *nestedLevel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['start', 'stop', 'startStop', False, None] = None*, *bracket: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True, False, 'slur'] = True*, *placement: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['above', 'below'] = 'above'*, *tupletActualShow: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['number', 'type', 'both', None] = 'number'*, *tupletNormalShow: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['number', 'type', 'both', None] = None*, *frozen: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/duration.html#Tuplet)
:   A tuplet object is a representation of a musical tuplet (like a triplet).
    It expresses a ratio that modifies duration values and are stored in
    Duration objects in a “tuple” (immutable list; since there can be nested
    tuplets) in the duration’s .tuplets property.

    The primary representation uses two pairs of note numbers and durations.

    The first pair of note numbers and durations describes the representation
    within the tuplet, or the value presented by the context. This is called
    “actual.” In a standard 8th note triplet this would be 3, eighth, meaning
    that a complete collection of this tuplet will be visually represented as
    three eighth notes. These
    attributes are numberNotesActual, durationActual.

    The second pair of note numbers and durations describes the space that
    would have been occupied in a normal context. This is called “normal.” In a
    standard 8th note triplet this would be 2, eighth, meaning that a complete
    collection of notes under this tuplet will occupy the space of two eighth notes.
    These attributes are
    numberNotesNormal, durationNormal.

    If duration values are not provided then durationActual and durationNormal are
    left as None – meaning that it is unspecified what the duration that completes the
    tuplet is. And this tuplet just represents a Ratio.
    PRIOR TO v4 durationActual and durationNormal were assumed to be eighths.

    If only one duration, either durationActual or durationNormal, is
    provided, both are set to the same value.

    Note that this is a duration modifier, or a generator of ratios to scale
    quarterLength values in Duration objects.

    ```python
    >>> myTup = duration.Tuplet(numberNotesActual=5, numberNotesNormal=4)
    >>> print(myTup.tupletMultiplier())
    4/5
    ```

    We know that it is 5 in the place of 4, but 5 what in the place of 4 what?

    ```python
    >>> myTup.durationActual is None
    True
    >>> myTup
    <music21.duration.Tuplet 5/4>
    ```

    But we can change that:

    ```python
    >>> myTup.setDurationType('eighth')
    >>> myTup.durationActual
    DurationTuple(type='eighth', dots=0, quarterLength=0.5)
    >>> myTup
    <music21.duration.Tuplet 5/4/eighth>
    ```

    In this case, the tupletMultiplier is a float because it can be expressed
    as a binary number:

    ```python
    >>> myTup2 = duration.Tuplet(8, 5)
    >>> tm = myTup2.tupletMultiplier()
    >>> tm
    0.625
    ```

    Here, six sixteenth notes occupy the space of four sixteenth notes.

    ```python
    >>> myTup2 = duration.Tuplet(6, 4, '16th')
    >>> print(myTup2.durationActual.type)
    16th
    >>> print(myTup2.durationNormal.type)
    16th
    ```

    ```python
    >>> print(myTup2.tupletMultiplier())
    2/3
    ```

    Tuplets may be frozen, in which case they become immutable. Tuplets
    which are attached to Durations are automatically frozen. Otherwise
    a tuplet could change without the attached duration knowing about it,
    which would be a real problem.

    ```python
    >>> myTup.frozen = True
    >>> myTup.tupletActual = [3, 2]
    Traceback (most recent call last):
    music21.duration.TupletException: A frozen tuplet (or one attached to a duration)
        has immutable length.
    ```

    ```python
    >>> myHalf = duration.Duration('half')
    >>> myHalf.appendTuplet(myTup2)
    >>> myTup2.tupletActual = [5, 4]
    Traceback (most recent call last):
    music21.duration.TupletException: A frozen tuplet (or one attached to a duration)
        has immutable length.
    ```

    Note that if you want to create a note with a simple Tuplet attached to it,
    you can just change the quarterLength of the note:

    ```python
    >>> myNote = note.Note('C#4')
    >>> myNote.duration.quarterLength = 0.8
    >>> myNote.duration.quarterLength
    Fraction(4, 5)
    >>> myNote.duration.fullName
    'Quarter Quintuplet (4/5 QL)'
    ```

    ```python
    >>> myNote.duration.tuplets
    (<music21.duration.Tuplet 5/4/quarter>,)
    ```

[`Tuplet`](#music21.duration.Tuplet "music21.duration.Tuplet") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Tuplet`](#music21.duration.Tuplet "music21.duration.Tuplet") read-only properties

Tuplet.fullName
:   Return the most complete representation of this tuplet in a readable
    form.

    ```python
    >>> tup = duration.Tuplet(numberNotesActual=5, numberNotesNormal=2)
    >>> tup.fullName
    'Quintuplet'
    ```

    ```python
    >>> tup = duration.Tuplet(numberNotesActual=3, numberNotesNormal=2)
    >>> tup.fullName
    'Triplet'
    ```

    ```python
    >>> tup = duration.Tuplet(numberNotesActual=17, numberNotesNormal=14)
    >>> tup.fullName
    'Tuplet of 17/14ths'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Tuplet`](#music21.duration.Tuplet "music21.duration.Tuplet") read/write properties

Tuplet.durationActual
:   durationActual is a DurationTuple that represents the notes that are
    actually present and counted in a tuplet. For instance, in a 7
    dotted-eighth in the place of 2 double-dotted quarter notes tuplet,
    the duration actual would be this:

    ```python
    >>> d = duration.Tuplet(7, 2)
    >>> print(d.durationActual)
    None
    >>> d.durationActual = duration.Duration('eighth', dots=1)
    ```

    Notice that the Duration object gets converted to a DurationTuple.

    ```python
    >>> d.durationActual
    DurationTuple(type='eighth', dots=1, quarterLength=0.75)
    ```

    ```python
    >>> d.durationActual = 'quarter'
    >>> d.durationActual
    DurationTuple(type='quarter', dots=0, quarterLength=1.0)
    ```

Tuplet.durationNormal
:   durationNormal is a DurationTuple that represents the notes that
    would be present in the space normally (if there were no tuplets). For instance, in a 7
    dotted-eighth in the place of 2 double-dotted quarter notes tuplet,
    the durationNormal would be:

    ```python
    >>> d = duration.Tuplet(7, 2)
    >>> print(d.durationNormal)
    None
    >>> d.durationNormal = duration.Duration('quarter', dots=2)
    ```

    Notice that the Duration object gets converted to a DurationTuple:

    ```python
    >>> d.durationNormal
    DurationTuple(type='quarter', dots=2, quarterLength=1.75)
    ```

    ```python
    >>> d.durationNormal = 'half'
    >>> d.durationNormal
    DurationTuple(type='half', dots=0, quarterLength=2.0)
    ```

Tuplet.tupletActual
:   Get or set a two element list of number notes actual and duration
    actual.

Tuplet.tupletNormal
:   Get or set a two element list of number notes actual and duration
    normal.

[`Tuplet`](#music21.duration.Tuplet "music21.duration.Tuplet") methods

Tuplet.\_\_eq\_\_(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Tuplet.__eq__)
:   Two Tuplets are equal if their numbers are equal and durations are equal.

    Visual details (type, bracket, placement, tupletActualShow, etc.) do
    not matter.

    ```python
    >>> triplet1 = duration.Tuplet(3, 2)
    >>> triplet2 = duration.Tuplet(3, 2)
    >>> triplet1 == triplet2
    True
    >>> quadruplet = duration.Tuplet(4, 3)
    >>> triplet1 == quadruplet
    False
    >>> triplet3 = duration.Tuplet(3, 2, 'half')
    >>> triplet1 == triplet3
    False
    ```

Tuplet.augmentOrDiminish(*amountToScale: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*)[[source]](../_modules/music21/duration.html#Tuplet.augmentOrDiminish)
:   Given a number greater than zero,
    multiplies the current quarterLength of the
    duration by the number and resets the components
    for the duration (by default). Or if inPlace is
    set to False, returns a new duration that has
    the new length.

    # TODO: add inPlace setting.

    ```python
    >>> a = duration.Tuplet()
    >>> a.setRatio(6, 2)
    >>> a.tupletMultiplier()
    Fraction(1, 3)
    >>> a.setDurationType('eighth')
    >>> a.durationActual
    DurationTuple(type='eighth', dots=0, quarterLength=0.5)
    ```

    ```python
    >>> c = a.augmentOrDiminish(0.5)
    >>> c.durationActual
    DurationTuple(type='16th', dots=0, quarterLength=0.25)
    ```

    ```python
    >>> c.tupletMultiplier()
    Fraction(1, 3)
    ```

    Raises ValueError if amountToScale is negative.

    ```python
    >>> a.augmentOrDiminish(-1)
    Traceback (most recent call last):
    ValueError: amountToScale must be greater than zero
    ```

Tuplet.setDurationType(*durType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *dots: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Tuplet.setDurationType)
:   Set both durationActual and durationNormal from either a string type or
    a quarterLength. optional dots can add dots to a string type (or I suppose
    a quarterLength.)

    ```python
    >>> a = duration.Tuplet()
    >>> a.tupletMultiplier()
    Fraction(2, 3)
    >>> a.totalTupletLength()
    1.0
    >>> a.setDurationType('half')
    >>> a.durationNormal
    DurationTuple(type='half', dots=0, quarterLength=2.0)
    >>> a.tupletMultiplier()
    Fraction(2, 3)
    >>> a.totalTupletLength()
    4.0
    >>> a.setDurationType('half', dots=1)
    >>> a.durationNormal
    DurationTuple(type='half', dots=1, quarterLength=3.0)
    >>> a.totalTupletLength()
    6.0
    ```

    ```python
    >>> a.setDurationType(2.0)
    >>> a.totalTupletLength()
    4.0
    >>> a.setDurationType(4.0)
    >>> a.totalTupletLength()
    8.0
    ```

Tuplet.setRatio(*actual: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *normal: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Tuplet.setRatio)
:   Set the ratio of actual divisions to represented in normal divisions.
    A triplet is 3 actual in the time of 2 normal.

    ```python
    >>> a = duration.Tuplet()
    >>> a.tupletMultiplier()
    Fraction(2, 3)
    >>> a.setRatio(6, 2)
    >>> a.numberNotesActual
    6
    >>> a.numberNotesNormal
    2
    >>> a.tupletMultiplier()
    Fraction(1, 3)
    ```

    One way of expressing 6/4-ish triplets without numbers:

    ```python
    >>> a = duration.Tuplet()
    >>> a.setRatio(3, 1)
    >>> a.durationActual = duration.durationTupleFromTypeDots('quarter', 0)
    >>> a.durationNormal = duration.durationTupleFromTypeDots('half', 0)
    >>> a.tupletMultiplier()
    Fraction(2, 3)
    >>> a.totalTupletLength()
    2.0
    ```

Tuplet.totalTupletLength() → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Tuplet.totalTupletLength)
:   The total duration in quarter length of the tuplet as defined,
    assuming that enough notes existed to fill all entire tuplet as defined.

    For instance, 3 quarters in the place of 2 quarters = 2.0
    5 half notes in the place of a 2 dotted half notes = 6.0
    (In the end it’s only the denominator that matters)

    If durationActual or durationNormal are None, then they will be
    assumed to be eighth notes (for the basic 3:2 eighth-note triplet)

    ```python
    >>> a = duration.Tuplet()
    >>> a.totalTupletLength()
    1.0
    ```

    ```python
    >>> a.numberNotesActual = 3
    >>> a.numberNotesNormal = 2
    >>> a.setDurationType('half')
    >>> a.totalTupletLength()
    4.0
    ```

    Let’s make it five halfs in the place of four:

    ```python
    >>> a.setRatio(5, 4)
    >>> a.setDurationType('half')
    >>> a.totalTupletLength()
    8.0
    ```

    Now five halfs in the place of two whole notes (same thing):

    ```python
    >>> a.setRatio(5, 2)
    >>> a.totalTupletLength()
    4.0
    >>> a.durationNormal = duration.durationTupleFromTypeDots('whole', 0)
    >>> a.totalTupletLength()
    8.0
    ```

Tuplet.tupletMultiplier() → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/duration.html#Tuplet.tupletMultiplier)
:   Get a Fraction() by which to scale the duration that
    this Tuplet is associated with.

    ```python
    >>> myTuplet = duration.Tuplet()
    >>> myTuplet.tupletMultiplier()
    Fraction(2, 3)
    >>> myTuplet.tupletActual = [5, duration.Duration('eighth')]
    >>> myTuplet.numberNotesActual
    5
    >>> myTuplet.durationActual.type
    'eighth'
    >>> print(myTuplet.tupletMultiplier())
    2/5
    >>> myTuplet.numberNotesNormal = 4
    >>> print(myTuplet.tupletMultiplier())
    4/5
    ```

## GraceDuration

class music21.duration.GraceDuration(*typeOrDuration: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/duration.html#GraceDuration)
:   A Duration that, no matter how it is created, always has a quarter length
    of zero.

    GraceDuration can be created with an implied quarter length and type; these
    values are used to configure the duration, but then may not be relevant
    after instantiation.

    ```python
    >>> gd = duration.GraceDuration(type='half')
    >>> gd.quarterLength
    0.0
    ```

    ```python
    >>> gd.type
    'half'
    ```

    ```python
    >>> gd = duration.GraceDuration(0.25)
    >>> gd.type
    '16th'
    ```

    ```python
    >>> gd.quarterLength
    0.0
    ```

    ```python
    >>> gd.linked
    False
    ```

    ```python
    >>> gd = duration.GraceDuration(1.25)
    >>> gd.type
    'complex'
    ```

    ```python
    >>> gd.quarterLength
    0.0
    ```

    ```python
    >>> [(x.quarterLength, x.type) for x in gd.components]
    [(0.0, 'quarter'), (0.0, '16th')]
    ```

[`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration") bases

* [`Duration`](#music21.duration.Duration "music21.duration.Duration")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration") read-only properties

Read-only properties inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](#music21.duration.Duration.fullName "music21.duration.Duration.fullName") * [`isComplex`](#music21.duration.Duration.isComplex "music21.duration.Duration.isComplex") | * [`ordinal`](#music21.duration.Duration.ordinal "music21.duration.Duration.ordinal") | * [`quarterLengthNoTuplets`](#music21.duration.Duration.quarterLengthNoTuplets "music21.duration.Duration.quarterLengthNoTuplets") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration") read/write properties

GraceDuration.makeTime
:   True, False, or None (=unknown) whether the grace note should occupy time
    in performance. Default False. Currently not used in generated playback.

    TODO: allow a duration object or number for duration.

GraceDuration.slash
:   True, False, or None (=unknown) whether the grace note should have a slash
    through it. Default True.

Read/write properties inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`components`](#music21.duration.Duration.components "music21.duration.Duration.components") * [`dotGroups`](#music21.duration.Duration.dotGroups "music21.duration.Duration.dotGroups") * [`dots`](#music21.duration.Duration.dots "music21.duration.Duration.dots") | * [`linked`](#music21.duration.Duration.linked "music21.duration.Duration.linked") * [`quarterLength`](#music21.duration.Duration.quarterLength "music21.duration.Duration.quarterLength") | * [`tuplets`](#music21.duration.Duration.tuplets "music21.duration.Duration.tuplets") * [`type`](#music21.duration.Duration.type "music21.duration.Duration.type") |

[`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration") methods

Methods inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.duration.Duration.__eq__ "music21.duration.Duration.__eq__") * [`addDurationTuple()`](#music21.duration.Duration.addDurationTuple "music21.duration.Duration.addDurationTuple") * [`aggregateTupletMultiplier()`](#music21.duration.Duration.aggregateTupletMultiplier "music21.duration.Duration.aggregateTupletMultiplier") * [`appendTuplet()`](#music21.duration.Duration.appendTuplet "music21.duration.Duration.appendTuplet") * [`augmentOrDiminish()`](#music21.duration.Duration.augmentOrDiminish "music21.duration.Duration.augmentOrDiminish") | * [`clear()`](#music21.duration.Duration.clear "music21.duration.Duration.clear") * [`componentIndexAtQtrPosition()`](#music21.duration.Duration.componentIndexAtQtrPosition "music21.duration.Duration.componentIndexAtQtrPosition") * [`componentStartTime()`](#music21.duration.Duration.componentStartTime "music21.duration.Duration.componentStartTime") * [`consolidate()`](#music21.duration.Duration.consolidate "music21.duration.Duration.consolidate") * [`currentComponents()`](#music21.duration.Duration.currentComponents "music21.duration.Duration.currentComponents") | * [`getGraceDuration()`](#music21.duration.Duration.getGraceDuration "music21.duration.Duration.getGraceDuration") * [`informClient()`](#music21.duration.Duration.informClient "music21.duration.Duration.informClient") * [`sliceComponentAtPosition()`](#music21.duration.Duration.sliceComponentAtPosition "music21.duration.Duration.sliceComponentAtPosition") * [`splitDotGroups()`](#music21.duration.Duration.splitDotGroups "music21.duration.Duration.splitDotGroups") |

[`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration") instance variables

GraceDuration.stealTimeFollowing
:   Float number from 0.0 to 1.0 or None (default) for the proportion
    of the following duration to steal from the following note.

GraceDuration.stealTimePrevious
:   Float number from 0.0 to 1.0, or None (default) for the proportion
    of the previous duration to steal from the previous note.

Instance variables inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.duration.Duration.client "music21.duration.Duration.client") | * [`expressionIsInferred`](#music21.duration.Duration.expressionIsInferred "music21.duration.Duration.expressionIsInferred") |  |

## TupletFixer

class music21.duration.TupletFixer(*streamIn: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/duration.html#TupletFixer)
:   The TupletFixer object takes in a flat stream and tries to fix the
    brackets and time modification values of the tuplet so that they
    reflect proper beaming, etc. It does not alter the quarterLength
    of any notes.

    See [`findTupletGroups()`](#music21.duration.TupletFixer.findTupletGroups "music21.duration.TupletFixer.findTupletGroups") and
    [`fixBrokenTupletDuration()`](#music21.duration.TupletFixer.fixBrokenTupletDuration "music21.duration.TupletFixer.fixBrokenTupletDuration") for
    demonstrations.

[`TupletFixer`](#music21.duration.TupletFixer "music21.duration.TupletFixer") methods

TupletFixer.findTupletGroups(*incorporateGroupings: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")]][[source]](../_modules/music21/duration.html#TupletFixer.findTupletGroups)
:   Finds all tuplets in the stream and puts them into groups.

    If incorporateGroupings is True, then a tuplet.type=”stop”
    ends a tuplet group even if the next note is a tuplet.

    This demonstration has three groups of tuplets, two sets of 8th note
    tuplets and one of 16ths:

    ```python
    >>> c = converter.parse(
    ...    'tinynotation: 4/4 trip{c8 d e} f4 trip{c#8 d# e#} g8 trip{c-16 d- e-}',
    ...    makeNotation=False)
    >>> tf = duration.TupletFixer(c)  # no need to flatten this stream
    >>> tupletGroups = tf.findTupletGroups()
    >>> tupletGroups
    [[<music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>],
     [<music21.note.Note C#>, <music21.note.Note D#>, <music21.note.Note E#>],
     [<music21.note.Note C->, <music21.note.Note D->, <music21.note.Note E->]]
    ```

    These groups are stored in TupletFixer.allTupletGroups:

    ```python
    >>> tupletGroups is tf.allTupletGroups
    True
    ```

    Demonstration with incorporateGroupings:

    ```python
    >>> s = stream.Stream()
    >>> for i in range(9):
    ...    n = note.Note()
    ...    n.pitch.ps = 60 + i
    ...    n.duration.quarterLength = 1/3
    ...    if i % 3 == 2:
    ...        n.duration.tuplets[0].type = 'stop'
    ...    s.append(n)
    >>> tf = duration.TupletFixer(s)
    >>> tupletGroups = tf.findTupletGroups(incorporateGroupings=True)
    >>> tupletGroups
    [[<music21.note.Note C>, <music21.note.Note C#>, <music21.note.Note D>],
     [<music21.note.Note E->, <music21.note.Note E>, <music21.note.Note F>],
     [<music21.note.Note F#>, <music21.note.Note G>, <music21.note.Note G#>]]
    ```

    Without incorporateGroupings we just get one big set of tuplets

    ```python
    >>> tupletGroups = tf.findTupletGroups()
    >>> len(tupletGroups)
    1
    >>> len(tupletGroups[0])
    9
    ```

TupletFixer.fixBrokenTupletDuration(*tupletGroup: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletFixer.fixBrokenTupletDuration)
:   Tries to fix cases like triplet quarter followed by triplet
    eighth to be a coherent tuplet.

    Requires a tuplet group from findTupletGroups() or TupletFixer.allTupletGroups.
    Note: this works on a single tupletGroup while findTupletGroups()
    returns a list of groups.

    ```python
    >>> s = stream.Stream()
    ```

    ```python
    >>> n1 = note.Note('C')
    >>> n1.duration.quarterLength = 2/3
    >>> n1.duration.quarterLength
    Fraction(2, 3)
    >>> s.append(n1)
    >>> n2 = note.Note('D')
    >>> n2.duration.quarterLength = 1/3
    >>> n2.duration.quarterLength
    Fraction(1, 3)
    >>> s.append(n2)
    ```

    Here are the current tuplets for the two notes:

    ```python
    >>> n1.duration.tuplets[0]
    <music21.duration.Tuplet 3/2/quarter>
    >>> n2.duration.tuplets[0]
    <music21.duration.Tuplet 3/2/eighth>
    ```

    Notice how the first note is waiting for 3 triplet quarters to
    complete itself. But it could be 2/3 of a quarter note divided into
    eighth note triplets. TupletFixer will work on this.

    It takes in a flattened stream, like this one:

    ```python
    >>> tf = duration.TupletFixer(s)
    ```

    Find the tuplet groups. Returning a list of one group, which has
    two notes in it:

    ```python
    >>> tupletGroups = tf.findTupletGroups()
    >>> tupletGroups
    [[<music21.note.Note C>, <music21.note.Note D>]]
    ```

    Now fix that single group:

    ```python
    >>> tg0 = tupletGroups[0]
    >>> [n.duration.tuplets[0].type for n in tg0]
    [None, None]
    ```

    ```python
    >>> tf.fixBrokenTupletDuration(tg0)
    ```

    Now the first quarter-note triplet knows that its group
    will be complete after the next note:

    ```python
    >>> n1.duration.tuplets[0]
    <music21.duration.Tuplet 3/2/eighth>
    >>> n1.duration.quarterLength
    Fraction(2, 3)
    >>> n2.duration.tuplets[0]
    <music21.duration.Tuplet 3/2/eighth>
    ```

    Note that the tuplet type is not affected by this call:

    ```python
    >>> [n.duration.tuplets[0].type for n in tg0]
    [None, None]
    ```

    To do that, call [`makeTupletBrackets()`](moduleStreamMakeNotation.html#music21.stream.makeNotation.makeTupletBrackets "music21.stream.makeNotation.makeTupletBrackets")
    on the flattened stream:

    ```python
    >>> stream.makeNotation.makeTupletBrackets(s, inPlace=True)
    >>> [n.duration.tuplets[0].type for n in tg0]
    ['start', 'stop']
    ```

    More complex example, from a piece by Josquin:

    ```python
    >>> humdrumExcerpt = '**kern *M3/1 3.c 6d 3e 3f 3d 3%2g 3e 3f#'
    >>> humdrumLines = '\n'.join(humdrumExcerpt.split())
    ```

    There is a side format of humdrum that the Josquin Research Project uses
    for long notes like the 3%2.

    ```python
    >>> humdrum.spineParser.flavors['JRP'] = True
    ```

    Since Humdrum parsing is going to apply TupletFixer, we will temporarily
    disable it:

    ```python
    >>> saved_fixed_broken = duration.TupletFixer.fixBrokenTupletDuration
    >>> duration.TupletFixer.fixBrokenTupletDuration = lambda x,y: None
    ```

    ```python
    >>> s = converter.parse(humdrumLines, format='humdrum')
    ```

    ```python
    >>> m1 = s.parts.first().measure(1)
    >>> m1.show('text', addEndTimes=True)
    {0.0 - 0.0} <music21.meter.TimeSignature 3/1>
    {0.0 - 2.0} <music21.note.Note C>
    {2.0 - 2.6667} <music21.note.Note D>
    {2.6667 - 4.0} <music21.note.Note E>
    {4.0 - 5.3333} <music21.note.Note F>
    {5.3333 - 6.6667} <music21.note.Note D>
    {6.6667 - 9.3333} <music21.note.Note G>
    {9.3333 - 10.6667} <music21.note.Note E>
    {10.6667 - 12.0} <music21.note.Note F#>
    ```

    ```python
    >>> duration.TupletFixer.fixBrokenTupletDuration = saved_fixed_broken
    >>> tf = duration.TupletFixer(m1)
    >>> tupletGroups = tf.findTupletGroups(incorporateGroupings=True)
    >>> tupletGroups
    [[<music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>],
     [<music21.note.Note F>, <music21.note.Note D>, <music21.note.Note G>,
      <music21.note.Note E>, <music21.note.Note F#>]]
    ```

    There’s a problem with the last group: it contains 5 notes and the
    third note is twice as long as the others, so none of them form a coherent
    triplet.

    ```python
    >>> [n.duration.tuplets[0] for n in tupletGroups[1]]
    [<music21.duration.Tuplet 3/2/half>, <music21.duration.Tuplet 3/2/half>,
     <music21.duration.Tuplet 3/2/whole>,
     <music21.duration.Tuplet 3/2/half>, <music21.duration.Tuplet 3/2/half>]
    >>> [n.duration.tuplets[0].type for n in tupletGroups[1]]
    ['start', None, None, None, 'stop']
    ```

    Fix the last broken tuplet group.

    ```python
    >>> tf.fixBrokenTupletDuration(tupletGroups[1])
    >>> [n.duration.tuplets[0] for n in tupletGroups[1]]
    [<music21.duration.Tuplet 3/2/whole>, <music21.duration.Tuplet 3/2/whole>,
     <music21.duration.Tuplet 3/2/whole>,
     <music21.duration.Tuplet 3/2/whole>, <music21.duration.Tuplet 3/2/whole>]
    ```

    Note that the changes appear in the notes in the Stream as well.

    ```python
    >>> m1.last().duration.tuplets[0]
    <music21.duration.Tuplet 3/2/whole>
    ```

    Again, TupletFixer is automatically called when parsing from Humdrum.
    (MusicXML specifies its tuplet groups explicitly.) But you may need it
    when building up a stream from scratch in your own projects.

TupletFixer.setStream(*streamIn: stream.Stream*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletFixer.setStream)
:   Define a stream to work on and reset all temporary variables.

## AppoggiaturaDuration

class music21.duration.AppoggiaturaDuration(*typeOrDuration: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/duration.html#AppoggiaturaDuration)
:   Renamed in v6 to correct spelling.

[`AppoggiaturaDuration`](#music21.duration.AppoggiaturaDuration "music21.duration.AppoggiaturaDuration") bases

* [`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration")
* [`Duration`](#music21.duration.Duration "music21.duration.Duration")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`AppoggiaturaDuration`](#music21.duration.AppoggiaturaDuration "music21.duration.AppoggiaturaDuration") read-only properties

Read-only properties inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](#music21.duration.Duration.fullName "music21.duration.Duration.fullName") * [`isComplex`](#music21.duration.Duration.isComplex "music21.duration.Duration.isComplex") | * [`ordinal`](#music21.duration.Duration.ordinal "music21.duration.Duration.ordinal") | * [`quarterLengthNoTuplets`](#music21.duration.Duration.quarterLengthNoTuplets "music21.duration.Duration.quarterLengthNoTuplets") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AppoggiaturaDuration`](#music21.duration.AppoggiaturaDuration "music21.duration.AppoggiaturaDuration") read/write properties

Read/write properties inherited from [`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration"):

|  |  |  |
| --- | --- | --- |
| * [`makeTime`](#music21.duration.GraceDuration.makeTime "music21.duration.GraceDuration.makeTime") | * [`slash`](#music21.duration.GraceDuration.slash "music21.duration.GraceDuration.slash") |  |

Read/write properties inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`components`](#music21.duration.Duration.components "music21.duration.Duration.components") * [`dotGroups`](#music21.duration.Duration.dotGroups "music21.duration.Duration.dotGroups") * [`dots`](#music21.duration.Duration.dots "music21.duration.Duration.dots") | * [`linked`](#music21.duration.Duration.linked "music21.duration.Duration.linked") * [`quarterLength`](#music21.duration.Duration.quarterLength "music21.duration.Duration.quarterLength") | * [`tuplets`](#music21.duration.Duration.tuplets "music21.duration.Duration.tuplets") * [`type`](#music21.duration.Duration.type "music21.duration.Duration.type") |

[`AppoggiaturaDuration`](#music21.duration.AppoggiaturaDuration "music21.duration.AppoggiaturaDuration") methods

Methods inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.duration.Duration.__eq__ "music21.duration.Duration.__eq__") * [`addDurationTuple()`](#music21.duration.Duration.addDurationTuple "music21.duration.Duration.addDurationTuple") * [`aggregateTupletMultiplier()`](#music21.duration.Duration.aggregateTupletMultiplier "music21.duration.Duration.aggregateTupletMultiplier") * [`appendTuplet()`](#music21.duration.Duration.appendTuplet "music21.duration.Duration.appendTuplet") * [`augmentOrDiminish()`](#music21.duration.Duration.augmentOrDiminish "music21.duration.Duration.augmentOrDiminish") | * [`clear()`](#music21.duration.Duration.clear "music21.duration.Duration.clear") * [`componentIndexAtQtrPosition()`](#music21.duration.Duration.componentIndexAtQtrPosition "music21.duration.Duration.componentIndexAtQtrPosition") * [`componentStartTime()`](#music21.duration.Duration.componentStartTime "music21.duration.Duration.componentStartTime") * [`consolidate()`](#music21.duration.Duration.consolidate "music21.duration.Duration.consolidate") * [`currentComponents()`](#music21.duration.Duration.currentComponents "music21.duration.Duration.currentComponents") | * [`getGraceDuration()`](#music21.duration.Duration.getGraceDuration "music21.duration.Duration.getGraceDuration") * [`informClient()`](#music21.duration.Duration.informClient "music21.duration.Duration.informClient") * [`sliceComponentAtPosition()`](#music21.duration.Duration.sliceComponentAtPosition "music21.duration.Duration.sliceComponentAtPosition") * [`splitDotGroups()`](#music21.duration.Duration.splitDotGroups "music21.duration.Duration.splitDotGroups") |

[`AppoggiaturaDuration`](#music21.duration.AppoggiaturaDuration "music21.duration.AppoggiaturaDuration") instance variables

Instance variables inherited from [`GraceDuration`](#music21.duration.GraceDuration "music21.duration.GraceDuration"):

|  |  |  |
| --- | --- | --- |
| * [`stealTimeFollowing`](#music21.duration.GraceDuration.stealTimeFollowing "music21.duration.GraceDuration.stealTimeFollowing") | * [`stealTimePrevious`](#music21.duration.GraceDuration.stealTimePrevious "music21.duration.GraceDuration.stealTimePrevious") |  |

Instance variables inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.duration.Duration.client "music21.duration.Duration.client") | * [`expressionIsInferred`](#music21.duration.Duration.expressionIsInferred "music21.duration.Duration.expressionIsInferred") |  |

## DurationTuple

class music21.duration.DurationTuple(*type*, *dots*, *quarterLength*)[[source]](../_modules/music21/duration.html#DurationTuple)

[`DurationTuple`](#music21.duration.DurationTuple "music21.duration.DurationTuple") read-only properties

DurationTuple.ordinal
:   Converts type to an ordinal number where maxima = 1 and 1024th = 14;
    whole = 4 and quarter = 6. Based on duration.ordinalTypeFromNum

    ```python
    >>> a = duration.DurationTuple('whole', 0, 4.0)
    >>> a.ordinal
    4
    ```

    ```python
    >>> b = duration.DurationTuple('maxima', 0, 32.0)
    >>> b.ordinal
    1
    ```

    ```python
    >>> c = duration.DurationTuple('1024th', 0, 1/256)
    >>> c.ordinal
    14
    ```

[`DurationTuple`](#music21.duration.DurationTuple "music21.duration.DurationTuple") methods

DurationTuple.augmentOrDiminish(*amountToScale*)[[source]](../_modules/music21/duration.html#DurationTuple.augmentOrDiminish)

## FrozenDuration

class music21.duration.FrozenDuration(*\*arguments*, *\*\*keywords*)[[source]](../_modules/music21/duration.html#FrozenDuration)
:   A FrozenDuration is one that must have all of its arguments specified
    at the time of construction. After that, it is immutable, like a Tuple
    and thus can be shared across different objects (like in MeterTerminals)
    or used as a hash.

    ```python
    >>> fd = duration.FrozenDuration(type='half', dots=2)
    >>> fd.quarterLength
    3.5
    >>> fd.dots = 1
    Traceback (most recent call last):
    TypeError: This FrozenDuration instance is immutable.
    ```

    FrozenDurations can be used as set/dict keys with stability.

    ```python
    >>> {fd}
    {<music21.duration.FrozenDuration 3.5>}
    ```

    Copying a FrozenDuration returns the original, so it is super fast.

    ```python
    >>> import copy
    >>> copy.deepcopy(fd) is fd
    True
    ```

[`FrozenDuration`](#music21.duration.FrozenDuration "music21.duration.FrozenDuration") bases

* [`FrozenObject`](moduleCommonObjects.html#music21.common.objects.FrozenObject "music21.common.objects.FrozenObject")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`Duration`](#music21.duration.Duration "music21.duration.Duration")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`FrozenDuration`](#music21.duration.FrozenDuration "music21.duration.FrozenDuration") read-only properties

Read-only properties inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](#music21.duration.Duration.fullName "music21.duration.Duration.fullName") * [`isComplex`](#music21.duration.Duration.isComplex "music21.duration.Duration.isComplex") | * [`ordinal`](#music21.duration.Duration.ordinal "music21.duration.Duration.ordinal") | * [`quarterLengthNoTuplets`](#music21.duration.Duration.quarterLengthNoTuplets "music21.duration.Duration.quarterLengthNoTuplets") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`FrozenDuration`](#music21.duration.FrozenDuration "music21.duration.FrozenDuration") read/write properties

Read/write properties inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`components`](#music21.duration.Duration.components "music21.duration.Duration.components") * [`dotGroups`](#music21.duration.Duration.dotGroups "music21.duration.Duration.dotGroups") * [`dots`](#music21.duration.Duration.dots "music21.duration.Duration.dots") | * [`linked`](#music21.duration.Duration.linked "music21.duration.Duration.linked") * [`quarterLength`](#music21.duration.Duration.quarterLength "music21.duration.Duration.quarterLength") | * [`tuplets`](#music21.duration.Duration.tuplets "music21.duration.Duration.tuplets") * [`type`](#music21.duration.Duration.type "music21.duration.Duration.type") |

[`FrozenDuration`](#music21.duration.FrozenDuration "music21.duration.FrozenDuration") methods

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

Methods inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`addDurationTuple()`](#music21.duration.Duration.addDurationTuple "music21.duration.Duration.addDurationTuple") * [`aggregateTupletMultiplier()`](#music21.duration.Duration.aggregateTupletMultiplier "music21.duration.Duration.aggregateTupletMultiplier") * [`appendTuplet()`](#music21.duration.Duration.appendTuplet "music21.duration.Duration.appendTuplet") * [`augmentOrDiminish()`](#music21.duration.Duration.augmentOrDiminish "music21.duration.Duration.augmentOrDiminish") * [`clear()`](#music21.duration.Duration.clear "music21.duration.Duration.clear") | * [`componentIndexAtQtrPosition()`](#music21.duration.Duration.componentIndexAtQtrPosition "music21.duration.Duration.componentIndexAtQtrPosition") * [`componentStartTime()`](#music21.duration.Duration.componentStartTime "music21.duration.Duration.componentStartTime") * [`consolidate()`](#music21.duration.Duration.consolidate "music21.duration.Duration.consolidate") * [`currentComponents()`](#music21.duration.Duration.currentComponents "music21.duration.Duration.currentComponents") | * [`getGraceDuration()`](#music21.duration.Duration.getGraceDuration "music21.duration.Duration.getGraceDuration") * [`informClient()`](#music21.duration.Duration.informClient "music21.duration.Duration.informClient") * [`sliceComponentAtPosition()`](#music21.duration.Duration.sliceComponentAtPosition "music21.duration.Duration.sliceComponentAtPosition") * [`splitDotGroups()`](#music21.duration.Duration.splitDotGroups "music21.duration.Duration.splitDotGroups") |

[`FrozenDuration`](#music21.duration.FrozenDuration "music21.duration.FrozenDuration") instance variables

Instance variables inherited from [`Duration`](#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.duration.Duration.client "music21.duration.Duration.client") | * [`expressionIsInferred`](#music21.duration.Duration.expressionIsInferred "music21.duration.Duration.expressionIsInferred") |  |

## QuarterLengthConversion

class music21.duration.QuarterLengthConversion(*components*, *tuplet*)[[source]](../_modules/music21/duration.html#QuarterLengthConversion)

## TupletSearchState

class music21.duration.TupletSearchState(*onlyIfTied=True*)[[source]](../_modules/music21/duration.html#TupletSearchState)
:   Private helper for makeNotation.consolidateCompletedTuplets().

[`TupletSearchState`](#music21.duration.TupletSearchState "music21.duration.TupletSearchState") methods

TupletSearchState.advance\_tuplet\_sum(*gn: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletSearchState.advance_tuplet_sum)

TupletSearchState.append(*gn: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletSearchState.append)

TupletSearchState.get\_consolidatable\_notes() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")][[source]](../_modules/music21/duration.html#TupletSearchState.get_consolidatable_notes)

TupletSearchState.is\_reexpressible(*gn: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletSearchState.is_reexpressible)

TupletSearchState.mark\_no\_consolidation() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletSearchState.mark_no_consolidation)

TupletSearchState.reset() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletSearchState.reset)

TupletSearchState.should\_be\_tested(*gn: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/duration.html#TupletSearchState.should_be_tested)

## Functions

music21.duration.convertQuarterLengthToType(*qLen: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/duration.html#convertQuarterLengthToType)
:   Return a type if there exists a type that is exactly equal to the
    duration of the provided quarterLength. Similar to
    quarterLengthToClosestType() but this
    function only returns exact matches.

    ```python
    >>> duration.convertQuarterLengthToType(2)
    'half'
    >>> duration.convertQuarterLengthToType(0.125)
    '32nd'
    >>> duration.convertQuarterLengthToType(0.33333)
    Traceback (most recent call last):
    music21.duration.DurationException: cannot convert quarterLength 0.33333 exactly to type
    ```

music21.duration.convertTypeToNumber(*dType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/duration.html#convertTypeToNumber)
:   Convert a duration type string (dType) to a numerical scalar representation that shows
    how many of that duration type fits within a whole note.

    ```python
    >>> duration.convertTypeToNumber('quarter')
    4.0
    >>> duration.convertTypeToNumber('half')
    2.0
    >>> duration.convertTypeToNumber('1024th')
    1024.0
    >>> duration.convertTypeToNumber('maxima')
    0.125
    ```

    These other types give these results:

    ```python
    >>> duration.convertTypeToNumber('zero')
    0.0
    >>> duration.convertTypeToNumber('complex')
    Traceback (most recent call last):
    music21.duration.DurationException: Could not determine durationNumber from complex
    ```

music21.duration.convertTypeToQuarterLength(*dType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *dots: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *tuplets: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Tuplet](#music21.duration.Tuplet "music21.duration.Tuplet")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *dotGroups=None*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/duration.html#convertTypeToQuarterLength)
:   Given a rhythm type (dType), number of dots (dots), an optional list of
    Tuplet objects (tuplets), and a (very) optional list of
    Medieval dot groups (dotGroups), return the equivalent quarter length.

    ```python
    >>> duration.convertTypeToQuarterLength('whole')
    4.0
    >>> duration.convertTypeToQuarterLength('16th')
    0.25
    >>> duration.convertTypeToQuarterLength('quarter', 2)
    1.75
    ```

    ```python
    >>> tup = duration.Tuplet(numberNotesActual=5, numberNotesNormal=4)
    >>> duration.convertTypeToQuarterLength('quarter', 0, [tup])
    Fraction(4, 5)
    >>> duration.convertTypeToQuarterLength('quarter', 1, [tup])
    Fraction(6, 5)
    ```

    ```python
    >>> tup = duration.Tuplet(numberNotesActual=3, numberNotesNormal=4)
    >>> duration.convertTypeToQuarterLength('quarter', 0, [tup])
    Fraction(4, 3)
    ```

    Also can handle those rare medieval dot groups
    (such as dotted-dotted half notes that take a full measure of 9/8.
    Conceptually, these are dotted-(dotted-half) notes. See
    trecento.trecentoCadence for more information
    ).
    >>> duration.convertTypeToQuarterLength(‘half’, dots=1, dotGroups=[1, 1])
    4.5

    Unknown values raise DurationException:

    ```python
    >>> duration.convertTypeToQuarterLength('minim')
    Traceback (most recent call last):
    music21.duration.DurationException: no such type (minim) available for conversion
    ```

music21.duration.dottedMatch(*qLen: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *maxDots=4*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False], [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]][[source]](../_modules/music21/duration.html#dottedMatch)
:   Given a quarterLength, determine if there is a dotted
    (or non-dotted) type that exactly matches. Returns a pair of
    (numDots, type) or (False, False) if no exact matches are found.

    Returns a maximum of four dots by default.

    ```python
    >>> duration.dottedMatch(3.0)
    (1, 'half')
    >>> duration.dottedMatch(1.75)
    (2, 'quarter')
    ```

    This value is not equal to any dotted note length

    ```python
    >>> duration.dottedMatch(1.6)
    (False, False)
    ```

    maxDots can be lowered for certain searches

    ```python
    >>> duration.dottedMatch(1.875)
    (3, 'quarter')
    >>> duration.dottedMatch(1.875, 2)
    (False, False)
    ```

    ```python
    >>> duration.dottedMatch(0.00001, 2)
    (False, False)
    ```

music21.duration.durationTupleFromQuarterLength(*ql=1.0*) → [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple")[[source]](../_modules/music21/duration.html#durationTupleFromQuarterLength)
:   Returns a DurationTuple for a given quarter length
    if the ql can be expressed as a type and number of dots
    (no tuplets, no complex duration, etc.). If it can’t be expressed,
    returns an “inexpressible” DurationTuple.

    ```python
    >>> dt = duration.durationTupleFromQuarterLength(3.0)
    >>> dt
    DurationTuple(type='half', dots=1, quarterLength=3.0)
    ```

    If it’s not possible, we return an “inexpressible” type:

    ```python
    >>> dt = duration.durationTupleFromQuarterLength(2.5)
    >>> dt
    DurationTuple(type='inexpressible', dots=0, quarterLength=2.5)
    ```

music21.duration.durationTupleFromTypeDots(*durType='quarter'*, *dots=0*)[[source]](../_modules/music21/duration.html#durationTupleFromTypeDots)
:   Returns a DurationTuple (which knows its quarterLength) for
    a given type and dots (no tuplets)

    ```python
    >>> dt = duration.durationTupleFromTypeDots('quarter', 0)
    >>> dt
    DurationTuple(type='quarter', dots=0, quarterLength=1.0)
    >>> dt2 = duration.durationTupleFromTypeDots('quarter', 0)
    >>> dt is dt2
    True
    ```

    Also with keyword arguments.

    ```python
    >>> dt = duration.durationTupleFromTypeDots(durType='zero', dots=0)
    >>> dt
    DurationTuple(type='zero', dots=0, quarterLength=0.0)
    ```

    Unknown values raise DurationException:

    ```python
    >>> dt = duration.durationTupleFromTypeDots(durType='minim', dots=0)
    Traceback (most recent call last):
    music21.duration.DurationException: Unknown type: minim
    ```

music21.duration.nextLargerType(*durType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/duration.html#nextLargerType)
:   Given a type (such as 16th or quarter), return the next larger type.

    ```python
    >>> duration.nextLargerType('16th')
    'eighth'
    ```

    ```python
    >>> duration.nextLargerType('whole')
    'breve'
    ```

    ```python
    >>> duration.nextLargerType('duplex-maxima')
    Traceback (most recent call last):
    music21.duration.DurationException: cannot get the next larger of duplex-maxima
    ```

music21.duration.nextSmallerType(*durType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/duration.html#nextSmallerType)
:   Given a type (such as 16th or quarter), return the next smaller type.

    ```python
    >>> duration.nextSmallerType('16th')
    '32nd'
    >>> duration.nextSmallerType('whole')
    'half'
    >>> duration.nextSmallerType('1024th')
    '2048th'
    >>> duration.nextSmallerType('2048th')
    Traceback (most recent call last):
    music21.duration.DurationException: cannot get the next smaller of 2048th
    ```

music21.duration.quarterLengthToClosestType(*qLen: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][[source]](../_modules/music21/duration.html#quarterLengthToClosestType)
:   Returns a two-unit tuple consisting of

    1. The type string (“quarter”) that is smaller than or equal to the
    quarterLength of provided.

    2. Boolean, True or False, whether the conversion was exact.

    ```python
    >>> duration.quarterLengthToClosestType(0.5)
    ('eighth', True)
    >>> duration.quarterLengthToClosestType(0.75)
    ('eighth', False)
    >>> duration.quarterLengthToClosestType(1.8)
    ('quarter', False)
    ```

    Some extremely close types will return True for exact conversion:

    ```python
    >>> duration.quarterLengthToClosestType(2.0000000000000001)
    ('half', True)
    ```

    Very long durations are fine:

    ```python
    >>> duration.quarterLengthToClosestType(129.99)
    ('duplex-maxima', False)
    ```

    Durations smaller than 2048th note raise a DurationException

    ```python
    >>> qL = duration.typeToDuration['2048th']
    >>> qL
    0.001953125
    ```

    ```python
    >>> qL = qL * 0.75
    >>> duration.quarterLengthToClosestType(qL)
    Traceback (most recent call last):
    music21.duration.DurationException: Cannot return types smaller than 2048th;
        qLen was: 0.00146484375
    ```

music21.duration.quarterLengthToNonPowerOf2Tuplet(*qLen: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Tuplet](#music21.duration.Tuplet "music21.duration.Tuplet"), [DurationTuple](#music21.duration.DurationTuple "music21.duration.DurationTuple")][[source]](../_modules/music21/duration.html#quarterLengthToNonPowerOf2Tuplet)
:   Slow, last chance function that returns a tuple of a single tuplet, probably with a non
    power of 2 denominator (such as 7:6) that represents the quarterLength and the
    DurationTuple that should be used to express the note.

    This could be a double-dotted note, but also a tuplet:

    ```python
    >>> duration.quarterLengthToNonPowerOf2Tuplet(7)
    (<music21.duration.Tuplet 8/7/quarter>, DurationTuple(type='breve', dots=0, quarterLength=8.0))
    ```

    ```python
    >>> duration.quarterLengthToNonPowerOf2Tuplet(7/16)
    (<music21.duration.Tuplet 8/7/64th>, DurationTuple(type='eighth', dots=0, quarterLength=0.5))
    ```

    ```python
    >>> duration.quarterLengthToNonPowerOf2Tuplet(7/3)
    (<music21.duration.Tuplet 12/7/16th>, DurationTuple(type='whole', dots=0, quarterLength=4.0))
    ```

    And of course:

    ```python
    >>> duration.quarterLengthToNonPowerOf2Tuplet(1)
    (<music21.duration.Tuplet 1/1/quarter>,
     DurationTuple(type='quarter', dots=0, quarterLength=1.0))
    ```

music21.duration.quarterLengthToTuplet(*qLen: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *maxToReturn: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 4*, *tupletNumerators=(3, 5, 7, 11, 13)*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Tuplet](#music21.duration.Tuplet "music21.duration.Tuplet")][[source]](../_modules/music21/duration.html#quarterLengthToTuplet)
:   Returns a list of possible Tuplet objects for a
    given qLen (quarterLength). As there may be more than one
    possible solution, the maxToReturn integer specifies the
    maximum number of values returned.

    Searches for numerators specified in duration.defaultTupletNumerators
    (3, 5, 7, 11, 13). Does not return dotted tuplets, nor nested tuplets.

    Note that 4:3 tuplets won’t be found, but will be found as dotted notes
    by dottedMatch.

    ```python
    >>> duration.quarterLengthToTuplet(0.33333333)
    [<music21.duration.Tuplet 3/2/eighth>, <music21.duration.Tuplet 3/1/quarter>]
    ```

    ```python
    >>> duration.quarterLengthToTuplet(0.20)
    [<music21.duration.Tuplet 5/4/16th>,
     <music21.duration.Tuplet 5/2/eighth>,
     <music21.duration.Tuplet 5/1/quarter>]
    ```

    By specifying only 1 maxToReturn, a single-length list containing the
    Tuplet with the smallest type will be returned.

    ```python
    >>> duration.quarterLengthToTuplet(0.3333333, 1)
    [<music21.duration.Tuplet 3/2/eighth>]
    ```

    ```python
    >>> tup = duration.quarterLengthToTuplet(0.3333333, 1)[0]
    >>> tup.tupletMultiplier()
    Fraction(2, 3)
    ```
