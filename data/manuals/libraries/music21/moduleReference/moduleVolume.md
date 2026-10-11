Source: https://music21.org/music21docs/moduleReference/moduleVolume.html

# music21.volume

This module defines the object model of Volume, covering all representation of
amplitude, volume, velocity, and related parameters.

## Volume

class music21.volume.Volume(*\**, *client: [NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *velocity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *velocityScalar: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *velocityIsRelative: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/volume.html#Volume)
:   The Volume object lives on NotRest objects and subclasses. It is not a
    Music21Object subclass.

    Generally, just assume that a Note has a volume object and don’t worry
    about creating this class directly:

    ```python
    >>> n = note.Note('C5')
    >>> v = n.volume
    >>> v.velocity = 20
    >>> v.client is n
    True
    ```

    But if you want to create it yourself, you can specify the client, velocity,
    velocityScalar, and

    ```python
    >>> v = volume.Volume(velocity=90)
    >>> v
    <music21.volume.Volume realized=0.71>
    >>> v.velocity
    90
    ```

    * Changed in v9: all constructor attributes are keyword only.
      :   (client as first attribute was confusing)

[`Volume`](#music21.volume.Volume "music21.volume.Volume") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Volume`](#music21.volume.Volume "music21.volume.Volume") read-only properties

Volume.cachedRealized
:   Return the cached realized value of this volume. This will be the last
    realized value or, if that value has not been set, a newly realized
    value. If the caller knows that the realized values have all been
    recently set, using this property will add significant performance
    boost.

    ```python
    >>> v = volume.Volume(velocity=128)
    >>> v.cachedRealized
    1.0
    ```

Volume.cachedRealizedStr
:   Convenience property for testing.

    ```python
    >>> v = volume.Volume(velocity=128)
    >>> v.cachedRealizedStr
    '1.0'
    ```

Volume.realized

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Volume`](#music21.volume.Volume "music21.volume.Volume") read/write properties

Volume.velocity
:   Get or set the velocity value, a numerical value between 0 and 127 and
    available setting amplitude on each Note or Pitch in chord.

    ```python
    >>> n = note.Note()
    >>> n.volume.velocity = 20
    >>> n.volume.client == n
    True
    ```

    ```python
    >>> n.volume.velocity
    20
    ```

Volume.velocityScalar
:   Get or set the velocityScalar value, a numerical value between 0
    and 1 and available setting amplitude on each Note or Pitch in
    chord. This value is mapped to the range 0 to 127 on output.

    Note that this value is derived from the set velocity value.
    Floating point error seen here will not be found in the velocity
    value.

    When setting this value, an integer-based velocity value will be
    derived and stored.

    ```python
    >>> n = note.Note()
    >>> n.volume.velocityScalar = 0.5
    >>> n.volume.velocity
    64
    ```

    ```python
    >>> n.volume.velocity = 127
    >>> n.volume.velocityScalar
    1.0
    ```

    If velocity is not set, then this will return None

    ```python
    >>> n = note.Note()
    >>> n.volume.velocityScalar is None
    True
    ```

[`Volume`](#music21.volume.Volume "music21.volume.Volume") methods

Volume.getDynamicContext()[[source]](../_modules/music21/volume.html#Volume.getDynamicContext)
:   Return the dynamic context of this Volume, based on the position of the
    client of this object.

    ```python
    >>> n = note.Note()
    >>> n.volume.velocityScalar = 0.9
    >>> s = stream.Measure([dynamics.Dynamic('ff'), n])
    >>> n.volume.getDynamicContext()
    <music21.dynamics.Dynamic ff>
    ```

Volume.getRealized(*useDynamicContext: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Dynamic](moduleDynamics.html#music21.dynamics.Dynamic "music21.dynamics.Dynamic") = True*, *useVelocity=True*, *useArticulations: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Articulation](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Articulation](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation")] = True*, *baseLevel=0.5*, *clip=True*)[[source]](../_modules/music21/volume.html#Volume.getRealized)
:   Get a realized unit-interval scalar for this Volume. This scalar is to
    be applied to the dynamic range of whatever output is available,
    whatever that may be.

    The baseLevel value is a middle value between 0 and 1 that all
    scalars modify. This also becomes the default value for unspecified
    dynamics. When scalars (between 0 and 1) are used, their values are
    doubled, such that mid-values (around 0.5, which become 1) make no
    change.

    This can optionally take into account dynamicContext, useVelocity,
    and useArticulation.

    If useDynamicContext is True, a context search for a dynamic will be
    done, else dynamics are ignored. Alternatively, the useDynamicContext
    may supply a Dynamic object that will be used instead of a context
    search.

    If useArticulations is True and client is not None, any articulations
    found on that client will be used to adjust the volume. Alternatively,
    the useArticulations parameter may supply an iterable of articulations
    that will be used instead of that available on a client.

    The velocityIsRelative tag determines if the velocity value includes
    contextual values, such as dynamics and accents, or not.

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note('d3', quarterLength=0.5), 8)
    >>> s.insert([0, dynamics.Dynamic('p'),
    ...           1, dynamics.Dynamic('mp'),
    ...           2, dynamics.Dynamic('mf'),
    ...           3, dynamics.Dynamic('f')])
    ```

    ```python
    >>> s.notes[0].volume.getRealized()
    0.496...
    ```

    ```python
    >>> s.notes[1].volume.getRealized()
    0.496...
    ```

    ```python
    >>> s.notes[2].volume.getRealized()
    0.63779...
    ```

    ```python
    >>> s.notes[7].volume.getRealized()
    0.99212...
    ```

    velocity, if set, will be scaled by dynamics:

    ```python
    >>> s.notes[7].volume.velocity = 20
    >>> s.notes[7].volume.getRealized()
    0.22047...
    ```

    Unless we set the velocity to not be relative:

    ```python
    >>> s.notes[7].volume.velocityIsRelative = False
    >>> s.notes[7].volume.getRealized()
    0.1574803...
    ```

Volume.getRealizedStr(*useDynamicContext: [Dynamic](moduleDynamics.html#music21.dynamics.Dynamic "music21.dynamics.Dynamic") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *useVelocity=True*, *useArticulations: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Articulation](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Articulation](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation")] = True*, *baseLevel=0.5*, *clip=True*)[[source]](../_modules/music21/volume.html#Volume.getRealizedStr)
:   Return the realized as rounded and formatted string value. Useful for testing.

    ```python
    >>> v = volume.Volume(velocity=64)
    >>> v.getRealizedStr()
    '0.5'
    ```

Volume.mergeAttributes(*other*)[[source]](../_modules/music21/volume.html#Volume.mergeAttributes)
:   Given another Volume object, gather all attributes except client.
    Values are always copied, not passed by reference.

    ```python
    >>> n1 = note.Note()
    >>> v1 = n1.volume
    >>> v1.velocity = 111
    ```

    ```python
    >>> v2 = volume.Volume()
    >>> v2.mergeAttributes(v1)
    >>> v2.client is None
    True
    >>> v2.velocity
    111
    ```

## Functions

music21.volume.realizeVolume(*srcStream*, *setAbsoluteVelocity=False*, *useDynamicContext=True*, *useVelocity=True*, *useArticulations=True*)[[source]](../_modules/music21/volume.html#realizeVolume)
:   Given a Stream with one level of dynamics
    (e.g., a Part, or two Staffs that share Dynamics),
    destructively modify it to set all realized volume levels.
    These values will be stored in the Volume object as cachedRealized values.

    This is a top-down routine, as opposed to bottom-up values available with
    context searches on Volume. This thus offers a performance benefit.

    This is always done in place.

    If setAbsoluteVelocity is True, the realized values will overwrite all
    existing velocity values, and the Volume objects velocityIsRelative
    parameters will be set to False.
