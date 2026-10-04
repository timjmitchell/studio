Source: https://music21.org/music21docs/moduleReference/moduleMeterCore.html

# music21.meter.core

This module defines two component objects for defining nested metrical structures:
[`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") and [`MeterSequence`](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence").

## MeterSequence

class music21.meter.core.MeterSequence(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *partitionRequest: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/meter/core.html#MeterSequence)
:   A meter sequence is a list of MeterTerminals, or other MeterSequences

[`MeterSequence`](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence") bases

* [`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`MeterSequence`](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence") read-only properties

MeterSequence.depth
:   Return how many unique levels deep this part is
    This should be optimized to store values unless the structure has changed.

MeterSequence.flatWeight
:   Return a list of flat weight values

MeterSequence.partitionDisplay
:   Property – Display the partition as a str without the surrounding curly brackets.

    ```python
    >>> a = meter.MeterSequence('4/4')
    >>> a.partitionDisplay
    '4/4'
    >>> a = meter.MeterSequence('2/4+6/8')
    >>> a.partitionDisplay
    '2/4+6/8'
    ```

    partitionDisplay is most useful for non-divided meter sequences. This is less helpful:

    ```python
    >>> a = meter.MeterSequence('4/4', 4)
    >>> a.partitionDisplay
    '1/4+1/4+1/4+1/4'
    ```

MeterSequence.partitionStr
:   Return the number of top-level partitions in this MeterSequence as a string.

    ```python
    >>> ms = meter.MeterSequence('2/4+2/4')
    >>> ms
    <music21.meter.core.MeterSequence {2/4+2/4}>
    >>> ms.partitionStr
    'Duple'
    ```

    ```python
    >>> ms = meter.MeterSequence('6/4', 6)
    >>> ms
    <music21.meter.core.MeterSequence {1/4+1/4+1/4+1/4+1/4+1/4}>
    >>> ms.partitionStr
    'Sextuple'
    ```

    ```python
    >>> ms = meter.MeterSequence('6/4', 2)
    >>> ms.partitionStr
    'Duple'
    ```

    ```python
    >>> ms = meter.MeterSequence('6/4', 3)
    >>> ms.partitionStr
    'Triple'
    ```

    Anything larger than 8 is simply the number followed by ‘-uple’

    ```python
    >>> ms = meter.MeterSequence('13/4', 13)
    >>> ms.partitionStr
    '13-uple'
    ```

    Single partition:

    ```python
    >>> ms = meter.MeterSequence('3/4', 1)
    >>> ms.partitionStr
    'Single'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MeterSequence`](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence") read/write properties

MeterSequence.weight
:   Get the weight for the MeterSequence, or set the weight and thereby change the weights
    for each object in this MeterSequence.

    By default, all the partitions of a MeterSequence’s weights sum to 1.0

    ```python
    >>> a = meter.MeterSequence('3/4')
    >>> a.weight
    1.0
    >>> a.partition(3)
    >>> a
    <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
    >>> a.weight
    1.0
    >>> a[0].weight
    0.3333...
    ```

    But this MeterSequence might be embedded in another one, so perhaps
    its weight should be 0.5?

    ```python
    >>> a.weight = 0.5
    >>> a[0].weight
    0.16666...
    ```

    When creating a new MeterSequence from MeterTerminals, the sequence has
    the weight of the sum of those creating it.

    ```python
    >>> downbeat = meter.MeterTerminal('1/4', 0.5)
    >>> upbeat = meter.MeterTerminal('1/4', 0.25)
    >>> accentSequence = meter.MeterSequence([downbeat, upbeat])
    >>> accentSequence.weight
    0.75
    ```

    Changing the weight of the child sequence will affect the parent, since this is
    not cached, but recomputed on each call.

    ```python
    >>> downbeat.weight = 0.375
    >>> accentSequence.weight
    0.625
    ```

    Changing the weight on the parent sequence will reset weights on the children

    ```python
    >>> accentSequence.weight = 1.0
    >>> (downbeat.weight, upbeat.weight)
    (0.5, 0.5)
    ```

    Assume this MeterSequence is a whole, not a part of some larger MeterSequence.
    Thus, we cannot use numerator/denominator relationship
    as a scalar.

Read/write properties inherited from [`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal"):

|  |  |  |
| --- | --- | --- |
| * [`denominator`](#music21.meter.core.MeterTerminal.denominator "music21.meter.core.MeterTerminal.denominator") | * [`duration`](#music21.meter.core.MeterTerminal.duration "music21.meter.core.MeterTerminal.duration") | * [`numerator`](#music21.meter.core.MeterTerminal.numerator "music21.meter.core.MeterTerminal.numerator") |

[`MeterSequence`](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence") methods

MeterSequence.\_\_getitem\_\_(*key: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")[[source]](../_modules/music21/meter/core.html#MeterSequence.__getitem__)
:   Get an MeterTerminal (or MeterSequence) from \_partition

    ```python
    >>> a = meter.MeterSequence('4/4', 4)
    >>> a[3].numerator
    1
    ```

MeterSequence.flatten() → [MeterSequence](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence")[[source]](../_modules/music21/meter/core.html#MeterSequence.flatten)
:   Return a new MeterSequence composed of the flattened representation.

    Here a sequence is already flattened:

    ```python
    >>> ms = meter.MeterSequence('3/4', 3)
    >>> ms
    <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
    >>> b = ms.flatten()
    >>> b
    <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
    >>> len(b)
    3
    >>> b is ms
    False
    ```

    Now take the original MeterSequence and subdivide the second beat into 4 parts:

    ```python
    >>> ms[1] = ms[1].subdivide(4)
    >>> ms
    <music21.meter.core.MeterSequence {1/4+{1/16+1/16+1/16+1/16}+1/4}>
    >>> b = ms.flatten()
    >>> len(b)
    6
    >>> b
    <music21.meter.core.MeterSequence {1/4+1/16+1/16+1/16+1/16+1/4}>
    ```

    ```python
    >>> ms[1][2] = ms[1][2].subdivide(4)
    >>> ms
    <music21.meter.core.MeterSequence {1/4+{1/16+1/16+{1/64+1/64+1/64+1/64}+1/16}+1/4}>
    >>> b = ms.flatten()
    >>> len(b)
    9
    >>> b
    <music21.meter.core.MeterSequence {1/4+1/16+1/16+1/64+1/64+1/64+1/64+1/16+1/4}>
    ```

MeterSequence.getLevel(*level=0*, *flat=True*)[[source]](../_modules/music21/meter/core.html#MeterSequence.getLevel)
:   Return a complete MeterSequence with the same numerator/denominator
    relationship but that represents any partitions found at the requested
    level. A sort of flatness with variable depth.

    ```python
    >>> b = meter.MeterSequence('4/4', 4)
    >>> b[1] = b[1].subdivide(2)
    >>> b[3] = b[3].subdivide(2)
    >>> b[3][0] = b[3][0].subdivide(2)
    >>> b
    <music21.meter.core.MeterSequence {1/4+{1/8+1/8}+1/4+{{1/16+1/16}+1/8}}>
    >>> b.getLevel(0)
    <music21.meter.core.MeterSequence {1/4+1/4+1/4+1/4}>
    >>> b.getLevel(1)
    <music21.meter.core.MeterSequence {1/4+1/8+1/8+1/4+1/8+1/8}>
    >>> b.getLevel(2)
    <music21.meter.core.MeterSequence {1/4+1/8+1/8+1/4+1/16+1/16+1/8}>
    ```

MeterSequence.getLevelList(*levelCount: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")][[source]](../_modules/music21/meter/core.html#MeterSequence.getLevelList)
:   Recursive utility function that gets everything at a certain level.

    If flat is True, it guarantees to return a list of MeterTerminals and not
    MeterSequences. Otherwise, there may be Sequences in there.

    Example: a Sequence representing something in 4/4 divided as
    1 quarter, 2 eighth, 1 quarter, ((2-sixteenths) + 1 eighth).

    ```python
    >>> b = meter.MeterSequence('4/4', 4)
    >>> b[1] = b[1].subdivide(2)
    >>> b[3] = b[3].subdivide(2)
    >>> b[3][0] = b[3][0].subdivide(2)
    >>> b
    <music21.meter.core.MeterSequence {1/4+{1/8+1/8}+1/4+{{1/16+1/16}+1/8}}>
    ```

    Get the top level of this structure, flattening everything underneath:

    ```python
    >>> b.getLevelList(0)
    [<music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterTerminal 1/4>]
    ```

    One level down:

    ```python
    >>> b.getLevelList(1)
    [<music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterTerminal 1/8>,
     <music21.meter.core.MeterTerminal 1/8>,
     <music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterTerminal 1/8>,
     <music21.meter.core.MeterTerminal 1/8>]
    ```

    Without flattening, first two levels:

    ```python
    >>> b.getLevelList(0, flat=False)
    [<music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterSequence {1/8+1/8}>,
     <music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterSequence {{1/16+1/16}+1/8}>]
    ```

    (Note that levelList 0, flat=False is essentially the same as iterating
    over a MeterSequence)

    ```python
    >>> list(b)
    [<music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterSequence {1/8+1/8}>,
     <music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterSequence {{1/16+1/16}+1/8}>]
    ```

    ```python
    >>> b.getLevelList(1, flat=False)
    [<music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterTerminal 1/8>,
     <music21.meter.core.MeterTerminal 1/8>,
     <music21.meter.core.MeterTerminal 1/4>,
     <music21.meter.core.MeterSequence {1/16+1/16}>,
     <music21.meter.core.MeterTerminal 1/8>]
    ```

    Generally, these level lists will be converted back to MeterSequences:

    ```python
    >>> meter.MeterSequence(b.getLevelList(0))
    <music21.meter.core.MeterSequence {1/4+1/4+1/4+1/4}>
    >>> meter.MeterSequence(b.getLevelList(1))
    <music21.meter.core.MeterSequence {1/4+1/8+1/8+1/4+1/8+1/8}>
    >>> meter.MeterSequence(b.getLevelList(2))
    <music21.meter.core.MeterSequence {1/4+1/8+1/8+1/4+1/16+1/16+1/8}>
    >>> meter.MeterSequence(b.getLevelList(3))
    <music21.meter.core.MeterSequence {1/4+1/8+1/8+1/4+1/16+1/16+1/8}>
    ```

MeterSequence.getLevelSpan(*level=0*)[[source]](../_modules/music21/meter/core.html#MeterSequence.getLevelSpan)
:   For a given level, return the time span of each terminal or sequence

    ```python
    >>> b = meter.MeterSequence('4/4', 4)
    >>> b[1] = b[1].subdivide(2)
    >>> b[3] = b[3].subdivide(2)
    >>> b[3][0] = b[3][0].subdivide(2)
    >>> b
    <music21.meter.core.MeterSequence {1/4+{1/8+1/8}+1/4+{{1/16+1/16}+1/8}}>
    >>> b.getLevelSpan(0)
    [(0.0, 1.0), (1.0, 2.0), (2.0, 3.0), (3.0, 4.0)]
    >>> b.getLevelSpan(1)
    [(0.0, 1.0), (1.0, 1.5), (1.5, 2.0), (2.0, 3.0), (3.0, 3.5), (3.5, 4.0)]
    >>> b.getLevelSpan(2)
    [(0.0, 1.0), (1.0, 1.5), (1.5, 2.0), (2.0, 3.0), (3.0, 3.25), (3.25, 3.5), (3.5, 4.0)]
    ```

MeterSequence.getLevelWeight(*level=0*)[[source]](../_modules/music21/meter/core.html#MeterSequence.getLevelWeight)
:   The weightList is an array of weights found in the components.
    The MeterSequence has a .\_weight attribute, but it is not used here

    ```python
    >>> a = meter.MeterSequence('4/4', 4)
    >>> a.getLevelWeight()
    [0.25, 0.25, 0.25, 0.25]
    ```

    ```python
    >>> b = meter.MeterSequence('4/4', 4)
    >>> b.getLevelWeight(0)
    [0.25, 0.25, 0.25, 0.25]
    ```

    ```python
    >>> b[1] = b[1].subdivide(2)
    >>> b[3] = b[3].subdivide(2)
    >>> b.getLevelWeight(0)
    [0.25, 0.25, 0.25, 0.25]
    ```

    ```python
    >>> b[3][0] = b[3][0].subdivide(2)
    >>> b
    <music21.meter.core.MeterSequence {1/4+{1/8+1/8}+1/4+{{1/16+1/16}+1/8}}>
    >>> b.getLevelWeight(0)
    [0.25, 0.25, 0.25, 0.25]
    >>> b.getLevelWeight(1)
    [0.25, 0.125, 0.125, 0.25, 0.125, 0.125]
    >>> b.getLevelWeight(2)
    [0.25, 0.125, 0.125, 0.25, 0.0625, 0.0625, 0.125]
    ```

MeterSequence.getPartitionOptions() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...], ...][[source]](../_modules/music21/meter/core.html#MeterSequence.getPartitionOptions)
:   Return either a cached or a new set of division/partition options.

    Calls tools.divisionOptionsAlgo and tools.divisionOptionsPreset
    (which will be empty except if the numerator is 5).

    Works on anything that has a .numerator and .denominator.

    ```python
    >>> meter.MeterSequence('3/4').getPartitionOptions()
    (('1/4', '1/4', '1/4'),
     ('1/8', '1/8', '1/8', '1/8', '1/8', '1/8'),
     ('1/16', '1/16', '1/16', '1/16', '1/16', '1/16', '1/16',
      '1/16', '1/16', '1/16', '1/16', '1/16'),
     ('3/4',), ('6/8',), ('12/16',), ('24/32',), ('48/64',), ('96/128',))
    ```

    The additional 2 + 2 + 1 and 2 + 1 + 2 options for numerator 5 are at the end.

    ```python
    >>> meter.MeterSequence('5/32').getPartitionOptions()
    (('2/32', '3/32'),
     ('3/32', '2/32'),
     ('1/32', '1/32', '1/32', '1/32', '1/32'),
     ('1/64', '1/64', '1/64', '1/64', '1/64',
      '1/64', '1/64', '1/64', '1/64', '1/64'),
     ('5/32',), ('10/64',), ('20/128',),
     ('2/32', '2/32', '1/32'), ('2/32', '1/32', '2/32'))
    ```

MeterSequence.isUniformPartition(*\**, *depth=0*)[[source]](../_modules/music21/meter/core.html#MeterSequence.isUniformPartition)
:   Return True if the top-level partitions (if depth=0)
    or a lower-level section has equal durations

    ```python
    >>> ms = meter.MeterSequence('3/8+2/8+3/4')
    >>> ms.isUniformPartition()
    False
    >>> ms = meter.MeterSequence('4/4')
    >>> ms.isUniformPartition()
    True
    >>> ms.partition(4)
    >>> ms.isUniformPartition()
    True
    >>> ms[0] = ms[0].subdivideByCount(2)
    >>> ms[1] = ms[1].subdivideByCount(4)
    >>> ms.isUniformPartition()
    True
    >>> ms.isUniformPartition(depth=1)
    False
    ```

    ```python
    >>> ms = meter.MeterSequence('2/4+2/4')
    >>> ms.isUniformPartition()
    True
    ```

    ```python
    >>> ms = meter.MeterSequence('5/8', 5)
    >>> ms.isUniformPartition()
    True
    >>> ms.partition(2)
    >>> ms.isUniformPartition()
    False
    ```

    * Changed in v7: depth is keyword only

MeterSequence.load(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *partitionRequest: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [MeterSequence](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *autoWeight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *targetWeight: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/meter/core.html#MeterSequence.load)
:   This method is called when a MeterSequence is created, or if a MeterSequence is re-set.

    User can enter a list of values or an abbreviated slash notation.

    autoWeight, if True, will attempt to set weights.
    targetWeight, if given, will be used instead of self.weight

    loading is a destructive operation.

    ```python
    >>> a = meter.MeterSequence()
    >>> a.load('4/4', 4)
    >>> a
    <music21.meter.core.MeterSequence {1/4+1/4+1/4+1/4}>
    >>> str(a)
    '{1/4+1/4+1/4+1/4}'
    ```

    ```python
    >>> a.load('4/4', 2)  # request 2 beats
    >>> a
    <music21.meter.core.MeterSequence {1/2+1/2}>
    >>> str(a)
    '{1/2+1/2}'
    ```

    ```python
    >>> a.load('5/8', 2)  # request 2 beats
    >>> str(a)
    '{2/8+3/8}'
    ```

    ```python
    >>> a.load('5/8+4/4')
    >>> str(a)
    '{5/8+4/4}'
    ```

MeterSequence.offsetToAddress(*qLenPos*, *includeCoincidentBoundaries=False*)[[source]](../_modules/music21/meter/core.html#MeterSequence.offsetToAddress)
:   Give a list of values that show all indices necessary to access
    the exact terminal at a given qLenPos.

    The len of the returned list also provides the depth at the specified qLen.

    ```python
    >>> a = meter.MeterSequence('3/4', 3)
    >>> a[1] = a[1].subdivide(4)
    >>> a
    <music21.meter.core.MeterSequence {1/4+{1/16+1/16+1/16+1/16}+1/4}>
    >>> len(a)
    3
    >>> a.offsetToAddress(0.5)
    [0]
    >>> a[0]
    <music21.meter.core.MeterTerminal 1/4>
    >>> a.offsetToAddress(1.0)
    [1, 0]
    >>> a.offsetToAddress(1.5)
    [1, 2]
    >>> a[1][2]
    <music21.meter.core.MeterTerminal 1/16>
    >>> a.offsetToAddress(1.99)
    [1, 3]
    >>> a.offsetToAddress(2.5)
    [2]
    ```

MeterSequence.offsetToDepth(*qLenPos*, *align='quantize'*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/meter/core.html#MeterSequence.offsetToDepth)
:   Given a qLenPos, return the maximum available depth at this position.

    ```python
    >>> b = meter.MeterSequence('4/4', 4)
    >>> b[1] = b[1].subdivide(2)
    >>> b[3] = b[3].subdivide(2)
    >>> b[3][0] = b[3][0].subdivide(2)
    >>> b
    <music21.meter.core.MeterSequence {1/4+{1/8+1/8}+1/4+{{1/16+1/16}+1/8}}>
    >>> b.offsetToDepth(0)
    3
    >>> b.offsetToDepth(0.25)  # quantizing active by default
    3
    >>> b.offsetToDepth(1)
    3
    >>> b.offsetToDepth(1.5)
    2
    ```

    ```python
    >>> b.offsetToDepth(-1)
    Traceback (most recent call last):
    music21.exceptions21.MeterException: cannot access from qLenPos -1.0
    ```

    * Changed in v7: index can be provided, if known, for a long
      MeterSequence to improve performance.

MeterSequence.offsetToIndex(*qLenPos*, *includeCoincidentBoundaries=False*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/meter/core.html#MeterSequence.offsetToIndex)
:   Given an offset in quarterLengths (0.0 through self.duration.quarterLength), return
    the index of the active MeterTerminal or MeterSequence

    ```python
    >>> a = meter.MeterSequence('4/4')
    >>> a.offsetToIndex(0.5)
    0
    >>> a.offsetToIndex(3.5)
    0
    >>> a.partition(4)
    >>> a.offsetToIndex(0.5)
    0
    >>> a.offsetToIndex(3.5)
    3
    ```

    ```python
    >>> a.partition([1, 2, 1])
    >>> len(a)
    3
    >>> a.offsetToIndex(2.9)
    1
    >>> a[a.offsetToIndex(2.9)]
    <music21.meter.core.MeterTerminal 2/4>
    ```

    ```python
    >>> a = meter.MeterSequence('4/4')
    >>> a.offsetToIndex(5.0)
    Traceback (most recent call last):
    music21.exceptions21.MeterException: cannot access from qLenPos 5.0
        where total duration is 4.0
    ```

    Negative numbers also raise an exception:

    ```python
    >>> a.offsetToIndex(-0.5)
    Traceback (most recent call last):
    music21.exceptions21.MeterException: cannot access from qLenPos -0.5
        where total duration is 4.0
    ```

MeterSequence.offsetToSpan(*qLenPos*, *permitMeterModulus=False*)[[source]](../_modules/music21/meter/core.html#MeterSequence.offsetToSpan)
:   Given a qLenPos, return the span of the active region.
    Only applies to the top most level of partitions

    If permitMeterModulus is True, quarter length positions
    greater than the duration of the Meter will be accepted
    as the modulus of the total meter duration.

    ```python
    >>> a = meter.MeterSequence('3/4', 3)
    >>> a.offsetToSpan(0.5)
    (0, 1.0)
    >>> a.offsetToSpan(1.5)
    (1.0, 2.0)
    ```

    This is the same as 1.5:

    ```python
    >>> a.offsetToSpan(4.5, permitMeterModulus=True)
    (1.0, 2.0)
    ```

    Make sure it works for tuplets even with so-so rounding:

    ```python
    >>> a.offsetToSpan(4.33333336, permitMeterModulus=True)
    (1.0, 2.0)
    ```

MeterSequence.offsetToWeight(*qLenPos*)[[source]](../_modules/music21/meter/core.html#MeterSequence.offsetToWeight)
:   Given a lenPos, return the weight of the active region.
    Only applies to the top-most level of partitions

    ```python
    >>> a = meter.MeterSequence('3/4', 3)
    >>> a.offsetToWeight(0.0)
    Fraction(1, 3)
    >>> a.offsetToWeight(1.5)
    Fraction(1, 3)
    ```

MeterSequence.partition(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[MeterTerminal](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [MeterSequence](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence")*, *loadDefault=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/core.html#MeterSequence.partition)
:   Partitioning creates and sets a number of MeterTerminals
    that make up this MeterSequence.

    A simple way to partition based on argument time. Single integers
    are treated as beat counts; lists are treated as numerator lists;
    MeterSequence objects are partitioned by calling partitionByOtherMeterSequence().

    ```python
    >>> a = meter.MeterSequence('5/4+3/8')
    >>> len(a)
    2
    >>> str(a)
    '{5/4+3/8}'
    ```

    ```python
    >>> b = meter.MeterSequence('13/8')
    >>> len(b)
    1
    >>> str(b)
    '{13/8}'
    >>> b.partition(13)
    >>> len(b)
    13
    >>> str(b)
    '{1/8+1/8+1/8+...+1/8}'
    ```

    ```python
    >>> a.partition(b)
    >>> len(a)
    13
    >>> str(a)
    '{1/8+1/8+1/8+...+1/8}'
    ```

    Demo of loadDefault: if impossible, then do it another way:

    ```python
    >>> c = meter.MeterSequence('3/128')
    >>> c.partition(2)
    Traceback (most recent call last):
    music21.exceptions21.MeterException: Cannot set partition by 2 (3/128)
    ```

    ```python
    >>> c = meter.MeterSequence('3/128')
    >>> c.partition(2, loadDefault=True)
    >>> len(c)
    3
    >>> str(c)
    '{1/128+1/128+1/128}'
    ```

    * Changed in v9.3: if given a list it must either be all numbers, all strings,
      or all MeterTerminals, not a mix (which was undocumented and buggy)

MeterSequence.partitionByCount(*countRequest: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loadDefault: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/core.html#MeterSequence.partitionByCount)
:   Divide the current MeterSequence into the requested number of parts.

    If it is not possible to divide it into the requested number, and
    loadDefault is True, then give the default partition:

    This will destroy any established structure in the stored partition.

    ```python
    >>> a = meter.MeterSequence('4/4')
    >>> a
    <music21.meter.core.MeterSequence {4/4}>
    >>> a.partitionByCount(2)
    >>> a
    <music21.meter.core.MeterSequence {1/2+1/2}>
    >>> str(a)
    '{1/2+1/2}'
    >>> a.partitionByCount(4)
    >>> a
    <music21.meter.core.MeterSequence {1/4+1/4+1/4+1/4}>
    >>> str(a)
    '{1/4+1/4+1/4+1/4}'
    ```

    The partitions are not guaranteed to be the same length if the
    meter is irregular:

    ```python
    >>> b = meter.MeterSequence('5/8')
    >>> b.partitionByCount(2)
    >>> b
     <music21.meter.core.MeterSequence {2/8+3/8}>
    ```

    This relies on a pre-defined exemption for partitioning 5 by 3:

    ```python
    >>> b.partitionByCount(3)
    >>> str(b)
    '{2/8+2/8+1/8}'
    ```

    Here we use loadDefault=True to get the default partition in case
    there is no known way to do this:

    ```python
    >>> a = meter.MeterSequence('5/8')
    >>> a.partitionByCount(11)
    >>> str(a)
    '{2/8+3/8}'
    ```

    If loadDefault is False then an error is raised:

    ```python
    >>> a.partitionByCount(11, loadDefault=False)
    Traceback (most recent call last):
    music21.exceptions21.MeterException: Cannot set partition by 11 (5/8)
    ```

MeterSequence.partitionByList(*numeratorList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/core.html#MeterSequence.partitionByList)
:   Given a numerator list, partition MeterSequence into a new list
    of MeterTerminals

    ```python
    >>> a = meter.MeterSequence('4/4')
    >>> a.partitionByList([1, 1, 1, 1])
    >>> str(a)
    '{1/4+1/4+1/4+1/4}'
    ```

    This divides it into two equal parts:

    ```python
    >>> a.partitionByList([1, 1])
    >>> str(a)
    '{1/2+1/2}'
    ```

    And now into one big part:

    ```python
    >>> a.partitionByList([1])
    >>> str(a)
    '{1/1}'
    ```

    Here we divide 4/4 very unconventionally:

    ```python
    >>> a.partitionByList(['3/4', '1/8', '1/8'])
    >>> a
    <music21.meter.core.MeterSequence {3/4+1/8+1/8}>
    ```

    But the basics of the MeterSequence must be observed:

    ```python
    >>> a.partitionByList(['3/4', '1/8', '5/8'])
    Traceback (most recent call last):
    music21.exceptions21.MeterException: Cannot set partition by ['3/4', '1/8', '5/8']
    ```

MeterSequence.partitionByOtherMeterSequence(*other: [MeterSequence](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/core.html#MeterSequence.partitionByOtherMeterSequence)
:   Set partition to that found in another
    MeterSequence.

    ```python
    >>> a = meter.MeterSequence('4/4', 4)
    >>> str(a)
    '{1/4+1/4+1/4+1/4}'
    ```

    ```python
    >>> b = meter.MeterSequence('4/4', 2)
    >>> a.partitionByOtherMeterSequence(b)
    >>> len(a)
    2
    >>> str(a)
    '{1/2+1/2}'
    ```

MeterSequence.setLevelWeight(*weightList*, *level=0*)[[source]](../_modules/music21/meter/core.html#MeterSequence.setLevelWeight)
:   The weightList is an array of weights to be applied to a
    single level of the MeterSequence.

    ```python
    >>> a = meter.MeterSequence('4/4', 4)
    >>> a.setLevelWeight([1, 2, 3, 4])
    >>> a.getLevelWeight()
    [1, 2, 3, 4]
    ```

    ```python
    >>> b = meter.MeterSequence('4/4', 4)
    >>> b.setLevelWeight([2, 3])
    >>> b.getLevelWeight(0)
    [2, 3, 2, 3]
    ```

    ```python
    >>> b[1] = b[1].subdivide(2)
    >>> b[3] = b[3].subdivide(2)
    >>> b.getLevelWeight(0)
    [2, 3.0, 2, 3.0]
    ```

    ```python
    >>> b[3][0] = b[3][0].subdivide(2)
    >>> b
    <music21.meter.core.MeterSequence {1/4+{1/8+1/8}+1/4+{{1/16+1/16}+1/8}}>
    >>> b.getLevelWeight(0)
    [2, 3.0, 2, 3.0]
    >>> b.getLevelWeight(1)
    [2, 1.5, 1.5, 2, 1.5, 1.5]
    >>> b.getLevelWeight(2)
    [2, 1.5, 1.5, 2, 0.75, 0.75, 1.5]
    ```

MeterSequence.subdivideNestedHierarchy(*depth*, *firstPartitionForm=None*, *normalizeDenominators=True*)[[source]](../_modules/music21/meter/core.html#MeterSequence.subdivideNestedHierarchy)
:   Create nested structure down to a specified depth;
    the first division is set to one; the second division
    may be by 2 or 3; remaining divisions are always by 2.

    This a destructive procedure that will remove
    any existing partition structures.

    normalizeDenominators, if True, will reduce all denominators to the same minimum level.

    ```python
    >>> ms = meter.MeterSequence('4/4')
    >>> ms.subdivideNestedHierarchy(1)
    >>> ms
    <music21.meter.core.MeterSequence {{1/2+1/2}}>
    >>> ms.subdivideNestedHierarchy(2)
    >>> ms
    <music21.meter.core.MeterSequence {{{1/4+1/4}+{1/4+1/4}}}>
    >>> ms.subdivideNestedHierarchy(3)
    >>> ms
    <music21.meter.core.MeterSequence {{{{1/8+1/8}+{1/8+1/8}}+{{1/8+1/8}+{1/8+1/8}}}}>
    ```

    I think you get the picture!

    The effects above are not cumulative. Users can skip directly to
    whatever level of hierarchy they want.

    ```python
    >>> ms2 = meter.MeterSequence('4/4')
    >>> ms2.subdivideNestedHierarchy(3)
    >>> ms2
    <music21.meter.core.MeterSequence {{{{1/8+1/8}+{1/8+1/8}}+{{1/8+1/8}+{1/8+1/8}}}}>
    ```

MeterSequence.subdividePartitionsEqual(*divisions: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/meter/core.html#MeterSequence.subdividePartitionsEqual)
:   Subdivide all partitions by equally-spaced divisions,
    given a divisions value. Manipulates this MeterSequence in place.

    Divisions value may optionally be a MeterSequence,
    from which a top-level partitioning structure is derived.

    Example: First we will do a normal partition (not subdivided partition)

    ```python
    >>> ms = meter.MeterSequence('2/4')
    >>> ms
    <music21.meter.core.MeterSequence {2/4}>
    >>> len(ms)
    1
    >>> ms[0]
    <music21.meter.core.MeterTerminal 2/4>
    >>> len(ms[0])
    Traceback (most recent call last):
    TypeError: object of type 'MeterTerminal' has no len()
    ```

    Divide the Sequence into two parts, so now there are two
    MeterTerminals of 1/4 each:

    ```python
    >>> ms.partition(2)
    >>> ms
    <music21.meter.core.MeterSequence {1/4+1/4}>
    >>> len(ms)
    2
    >>> ms[0]
    <music21.meter.core.MeterTerminal 1/4>
    >>> ms[1]
    <music21.meter.core.MeterTerminal 1/4>
    ```

    But what happens if we want to divide each of those into 1/8+1/8 are replace
    them by MeterSequences? subdividePartitionsEqual is what is needed.

    ```python
    >>> ms.subdividePartitionsEqual(2)
    >>> ms
    <music21.meter.core.MeterSequence {{1/8+1/8}+{1/8+1/8}}>
    ```

    Length is still 2, but each of the components are now MeterSequences of their
    own:

    ```python
    >>> len(ms)
    2
    >>> ms[0]
    <music21.meter.core.MeterSequence {1/8+1/8}>
    >>> ms[1]
    <music21.meter.core.MeterSequence {1/8+1/8}>
    ```

    There is not a way (the authors know of) to get to the next level.
    You would just need to do them individually.

    ```python
    >>> ms[0].subdividePartitionsEqual(2)
    >>> ms
    <music21.meter.core.MeterSequence {{{1/16+1/16}+{1/16+1/16}}+{1/8+1/8}}>
    >>> ms[1].subdividePartitionsEqual(2)
    >>> ms
    <music21.meter.core.MeterSequence {{{1/16+1/16}+{1/16+1/16}}+{{1/16+1/16}+{1/16+1/16}}}>
    ```

    If None is given as a parameter, then it will try to find something logical.

    ```python
    >>> ms = meter.MeterSequence('2/4+3/4')
    >>> ms.subdividePartitionsEqual(None)
    >>> ms
    <music21.meter.core.MeterSequence {{1/4+1/4}+{1/4+1/4+1/4}}>
    ```

    If any partition cannot be divided by the given count, a MeterException is raised:

    ```python
    >>> ms = meter.MeterSequence('5/8+3/8')
    >>> len(ms)
    2
    >>> ms.subdividePartitionsEqual(5)
    Traceback (most recent call last):
    music21.exceptions21.MeterException: Cannot set partition by 5 (3/8)
    ```

Methods inherited from [`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal"):

|  |  |  |
| --- | --- | --- |
| * [`ratioEqual()`](#music21.meter.core.MeterTerminal.ratioEqual "music21.meter.core.MeterTerminal.ratioEqual") * [`subdivide()`](#music21.meter.core.MeterTerminal.subdivide "music21.meter.core.MeterTerminal.subdivide") | * [`subdivideByCount()`](#music21.meter.core.MeterTerminal.subdivideByCount "music21.meter.core.MeterTerminal.subdivideByCount") * [`subdivideByList()`](#music21.meter.core.MeterTerminal.subdivideByList "music21.meter.core.MeterTerminal.subdivideByList") | * [`subdivideByOther()`](#music21.meter.core.MeterTerminal.subdivideByOther "music21.meter.core.MeterTerminal.subdivideByOther") |

## MeterTerminal

class music21.meter.core.MeterTerminal(*slashNotation: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *weight: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 1*)[[source]](../_modules/music21/meter/core.html#MeterTerminal)
:   A MeterTerminal is a nestable primitive of rhythmic division.

    ```python
    >>> a = meter.MeterTerminal('2/4')
    >>> a.duration.quarterLength
    2.0
    >>> a = meter.MeterTerminal('3/8')
    >>> a.duration.quarterLength
    1.5
    >>> a = meter.MeterTerminal('5/2')
    >>> a.duration.quarterLength
    10.0
    ```

[`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") read-only properties

MeterTerminal.depth
:   Return how many levels deep this part is – the depth of a terminal is always 1

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") read/write properties

MeterTerminal.denominator
:   Get or set the denominator of the meter terminal

    ```python
    >>> a = meter.MeterTerminal('2/4')
    >>> a.denominator
    4
    >>> a.duration.quarterLength
    2.0
    >>> a.denominator = 8
    >>> a.duration.quarterLength
    1.0
    ```

    ```python
    >>> a.denominator = 7
    Traceback (most recent call last):
    music21.exceptions21.MeterException: bad denominator value: 7
    ```

MeterTerminal.duration
:   duration gets or sets a duration value that
    is equal in length of the terminal.

    ```python
    >>> a = meter.MeterTerminal()
    >>> a.numerator = 3
    >>> a.denominator = 8
    >>> d = a.duration
    >>> d.type
    'quarter'
    >>> d.dots
    1
    >>> d.quarterLength
    1.5
    ```

MeterTerminal.numerator
:   Return or set the numerator of the MeterTerminal

    ```python
    >>> a = meter.MeterTerminal('2/4')
    >>> a.numerator
    2
    >>> a.duration.quarterLength
    2.0
    >>> a.numerator = 11
    >>> a.duration.quarterLength
    11.0
    ```

MeterTerminal.weight
:   Return or set the weight of a MeterTerminal

    ```python
    >>> a = meter.MeterTerminal('2/4')
    >>> a.weight = 0.5
    >>> a.weight
    0.5
    ```

[`MeterTerminal`](#music21.meter.core.MeterTerminal "music21.meter.core.MeterTerminal") methods

MeterTerminal.ratioEqual(*other*)[[source]](../_modules/music21/meter/core.html#MeterTerminal.ratioEqual)
:   Compare the numerator and denominator of another object.
    Note that these have to be exact matches; 3/4 is not the same as 6/8

    ```python
    >>> a = meter.MeterTerminal('3/4')
    >>> b = meter.MeterTerminal('6/4')
    >>> c = meter.MeterTerminal('2/4')
    >>> d = meter.MeterTerminal('3/4')
    >>> a.ratioEqual(b)
    False
    >>> a.ratioEqual(c)
    False
    >>> a.ratioEqual(d)
    True
    ```

MeterTerminal.subdivide(*value: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [MeterSequence](#music21.meter.core.MeterSequence "music21.meter.core.MeterSequence") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](../_modules/music21/meter/core.html#MeterTerminal.subdivide)
:   Subdivision takes a MeterTerminal and, making it into a collection of MeterTerminals,
    Returns a MeterSequence.

    This is different from partitioning a MeterSequence. subdivide does not happen
    in place and instead returns a new object.

    If an integer is provided, assume it is a partition count.

MeterTerminal.subdivideByCount(*countRequest=None*)[[source]](../_modules/music21/meter/core.html#MeterTerminal.subdivideByCount)
:   returns a MeterSequence made up of taking this MeterTerminal and
    subdividing it into the given number of parts. Each of those parts
    is a MeterTerminal

    ```python
    >>> a = meter.MeterTerminal('3/4')
    >>> b = a.subdivideByCount(3)
    >>> b
    <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
    >>> len(b)
    3
    >>> b[0]
    <music21.meter.core.MeterTerminal 1/4>
    ```

    What happens if we do this?

    ```python
    >>> a = meter.MeterTerminal('5/8')
    >>> b = a.subdivideByCount(2)
    >>> b
    <music21.meter.core.MeterSequence {2/8+3/8}>
    >>> len(b)
    2
    >>> b[0]
    <music21.meter.core.MeterTerminal 2/8>
    >>> b[1]
    <music21.meter.core.MeterTerminal 3/8>
    ```

    But what if you want to divide into 3/8+2/8 or something else?
    for that, see the `load()` method
    of `MeterSequence`.

MeterTerminal.subdivideByList(*numeratorList*)[[source]](../_modules/music21/meter/core.html#MeterTerminal.subdivideByList)
:   Return a MeterSequence dividing this
    MeterTerminal according to the numeratorList

    ```python
    >>> a = meter.MeterTerminal('3/4')
    >>> b = a.subdivideByList([1, 1, 1])
    >>> b
    <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
    >>> len(b)
    3
    >>> b[0]
    <music21.meter.core.MeterTerminal 1/4>
    ```

    Unequal subdivisions work:

    ```python
    >>> c = a.subdivideByList([1, 2])
    >>> c
    <music21.meter.core.MeterSequence {1/4+2/4}>
    >>> len(c)
    2
    >>> (c[0], c[1])
    (<music21.meter.core.MeterTerminal 1/4>, <music21.meter.core.MeterTerminal 2/4>)
    ```

    So does subdividing by strings

    ```python
    >>> c = a.subdivideByList(['2/4', '1/4'])
    >>> len(c)
    2
    >>> (c[0], c[1])
    (<music21.meter.core.MeterTerminal 2/4>, <music21.meter.core.MeterTerminal 1/4>)
    ```

    See `partitionByList()` method
    of `MeterSequence` for more details.

MeterTerminal.subdivideByOther(*other: music21.meter.MeterSequence*)[[source]](../_modules/music21/meter/core.html#MeterTerminal.subdivideByOther)
:   Return a MeterSequence based on another MeterSequence

    ```python
    >>> a = meter.MeterSequence('1/4+1/4+1/4')
    >>> a
    <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
    >>> b = meter.MeterSequence('3/8+3/8')
    >>> a.subdivideByOther(b)
    <music21.meter.core.MeterSequence {{3/8+3/8}}>
    ```

    ```python
    >>> terminal = meter.MeterTerminal('1/4')
    >>> divider = meter.MeterSequence('1/8+1/8')
    >>> terminal.subdivideByOther(divider)
    <music21.meter.core.MeterSequence {{1/8+1/8}}>
    ```
