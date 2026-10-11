Source: https://music21.org/music21docs/moduleReference/moduleSieve.html

# music21.sieve

A comprehensive, object model of the Xenakis Sieve. [`music21.sieve.Sieve`](#music21.sieve.Sieve "music21.sieve.Sieve")
objects can be created from high-level string notations, and used to generate line segments
in various representation. Additional functionality is available through associated objects.

The [`music21.sieve.Sieve`](#music21.sieve.Sieve "music21.sieve.Sieve") class permits generation segments in four formats.

```python
>>> a = sieve.Sieve('3@2|7@1')
>>> a.segment()
[1, 2, 5, 8, 11, 14, 15, 17, 20, 22, 23, 26, 29, 32, 35, 36, 38, 41, 43, 44,
 47, 50, 53, 56, 57, 59, 62, 64, 65, 68, 71, 74, 77, 78, 80, 83, 85, 86, 89, 92, 95, 98, 99]
```

```python
>>> a.segment(segmentFormat='binary')
[0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1,
 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1,
 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
```

```python
>>> a.segment(segmentFormat='width')
[1, 3, 3, 3, 3, 1, 2, 3, 2, 1, 3, 3, 3, 3, 1, 2, 3, 2, 1, 3, 3, 3, 3, 1, 2, 3, 2,
 1, 3, 3, 3, 3, 1, 2, 3, 2, 1, 3, 3, 3, 3, 1]
```

```python
>>> len(a.segment(segmentFormat='unit'))
43
```

A [`music21.sieve.CompressionSegment`](#music21.sieve.CompressionSegment "music21.sieve.CompressionSegment") can be used to derive a Sieve from a
ny sequence of integers.

```python
>>> a = sieve.CompressionSegment([3, 4, 5, 6, 7, 8, 13, 19])
>>> str(a)
'6@1|7@6|8@5|9@4|10@3|11@8'
```

The [`music21.sieve.PitchSieve`](#music21.sieve.PitchSieve "music21.sieve.PitchSieve") class provides a quick generation of
[`music21.pitch.Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") lists from Sieves.

```python
>>> a = sieve.PitchSieve('13@3|13@6|13@9', 'c1', 'c10', 'f#4')
>>> pitches = a()
>>> ', '.join([str(p) for p in pitches])
'F#1, A1, C2, G2, B-2, C#3, G#3, B3, D4, A4, C5, E-5, B-5, C#6, E6, B6, D7,
 F7, C8, E-8, F#8, C#9, E9, G9'
```

## CompressionSegment

class music21.sieve.CompressionSegment(*src*, *z=None*)[[source]](../_modules/music21/sieve.html#CompressionSegment)
:   Utility to convert from a point sequence to sieve.

    A z range can be supplied to explicitly provide the complete sieve segment,
    both positive and negative values. all values in the z range not in the
    segment are interpreted as negative values. thus, there is an essential
    dependency on the z range and the realized sieve.

    No matter the size of the z range, there is a modulus at which one point
    in the segment can be found. As such, any segment can be reduced to, at a
    minimum, a residual for each point in the segment, each, for the supplied z,
    providing a segment with one point.

    The same segment can then have multiplied logical string representations,
    depending on the provided z.

    ```python
    >>> a = sieve.CompressionSegment([3, 4, 5, 6, 7, 8, 13, 19])
    >>> str(a)
    '6@1|7@6|8@5|9@4|10@3|11@8'
    ```

    ```python
    >>> b = sieve.CompressionSegment([0, 2, 4, 6, 8])
    >>> str(b)
    '2@0'
    ```

    ```python
    >>> c = sieve.CompressionSegment([0, 2, 4, 5, 7, 9, 11, 12])
    >>> str(c)
    '5@2|5@4|6@5|7@0'
    ```

## PitchSieve

class music21.sieve.PitchSieve(*sieveString*, *pitchLower: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchUpper: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchOrigin: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *eld: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 1*)[[source]](../_modules/music21/sieve.html#PitchSieve)
:   Quick utility generator of [`music21.pitch.Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") lists
    from [`music21.sieve.Sieve`](#music21.sieve.Sieve "music21.sieve.Sieve") objects.

    ```python
    >>> ps = sieve.PitchSieve('6@0', 'c4', 'c8')
    >>> [str(p) for p in ps()]
    ['C4', 'F#4', 'C5', 'F#5', 'C6', 'F#6', 'C7', 'F#7', 'C8']
    ```

    ```python
    >>> a = sieve.PitchSieve('4@7')
    >>> [str(p) for p in a()]
    ['E-3', 'G3', 'B3', 'E-4', 'G4', 'B4']
    ```

[`PitchSieve`](#music21.sieve.PitchSieve "music21.sieve.PitchSieve") methods

PitchSieve.getIntervalSequence() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")][[source]](../_modules/music21/sieve.html#PitchSieve.getIntervalSequence)
:   Return a list of Interval objects that defines the complete structure
    of this [`music21.sieve.Sieve`](#music21.sieve.Sieve "music21.sieve.Sieve").

    ```python
    >>> a = sieve.PitchSieve('3@0')
    >>> a.getIntervalSequence()
    [<music21.interval.Interval m3>]
    ```

    ```python
    >>> a = sieve.PitchSieve('3@0|7@0')
    >>> a.sieveObject.segment()
    [0, 3, 6, 7, 9, 12, 14, 15, 18, 21, 24, 27, 28, 30, 33, 35, 36, 39, 42, 45, 48, 49,
     51, 54, 56, 57, 60, 63, 66, 69, 70, 72, 75, 77, 78, 81, 84, 87, 90, 91, 93, 96, 98, 99]
    >>> a.sieveObject.period()
    21
    >>> a.getIntervalSequence()
    [<music21.interval.Interval m3>, <music21.interval.Interval m3>,
     <music21.interval.Interval m2>, <music21.interval.Interval M2>,
     <music21.interval.Interval m3>, <music21.interval.Interval M2>,
     <music21.interval.Interval m2>, <music21.interval.Interval m3>,
     <music21.interval.Interval m3>]
    ```

    This is the PitchSieve for a major scale:

    ```python
    >>> b = sieve.PitchSieve('(-3@2 & 4) | (-3@1 & 4@1) | (3@2 & 4@2) | (-3 & 4@3)')
    >>> b.getIntervalSequence()
    [<music21.interval.Interval M2>,
     <music21.interval.Interval M2>,
     <music21.interval.Interval m2>,
     <music21.interval.Interval M2>,
     <music21.interval.Interval M2>,
     <music21.interval.Interval M2>,
     <music21.interval.Interval m2>]
    ```

## PrimeSegment

class music21.sieve.PrimeSegment(*start*, *length*)[[source]](../_modules/music21/sieve.html#PrimeSegment)

## Residual

class music21.sieve.Residual(*m*, *shift=0*, *neg=0*, *z=None*)[[source]](../_modules/music21/sieve.html#Residual)
:   object that represents a modulus and a start point
    each object stores a range of integers (self.\_z) from which sections are drawn
    this range of integers can be changed whenever the section os drawn

    ```python
    >>> residual = sieve.Residual(3, 2)
    ```

[`Residual`](#music21.sieve.Residual "music21.sieve.Residual") methods

Residual.\_\_eq\_\_(*other*)[[source]](../_modules/music21/sieve.html#Residual.__eq__)
:   ==, compare residual classes in terms of m and shift

Residual.copy()[[source]](../_modules/music21/sieve.html#Residual.copy)

Residual.period() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/sieve.html#Residual.period)
:   period is M; obvious, but nice for completeness

    ```python
    >>> a = sieve.Residual(3, 2)
    >>> a.period()
    3
    ```

Residual.represent(*style=None*)[[source]](../_modules/music21/sieve.html#Residual.represent)
:   does not show any logical operator but unary negation

Residual.segment(*n=0*, *z=None*, *segmentFormat=None*)[[source]](../_modules/music21/sieve.html#Residual.segment)
:   get a residual subset of this modulus at this n
    within the integer range provided by z
    format can be ‘int’ or ‘bin’, for integer or binary

    ```python
    >>> a = sieve.Residual(3, 2)
    >>> a.segment(3)
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59,
     62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
    >>> a.segment(3, range(3, 15))
    [5, 8, 11, 14]
    ```

Residual.setSegmentFormat(*fmt*)[[source]](../_modules/music21/sieve.html#Residual.setSegmentFormat)

Residual.setZ(*z*)[[source]](../_modules/music21/sieve.html#Residual.setZ)
:   z is the range of integers to use when generating a list

Residual.setZRange(*minInt*, *maxInt*)[[source]](../_modules/music21/sieve.html#Residual.setZRange)
:   z is the range of integers to use when generating a list
    convenience function that fixes max

## Sieve

class music21.sieve.Sieve(*usrStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *z: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/sieve.html#Sieve)
:   Create a sieve segment from a sieve logical string of any complexity.

    ```python
    >>> a = sieve.Sieve('3@11')
    >>> b = sieve.Sieve('2&4&8|5')
    >>> c = sieve.Sieve('(5|2)&4&8')
    ```

[`Sieve`](#music21.sieve.Sieve "music21.sieve.Sieve") methods

Sieve.collect(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *zMinimum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *segmentFormat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *zStep: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 100*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/sieve.html#Sieve.collect)
:   Collect sieve segment points for the provided length and format.

    ```python
    >>> a = sieve.Sieve('3@11')
    >>> a.collect(10, 100, 10, 'int')
    [102, 105, 108, 111, 114, 117, 120, 123, 126, 129]
    ```

Sieve.compress(*z=None*)[[source]](../_modules/music21/sieve.html#Sieve.compress)
:   Set this sieve to its compressed state.

Sieve.expand()[[source]](../_modules/music21/sieve.html#Sieve.expand)
:   Set this Sieve to its expanded state.

Sieve.period() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/sieve.html#Sieve.period)
:   Return the period of the sieve.

    ```python
    >>> a = sieve.Sieve('3@11')
    >>> a.period()
    3
    >>> b = sieve.Sieve('2&4&8|5')
    >>> b.period()
    40
    >>> c = sieve.Sieve('(5|2)&4&8')
    >>> c.period()
    40
    ```

    * Changed in v9: state is taken from the object.

Sieve.represent(*state=None*, *style=None*)[[source]](../_modules/music21/sieve.html#Sieve.represent)
:   style of None is use for users; adds | to single residuals
    style abs (absolute) does not add | tos single residual class

Sieve.segment(*state: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['cmp'] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['exp'] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *n=0*, *z=None*, *segmentFormat=None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/sieve.html#Sieve.segment)
:   Return a sieve segment in various formats.

    ```python
    >>> a = sieve.Sieve('3@11')
    >>> a.segment('exp')
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47,
     50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
    ```

    ```python
    >>> c = sieve.Sieve('(5|2)&4&8')
    >>> c.segment('cmp', segmentFormat='wid')
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    ```

Sieve.setSegmentFormat(*fmt*)[[source]](../_modules/music21/sieve.html#Sieve.setSegmentFormat)

Sieve.setZ(*z*)[[source]](../_modules/music21/sieve.html#Sieve.setZ)
:   Set the z as a list. The z is the range of integers to use when
    generating a sieve segment.

Sieve.setZRange(*minInt*, *maxInt*)[[source]](../_modules/music21/sieve.html#Sieve.setZRange)
:   Set the z as a min and max value. The z is the range of
    integers to use when generating a sieve segment.

## Functions

music21.sieve.discreteBinaryPad(*series: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *fixRange=None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/sieve.html#discreteBinaryPad)
:   Treat a sequence of integers as defining contiguous binary integers,
    where provided values are 1’s and excluded values are zero.

    For instance, running [3, 10, 12] through this method gives a 1 for
    the first entry (signifying 3), 0s for the next six entries (signifying
    4-9), a 1 (for 10), a 0 (for 11), and a 1 (for 12).

    ```python
    >>> sieve.discreteBinaryPad([3, 10, 12])
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
    ```

    ```python
    >>> sieve.discreteBinaryPad([3, 4, 5])
    [1, 1, 1]
    ```

music21.sieve.eratosthenes(*firstCandidate=2*)[[source]](../_modules/music21/sieve.html#eratosthenes)
:   Yields the sequence of prime numbers via the Sieve of Eratosthenes.
    rather than creating a fixed list of a range (z) and crossing out
    multiples of sequential candidates, this algorithm stores primes under
    their next possible candidate, thus allowing the generation of primes
    in sequence without storing a complete range (z).

    Create a dictionary. Each entry in the dictionary is a key:item pair of
    (key) the largest multiple of this prime so far found and (item)
    the prime. The dictionary only has as many entries as found primes.

    If a candidate is not a key in the dictionary, it is not a multiple of
    any already-found prime; it is thus a prime. a new entry is added to the
    dictionary, with the square of the prime as the key. The square of the prime
    is the next possible multiple to be found.

    To use this generator, create an instance and then call the .next() method
    on the instance.

    ```python
    >>> a = sieve.eratosthenes()
    >>> next(a)
    2
    >>> next(a)
    3
    ```

    We can also specify a starting value for the sequence, skipping over
    initial primes smaller than this number:

    ```python
    >>> a = sieve.eratosthenes(95)
    >>> next(a)
    97
    >>> next(a)
    101
    ```

music21.sieve.rabinMiller(*n*)[[source]](../_modules/music21/sieve.html#rabinMiller)
:   Returns True if an integer is likely prime or False if it is likely composite using the
    Rabin Miller primality test.

    See also here: <http://www.4dsolutions.net/ocn/numeracy2.html>

    ```python
    >>> sieve.rabinMiller(234)
    False
    >>> sieve.rabinMiller(5)
    True
    >>> sieve.rabinMiller(4)
    False
    ```

    ```python
    >>> sieve.rabinMiller(97 * 2)
    False
    ```

    ```python
    >>> sieve.rabinMiller(6 ** 4 + 1)  # prime
    True
    ```

    ```python
    >>> sieve.rabinMiller(123986234193)  # divisible by 3, runs fast
    False
    ```

music21.sieve.unitNormEqual(*parts*)[[source]](../_modules/music21/sieve.html#unitNormEqual)
:   Given a certain number of parts, return a list unit-interval values
    between 0 and 1, with as many divisions as parts; 0 and 1 are always inclusive.

    ```python
    >>> sieve.unitNormEqual(3)
    [0.0, 0.5, 1]
    ```

    If parts is 0 or 1, then a single entry of [0] is given:

    ```python
    >>> sieve.unitNormEqual(1)
    [0]
    ```

music21.sieve.unitNormRange(*series*, *fixRange=None*)[[source]](../_modules/music21/sieve.html#unitNormRange)
:   Given a list of numbers, create a proportional spacing across the unit interval.

    The first entry will always be 0 and the last 1, other entries will be spaced
    according to their distance between these two units. For instance, for 0, 3, 4
    the middle entry will be 0.75 since 3 is 3/4 of the distance between 0 and 4:

    ```python
    >>> sieve.unitNormRange([0, 3, 4])
    [0.0, 0.75, 1.0]
    ```

    but for [1, 3, 4], it will be 0.666… because 3 is 2/3 of the distance between
    1 and 4

    ```python
    >>> sieve.unitNormRange([1, 3, 4])
    [0.0, 0.666..., 1.0]
    ```

music21.sieve.unitNormStep(*step*, *a=0*, *b=1*, *normalized=True*)[[source]](../_modules/music21/sieve.html#unitNormStep)
:   Given a step size and an a/b min/max range, calculate number of parts
    to fill step through inclusive a,b, then return a unit interval list of values
    necessary to cover region.

    Note that returned values are, by default, normalized within the unit interval.

    ```python
    >>> sieve.unitNormStep(0.5, 0, 1)
    [0.0, 0.5, 1]
    ```

    ```python
    >>> sieve.unitNormStep(0.5, -1, 1)
    [0.0, 0.25, 0.5, 0.75, 1]
    ```

    ```python
    >>> sieve.unitNormStep(0.5, -1, 1, normalized=False)
    [-1, -0.5, 0.0, 0.5, 1.0]
    ```

    ```python
    >>> post = sieve.unitNormStep(0.25, 0, 20)
    >>> len(post)
    81
    >>> post = sieve.unitNormStep(0.25, 0, 20, normalized=False)
    >>> len(post)
    81
    ```
