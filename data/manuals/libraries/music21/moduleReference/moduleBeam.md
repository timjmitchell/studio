Source: https://music21.org/music21docs/moduleReference/moduleBeam.html

# music21.beam

The module defines Beam and Beams (note plural) objects.

The Beams object holds multiple Beam objects (e.g., a 32nd note might have
three Beam objects in its Beam object).

The Beams object is stored in [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") and
[`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") objects as their `beams`
attributes. Beams objects can largely be treated as a list.

See meter.TimeSignature. `getBeams()` for a
way of getting beam information for a measure given the meter. The
meter.TimeSignature. `beamSequence`
attribute holds information about how to beam given the TimeSignature

Run Stream. `makeBeams()` to set beaming
information automatically given the current meter.

Suppose you had a measure of two eighths and a quarter and wanted to explicitly
beam the two eighth notes. You could do this:

```python
>>> m = stream.Measure()
>>> n1 = note.Note('C4', quarterLength=0.5)
>>> n2 = note.Note('D4', quarterLength=0.5)
>>> n3 = note.Note('E4', quarterLength=1.0)
>>> m.append(n1)
>>> m.append(n2)
>>> m.append(n3)
>>> n1.beams.fill('eighth', type='start')
>>> n2.beams.fill('eighth', type='stop')
>>> n1.beams
<music21.beam.Beams <music21.beam.Beam 1/start>>
```

```python
>>> n2.beams
<music21.beam.Beams <music21.beam.Beam 1/stop>>
```

But suppose you wanted something harder: two 16ths, an 8th, a quarter, with the
first 3 notes beamed? The first note and 3rd are easy to do, using the method
above:

```python
>>> m = stream.Measure()
>>> n1 = note.Note('C4', quarterLength=0.25)
>>> n2 = note.Note('D4', quarterLength=0.25)
>>> n3 = note.Note('E4', quarterLength=0.5)
>>> n4 = note.Note('F4', quarterLength=1.0)
>>> for n in [n1, n2, n3, n4]:
...     m.append(n)
>>> n1.beams.fill('16th', type='start')
>>> n3.beams.fill('eighth', type='stop')
```

but the second note has an 8th beam that continues and a 16th beam that stops.
So you will need to set them separately:

```python
>>> n2.beams.append('continue')
>>> n2.beams.append('stop')
>>> n2.beams
<music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/stop>>
```

To get rid of beams on a note do:

```python
>>> n2.beams.beamsList = []
```

## Beams

class music21.beam.Beams[[source]](../_modules/music21/beam.html#Beams)
:   The Beams object stores in it attribute beamsList (a list) all the Beam
    objects defined above. Thus, len(beam.Beams) tells you how many beams the
    note currently has on it, and iterating over a Beams object gives you each
    Beam.

    ```python
    >>> n = note.Note(type='16th')
    >>> isinstance(n.beams, beam.Beams)
    True
    ```

    ```python
    >>> n.beams.fill(2, 'start')
    >>> len(n.beams)
    2
    ```

    ```python
    >>> for thisBeam in n.beams:
    ...     thisBeam.type
    'start'
    'start'
    ```

    ```python
    >>> print(n.beams)
    <music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>
    ```

[`Beams`](#music21.beam.Beams "music21.beam.Beams") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Beams`](#music21.beam.Beams "music21.beam.Beams") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Beams`](#music21.beam.Beams "music21.beam.Beams") methods

Beams.\_\_eq\_\_(*other*)[[source]](../_modules/music21/beam.html#Beams.__eq__)
:   Return self==value.

Beams.append(*type=None*, *direction=None*)[[source]](../_modules/music21/beam.html#Beams.append)
:   Append a new Beam object to this Beams object, automatically creating the Beam
    object and incrementing the number count.

    ```python
    >>> beams = beam.Beams()
    >>> beams.append('start')
    >>> beams.beamsList
    [<music21.beam.Beam 1/start>]
    ```

    ```python
    >>> beams.append('partial', 'right')
    >>> beams.beamsList
    [<music21.beam.Beam 1/start>, <music21.beam.Beam 2/partial/right>]
    ```

    A beam object can also be specified:

    ```python
    >>> beams = beam.Beams()
    >>> beam1 = beam.Beam(type='start', number=1)
    >>> beams.append(beam1)
    >>> beams.beamsList
    [<music21.beam.Beam 1/start>]
    ```

Beams.fill(*level=None*, *type=None*)[[source]](../_modules/music21/beam.html#Beams.fill)
:   A quick way of setting the beams list for a particular duration, for
    instance, fill(‘16th’) will clear the current list of beams in the
    Beams object and add two beams. fill(2) will do the same (though note
    that that is an int, not a string).

    It does not do anything to the direction that the beams are going in,
    or by default. Either set type here or call setAll() on the Beams
    object afterwards.

    Both “eighth” and “8th” work. Adding more than nine beams (i.e. things
    like 4096th notes) raises an error.

    ```python
    >>> a = beam.Beams()
    >>> a.fill('16th')
    >>> len(a)
    2
    ```

    ```python
    >>> a.fill('32nd', type='start')
    >>> len(a)
    3
    ```

    ```python
    >>> a.beamsList[2]
    <music21.beam.Beam 3/start>
    ```

    ```python
    >>> a.beamsList[2].type
    'start'
    ```

    Filling a smaller number wipes larger numbers of beams:

    ```python
    >>> a.fill('eighth', type='start')
    >>> len(a)
    1
    ```

Beams.getByNumber(*number*)[[source]](../_modules/music21/beam.html#Beams.getByNumber)
:   Gets an internal beam object by number.

    ```python
    >>> a = beam.Beams()
    >>> a.fill('16th')
    >>> a.setAll('start')
    >>> a.getByNumber(2).type
    'start'
    ```

    ```python
    >>> a.getByNumber(30)
    Traceback (most recent call last):
    IndexError: beam number 30 cannot be accessed
    ```

Beams.getNumbers()[[source]](../_modules/music21/beam.html#Beams.getNumbers)
:   Returns a list of all defined beam numbers; it should normally be a set
    of consecutive integers, but it might not be.

    ```python
    >>> a = beam.Beams()
    >>> a.fill('32nd')
    >>> a.getNumbers()
    [1, 2, 3]
    ```

Beams.getTypeByNumber(*number*)[[source]](../_modules/music21/beam.html#Beams.getTypeByNumber)
:   Get beam type, with direction, by number

    ```python
    >>> a = beam.Beams()
    >>> a.fill('16th')
    >>> a.setAll('start')
    >>> a.setByNumber(2, 'partial-right')
    >>> a.getTypeByNumber(2)
    'partial-right'
    ```

    ```python
    >>> a.getTypeByNumber(1)
    'start'
    ```

Beams.getTypes()[[source]](../_modules/music21/beam.html#Beams.getTypes)
:   Returns a list of all beam types defined for the current beams

    ```python
    >>> a = beam.Beams()
    >>> a.fill('16th')
    >>> a.setAll('start')
    >>> a.getTypes()
    ['start', 'start']
    ```

static Beams.mergeConnectingPartialBeams(*beamsList*)[[source]](../_modules/music21/beam.html#Beams.mergeConnectingPartialBeams)
:   Partial-right followed by partial-left must also be connected, even if otherwise
    over a archetypeSpan, such as 16th notes 2 and 3 in a quarter note span where
    16ths are not beamed by default.

static Beams.naiveBeams(*srcList: Iterable[[base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*)[[source]](../_modules/music21/beam.html#Beams.naiveBeams)
:   Given a list or iterator of elements, return a list of None or Beams for
    each element: None if the element is a quarter or larger or
    if the element is a Rest, and the fullest possible set of beams
    for the duration if it is a beamable. Each beam object has type of None

    staticmethod, does not need instance:

    ```python
    >>> durList = [0, -1, -2, -3]
    >>> srcList = [note.Note(quarterLength=2 ** x) for x in durList]
    >>> srcList.append(note.Rest(type='32nd'))
    >>> beam.Beams.naiveBeams(srcList)
    [None,
     <music21.beam.Beams <music21.beam.Beam 1/None>>,
     <music21.beam.Beams <music21.beam.Beam 1/None>/<music21.beam.Beam 2/None>>,
     <music21.beam.Beams <music21.beam.Beam 1/None>/<music21.beam.Beam
                 2/None>/<music21.beam.Beam 3/None>>,
     None]
    ```

static Beams.removeSandwichedUnbeamables(*beamsList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Beams](#music21.beam.Beams "music21.beam.Beams") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*)[[source]](../_modules/music21/beam.html#Beams.removeSandwichedUnbeamables)
:   Go through the naiveBeamsList and remove beams from objects surrounded
    by None objects – you can’t beam to nothing!

    Modifies beamsList in place

    ```python
    >>> N = note.Note
    >>> R = note.Rest
    >>> e = 'eighth'
    >>> nList = [N(type=e), R(type=e), N(type=e), N(type=e),
    ...          R(type=e), N(type=e), R(type=e), N(type=e)]
    >>> beamsList = beam.Beams.naiveBeams(nList)
    >>> beamsList
    [<music21.beam.Beams <music21.beam.Beam 1/None>>,
     None,
     <music21.beam.Beams <music21.beam.Beam 1/None>>,
     <music21.beam.Beams <music21.beam.Beam 1/None>>,
     None,
     <music21.beam.Beams <music21.beam.Beam 1/None>>,
     None,
     <music21.beam.Beams <music21.beam.Beam 1/None>>]
    ```

    ```python
    >>> beamsList2 = beam.Beams.removeSandwichedUnbeamables(beamsList)
    >>> beamsList2 is beamsList
    True
    >>> beamsList2
    [None,
     None,
     <music21.beam.Beams <music21.beam.Beam 1/None>>,
     <music21.beam.Beams <music21.beam.Beam 1/None>>,
     None,
     None,
     None,
     None]
    ```

static Beams.sanitizePartialBeams(*beamsList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Beams](#music21.beam.Beams "music21.beam.Beams") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Beams](#music21.beam.Beams "music21.beam.Beams") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/beam.html#Beams.sanitizePartialBeams)
:   It is possible at a late stage to have beams that only consist of partials
    or beams with a ‘start’ followed by ‘partial/left’ or possibly ‘stop’ followed
    by ‘partial/right’; beams entirely consisting of partials are removed
    and the direction of irrational partials is fixed.

Beams.setAll(*type*, *direction=None*)[[source]](../_modules/music21/beam.html#Beams.setAll)
:   setAll is a method of convenience that sets the type
    of each of the beam objects within the beamsList to the specified type.
    It also takes an optional “direction” attribute that sets the direction
    for each beam (otherwise the direction of each beam is set to None)
    Acceptable directions (start, stop, continue, etc.) are listed under
    Beam() above.

    ```python
    >>> a = beam.Beams()
    >>> a.fill('16th')
    >>> a.setAll('start')
    >>> a.getTypes()
    ['start', 'start']
    ```

    ```python
    >>> a.setAll('sexy')
    Traceback (most recent call last):
    music21.beam.BeamException: beam type cannot be sexy
    ```

Beams.setByNumber(*number*, *type*, *direction=None*)[[source]](../_modules/music21/beam.html#Beams.setByNumber)
:   Set an internal beam object by number, or rhythmic symbol level.

    ```python
    >>> a = beam.Beams()
    >>> a.fill('16th')
    >>> a.setAll('start')
    >>> a.setByNumber(1, 'continue')
    >>> a.beamsList[0].type
    'continue'
    ```

    ```python
    >>> a.setByNumber(2, 'stop')
    >>> a.beamsList[1].type
    'stop'
    ```

    ```python
    >>> a.setByNumber(2, 'partial-right')
    >>> a.beamsList[1].type
    'partial'
    ```

    ```python
    >>> a.beamsList[1].direction
    'right'
    ```

    ```python
    >>> a.setByNumber(30, 'stop')
    Traceback (most recent call last):
    IndexError: beam number 30 cannot be accessed
    ```

    ```python
    >>> a.setByNumber(2, 'crazy')
    Traceback (most recent call last):
    music21.beam.BeamException: beam type cannot be crazy
    ```

[`Beams`](#music21.beam.Beams "music21.beam.Beams") instance variables

Beams.feathered
:   Boolean determining if this is a feathered beam or not
    (does nothing for now).

## Beam

class music21.beam.Beam(*type=None*, *direction=None*, *number=None*)[[source]](../_modules/music21/beam.html#Beam)
:   A Beam is an object representation of one single beam, that is, one
    horizontal line connecting two notes together (or less commonly a note to a
    rest). Thus, it takes two separate Beam objects to represent the beaming of
    a 16th note.

    The Beams object (note the plural) is the object that handles groups of
    Beam objects; it is defined later on.

    Here are two ways to define the start of a beam

    ```python
    >>> b1 = beam.Beam(type='start')
    >>> b2 = beam.Beam('start')
    ```

    Here is a partial beam (that is, one that does not connect to any other
    note, such as the second beam of a dotted eighth, sixteenth group)

    Two ways of doing the same thing

    ```python
    >>> b3 = beam.Beam(number=1, type='partial', direction='left')
    >>> b3
    <music21.beam.Beam 1/partial/left>
    ```

    ```python
    >>> b4 = beam.Beam('partial', 'left')
    >>> b4.number = 1
    >>> b4
    <music21.beam.Beam 1/partial/left>
    ```

    All attributes must be the same for equality:

    ```python
    >>> b3 == b4
    True
    ```

    ```python
    >>> b2
    <music21.beam.Beam None/start>
    >>> b2 == b3
    False
    ```

[`Beam`](#music21.beam.Beam "music21.beam.Beam") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Beam`](#music21.beam.Beam "music21.beam.Beam") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

Read-only properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleStyle.html#music21.style.StyleMixin.hasEditorialInformation "music21.style.StyleMixin.hasEditorialInformation") | * [`hasStyleInformation`](moduleStyle.html#music21.style.StyleMixin.hasStyleInformation "music21.style.StyleMixin.hasStyleInformation") |  |

[`Beam`](#music21.beam.Beam "music21.beam.Beam") read/write properties

Read/write properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`editorial`](moduleStyle.html#music21.style.StyleMixin.editorial "music21.style.StyleMixin.editorial") | * [`style`](moduleStyle.html#music21.style.StyleMixin.style "music21.style.StyleMixin.style") |  |

[`Beam`](#music21.beam.Beam "music21.beam.Beam") methods

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |
