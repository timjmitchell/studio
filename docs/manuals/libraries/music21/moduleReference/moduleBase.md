Source: https://music21.org/music21docs/moduleReference/moduleBase.html

# music21.base

music21.base is what you get in music21 if you type `import music21`. It
contains all the most low-level objects that also appear in the music21 module
(i.e., music21.base.Music21Object is the same as music21.Music21Object).

Music21 base classes for `Stream` objects and all
elements contained within them including Notes, etc. Additional objects for
defining and manipulating elements are included.

The namespace of this file, as all base.py files, is loaded into the package
that contains this file via \_\_init\_\_.py. Everything in this file is thus
available after importing music21.

```python
>>> import music21
>>> music21.Music21Object
<class 'music21.base.Music21Object'>
```

```python
>>> music21.VERSION_STR
'10.1.0'
```

Alternatively, after doing a complete import, these classes are available
under the module “base”:

```python
>>> base.Music21Object
<class 'music21.base.Music21Object'>
```

## Music21Object

class music21.base.Music21Object(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *groups: [Groups](#music21.base.Groups "music21.base.Groups") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sites: [Sites](moduleSites.html#music21.sites.Sites "music21.sites.Sites") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *duration: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *activeSite: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *style: [Style](moduleStyle.html#music21.style.Style "music21.style.Style") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *editorial: [Editorial](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *offset: OffsetQL = 0.0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/base.html#Music21Object)
:   Music21Object is the base class for all elements that can go into Streams.
    Notes, Clefs, TimeSignatures are all sublcasses of Music21Object. Durations
    and Pitches (which need to be attached to Notes, etc.) are not.

    All music21 objects have these pieces of information:

    1. id: identification string unique to the object’s container (optional).
       Defaults to the id() of the element.
    2. groups: a [`Groups`](#music21.base.Groups "music21.base.Groups") object: which is a
       list of strings identifying internal sub-collections
       (voices, parts, selections) to which this element belongs
    3. duration: [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object representing the length of the object
    4. activeSite: a reference to the currently active `Stream` or None
    5. offset: a floating point or Fraction value, generally in quarter lengths,
       specifying the position of the object in a site.
    6. priority: int representing the position of an object among all
       objects at the same offset.
    7. sites: a `Sites` object that stores all
       the Streams and Contexts that an
       object is in.
    8. derivation: a [`Derivation`](moduleDerivation.html#music21.derivation.Derivation "music21.derivation.Derivation") object, or None, that shows
       where the object came from.
    9. style: a [`Style`](moduleStyle.html#music21.style.Style "music21.style.Style") object, that contains Style information
       automatically created if it doesn’t exist, so check .hasStyleInformation first
       if that is not desired.
    10. editorial: a [`Editorial`](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") object

    Each of these may be passed in as a named keyword to any music21 object.

    Some of these may be intercepted by the subclassing object (e.g., duration
    within Note)

    **Equality**

    For historical reasons, music21 uses a different idea of object equality
    for Music21Objects than recommended by modern Python standards.

    Two Music21Objects are equal if they are the same class and same duration.

    Their offset, activeSite, id, and groups do not matter for equality.

    Since these two objects are therefore not interchangable, they do not have
    the same hash value.

    ```python
    >>> obj1 = base.Music21Object(id='obj1')
    >>> obj2 = base.Music21Object(id='obj2')
    >>> obj1 == obj2
    True
    >>> hash(obj1) == hash(obj2)
    False
    ```

    This has the stange side effect that structures that use equality to
    report containment (such as lists and tuples) will report differently from
    structures that use hash values to report containment (such as dicts and sets):

    ```python
    >>> obj1 in [obj2]
    True
    >>> obj1 in {obj2}
    False
    ```

    Subclasses need to apply stricter criteria for equality, like Barline does here
    with .location

    ```python
    >>> bar1 = bar.Barline('double', 'left')
    >>> bar2 = bar.Barline('double', 'right')
    >>> bar1 == bar2
    False
    >>> bar2.location = 'left'
    >>> bar1 == bar2
    True
    >>> bar1.duration.type = 'whole'  # Buh?
    >>> bar1 == bar2
    False
    ```

    In general, a subclass of Music21Object must match all super-class criteria for
    equality before they can be considered equal themselves. However, there are some
    exceptions. For instance, RomanNumeral objects with the same figure and key are
    equal even if their notes are in different octaves or have different doublings.

    Developers creating their own Music21Object subclasses should add a class attribute
    equalityAttributes = (‘one’, ‘two’). (Remember that as a tuple of strings, if there
    is only one string, don’t forget the trailing comma: (‘only’,).

    ```python
    >>> class CarolineShawBreathMark(base.Music21Object):
    ...     equalityAttributes = ('direction',)
    ...     def __init__(self, direction, speed):
    ...         super().__init__(self)
    ...         self.direction = direction
    ...         self.speed = speed
    >>> bm1 = CarolineShawBreathMark('in', 'fast')
    >>> bm2 = CarolineShawBreathMark('out', 'fast')
    >>> bm1 == bm2
    False
    ```

    “speed” is not in the equalityAttributes so it can differ while objects are still
    equal.

    ```python
    >>> bm3 = CarolineShawBreathMark('in', 'slow')
    >>> bm1 == bm3
    True
    ```

[`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object") read-only properties

Music21Object.beat
:   Return the beat of this object as found in the most
    recently positioned Measure. Beat values count from 1 and
    contain a floating-point designation between 0 and 1 to
    show proportional progress through the beat.

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 0.5
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.repeatAppend(n, 6)
    >>> [n.beat for n in m.notes]
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
    ```

    Fractions are returned for positions that cannot be represented perfectly using floats:

    ```python
    >>> m.timeSignature = meter.TimeSignature('6/8')
    >>> [n.beat for n in m.notes]
    [1.0, Fraction(4, 3), Fraction(5, 3), 2.0, Fraction(7, 3), Fraction(8, 3)]
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, meter.TimeSignature('3/4'))
    >>> s.repeatAppend(note.Note(), 8)
    >>> [n.beat for n in s.notes]
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0]
    ```

    Notes inside flat streams can still find the original beat placement from outer
    streams:

    ```python
    >>> p = stream.Part()
    >>> ts = meter.TimeSignature('2/4')
    >>> p.insert(0, ts)
    ```

    ```python
    >>> n = note.Note('C4', type='eighth')
    >>> m1 = stream.Measure(number=1)
    >>> m1.repeatAppend(n, 4)
    ```

    ```python
    >>> m2 = stream.Measure(number=2)
    >>> m2.repeatAppend(n, 4)
    ```

    ```python
    >>> p.append([m1, m2])
    >>> [n.beat for n in p.flatten().notes]
    [1.0, 1.5, 2.0, 2.5, 1.0, 1.5, 2.0, 2.5]
    ```

    Fractions print out as improper fraction strings

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('4/4')
    >>> n = note.Note()
    >>> n.quarterLength = 1/3
    >>> m.repeatAppend(n, 12)
    >>> for n in m.notes[:5]:
    ...    print(n.beat)
    1.0
    4/3
    5/3
    2.0
    7/3
    ```

    If there is no TimeSignature object in sites then returns the special float
    nan meaning “Not a Number”:

    ```python
    >>> isolatedNote = note.Note('E4')
    >>> isolatedNote.beat
    nan
    ```

    Not-a-number objects do not compare equal to themselves:

    ```python
    >>> isolatedNote.beat == isolatedNote.beat
    False
    ```

    Instead, to test for nan, import the math module and use isnan():

    ```python
    >>> import math
    >>> math.isnan(isolatedNote.beat)
    True
    ```

    * Changed in v6.3: returns nan if
      there is no TimeSignature in sites.
      Previously raised an exception.

Music21Object.beatDuration
:   Return a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") of the beat
    active for this object as found in the most recently
    positioned Measure.

    If extending beyond the Measure, or in a Stream with a TimeSignature,
    the meter modulus value will be returned.

    ```python
    >>> n = note.Note('C4', type='eighth')
    >>> n.duration
    <music21.duration.Duration 0.5>
    ```

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.repeatAppend(n, 6)
    >>> n0 = m.notes.first()
    >>> n0.beatDuration
    <music21.duration.Duration 1.0>
    ```

    Notice that the beat duration is the same for all these notes
    and has nothing to do with the duration of the element itself

    ```python
    >>> [n.beatDuration.quarterLength for n in m.notes]
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    ```

    Changing the time signature changes the beat duration:

    ```python
    >>> m.timeSignature = meter.TimeSignature('6/8')
    >>> [n.beatDuration.quarterLength for n in m.notes]
    [1.5, 1.5, 1.5, 1.5, 1.5, 1.5]
    ```

    Complex time signatures will give different note lengths:

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, meter.TimeSignature('2/4+3/4'))
    >>> s.repeatAppend(note.Note(type='quarter'), 8)
    >>> [n.beatDuration.quarterLength for n in s.notes]
    [2.0, 2.0, 3.0, 3.0, 3.0, 2.0, 2.0, 3.0]
    ```

    If there is no TimeSignature object in sites then returns a duration object
    of Zero length.

    ```python
    >>> isolatedNote = note.Note('E4')
    >>> isolatedNote.beatDuration
    <music21.duration.Duration 0.0>
    ```

    * Changed in v6.3: returns a duration.Duration object of length 0 if
      there is no TimeSignature in sites. Previously raised an exception.

Music21Object.beatStr
:   Return a string representation of the beat of
    this object as found in the most recently positioned
    Measure. Beat values count from 1 and contain a
    fractional designation to show progress through the beat.

    ```python
    >>> n = note.Note(type='eighth')
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.repeatAppend(n, 6)
    ```

    ```python
    >>> [n.beatStr for n in m.notes]
    ['1', '1 1/2', '2', '2 1/2', '3', '3 1/2']
    ```

    ```python
    >>> m.timeSignature = meter.TimeSignature('6/8')
    >>> [n.beatStr for n in m.notes]
    ['1', '1 1/3', '1 2/3', '2', '2 1/3', '2 2/3']
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, meter.TimeSignature('3/4'))
    >>> s.repeatAppend(note.Note(type='quarter'), 8)
    >>> [n.beatStr for n in s.notes]
    ['1', '2', '3', '1', '2', '3', '1', '2']
    ```

    If there is no TimeSignature object in sites then returns ‘nan’ for not a number.

    ```python
    >>> isolatedNote = note.Note('E4')
    >>> isolatedNote.beatStr
    'nan'
    ```

    * Changed in v6.3: returns ‘nan’ if
      there is no TimeSignature in sites.
      Previously raised an exception.

Music21Object.beatStrength
:   Return the metrical accent of this object
    in the most recently positioned Measure. Accent values
    are between zero and one, and are derived from the local
    TimeSignature’s accent MeterSequence weights. If the offset
    of this object does not match a defined accent weight, a
    minimum accent weight will be returned.

    ```python
    >>> n = note.Note(type='eighth')
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.repeatAppend(n, 6)
    ```

    The first note of a measure is (generally?) always beat strength 1.0:

    ```python
    >>> m.notes.first().beatStrength
    1.0
    ```

    Notes on weaker beats have lower strength:

    ```python
    >>> [n.beatStrength for n in m.notes]
    [1.0, 0.25, 0.5, 0.25, 0.5, 0.25]
    ```

    ```python
    >>> m.timeSignature = meter.TimeSignature('6/8')
    >>> [n.beatStrength for n in m.notes]
    [1.0, 0.25, 0.25, 0.5, 0.25, 0.25]
    ```

    Importantly, the actual numbers here have no particular meaning. You cannot
    “add” two beatStrengths of 0.25 and say that they have the same beat strength
    as one note of 0.5. Only the ordinal relations really matter. Even taking
    an average of beat strengths is a tiny bit methodologically suspect (though
    it is common in research for lack of a better method).

    We can also get the beatStrength for elements not in
    a measure, if the enclosing stream has a `TimeSignature`.
    We just assume that the time signature carries through to
    hypothetical following measures:

    ```python
    >>> n = note.Note('E-3', type='quarter')
    >>> s = stream.Stream()
    >>> s.insert(0.0, meter.TimeSignature('2/2'))
    >>> s.repeatAppend(n, 12)
    >>> [n.beatStrength for n in s.notes]
    [1.0, 0.25, 0.5, 0.25, 1.0, 0.25, 0.5, 0.25, 1.0, 0.25, 0.5, 0.25]
    ```

    Changing the meter changes the output, of course, as can be seen from the
    fourth quarter note onward:

    ```python
    >>> s.insert(4.0, meter.TimeSignature('3/4'))
    >>> [n.beatStrength for n in s.notes]
    [1.0, 0.25, 0.5, 0.25, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 0.5]
    ```

    The method returns correct numbers for the prevailing time signature
    even if no measures have been made:

    ```python
    >>> n = note.Note('E--3', type='half')
    >>> s = stream.Stream()
    >>> s.isMeasure
    False
    ```

    ```python
    >>> s.insert(0, meter.TimeSignature('2/2'))
    >>> s.repeatAppend(n, 16)
    >>> s.notes[0].beatStrength
    1.0
    >>> s.notes[1].beatStrength
    0.5
    >>> s.notes[4].beatStrength
    1.0
    >>> s.notes[5].beatStrength
    0.5
    ```

    Getting the beatStrength of an object without a time signature in its context
    returns the not-a-number special object ‘nan’:

    ```python
    >>> n2 = note.Note(type='whole')
    >>> n2.beatStrength
    nan
    >>> from math import isnan
    >>> isnan(n2.beatStrength)
    True
    ```

    * Changed in v6.3: return ‘nan’ instead of raising an exception.

Music21Object.hasEditorialInformation
:   Returns True if there is a [`Editorial`](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") object
    already associated with this object, False otherwise.

    Calling .editorial on an object will always create a new
    Editorial object, so even though a new Editorial object isn’t too expensive
    to create, this property helps to prevent creating new Editorial objects
    more than is necessary.

    ```python
    >>> mObj = base.Music21Object()
    >>> mObj.hasEditorialInformation
    False
    >>> mObj.editorial
    <music21.editorial.Editorial {}>
    >>> mObj.hasEditorialInformation
    True
    ```

Music21Object.hasStyleInformation
:   Returns True if there is a [`Style`](moduleStyle.html#music21.style.Style "music21.style.Style") object
    already associated with this object, False otherwise.

    Calling .style on an object will always create a new
    Style object, so even though a new Style object isn’t too expensive
    to create, this property helps to prevent creating new Styles more than
    necessary.

    ```python
    >>> mObj = base.Music21Object()
    >>> mObj.hasStyleInformation
    False
    >>> mObj.style
    <music21.style.Style object at 0x10b0a2080>
    >>> mObj.hasStyleInformation
    True
    ```

Music21Object.measureNumber
:   Return the measure number of a `Measure` that contains this
    object if the object is in a measure.

    Returns None if the object is not in a measure. Also note that by
    default Measure objects
    have measure number 0.

    If an object belongs to multiple measures (not in the same hierarchy)
    then it returns the
    measure number of the [`activeSite()`](#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") if that is a
    `Measure` object. Otherwise, it will use
    [`getContextByClass()`](#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass")
    to find the number of the measure it was most recently added to.

    ```python
    >>> m = stream.Measure()
    >>> m.number = 12
    >>> n = note.Note()
    >>> m.append(n)
    >>> n.measureNumber
    12
    ```

    ```python
    >>> n2 = note.Note()
    >>> n2.measureNumber is None
    True
    >>> m2 = stream.Measure()
    >>> m2.append(n2)
    >>> n2.measureNumber
    0
    ```

    The property updates if the object’s surrounding measure’s number changes:

    ```python
    >>> m2.number = 11
    >>> n2.measureNumber
    11
    ```

    The most recent measure added to is used unless activeSite is a measure:

    ```python
    >>> m.append(n2)
    >>> n2.measureNumber
    12
    >>> n2.activeSite = m2
    >>> n2.measureNumber
    11
    ```

    Copies can retain measure numbers until set themselves:

    ```python
    >>> import copy
    >>> nCopy = copy.deepcopy(n2)
    >>> nCopy.measureNumber
    12
    >>> m3 = stream.Measure()
    >>> m3.number = 4
    >>> m3.append(nCopy)
    >>> nCopy.measureNumber
    4
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object") read/write properties

Music21Object.activeSite
:   A reference to the most-recent object used to
    contain this object. In most cases, this will be a
    Stream or Stream sub-class. In most cases, an object’s
    activeSite attribute is automatically set when the
    object is attached to a Stream.

    ```python
    >>> n = note.Note('C#4')
    >>> p = stream.Part()
    >>> p.insert(20.0, n)
    >>> n.activeSite is p
    True
    >>> n.offset
    20.0
    ```

    ```python
    >>> m = stream.Measure()
    >>> m.insert(10.0, n)
    >>> n.activeSite is m
    True
    >>> n.offset
    10.0
    >>> n.activeSite = p
    >>> n.offset
    20.0
    ```

Music21Object.derivation
:   Return the [`Derivation`](moduleDerivation.html#music21.derivation.Derivation "music21.derivation.Derivation") object for this element.

    Or create one if none exists:

    ```python
    >>> n = note.Note()
    >>> n.derivation
    <Derivation of <music21.note.Note C> from None>
    ```

    Make a copy of n but change the pitch to D to see which is which later:

    ```python
    >>> import copy
    >>> n2 = copy.deepcopy(n)
    >>> n2.pitch.step = 'D'
    ```

    Because n2 was originally a copy of n, it has a derivation set to show it.

    ```python
    >>> n2.derivation
    <Derivation of <music21.note.Note D> from <music21.note.Note C> via '__deepcopy__'>
    >>> n2.derivation.origin is n
    True
    ```

    Note that (for now at least) derivation.origin is NOT a weakref:

    ```python
    >>> del n
    >>> n2.derivation
    <Derivation of <music21.note.Note D> from <music21.note.Note C> via '__deepcopy__'>
    >>> n2.derivation.origin
    <music21.note.Note C>
    ```

Music21Object.duration
:   Get and set the duration of this object as a Duration object.

Music21Object.editorial
:   a [`Editorial`](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") object that stores editorial information
    (comments, footnotes, harmonic information, ficta).

    Created automatically as needed:

    ```python
    >>> n = note.Note('C4')
    >>> n.editorial
    <music21.editorial.Editorial {}>
    >>> n.editorial.ficta = pitch.Accidental('sharp')
    >>> n.editorial.ficta
    <music21.pitch.Accidental sharp>
    >>> n.editorial
    <music21.editorial.Editorial {'ficta': <music21.pitch.Accidental sharp>}>
    ```

Music21Object.id
:   A unique identification string or int; not to be confused with Python’s
    built-in id() method. However, if not set, will return
    Python’s id() number.

    “Unique” is intended with respect to the stream hierarchy one is likely
    to query with `getElementById()`. For
    instance, the .id of a Voice should be unique in any single Measure,
    but the id’s may reset from measure to measure across a Part.

Music21Object.offset
:   The offset property sets or returns the position of this object
    as a float or fractions.Fraction value
    (generally in quarterLengths), depending on what is representable.

    Offsets are measured from the start of the object’s activeSite,
    that is, the most recently referenced Stream or Stream subclass such
    as Part, Measure, or Voice. It is a simpler
    way of calling o.getOffsetBySite(o.activeSite, returnType=’rational’).

    If we put a Note into a Stream, we will see the activeSite changes.

    ```python
    >>> import fractions
    >>> n1 = note.Note('D#3')
    >>> n1.activeSite is None
    True
    ```

    ```python
    >>> m1 = stream.Measure()
    >>> m1.number = 4
    >>> m1.insert(10.0, n1)
    >>> n1.offset
    10.0
    >>> n1.activeSite
    <music21.stream.Measure 4 offset=0.0>
    ```

    ```python
    >>> n1.activeSite is m1
    True
    ```

    The most recently referenced Stream becomes an object’s activeSite and
    thus the place where .offset looks to find its number.

    ```python
    >>> m2 = stream.Measure()
    >>> m2.insert(3/5, n1)
    >>> m2.number = 5
    >>> n1.offset
    Fraction(3, 5)
    >>> n1.activeSite is m2
    True
    ```

    Notice though that .offset depends on the .activeSite which is the most
    recently accessed/referenced Stream.

    Here we will iterate over the elements in m1 and we
    will see that the .offset of n1 now is its offset in
    m1 even though we haven’t done anything directly to n1.
    Simply iterating over a site is enough to change the .activeSite
    of its elements:

    ```python
    >>> for element in m1:
    ...     pass
    >>> n1.offset
    10.0
    ```

    The property can also set the offset for the object if no
    container has been set:

    ```python
    >>> n1 = note.Note()
    >>> n1.id = 'hi'
    >>> n1.offset = 20/3
    >>> n1.offset
    Fraction(20, 3)
    >>> float(n1.offset)
    6.666...
    ```

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(n1)
    >>> n1.offset
    0.0
    >>> s2 = stream.Stream()
    >>> s2.insert(30.5, n1)
    >>> n1.offset
    30.5
    ```

    After calling getElementById on s1, the
    returned element’s offset will be its offset in s1.

    ```python
    >>> n2 = s1.getElementById('hi')
    >>> n2 is n1
    True
    >>> n2.offset
    0.0
    ```

    Iterating over the elements in a Stream will
    make its offset be the offset in iterated
    Stream.

    ```python
    >>> for thisElement in s2:
    ...     thisElement.offset
    30.5
    ```

    When in doubt, use .getOffsetBySite(streamObj)
    which is safer or streamObj.elementOffset(self) which is 3x faster.

    * Changed in v8: using a Duration object as an offset is not allowed.

Music21Object.priority
:   Get and set the priority integer value.

    Priority specifies the order of processing from left (lowest number)
    to right (highest number) of objects at the same offset. For
    instance, if you want a key change and a clef change to happen at
    the same time but the key change to appear first, then set:
    keySigElement.priority = 1; clefElement.priority = 2 this might be
    a slightly counterintuitive numbering of priority, but it does
    mean, for instance, if you had two elements at the same offset,
    an allegro tempo change and an andante tempo change, then the
    tempo change with the higher priority number would apply to the
    following notes (by being processed second).

    Default priority is 0; thus negative priorities are encouraged
    to have Elements that appear before non-priority set elements.

    In case of tie, there are defined class sort orders defined in
    music21.base.classSortOrder. For instance, a key signature
    change appears before a time signature change before a
    note at the same offset. This produces the familiar order of
    materials at the start of a musical score.

    ```python
    >>> import music21
    >>> a = music21.Music21Object()
    >>> a.priority = 3
    >>> a.priority = 'high'
    Traceback (most recent call last):
    music21.base.ElementException: priority values must be integers.
    ```

Music21Object.quarterLength
:   Set or Return the Duration as represented in Quarter Length, possibly as a fraction.

    Same as setting .duration.quarterLength.

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 2.0
    >>> n.quarterLength
    2.0
    >>> n.quarterLength = 1/3
    >>> n.quarterLength
    Fraction(1, 3)
    ```

Music21Object.seconds
:   Get or set the duration of this object in seconds, assuming
    that this object has a [`MetronomeMark`](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark")
    or [`MetricModulation`](moduleTempo.html#music21.tempo.MetricModulation "music21.tempo.MetricModulation")
    (or any [`TempoIndication`](moduleTempo.html#music21.tempo.TempoIndication "music21.tempo.TempoIndication")) in its past context.

    ```python
    >>> s = stream.Stream()
    >>> for i in range(3):
    ...    s.append(note.Note(type='quarter'))
    ...    s.append(note.Note(type='quarter', dots=1))
    >>> s.insert(0, tempo.MetronomeMark(number=60))
    >>> s.insert(2, tempo.MetronomeMark(number=120))
    >>> s.insert(4, tempo.MetronomeMark(number=30))
    >>> [n.seconds for n in s.notes]
    [1.0, 1.5, 0.5, 0.75, 2.0, 3.0]
    ```

    Setting the number of seconds on a music21 object changes its duration:

    ```python
    >>> lastNote = s.notes[-1]
    >>> lastNote.duration.fullName
    'Dotted Quarter'
    >>> lastNote.seconds = 4.0
    >>> lastNote.duration.fullName
    'Half'
    ```

    Any object of length 0 has zero-second length:

    ```python
    >>> tc = clef.TrebleClef()
    >>> tc.seconds
    0.0
    ```

    If an object has positive duration but no tempo indication in its context,
    then the special number ‘nan’ for “not-a-number” is returned:

    ```python
    >>> r = note.Rest(type='whole')
    >>> r.seconds
    nan
    ```

    Check for ‘nan’ with the math.isnan() routine:

    ```python
    >>> import math
    >>> math.isnan(r.seconds)
    True
    ```

    Setting seconds for an element without a tempo-indication in its sites raises
    a Music21ObjectException:

    ```python
    >>> r.seconds = 2.0
    Traceback (most recent call last):
    music21.base.Music21ObjectException: this object does not have a TempoIndication in Sites
    ```

    Note that if an object is in multiple Sites with multiple Metronome marks,
    the activeSite (or the hierarchy of the activeSite)
    determines its seconds for getting or setting:

    ```python
    >>> r = note.Rest(type='whole')
    >>> m1 = stream.Measure()
    >>> m1.insert(0, tempo.MetronomeMark(number=60))
    >>> m1.append(r)
    >>> r.seconds
    4.0
    ```

    ```python
    >>> m2 = stream.Measure()
    >>> m2.insert(0, tempo.MetronomeMark(number=120))
    >>> m2.append(r)
    >>> r.seconds
    2.0
    >>> r.activeSite = m1
    >>> r.seconds
    4.0
    >>> r.seconds = 1.0
    >>> r.duration.type
    'quarter'
    >>> r.activeSite = m2
    >>> r.seconds = 1.0
    >>> r.duration.type
    'half'
    ```

    * Changed in v6.3: return nan instead of raising an exception.

Music21Object.style
:   Returns (or Creates and then Returns) the Style object
    associated with this object, or sets a new
    style object. Different classes might use
    different Style objects because they might have different
    style needs (such as text formatting or bezier positioning)

    Eventually will also query the groups to see if they have
    any styles associated with them.

    ```python
    >>> n = note.Note()
    >>> st = n.style
    >>> st
    <music21.style.NoteStyle object at 0x10ba96208>
    >>> st.absoluteX = 20.0
    >>> st.absoluteX
    20.0
    >>> n.style = style.Style()
    >>> n.style.absoluteX is None
    True
    ```

[`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object") methods

Music21Object.\_\_eq\_\_(*other*) → [TypeGuard](https://docs.python.org/3/library/typing.html#typing.TypeGuard "(in Python v3.14)")[[Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")][[source]](../_modules/music21/base.html#Music21Object.__eq__)
:   Define equality for Music21Objects. See main class docs.

Music21Object.clearCache(*\*\*keywords*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.clearCache)
:   A number of music21 attributes (especially with Chords and RomanNumerals, etc.)
    are expensive to compute and are therefore cached. Generally speaking
    objects are responsible for making sure that their own caches are up to date,
    but a power user might want to do something in an unusual way (such as manipulating
    private attributes on a Pitch object) and need to be able to clear caches.

    That’s what this is here for. If all goes well, you’ll never need to call it
    unless you’re expanding music21’s core functionality.

    \*\*keywords is not used in Music21Object but is included for subclassing.

    Look at [`cacheMethod()`](moduleCommonDecorators.html#music21.common.decorators.cacheMethod "music21.common.decorators.cacheMethod") for the other half of this
    utility.

    * New in v6: exposes previously hidden functionality.

Music21Object.containerHierarchy(*\**, *followDerivation=True*, *includeNonStreamDerivations=False*)[[source]](../_modules/music21/base.html#Music21Object.containerHierarchy)
:   Return a list of Stream subclasses that this object
    is contained within or (if followDerivation is set) is derived from.

    This method gives access to the hierarchy that contained or
    created this object.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> noteE = s[1][2][3]
    >>> noteE
    <music21.note.Note E>
    >>> [e for e in noteE.containerHierarchy()]
    [<music21.stream.Measure 1 offset=1.0>,
     <music21.stream.Part Soprano>,
     <music21.stream.Score bach/bwv66.6.mxl>]
    ```

    Note that derived objects also can follow the container hierarchy:

    ```python
    >>> import copy
    >>> n2 = copy.deepcopy(noteE)
    >>> [e for e in n2.containerHierarchy()]
    [<music21.stream.Measure 1 offset=1.0>,
     <music21.stream.Part Soprano>,
     <music21.stream.Score bach/bwv66.6.mxl>]
    ```

    Unless followDerivation is False:

    ```python
    >>> [e for e in n2.containerHierarchy(followDerivation=False)]
    []
    ```

    if includeNonStreamDerivations is True then n2’s containerHierarchy will include
    n even though it’s not a container. It gives a good idea of how the hierarchy is being
    constructed.

    ```python
    >>> [e for e in n2.containerHierarchy(includeNonStreamDerivations=True)]
    [<music21.note.Note E>,
     <music21.stream.Measure 1 offset=1.0>,
     <music21.stream.Part Soprano>,
     <music21.stream.Score bach/bwv66.6.mxl>]
    ```

    The method follows activeSites, so set the activeSite as necessary.

    ```python
    >>> p = stream.Part(id='newPart')
    >>> m = stream.Measure(number=20)
    >>> p.insert(0, m)
    >>> m.insert(0, noteE)
    >>> noteE.activeSite
    <music21.stream.Measure 20 offset=0.0>
    >>> noteE.containerHierarchy()
    [<music21.stream.Measure 20 offset=0.0>,
     <music21.stream.Part newPart>]
    ```

    * Changed in v5.7: followDerivation and
      includeNonStreamDerivations are now keyword only

Music21Object.contextSites(*\**, *returnSortTuples: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *callerFirst=None*, *memo=None*, *offsetAppend: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") = 0.0*, *sortByCreationTime: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['reverse'] | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *priorityTarget=None*, *followDerivation=True*, *priorityTargetOnly=False*) → [Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.14)")[[ContextSortTuple](#music21.base.ContextSortTuple "music21.base.ContextSortTuple"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/base.html#Music21Object.contextSites)

Music21Object.contextSites(*\**, *callerFirst=None*, *memo=None*, *offsetAppend: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") = 0.0*, *sortByCreationTime: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['reverse'] | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *priorityTarget=None*, *returnSortTuples: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *followDerivation=True*, *priorityTargetOnly=False*) → [Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.14)")[[ContextTuple](#music21.base.ContextTuple "music21.base.ContextTuple"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]
:   A generator that returns a list of namedtuples of sites to search for a context.

    Each tuple contains three elements:

    .site – Stream object
    .offset – the offset or position (sortTuple) of this element in that Stream
    .recurseType – the way of searching that should be applied to search for a context.

    The recurseType values are all music21.stream.enums.RecurseType:

    > * FLATTEN – flatten the stream and then look from this offset backwards.
    > * ELEMENTS\_ONLY – only search the stream’s personal
    >   :   elements from this offset backwards
    > * ELEMENTS\_FIRST – search this stream backwards,
    >   :   and then flatten and search backwards

    ```python
    >>> c = corpus.parse('bwv66.6')
    >>> c.id = 'bach'
    >>> n = c[2][4][2]
    >>> n
    <music21.note.Note G#>
    ```

    Returning sortTuples are important for distinguishing the order of multiple sites
    at the same offset.

    ```python
    >>> for csTuple in n.contextSites(returnSortTuples=True):
    ...      yClearer = (csTuple.site, csTuple.offset.shortRepr(), csTuple.recurseType)
    ...      print(yClearer)
    (<music21.stream.Measure 3 offset=9.0>, '0.5 <0.20...>', <RecursionType.ELEMENTS_FIRST>)
    (<music21.stream.Part Alto>, '9.5 <0.20...>', <RecursionType.FLATTEN>)
    (<music21.stream.Score bach>, '9.5 <0.20...>', <RecursionType.ELEMENTS_ONLY>)
    ```

    Streams have themselves as the first element in their context sites, at position
    zero and classSortOrder negative infinity.

    This example shows the context sites for Measure 3 of the
    Alto part. We will get the measure object using direct access to
    indices to ensure that no other temporary
    streams are created; normally, we would do c.parts[‘#Alto’].measure(3).

    ```python
    >>> m = c.parts['#Alto'].getElementsByClass(stream.Measure)[3]
    >>> m
    <music21.stream.Measure 3 offset=9.0>
    ```

    If returnSortTuples is true then ContextSortTuples are returned, where the
    second element is a SortTuple:

    ```python
    >>> for csTuple in m.contextSites(returnSortTuples=True):
    ...     print(csTuple)
    ContextSortTuple(site=<music21.stream.Measure 3 offset=9.0>,
                     offset=SortTuple(atEnd=0, offset=0.0, priority=-inf, ...),
                     recurseType=<RecursionType.ELEMENTS_FIRST>)
    ContextSortTuple(...)
    ContextSortTuple(...)
    ```

    Because SortTuples are so detailed, we’ll use their shortRepr() to see the
    values, removing the insertIndex because it changes from run to run:

    ```python
    >>> for csTuple in m.contextSites(returnSortTuples=True):
    ...      yClearer = (csTuple.site, csTuple.offset.shortRepr(), csTuple.recurseType)
    ...      print(yClearer)
    (<music21.stream.Measure 3 offset=9.0>, '0.0 <-inf.-20...>', <RecursionType.ELEMENTS_FIRST>)
    (<music21.stream.Part Alto>, '9.0 <0.-20...>', <RecursionType.FLATTEN>)
    (<music21.stream.Score bach>, '9.0 <0.-20...>', <RecursionType.ELEMENTS_ONLY>)
    ```

    Here we make a copy of the earlier measure, and we see that its contextSites
    follow the derivationChain from the original measure and still find the Part
    and Score of the original Measure 3 (and also the original Measure 3)
    even though mCopy is not in any of these objects.

    ```python
    >>> import copy
    >>> mCopy = copy.deepcopy(m)
    >>> mCopy.number = 3333
    >>> for csTuple in mCopy.contextSites():
    ...      print(csTuple, mCopy in csTuple.site)
    ContextTuple(site=<music21.stream.Measure 3333 offset=0.0>,
                 offset=0.0,
                 recurseType=<RecursionType.ELEMENTS_FIRST>) False
    ContextTuple(site=<music21.stream.Measure 3 offset=9.0>,
                 offset=0.0,
                 recurseType=<RecursionType.ELEMENTS_FIRST>) False
    ContextTuple(site=<music21.stream.Part Alto>,
                 offset=9.0,
                 recurseType=<RecursionType.FLATTEN>) False
    ContextTuple(site=<music21.stream.Score bach>,
                 offset=9.0,
                 recurseType=<RecursionType.ELEMENTS_ONLY>) False
    ```

    If followDerivation were False, then the Part and Score would not be found.

    ```python
    >>> for csTuple in mCopy.contextSites(followDerivation=False):
    ...     print(csTuple)
    ContextTuple(site=<music21.stream.Measure 3333 offset=0.0>,
                 offset=0.0,
                 recurseType=<RecursionType.ELEMENTS_FIRST>)
    ```

    ```python
    >>> partIterator = c.parts
    >>> m3 = partIterator[1].measure(3)
    >>> for csTuple in m3.contextSites():
    ...      print(csTuple)
    ContextTuple(site=<music21.stream.Measure 3 offset=9.0>,
                 offset=0.0,
                 recurseType=<RecursionType.ELEMENTS_FIRST>)
    ContextTuple(site=<music21.stream.Part Alto>,
                 offset=9.0,
                 recurseType=<RecursionType.FLATTEN>)
    ContextTuple(site=<music21.stream.Score bach>,
                 offset=9.0,
                 recurseType=<RecursionType.ELEMENTS_ONLY>)
    ```

    Sorting order:

    ```python
    >>> p1 = stream.Part()
    >>> p1.id = 'p1'
    >>> m1 = stream.Measure()
    >>> m1.number = 1
    >>> n = note.Note()
    >>> m1.append(n)
    >>> p1.append(m1)
    >>> for csTuple in n.contextSites():
    ...     print(csTuple.site)
    <music21.stream.Measure 1 offset=0.0>
    <music21.stream.Part p1>
    ```

    ```python
    >>> p2 = stream.Part()
    >>> p2.id = 'p2'
    >>> m2 = stream.Measure()
    >>> m2.number = 2
    >>> m2.append(n)
    >>> p2.append(m2)
    ```

    The keys could have appeared in any order, but by default
    we set priorityTarget to activeSite. So this is the same as omitting.

    ```python
    >>> for y in n.contextSites(priorityTarget=n.activeSite):
    ...     print(y[0])
    <music21.stream.Measure 2 offset=0.0>
    <music21.stream.Part p2>
    <music21.stream.Measure 1 offset=0.0>
    <music21.stream.Part p1>
    ```

    We can sort sites by creationTime:

    ```python
    >>> for csTuple in n.contextSites(sortByCreationTime=True):
    ...     print(csTuple.site)
    <music21.stream.Measure 2 offset=0.0>
    <music21.stream.Part p2>
    <music21.stream.Measure 1 offset=0.0>
    <music21.stream.Part p1>
    ```

    Use reverse for oldest first:

    ```python
    >>> for csTuple in n.contextSites(sortByCreationTime='reverse'):
    ...     print(csTuple.site)
    <music21.stream.Measure 1 offset=0.0>
    <music21.stream.Part p1>
    <music21.stream.Measure 2 offset=0.0>
    <music21.stream.Part p2>
    ```

    Note that by default we search all sites, but you might want to only search
    one, for instance:

    ```python
    >>> c = note.Note('C')
    >>> m1 = stream.Measure()
    >>> m1.append(c)
    ```

    ```python
    >>> d = note.Note('D')
    >>> m2 = stream.Measure()
    >>> m2.append([c, d])
    ```

    ```python
    >>> c.activeSite = m1
    >>> c.next('Note')  # uses contextSites
    <music21.note.Note D>
    ```

    There is a particular site in which there is a Note after c,
    but we want to know if there is one in m1 or its hierarchy, so
    we can pass in activeSiteOnly to .next() which sets
    priorityTargetOnly=True for contextSites

    ```python
    >>> print(c.next('Note', activeSiteOnly=True))
    None
    ```

    * Removed in v3: priorityTarget cannot be set, in order
      to use .sites.yieldSites()
    * Changed in v5.5: all arguments are keyword only.
    * Changed in v6: added priorityTargetOnly=False to only search in the
      context of the priorityTarget.
    * Changed in v8: returnSortTuple=True returns a new ContextSortTuple

Music21Object.getAllContextsByClass(*className*)[[source]](../_modules/music21/base.html#Music21Object.getAllContextsByClass)
:   Returns a generator that yields elements found by .getContextByClass and
    then finds the previous contexts for that element.

    ```python
    >>> s = stream.Stream()
    >>> s.append(meter.TimeSignature('2/4'))
    >>> s.append(note.Note('C'))
    >>> s.append(meter.TimeSignature('3/4'))
    >>> n = note.Note('D')
    >>> s.append(n)
    ```

    ```python
    >>> for ts in n.getAllContextsByClass(meter.TimeSignature):
    ...     print(ts, ts.offset)
    <music21.meter.TimeSignature 3/4> 1.0
    <music21.meter.TimeSignature 2/4> 0.0
    ```

    TODO: make it so that it does not skip over multiple matching classes
    at the same offset. with sortTuple

Music21Object.getContextByClass(*className: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[\_M21T]*, *\**, *getElementMethod=ElementSearch.AT\_OR\_BEFORE*, *sortByCreationTime=False*, *followDerivation=True*, *priorityTargetOnly=False*) → \_M21T | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.getContextByClass)

Music21Object.getContextByClass(*className: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *\**, *getElementMethod=ElementSearch.AT\_OR\_BEFORE*, *sortByCreationTime=False*, *followDerivation=True*, *priorityTargetOnly=False*) → [Music21Object](#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   A very powerful method in music21 of fundamental importance: Returns
    the element matching the className that is closest to this element in
    its current hierarchy (or the hierarchy of the derivation origin unless
    followDerivation is False). For instance, take this stream of changing time
    signatures:

    ```python
    >>> p = converter.parse('tinynotation: 3/4 C4 D E 2/4 F G A B 1/4 c')
    >>> p
    <music21.stream.Part 0x104ce64e0>
    ```

    ```python
    >>> p.show('t')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note F>
        {1.0} <music21.note.Note G>
    {5.0} <music21.stream.Measure 3 offset=5.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
    {7.0} <music21.stream.Measure 4 offset=7.0>
        {0.0} <music21.meter.TimeSignature 1/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.bar.Barline type=final>
    ```

    Let’s get the last two notes of the piece, the B and high c:

    ```python
    >>> m4 = p.measure(4)
    >>> c = m4.notes.first()
    >>> c
    <music21.note.Note C>
    ```

    ```python
    >>> m3 = p.measure(3)
    >>> b = m3.notes.last()
    >>> b
    <music21.note.Note B>
    ```

    Now when we run getContextByClass(meter.TimeSignature) on c, we get a
    time signature of 1/4.

    ```python
    >>> c.getContextByClass(meter.TimeSignature)
    <music21.meter.TimeSignature 1/4>
    ```

    Doing what we just did wouldn’t be hard to do with other methods,
    though getContextByClass makes it easier. But the time signature
    context for b would be much harder to get without this method, since in
    order to do it, it searches backwards within the measure, finds that
    there’s nothing there. It goes to the previous measure and searches
    inside that one from the end backwards until it gets the proper
    TimeSignature of 2/4:

    ```python
    >>> b.getContextByClass(meter.TimeSignature)
    <music21.meter.TimeSignature 2/4>
    ```

    For backwards compatibility you can also pass in a string of the
    class name:

    ```python
    >>> b.getContextByClass('TimeSignature')
    <music21.meter.TimeSignature 2/4>
    ```

    But if you use Python typing or a typing-aware IDE, then the first call
    (with class name) will signal that it is returning a TimeSignature object
    and allow for error detection, autocomplete, etc. The latter call
    (with string) will only know that some Music21Object was returned.

    The method is smart enough to stop when it gets to the beginning of the
    part. This is all you need to know for most uses. The rest of the
    docs are for advanced uses:

    The method searches Sites and also associated objects to find a
    matching class. Returns None if no match is found.

    A reference to the caller is required to find the offset of the object
    of the caller.

    The caller may be a Sites reference from a lower-level object. If so,
    we can access the location of that lower-level object. However, if we
    need a flat representation, the caller needs to be the source Stream,
    not its Sites reference.

    The getElementMethod is an enum value (new in v7) from
    [`ElementSearch`](moduleCommonEnums.html#music21.common.enums.ElementSearch "music21.common.enums.ElementSearch") that selects which
    Stream method is used to get elements for searching. (The historical form
    of supplying one of the following values as a string is also supported.)

    ```python
    >>> from music21.common.enums import ElementSearch
    >>> [x for x in ElementSearch]
    [<ElementSearch.BEFORE>,
     <ElementSearch.AFTER>,
     <ElementSearch.AT_OR_BEFORE>,
     <ElementSearch.AT_OR_AFTER>,
     <ElementSearch.BEFORE_OFFSET>,
     <ElementSearch.AFTER_OFFSET>,
     <ElementSearch.AT_OR_BEFORE_OFFSET>,
     <ElementSearch.AT_OR_AFTER_OFFSET>,
     <ElementSearch.BEFORE_NOT_SELF>,
     <ElementSearch.AFTER_NOT_SELF>,
     <ElementSearch.ALL>]
    ```

    The “after” do forward contexts – looking ahead.

    Demonstrations of these keywords:

    Because b is a Note, .getContextByClass(note.Note) will only find itself:

    ```python
    >>> b.getContextByClass(note.Note) is b
    True
    ```

    To get the previous Note, use getElementMethod=ElementSearch.BEFORE:

    ```python
    >>> a = b.getContextByClass(note.Note, getElementMethod=ElementSearch.BEFORE)
    >>> a
    <music21.note.Note A>
    ```

    This is similar to .previous(note.Note), though that method is a bit more
    sophisticated:

    ```python
    >>> b.previous(note.Note)
    <music21.note.Note A>
    ```

    To get the following Note use getElementMethod=ElementSearch.AFTER:

    ```python
    >>> c = b.getContextByClass(note.Note, getElementMethod=ElementSearch.AFTER)
    >>> c
    <music21.note.Note C>
    ```

    This is similar to .next(note.Note), though, again, that method is a bit more
    sophisticated:

    ```python
    >>> b.next(note.Note)
    <music21.note.Note C>
    ```

    A Stream might contain several elements at the same offset, leading to
    potentially surprising results where searching by ElementSearch.AT\_OR\_BEFORE
    does not find an element that is technically the NEXT node but still at 0.0:

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, clef.BassClef())
    >>> s.next()
    <music21.clef.BassClef>
    >>> s.getContextByClass(clef.Clef) is None
    True
    >>> s.getContextByClass(clef.Clef, getElementMethod=ElementSearch.AT_OR_AFTER)
    <music21.clef.BassClef>
    ```

    This can be remedied by explicitly searching by offsets:

    ```python
    >>> s.getContextByClass(clef.Clef, getElementMethod=ElementSearch.AT_OR_BEFORE_OFFSET)
    <music21.clef.BassClef>
    ```

    Or by not limiting the search by temporal position at all:

    ```python
    >>> s.getContextByClass(clef.Clef, getElementMethod=ElementSearch.ALL)
    <music21.clef.BassClef>
    ```

    Notice that if searching for a Stream context, the element is not
    guaranteed to be in that Stream. This is obviously true in this case:

    ```python
    >>> p2 = stream.Part()
    >>> m = stream.Measure(number=1)
    >>> p2.insert(0, m)
    >>> n = note.Note('D')
    >>> m.insert(2.0, n)
    >>> try:
    ...     n.getContextByClass(stream.Part).elementOffset(n)
    ... except Music21Exception:
    ...     print('not there')
    not there
    ```

    But it is less clear with something like this:

    ```python
    >>> import copy
    >>> n2 = copy.deepcopy(n)
    >>> try:
    ...     n2.getContextByClass(stream.Measure).elementOffset(n2)
    ... except Music21Exception:
    ...     print('not there')
    not there
    ```

    A measure context is being found, but only through the derivation chain.

    ```python
    >>> n2.getContextByClass(stream.Measure)
    <music21.stream.Measure 1 offset=0.0>
    ```

    To prevent this error, use the followDerivation=False setting

    ```python
    >>> print(n2.getContextByClass(stream.Measure, followDerivation=False))
    None
    ```

    Or if you want the offset of the element following the derivation chain,
    call getOffsetBySite() on the object:

    ```python
    >>> n2.getOffsetBySite(n2.getContextByClass(stream.Measure))
    2.0
    ```

    Raises ValueError if getElementMethod is not a value in ElementSearch.

    ```python
    >>> n2.getContextByClass(expressions.TextExpression, getElementMethod='invalid')
    Traceback (most recent call last):
    ValueError: Invalid getElementMethod: invalid
    ```

    Raises ValueError for incompatible values followDerivation=True
    and priorityTargetOnly=True.

    * Changed in v5.7: added followDerivation=False and made
      everything but the class keyword only
    * New in v6: added priorityTargetOnly – see contextSites for description.
    * New in v7: added getElementMethod all and ElementSearch enum.
    * Changed in v8: class-based calls return properly typed items. Putting
      multiple types into className (never documented) is no longer allowed.

Music21Object.getOffsetBySite(*site: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *\**, *returnSpecial: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.getOffsetBySite)

Music21Object.getOffsetBySite(*site: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *\**, *returnSpecial: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [OffsetSpecial](moduleCommonEnums.html#music21.common.enums.OffsetSpecial "music21.common.enums.OffsetSpecial")
:   If this class has been registered in a container such as a Stream,
    that container can be provided here, and the offset in that object
    can be returned.

    ```python
    >>> n = note.Note('A-4')  # a Music21Object
    >>> n.offset = 30
    >>> n.getOffsetBySite(None)
    30.0
    ```

    ```python
    >>> s1 = stream.Stream()
    >>> s1.id = 'containingStream'
    >>> s1.insert(20 / 3, n)
    >>> n.getOffsetBySite(s1)
    Fraction(20, 3)
    >>> float(n.getOffsetBySite(s1))
    6.6666...
    ```

    n.getOffsetBySite(None) should still return 30.0

    ```python
    >>> n.getOffsetBySite(None)
    30.0
    ```

    If the Stream does not contain the element and the element is not derived from
    an element that does, then a SitesException is raised:

    ```python
    >>> s2 = stream.Stream()
    >>> s2.id = 'notContainingStream'
    >>> n.getOffsetBySite(s2)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object <music21.note.Note A-> is not
          stored in stream <music21.stream.Stream notContainingStream>
    ```

    Consider this use of derivations:

    ```python
    >>> import copy
    >>> nCopy = copy.deepcopy(n)
    >>> nCopy.derivation
    <Derivation of <music21.note.Note A-> from <music21.note.Note A-> via '__deepcopy__'>
    >>> nCopy.getOffsetBySite(s1)
    Fraction(20, 3)
    ```

    nCopy can still find the offset of n in s1!
    This is the primary difference between element.getOffsetBySite(stream)
    and stream.elementOffset(element)

    ```python
    >>> s1.elementOffset(nCopy)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object ... is not
        stored in stream <music21.stream.Stream containingStream>
    ```

    If the object is stored at the end of the Stream, then the highest time
    is usually returned:

    ```python
    >>> s3 = stream.Stream()
    >>> n3 = note.Note(type='whole')
    >>> s3.append(n3)
    >>> rb = bar.Barline()
    >>> s3.storeAtEnd(rb)  # s3.rightBarline = rb would do the same
    >>> rb.getOffsetBySite(s3)
    4.0
    ```

    However, setting returnSpecial to True will return OffsetSpecial.AT\_END

    ```python
    >>> rb.getOffsetBySite(s3, returnSpecial=True)
    <OffsetSpecial.AT_END>
    ```

    Even with returnSpecial normal offsets are still returned as a float or Fraction:

    ```python
    >>> n3.getOffsetBySite(s3, returnSpecial=True)
    0.0
    ```

    * Changed in v7: stringReturns renamed to returnSpecial.
      Returns an OffsetSpecial Enum.

Music21Object.getOffsetInHierarchy(*site: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → OffsetQL[[source]](../_modules/music21/base.html#Music21Object.getOffsetInHierarchy)
:   For an element which may not be in site, but might be in a Stream in site (or further
    in streams), find the cumulative offset of the element in that site.

    ```python
    >>> s = stream.Score(id='mainScore')
    >>> p = stream.Part()
    >>> m = stream.Measure()
    >>> n = note.Note()
    >>> m.insert(5.0, n)
    >>> p.insert(10.0, m)
    >>> s.insert(0.0, p)
    >>> n.getOffsetInHierarchy(s)
    15.0
    ```

    If no hierarchy beginning with site contains the element
    and the element is not derived from
    an element that does, then a SitesException is raised:

    ```python
    >>> s2 = stream.Score(id='otherScore')
    >>> n.getOffsetInHierarchy(s2)
    Traceback (most recent call last):
    music21.sites.SitesException: Element <music21.note.Note C>
        is not in hierarchy of <music21.stream.Score otherScore>
    ```

    But if the element is derived from an element in
    a hierarchy then it can get the offset:

    ```python
    >>> n2 = n.transpose('P5')
    >>> n2.derivation.origin is n
    True
    >>> n2.derivation.method
    'transpose'
    >>> n2.getOffsetInHierarchy(s)
    15.0
    ```

    There is no corresponding .setOffsetInHierarchy()
    since it’s unclear what that would mean.

    See also [`music21.stream.iterator.RecursiveIterator.currentHierarchyOffset()`](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator.currentHierarchyOffset "music21.stream.iterator.RecursiveIterator.currentHierarchyOffset")
    for a method that is about 10x faster when running through a recursed stream.

    * New in v3.

Music21Object.getSpannerSites(*spannerClassList: Iterable | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[spanner.Spanner](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")][[source]](../_modules/music21/base.html#Music21Object.getSpannerSites)
:   Return a list of all [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner") objects
    (or Spanner subclasses) that contain
    this element. This method provides a way for
    objects to be aware of what Spanners they
    reside in. Note that Spanners are not Streams
    but specialized Music21Objects that use a
    Stream subclass, SpannerStorage, internally to keep track
    of the elements that are spanned.

    ```python
    >>> c = note.Note('C4')
    >>> d = note.Note('D4')
    >>> slur1 = spanner.Slur(c, d)
    >>> c.getSpannerSites() == [slur1]
    True
    ```

    Note that not all Spanners are in the spanner module. They
    tend to reside in modules closer to their musical function:

    ```python
    >>> cresc = dynamics.Crescendo(d, c)
    ```

    The order that Spanners are returned is by sortTuple. For spanners
    created the same way and in the same order, the order returned will
    be consistent:

    ```python
    >>> d.getSpannerSites() == [slur1, cresc]
    True
    ```

    Optionally a class name or list of class names (as Classes or strings)
    can be specified and only Spanners of that class will be returned

    ```python
    >>> dim = dynamics.Diminuendo(c, d)
    >>> d.getSpannerSites(dynamics.Diminuendo) == [dim]
    True
    ```

    A larger class name can be used to get all subclasses:

    ```python
    >>> d.getSpannerSites(dynamics.DynamicWedge) == [cresc, dim]
    True
    >>> d.getSpannerSites(['Slur', 'Diminuendo']) == [slur1, dim]
    True
    ```

    Note that the order of spanners returned from this routine can vary, so
    changing to a set is useful for comparisons

    ```python
    >>> set(d.getSpannerSites(['Slur', 'Diminuendo'])) == {dim, slur1}
    True
    ```

    Example: see which pairs of notes are in the same slur.

    ```python
    >>> e = note.Note('E4')
    >>> slur2 = spanner.Slur(c, e)
    ```

    ```python
    >>> for n in [c, d, e]:
    ...    nSlurs = n.getSpannerSites(spanner.Slur)
    ...    for nOther in [c, d, e]:
    ...        if n is nOther:
    ...            continue
    ...        nOtherSlurs = nOther.getSpannerSites(spanner.Slur)
    ...        for thisSlur in nSlurs:
    ...            if thisSlur in nOtherSlurs:
    ...               print(f'{n.name} shares a slur with {nOther.name}')
    C shares a slur with D
    C shares a slur with E
    D shares a slur with C
    E shares a slur with C
    ```

Music21Object.informSites(*changedInformation=None*)[[source]](../_modules/music21/base.html#Music21Object.informSites)
:   trigger called whenever sites need to be informed of a change
    in the parameters of this object.

    changedInformation is not used now, but it can be a dictionary
    of what has changed.

    subclass this to do very interesting things.

Music21Object.mergeAttributes(*other: [Music21Object](#music21.base.Music21Object "music21.base.Music21Object")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.mergeAttributes)
:   Merge all elementary, static attributes. Namely,
    id and groups attributes from another music21 object.
    Can be useful for copy-like operations.

    ```python
    >>> m1 = base.Music21Object()
    >>> m2 = base.Music21Object()
    >>> m1.id = 'music21Object1'
    >>> m1.groups.append('group1')
    >>> m2.mergeAttributes(m1)
    >>> m2.id
    'music21Object1'
    >>> 'group1' in m2.groups
    True
    ```

Music21Object.next(*className: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Music21Object](#music21.base.Music21Object "music21.base.Music21Object")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *activeSiteOnly=False*)[[source]](../_modules/music21/base.html#Music21Object.next)
:   Get the next element found in the activeSite (or other Sites)
    of this Music21Object.

    The className can be used to specify one or more classes to match.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> m3 = s.parts[0].measure(3)
    >>> m4 = s.parts[0].measure(4)
    >>> m3
    <music21.stream.Measure 3 offset=9.0>
    >>> m3.show('t')
    {0.0} <music21.layout.SystemLayout>
    {0.0} <music21.note.Note A>
    {0.5} <music21.note.Note B>
    {1.0} <music21.note.Note G#>
    {2.0} <music21.note.Note F#>
    {3.0} <music21.note.Note A>
    >>> m3.next()
    <music21.layout.SystemLayout>
    >>> nextM3 = m3.next('Measure')
    >>> nextM3 is m4
    True
    ```

    Note that calling next() repeatedly gives the same object. You’ll want to
    call next on that object.

    ```python
    >>> m3.next('Measure') is s.parts[0].measure(4)
    True
    >>> m3.next('Measure') is s.parts[0].measure(4)
    True
    ```

    So do this instead:

    ```python
    >>> o = m3
    >>> for i in range(5):
    ...     print(o)
    ...     o = o.next('Measure')
    <music21.stream.Measure 3 offset=9.0>
    <music21.stream.Measure 4 offset=13.0>
    <music21.stream.Measure 5 offset=17.0>
    <music21.stream.Measure 6 offset=21.0>
    <music21.stream.Measure 7 offset=25.0>
    ```

    We can find the next element given a certain class with the className:

    ```python
    >>> n = m3.next('Note')
    >>> n
    <music21.note.Note A>
    >>> n.measureNumber
    3
    >>> n is m3.notes.first()
    True
    >>> n.next()
    <music21.note.Note B>
    ```

    Notice though that when we get to the end of the set of measures, something
    interesting happens (maybe it shouldn’t? don’t count on this.): we descend
    into the last measure and give its elements instead.

    We’ll leave o where it is (m8 now) to demonstrate what happens, and also
    print its Part for more information:

    ```python
    >>> while o is not None:
    ...     print(o, o.getContextByClass(stream.Part))
    ...     o = o.next()
    <music21.stream.Measure 8 offset=29.0> <music21.stream.Part Soprano>
    <music21.note.Note F#> <music21.stream.Part Soprano>
    <music21.note.Note F#> <music21.stream.Part Soprano>
    <music21.note.Note F#> <music21.stream.Part Soprano>
    <music21.stream.Measure 9 offset=33.0> <music21.stream.Part Soprano>
    <music21.note.Note F#> <music21.stream.Part Soprano>
    <music21.note.Note F#> <music21.stream.Part Soprano>
    <music21.note.Note E#> <music21.stream.Part Soprano>
    <music21.note.Note F#> <music21.stream.Part Soprano>
    <music21.bar.Barline type=final> <music21.stream.Part Soprano>
    ```

    * Changed in v6: added activeSiteOnly – see description in .contextSites()

Music21Object.previous(*className: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Music21Object](#music21.base.Music21Object "music21.base.Music21Object")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *activeSiteOnly=False*)[[source]](../_modules/music21/base.html#Music21Object.previous)
:   Get the previous element found in the activeSite or other .sites of this
    Music21Object.

    The className can be used to specify one or more classes to match.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> m2 = s.parts[0].getElementsByClass(stream.Measure)[2]  # pickup measure
    >>> m3 = s.parts[0].getElementsByClass(stream.Measure)[3]
    >>> m3
    <music21.stream.Measure 3 offset=9.0>
    >>> m3prev = m3.previous()
    >>> m3prev
    <music21.note.Note C#>
    >>> m3prev is m2.notes[-1]
    True
    >>> m3.previous('Measure') is m2
    True
    ```

    We’ll iterate backwards from the first note of the second measure of the Alto part.

    ```python
    >>> o = s.parts[1].getElementsByClass(stream.Measure)[2][0]
    >>> while o:
    ...    print(o)
    ...    o = o.previous()
    <music21.note.Note E>
    <music21.stream.Measure 2 offset=5.0>
    <music21.note.Note E>
    <music21.note.Note E>
    <music21.note.Note E>
    <music21.note.Note F#>
    <music21.stream.Measure 1 offset=1.0>
    <music21.note.Note E>
    <music21.meter.TimeSignature 4/4>
    f# minor
    <music21.tempo.MetronomeMark Quarter=96 (playback only)>
    <music21.clef.TrebleClef>
    <music21.stream.Measure 0 offset=0.0>
    P2: Alto: Instrument 2
    <music21.stream.Part Alto>
    <music21.stream.Part Soprano>
    <music21.metadata.Metadata object at 0x11116d080>
    <music21.stream.Score bach/bwv66.6.mxl>
    ```

    * Changed in v6: added activeSiteOnly – see description in .contextSites()

Music21Object.purgeLocations(*rescanIsDead=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.purgeLocations)
:   Remove references to all locations in objects that no longer exist.

Music21Object.purgeOrphans(*excludeStorageStreams=True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.purgeOrphans)
:   A Music21Object may, due to deep copying or other reasons,
    have a site (with an offset) which
    no longer contains the Music21Object. These lingering sites
    are called orphans. This method gets rid of them.

    The excludeStorageStreams are SpannerStorage and VariantStorage.

Music21Object.setOffsetBySite(*site: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *value: OffsetQLIn*)[[source]](../_modules/music21/base.html#Music21Object.setOffsetBySite)
:   Change the offset for a site. These are equivalent:

    > n1.setOffsetBySite(stream1, 20)

    and

    > stream1.setElementOffset(n1, 20)

    Which you choose to use will depend on whether you are iterating over a list
    of notes (etc.) or streams.

    ```python
    >>> import music21
    >>> aSite = stream.Stream()
    >>> aSite.id = 'aSite'
    >>> a = music21.Music21Object()
    >>> aSite.insert(0, a)
    >>> aSite.setElementOffset(a, 20)
    >>> a.setOffsetBySite(aSite, 30)
    >>> a.getOffsetBySite(aSite)
    30.0
    ```

    And if it isn’t in a Stream? Raises an exception and the offset does not change.

    ```python
    >>> b = note.Note('D')
    >>> b.setOffsetBySite(aSite, 40)
    Traceback (most recent call last):
    music21.exceptions21.StreamException: Cannot set the offset for element
        <music21.note.Note D>, not in Stream <music21.stream.Stream aSite>.
    ```

    ```python
    >>> b.offset
    0.0
    ```

    Setting offset for None changes the “naive offset” of an object:

    ```python
    >>> b.setOffsetBySite(None, 32)
    >>> b.offset
    32.0
    >>> b.activeSite is None
    True
    ```

    Running setOffsetBySite also changes the activeSite of the object.

Music21Object.show(*fmt=None*, *app=None*, *\*\*keywords*)[[source]](../_modules/music21/base.html#Music21Object.show)
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

Music21Object.sortTuple(*useSite: t.Literal[False] | stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = False*, *raiseExceptionOnMiss: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [SortTuple](moduleSorting.html#music21.sorting.SortTuple "music21.sorting.SortTuple")[[source]](../_modules/music21/base.html#Music21Object.sortTuple)
:   Returns a collections.namedtuple called SortTuple(atEnd, offset, priority, classSortOrder,
    isNotGrace, insertIndex)
    which contains the six elements necessary to determine the sort order of any set of
    objects in a Stream.

    1) atEnd = {0, 1}; Elements specified to always stay at
    the end of a stream (`stream.storeAtEnd`)
    sort after normal elements.

    2) offset = float; Offset (with respect to the active site) is the next and most
    important parameter in determining the order of elements in a stream (the note on beat 1
    has offset 0.0, while the note on beat 2 might have offset 1.0).

    3) priority = int; Priority is a
    user-specified property (default 0) that can set the order of
    elements which have the same
    offset (for instance, two Parts both at offset 0.0).

    4) classSortOrder = int or float; ClassSortOrder
    is the third level of comparison that gives an ordering to elements with different classes,
    ensuring, for instance that Clefs (classSortOrder = 0) sort before Notes
    (classSortOrder = 20).

    5. isNotGrace = {0, 1}; 0 = grace, 1 = normal. Grace notes sort before normal notes

    6) The last tie-breaker is the creation time (insertIndex) of the site object
    represented by the activeSite.

    By default, the site used will be the activeSite:

    ```python
    >>> n = note.Note()
    >>> n.offset = 4.0
    >>> n.priority = -3
    >>> n.sortTuple()
    SortTuple(atEnd=0, offset=4.0, priority=-3, classSortOrder=20,
                isNotGrace=1, insertIndex=0)
    ```

    ```python
    >>> st = n.sortTuple()
    ```

    Check that all these values are the same as above:

    ```python
    >>> st.offset == n.offset
    True
    >>> st.priority == n.priority
    True
    ```

    An object’s classSortOrder comes from the Class object itself:

    ```python
    >>> st.classSortOrder == note.Note.classSortOrder
    True
    ```

    SortTuples have a few methods that are documented in [`SortTuple`](moduleSorting.html#music21.sorting.SortTuple "music21.sorting.SortTuple").
    The most useful one for documenting is .shortRepr().

    ```python
    >>> st.shortRepr()
    '4.0 <-3.20.0>'
    ```

    Inserting the note into the Stream will set the insertIndex. Most implementations of
    music21 will use a global counter rather than an actual timer. Note that this is a
    last resort, but useful for things such as multiple Parts inserted in order. It changes
    with each run, so we can’t display it here.

    ```python
    >>> s = stream.Stream()
    >>> s.insert(n)
    >>> n.sortTuple()
    SortTuple(atEnd=0, offset=4.0, priority=-3, classSortOrder=20,
                 isNotGrace=1, insertIndex=...)
    ```

    ```python
    >>> nInsertIndex = n.sortTuple().insertIndex
    ```

    If we create another nearly identical note, the insertIndex will be different:

    ```python
    >>> n2 = note.Note()
    >>> n2.offset = 4.0
    >>> n2.priority = -3
    >>> s.insert(n2)
    >>> n2InsertIndex = n2.sortTuple().insertIndex
    >>> n2InsertIndex > nInsertIndex
    True
    ```

    ```python
    >>> rb = bar.Barline()
    >>> s.storeAtEnd(rb)
    >>> rb.sortTuple()
    SortTuple(atEnd=1, offset=0.0, priority=0, classSortOrder=-5,
                isNotGrace=1, insertIndex=...)
    ```

    Normally if there’s a site specified and the element is not in the site,
    the offset of None will be used, but if raiseExceptionOnMiss is set to True
    then a SitesException will be raised:

    ```python
    >>> aloneNote = note.Note()
    >>> aloneNote.offset = 30
    >>> aloneStream = stream.Stream(id='aloneStream')  # no insert
    >>> aloneNote.sortTuple(aloneStream)
    SortTuple(atEnd=0, offset=30.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=0)
    ```

    ```python
    >>> aloneNote.sortTuple(aloneStream, raiseExceptionOnMiss=True)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object 0x... is not stored in
        stream <music21.stream.Stream aloneStream>
    ```

Music21Object.splitAtDurations() → \_SplitTuple[[source]](../_modules/music21/base.html#Music21Object.splitAtDurations)
:   Takes a Music21Object (e.g., a note.Note) and returns a list of similar
    objects with only a single duration.DurationTuple in each.
    Ties are added if the object supports ties.

    Articulations only appear on the first note. Same with lyrics.

    Fermatas should be on last note, but not done yet.

    ```python
    >>> a = note.Note()
    >>> a.duration.clear()  # remove defaults
    >>> a.duration.addDurationTuple(duration.durationTupleFromTypeDots('half', 0))
    >>> a.duration.quarterLength
    2.0
    >>> a.duration.addDurationTuple(duration.durationTupleFromTypeDots('whole', 0))
    >>> a.duration.quarterLength
    6.0
    >>> b = a.splitAtDurations()
    >>> b
    (<music21.note.Note C>, <music21.note.Note C>)
    >>> b[0].pitch == b[1].pitch
    True
    >>> b[0].duration
    <music21.duration.Duration 2.0>
    >>> b[0].duration.type
    'half'
    >>> b[1].duration.type
    'whole'
    >>> b[0].quarterLength, b[1].quarterLength
    (2.0, 4.0)
    ```

    ```python
    >>> c = note.Note()
    >>> c.quarterLength = 2.5
    >>> d, e = c.splitAtDurations()
    >>> d.duration.type
    'half'
    >>> e.duration.type
    'eighth'
    >>> d.tie.type
    'start'
    >>> print(e.tie)
    <music21.tie.Tie stop>
    ```

    Assume c is tied to the next note. Then the last split note should also be tied

    ```python
    >>> c.tie = tie.Tie('start')
    >>> d, e = c.splitAtDurations()
    >>> d.tie.type
    'start'
    >>> e.tie.type
    'continue'
    ```

    Rests have no ties:

    ```python
    >>> f = note.Rest()
    >>> f.quarterLength = 2.5
    >>> g, h = f.splitAtDurations()
    >>> (g.duration.type, h.duration.type)
    ('half', 'eighth')
    >>> f.tie is None
    True
    >>> g.tie is None
    True
    ```

    It should work for complex notes with tuplets.

    (this duration occurs in Modena A, Le greygnour bien, from the ars subtilior, c. 1380;
    hence how I discovered this bug)

    ```python
    >>> n = note.Note()
    >>> n.duration.quarterLength = 0.5 + 0.0625  # eighth + 64th
    >>> tup = duration.Tuplet(4, 3)
    >>> n.duration.appendTuplet(tup)
    >>> first, last = n.splitAtDurations()
    >>> (first.duration, last.duration)
    (<music21.duration.Duration 0.375>, <music21.duration.Duration 0.046875>)
    ```

    Notice that this duration could have been done w/o tuplets, so no tuplets in output:

    ```python
    >>> (first.duration.type, first.duration.dots, first.duration.tuplets)
    ('16th', 1, ())
    >>> (last.duration.type, last.duration.dots, last.duration.tuplets)
    ('128th', 1, ())
    ```

    Test of one with tuplets that cannot be split:

    ```python
    >>> n = note.Note()
    >>> n.duration.quarterLength = 0.5 + 0.0625  # eighth + 64th
    >>> tup = duration.Tuplet(3, 2, 'eighth')
    >>> n.duration.appendTuplet(tup)
    >>> (n.duration.type, n.duration.dots, n.duration.tuplets)
    ('complex', 0, (<music21.duration.Tuplet 3/2/eighth>,))
    ```

    ```python
    >>> first, last = n.splitAtDurations()
    >>> (first.duration, last.duration)
    (<music21.duration.Duration 1/3>, <music21.duration.Duration 1/24>)
    ```

    ```python
    >>> (first.duration.type, first.duration.dots, first.duration.tuplets)
    ('eighth', 0, (<music21.duration.Tuplet 3/2/eighth>,))
    >>> (last.duration.type, last.duration.dots, last.duration.tuplets)
    ('64th', 0, (<music21.duration.Tuplet 3/2/64th>,))
    ```

    TODO: unite this and other functions into a “split” function – document obscure uses.

Music21Object.splitAtQuarterLength(*quarterLength*, *\**, *retainOrigin=True*, *addTies=True*, *displayTiedAccidentals=False*) → \_SplitTuple[[source]](../_modules/music21/base.html#Music21Object.splitAtQuarterLength)
:   Split an Element into two Elements at a provided
    quarterLength (offset) into the Element.

    Returns a specialized tuple (\_SplitTuple) that also has
    a .spannerList element which is a list of spanners
    that were created during the split, such as by splitting a trill
    note into more than one trill.

    TODO: unite into a “split” function – document obscure uses.

    ```python
    >>> a = note.Note('C#5')
    >>> a.duration.type = 'whole'
    >>> a.articulations = [articulations.Staccato()]
    >>> a.lyric = 'hi'
    >>> a.expressions = [expressions.Mordent(), expressions.Trill(), expressions.Fermata()]
    >>> st = a.splitAtQuarterLength(3)
    >>> b, c = st
    >>> b.duration.type
    'half'
    >>> b.duration.dots
    1
    >>> b.duration.quarterLength
    3.0
    >>> b.articulations
    []
    >>> b.lyric
    'hi'
    >>> b.expressions
    [<music21.expressions.Mordent>, <music21.expressions.Trill>]
    >>> c.duration.type
    'quarter'
    >>> c.duration.dots
    0
    >>> c.duration.quarterLength
    1.0
    >>> c.articulations
    [<music21.articulations.Staccato>]
    >>> c.lyric
    >>> c.expressions
    [<music21.expressions.Fermata>]
    >>> c.getSpannerSites()
    [<music21.expressions.TrillExtension <music21.note.Note C#><music21.note.Note C#>>]
    ```

    st is a \_SplitTuple which can get the spanners from it for inserting into a Stream.

    ```python
    >>> st.spannerList
    [<music21.expressions.TrillExtension <music21.note.Note C#><music21.note.Note C#>>]
    ```

    Make sure that ties and accidentals remain as they should be:

    ```python
    >>> d = note.Note('D#4')
    >>> d.duration.quarterLength = 3.0
    >>> d.tie = tie.Tie('start')
    >>> e, f = d.splitAtQuarterLength(2.0)
    >>> e.tie, f.tie
    (<music21.tie.Tie start>, <music21.tie.Tie continue>)
    >>> e.pitch.accidental.displayStatus is None
    True
    >>> f.pitch.accidental.displayStatus
    False
    ```

    Should be the same for chords:

    ```python
    >>> g = chord.Chord(['C4', 'E4', 'G#4'])
    >>> g.duration.quarterLength = 3.0
    >>> g[1].tie = tie.Tie('start')
    >>> h, i = g.splitAtQuarterLength(2.0)
    >>> for j in range(3):
    ...   (h[j].tie, i[j].tie)
    (<music21.tie.Tie start>, <music21.tie.Tie stop>)
    (<music21.tie.Tie start>, <music21.tie.Tie continue>)
    (<music21.tie.Tie start>, <music21.tie.Tie stop>)
    ```

    ```python
    >>> h[2].pitch.accidental.displayStatus, i[2].pitch.accidental.displayStatus
    (None, False)
    ```

    If quarterLength == self.quarterLength then the second element will be None.

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 0.5
    >>> firstPart, secondPart = n.splitAtQuarterLength(0.5)
    >>> secondPart is None
    True
    >>> firstPart is n
    True
    ```

    (same with retainOrigin off)

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 0.5
    >>> firstPart, secondPart = n.splitAtQuarterLength(0.5, retainOrigin=False)
    >>> firstPart is n
    False
    ```

    If quarterLength > self.quarterLength then a DurationException will be raised:

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 0.5
    >>> first, second = n.splitAtQuarterLength(0.7)
    Traceback (most recent call last):
    music21.duration.DurationException: cannot split a duration (0.5)
        at this quarterLength (7/10)
    ```

    * Changed in v7: all but quarterLength are keyword only

Music21Object.splitByQuarterLengths(*quarterLengthList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [fractions.Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")]*, *addTies=True*, *displayTiedAccidentals=False*) → \_SplitTuple[[source]](../_modules/music21/base.html#Music21Object.splitByQuarterLengths)
:   Given a list of quarter lengths, return a “SplitTuple” of
    Music21Object objects, copied from this Music21Object,
    that are partitioned and tied with the specified quarter
    length list durations.

    THe SplitTuple will also have a .spannerList which
    contains a list of spanner created during the split, such as by splitting a trill
    note into more than one trill.

    TODO: unite into a “split” function – document obscure uses.

    ```python
    >>> n = note.Note()
    >>> n.quarterLength = 3
    >>> post = n.splitByQuarterLengths([1, 1, 1])
    >>> [n.quarterLength for n in post]
    [1.0, 1.0, 1.0]
    ```

Music21Object.write(*fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | IOBase | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*) → [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/base.html#Music21Object.write)
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

[`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object") instance variables

Music21Object.classSortOrder
:   Property which returns an number (int or otherwise)
    depending on the class of the Music21Object that
    represents a priority for an object based on its class alone –
    used as a tie for stream sorting in case two objects have the
    same offset and priority. Lower numbers are sorted to the left
    of higher numbers. For instance, Clef, KeySignature, TimeSignature
    all come (in that order) before Note.

    All undefined classes have classSortOrder of 20 – same as note.Note

    ```python
    >>> m21o = base.Music21Object()
    >>> m21o.classSortOrder
    20
    ```

    ```python
    >>> tc = clef.TrebleClef()
    >>> tc.classSortOrder
    0
    ```

    ```python
    >>> ks = key.KeySignature(3)
    >>> ks.classSortOrder
    2
    ```

    New classes can define their own default classSortOrder

    ```python
    >>> class ExampleClass(base.Music21Object):
    ...     classSortOrder = 5
    ...
    >>> ec1 = ExampleClass()
    >>> ec1.classSortOrder
    5
    ```

Music21Object.groups
:   An instance of a [`Groups`](#music21.base.Groups "music21.base.Groups")
    object which describes
    arbitrary Groups that this object belongs to.

Music21Object.isStream
:   Boolean value for quickly identifying
    `Stream` objects (False by default).

Music21Object.sites
:   a [`Sites`](moduleSites.html#music21.sites.Sites "music21.sites.Sites") object that stores
    references to Streams that hold this object.

## ElementWrapper

class music21.base.ElementWrapper(*obj: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/base.html#ElementWrapper)
:   An ElementWrapper is a way of containing any object that is not a
    [`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object"), so that that object can be positioned
    within a `Stream`.

    The object stored within ElementWrapper is available from the
    [`obj`](#music21.base.ElementWrapper.obj "music21.base.ElementWrapper.obj") attribute. All the attributes of
    the stored object (except .id and anything else that conflicts with a
    Music21Object attribute) are gettable and settable by querying the
    ElementWrapper. This feature makes it possible easily to mix
    Music21Objects and non-Music21Objects with similarly named attributes in
    the same Stream.

    This example inserts 10 random wave files into a music21 Stream and then
    reports their filename and number of audio channels (in this example, it’s
    always 2) if they fall on a strong beat in fast 6/8

    ```python
    >>> import music21
    >>> import wave
    >>> import random
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.id = 'mainStream'
    >>> s.append(meter.TimeSignature('fast 6/8'))
    >>> for i in range(10):
    ...    fileName = 'thisSound_' + str(random.randint(1, 20)) + '.wav'
    ...    soundFile = wave.open(fileName)
    ...    soundFile.fileName = fileName
    ...    el = music21.ElementWrapper(soundFile)
    ...    s.insert(i, el)
    ```

    ```python
    >>> for j in s.getElementsByClass(base.ElementWrapper):
    ...    if j.beatStrength > 0.4:
    ...        (j.offset, j.beatStrength, j.getnchannels(), j.fileName)
    (0.0, 1.0, 2, 'thisSound_1.wav')
    (3.0, 1.0, 2, 'thisSound_16.wav')
    (6.0, 1.0, 2, 'thisSound_12.wav')
    (9.0, 1.0, 2, 'thisSound_8.wav')
    >>> for j in s.getElementsByClass(base.ElementWrapper):
    ...    if j.beatStrength > 0.4:
    ...        (j.offset, j.beatStrength, j.getnchannels() + 1, j.fileName)
    (0.0, 1.0, 3, 'thisSound_1.wav')
    (3.0, 1.0, 3, 'thisSound_16.wav')
    (6.0, 1.0, 3, 'thisSound_12.wav')
    (9.0, 1.0, 3, 'thisSound_8.wav')
    ```

    Test representation of an ElementWrapper

    ```python
    >>> for i, j in enumerate(s.getElementsByClass(base.ElementWrapper)):
    ...     if i == 2:
    ...         j.id = None
    ...     else:
    ...         j.id = str(i) + '_wrapper'
    ...     if i <=2:
    ...         print(j)
    <music21.base.ElementWrapper id=0_wrapper offset=0.0 obj='<...Wave_read object...'>
    <music21.base.ElementWrapper id=1_wrapper offset=1.0 obj='<...Wave_read object...'>
    <music21.base.ElementWrapper offset=2.0 obj='<...Wave_read object...>'>
    ```

    ### Equality

    Two ElementWrappers are equal if they would be equal as Music21Objects and they
    wrap objects that are equal.

    ```python
    >>> list1 = ['a', 'b', 'c']
    >>> a = base.ElementWrapper(list1)
    >>> a.offset = 3.0
    ```

    ```python
    >>> list2 = ['a', 'b', 'c']
    >>> b = base.ElementWrapper(list2)
    >>> b.offset = 3.0
    >>> a == b
    True
    >>> a is not b
    True
    ```

    Offset does not need to be equal for equality:

    ```python
    >>> b.offset = 4.0
    >>> a == b
    True
    ```

    But elements must compare equal

    ```python
    >>> list2.append('d')
    >>> a == b
    False
    ```

    * Changed in v9: completely different approach to equality, unified w/
      the rest of music21.

[`ElementWrapper`](#music21.base.ElementWrapper "music21.base.ElementWrapper") bases

* [`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ElementWrapper`](#music21.base.ElementWrapper "music21.base.ElementWrapper") read-only properties

Read-only properties inherited from [`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ElementWrapper`](#music21.base.ElementWrapper "music21.base.ElementWrapper") read/write properties

Read/write properties inherited from [`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ElementWrapper`](#music21.base.ElementWrapper "music21.base.ElementWrapper") methods

Methods inherited from [`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ElementWrapper`](#music21.base.ElementWrapper "music21.base.ElementWrapper") instance variables

ElementWrapper.obj
:   The object this wrapper wraps. It should not be a Music21Object, since
    if so, you might as well put that directly into the Stream itself.

Instance variables inherited from [`Music21Object`](#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ContextSortTuple

class music21.base.ContextSortTuple(*site*, *offset*, *recurseType*)[[source]](../_modules/music21/base.html#ContextSortTuple)

## ContextTuple

class music21.base.ContextTuple(*site*, *offset*, *recurseType*)[[source]](../_modules/music21/base.html#ContextTuple)

## Groups

class music21.base.Groups(*iterable=()*, */*)[[source]](../_modules/music21/base.html#Groups)
:   Groups is a list (subclass) of strings used to identify
    associations that an element might have.

    (in the future, Groups will become a set subclass)

    The Groups object enforces that all elements must be strings, and that
    the same element cannot be provided more than once.

    NOTE: In the future, spaces will not be allowed in group names.

    ```python
    >>> g = Groups()
    >>> g.append('hello')
    >>> g[0]
    'hello'
    ```

    ```python
    >>> g.append('hello')  # not added as already present
    >>> len(g)
    1
    ```

    ```python
    >>> g
    ['hello']
    ```

    ```python
    >>> g.append(5)  # type: ignore
    Traceback (most recent call last):
    music21.exceptions21.GroupException: Only strings can be used as group names, not 5
    ```

[`Groups`](#music21.base.Groups "music21.base.Groups") methods

Groups.\_\_eq\_\_(*other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")*)[[source]](../_modules/music21/base.html#Groups.__eq__)
:   Test Group equality. In normal lists, order matters; here it does not. More like a set.

    ```python
    >>> a = base.Groups()
    >>> a.append('red')
    >>> a.append('green')
    >>> a
    ['red', 'green']
    ```

    ```python
    >>> b = base.Groups()
    >>> b.append('green')
    >>> a == b
    False
    ```

    ```python
    >>> b.append('reD')  # case insensitive
    >>> a == b
    True
    ```

    ```python
    >>> a == ['red', 'green']  # need both to be groups
    False
    ```

    ```python
    >>> c = base.Groups()
    >>> c.append('black')
    >>> c.append('tuba')
    >>> a == c
    False
    ```

Groups.append(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/base.html#Groups.append)
:   Append object to the end of the list.
