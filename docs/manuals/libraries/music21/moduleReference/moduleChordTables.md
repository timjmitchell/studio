Source: https://music21.org/music21docs/moduleReference/moduleChordTables.html

# music21.chord.tables

This module stores numerous data lists used in deriving set-class values and other post-tonal
chord representations. All features of this module are made available through
[`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") objects. Use of this module directly is thus not necessary.

## ChordTableAddress

class music21.chord.tables.ChordTableAddress(*cardinality*, *forteClass*, *inversion*, *pcOriginal*)

## Functions

music21.chord.tables.addressToForteName(*address*, *classification='tn'*)[[source]](../_modules/music21/chord/tables.html#addressToForteName)
:   Given an address, return the set-class name as a string. By default,
    A and B are appended to chords without inversional equivalence:

    ```python
    >>> octachord_address = chord.tables.ChordTableAddress(8, 15, -1, 10)
    >>> chord.tables.addressToForteName(octachord_address)
    '8-15B'
    >>> chord.tables.addressToForteName((8, 15))
    '8-15A'
    ```

    The augmented triad is invariant under inversion, so it gets no designation:

    ```python
    >>> chord.tables.addressToForteName((3, 12))
    '3-12'
    ```

    If classification is the string ‘tni’ then the “A” and “B” for inversions
    will be omitted.

    ```python
    >>> chord.tables.addressToForteName((8, 15), 'tni')
    '8-15'
    >>> chord.tables.addressToForteName((5, 37))
    '5-37'
    ```

music21.chord.tables.addressToPrimeForm(*address*)[[source]](../_modules/music21/chord/tables.html#addressToPrimeForm)
:   Given a TN address, return the prime form

    ```python
    >>> chord.tables.addressToPrimeForm((3, 1, 0))
    (0, 1, 2)
    ```

    Since we are talking about primeForm, inversion does not matter.
    These both return the minor triad.

    ```python
    >>> chord.tables.addressToPrimeForm((3, 11, -1))
    (0, 3, 7)
    >>> chord.tables.addressToPrimeForm((3, 11, 1))
    (0, 3, 7)
    ```

    If inversion is omitted or None the default value is used:

    ```python
    >>> chord.tables.addressToPrimeForm((3, 11))
    (0, 3, 7)
    >>> chord.tables.addressToPrimeForm((3, 11, None))
    (0, 3, 7)
    ```

music21.chord.tables.seekChordTablesAddress(*c*)[[source]](../_modules/music21/chord/tables.html#seekChordTablesAddress)
:   Utility method to return the address to the chord table; used by
    many Chord operations, such as .primeForm, .normalOrder, etc.

    Table addresses are a ChordTableAddress named-tuple giving
    the cardinality, the Forte-index-number, the inversion, and the original
    pitch class that matched (it may be arbitrary for a symmetrical chord like
    the diminished seventh chord).

    Inversion is either 0 (for symmetrical under inversion) or -1, 1

    ```python
    >>> c1 = chord.Chord(['c3'])
    >>> chord.tables.seekChordTablesAddress(c1)
    ChordTableAddress(cardinality=1, forteClass=1, inversion=0, pcOriginal=0)
    ```

    Here the only note that is missing is A-sharp/B-flat.

    ```python
    >>> c1 = chord.Chord(
    ...     ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b']
    ...     )
    >>> chord.tables.seekChordTablesAddress(c1)
    ChordTableAddress(cardinality=11, forteClass=1, inversion=0, pcOriginal=11)
    ```

    The major chord is considered the inversion of the minor:

    ```python
    >>> c1 = chord.Chord(['g', 'b', 'd'])
    >>> chord.tables.seekChordTablesAddress(c1)
    ChordTableAddress(cardinality=3, forteClass=11, inversion=-1, pcOriginal=7)
    ```

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> chord.tables.seekChordTablesAddress(c1)
    ChordTableAddress(cardinality=3, forteClass=11, inversion=1, pcOriginal=0)
    ```

    Chords invariant under inversion give an inversion of 0.

    ```python
    >>> c1 = chord.Chord(['c', 'c#', 'd#', 'e', 'f#', 'g#', 'a#'])
    >>> chord.tables.seekChordTablesAddress(c1)
    ChordTableAddress(cardinality=7, forteClass=34, inversion=0, pcOriginal=0)
    ```

    ```python
    >>> c1 = chord.Chord(['c', 'c#', 'b'])
    >>> chord.tables.seekChordTablesAddress(c1)
    ChordTableAddress(cardinality=3, forteClass=1, inversion=0, pcOriginal=11)
    ```

    Zero-length chords raise a pitch exception:

    ```python
    >>> c2 = chord.Chord()
    >>> chord.tables.seekChordTablesAddress(c2)
    Traceback (most recent call last):
    music21.chord.tables.ChordTablesException: cannot access chord tables address
        for Chord with 0 pitches
    ```

    NOTE: this was once a time-consuming operation, though it is
    now quite a bit faster than before (order of 100 microseconds). Nonetheless, it
    should only be run when necessary. Methods that call this should
    try (as chord.Chord does) to cache the result.

music21.chord.tables.addressToCommonNames(*address*)[[source]](../_modules/music21/chord/tables.html#addressToCommonNames)
:   Given a TN address, return one or more common names if available:

    ```python
    >>> chord.tables.addressToCommonNames((3, 1, 0))
    ['chromatic trimirror']
    ```

    ```python
    >>> major_address = chord.tables.ChordTableAddress(3, 11, -1, 2)
    >>> chord.tables.addressToCommonNames(major_address)
    ['major triad']
    ```

    More than one name might be returned:
    >>> chord.tables.addressToCommonNames([7, 33])
    [‘Neapolitan-major mode’, ‘leading-whole-tone mode’]

    This system does not take into account spelling or inversion, so
    that the minor triad would give the same name. The .commonName
    property of the chord.Chord object itself takes into account
    non-post-tonal spellings.

    Note that names referring to ethnic stereotypes that are not in
    common usage will be removed in music21 v8 or at any time
    thereafter without a deprecation cycle.
    Those matching this description that are still in common use will be demoted
    to the end of the list of names and may still be removed in the future.

music21.chord.tables.addressToIntervalVector(*address*)[[source]](../_modules/music21/chord/tables.html#addressToIntervalVector)
:   Given a TN address, return the interval class vector as a 6-tuple

    ```python
    >>> chord.tables.addressToIntervalVector((3, 1, 0))
    (2, 1, 0, 0, 0, 0)
    >>> chord.tables.addressToIntervalVector((3, 11, -1))
    (0, 0, 1, 1, 1, 0)
    >>> chord.tables.addressToIntervalVector((3, 11, 1))
    (0, 0, 1, 1, 1, 0)
    ```

    Inversion can be omitted or None without causing an error (or, of course,
    changing the output)

    ```python
    >>> chord.tables.addressToIntervalVector((4, 29))
    (1, 1, 1, 1, 1, 1)
    >>> chord.tables.addressToIntervalVector((3, 11, None))
    (0, 0, 1, 1, 1, 0)
    ```

music21.chord.tables.addressToTransposedNormalForm(*address*)[[source]](../_modules/music21/chord/tables.html#addressToTransposedNormalForm)
:   Given a TN address, return the normal form transposed to start on 0.

    ```python
    >>> chord.tables.addressToTransposedNormalForm((3, 1, 0))
    (0, 1, 2)
    >>> chord.tables.addressToTransposedNormalForm((3, 11, -1))
    (0, 4, 7)
    >>> chord.tables.addressToTransposedNormalForm((3, 11, 1))
    (0, 3, 7)
    ```

    If the inversion in the address is omitted or None,
    then the default inversion is used:

    ```python
    >>> chord.tables.addressToTransposedNormalForm((3, 11))
    (0, 3, 7)
    >>> chord.tables.addressToTransposedNormalForm((3, 11, None))
    (0, 3, 7)
    >>> chord.tables.addressToTransposedNormalForm((3, 1))
    (0, 1, 2)
    ```

music21.chord.tables.addressToZAddress(*address*)[[source]](../_modules/music21/chord/tables.html#addressToZAddress)
:   Given a TN address, return the ChordTableAddress of the Z-set if one exists.
    If none exists, returns None.

    ```python
    >>> chord.tables.addressToZAddress((5, 12))
    ChordTableAddress(cardinality=5, forteClass=36, inversion=1, pcOriginal=None)
    >>> chord.tables.addressToZAddress((5, 36, None))
    ChordTableAddress(cardinality=5, forteClass=12, inversion=0, pcOriginal=None)
    ```

    ```python
    >>> print(chord.tables.addressToZAddress([3, 11]))
    None
    ```

    ```python
    >>> chord.tables.addressToZAddress((5, 37))
    ChordTableAddress(cardinality=5, forteClass=17, inversion=0, pcOriginal=None)
    >>> chord.tables.addressToZAddress((8, 29))
    ChordTableAddress(cardinality=8, forteClass=15, inversion=1, pcOriginal=None)
    ```

music21.chord.tables.forteIndexToInversionsAvailable(*card*, *index*)[[source]](../_modules/music21/chord/tables.html#forteIndexToInversionsAvailable)
:   Return possible inversion values for any cardinality and Forte index

    ```python
    >>> chord.tables.forteIndexToInversionsAvailable(3, 1)
    [0]
    >>> chord.tables.forteIndexToInversionsAvailable(3, 2)
    [-1, 1]
    >>> chord.tables.forteIndexToInversionsAvailable(3, 3)
    [-1, 1]
    >>> chord.tables.forteIndexToInversionsAvailable(3, 6)
    [0]
    >>> chord.tables.forteIndexToInversionsAvailable(3, 12)
    [0]
    ```

music21.chord.tables.intervalVectorToAddress(*vector*)[[source]](../_modules/music21/chord/tables.html#intervalVectorToAddress)
:   Given a vector as a 6-tuple, return a list of
    ChordTableAddress namedtuples for
    all addresses that match that vector.

    ```python
    >>> chord.tables.intervalVectorToAddress((7, 6, 5, 4, 4, 2))
    [ChordTableAddress(cardinality=8, forteClass=1, inversion=None, pcOriginal=None)]
    >>> chord.tables.intervalVectorToAddress((12, 12, 12, 12, 12, 6))
    [ChordTableAddress(cardinality=12, forteClass=1, inversion=None, pcOriginal=None)]
    ```

    Vector can also be a list:

    ```python
    >>> chord.tables.intervalVectorToAddress([2, 2, 3, 1, 1, 1])
    [ChordTableAddress(cardinality=5, forteClass=10, inversion=None, pcOriginal=None)]
    ```

    A value that matches nothing returns an empty set.

    ```python
    >>> chord.tables.intervalVectorToAddress((2, 2, 3, 1, 1, 99))
    []
    ```

    In the case of Z-related pairs, such as the all-interval tetrachord,
    more than one address will be returned.

    ```python
    >>> chord.tables.intervalVectorToAddress((1, 1, 1, 1, 1, 1))
    [ChordTableAddress(cardinality=4, forteClass=15, inversion=None, pcOriginal=None),
     ChordTableAddress(cardinality=4, forteClass=29, inversion=None, pcOriginal=None)]
    ```

    If the vector does not have six elements, raises a ValueError:

    ```python
    >>> chord.tables.intervalVectorToAddress([0, 2, 4])
    Traceback (most recent call last):
    ValueError: Vector must have exactly six entries
    ```
