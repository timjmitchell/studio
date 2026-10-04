Source: https://music21.org/music21docs/moduleReference/moduleSorting.html

# music21.sorting

This module defines a single class, SortTuple, which is a named tuple that can
sort against bare offsets and other SortTuples.

This is a performance-critical object.

It also defines three singleton instances of the SortTupleLow class as ZeroSortTupleDefault,
ZeroSortTupleLow and
ZeroSortTupleHigh which are sortTuple at
offset 0.0, priority [0, -inf, inf] respectively:

```python
>>> sorting.ZeroSortTupleDefault
SortTuple(atEnd=0, offset=0.0, priority=0, classSortOrder=0, isNotGrace=1, insertIndex=0)
>>> sorting.ZeroSortTupleLow
SortTuple(atEnd=0, offset=0.0, priority=-inf, classSortOrder=0, isNotGrace=1, insertIndex=0)
>>> sorting.ZeroSortTupleHigh
SortTuple(atEnd=0, offset=0.0, priority=inf, classSortOrder=0, isNotGrace=1, insertIndex=0)
```

## SortTuple

class music21.sorting.SortTuple(*\*tupEls*, *\*\*keywords*)[[source]](../_modules/music21/sorting.html#SortTuple)
:   Derived class of namedTuple which allows for comparisons with pure ints/fractions.

    ```python
    >>> n = note.Note()
    >>> s = stream.Stream()
    >>> s.insert(4, n)
    >>> st = n.sortTuple()
    >>> st
    SortTuple(atEnd=0, offset=4.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=...)
    >>> st.shortRepr()
    '4.0 <0.20...>'
    >>> st.atEnd
    0
    >>> st.offset
    4.0
    ```

    ```python
    >>> st < 5.0
    True
    >>> 5.0 > st
    True
    >>> st > 3.0
    True
    >>> 3.0 < st
    True
    ```

    ```python
    >>> st == 4.0
    True
    ```

    ```python
    >>> ts = bar.Barline('double')
    >>> s2 = stream.Stream()
    >>> s2.storeAtEnd(ts)
    >>> ts_st = ts.sortTuple()
    >>> ts_st
    SortTuple(atEnd=1, offset=0.0, priority=0, classSortOrder=-5, isNotGrace=1, insertIndex=...)
    >>> st < ts_st
    True
    >>> ts_st > 999999
    True
    >>> import math
    >>> ts_st == math.inf
    True
    ```

    Construct one w/ keywords:

    ```python
    >>> st = sorting.SortTuple(atEnd=0, offset=1.0, priority=0, classSortOrder=20,
    ...           isNotGrace=1, insertIndex=323)
    >>> st.shortRepr()
    '1.0 <0.20.323>'
    ```

    or as tuple:

    ```python
    >>> st = sorting.SortTuple(0, 1.0, 0, 20, 1, 323)
    >>> st.shortRepr()
    '1.0 <0.20.323>'
    ```

[`SortTuple`](#music21.sorting.SortTuple "music21.sorting.SortTuple") bases

* [`SortTuple`](#music21.sorting.SortTuple "music21.sorting.SortTuple")

[`SortTuple`](#music21.sorting.SortTuple "music21.sorting.SortTuple") methods

SortTuple.\_\_eq\_\_(*other*)[[source]](../_modules/music21/sorting.html#SortTuple.__eq__)
:   Return self==value.

SortTuple.add(*other*)[[source]](../_modules/music21/sorting.html#SortTuple.add)
:   Add all attributes from one sortTuple to another,
    returning a new one.

    ```python
    >>> n = note.Note()
    >>> n.offset = 10
    >>> s = stream.Stream()
    >>> s.offset = 10
    >>> n.sortTuple()
    SortTuple(atEnd=0, offset=10.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=0)
    >>> s.sortTuple()
    SortTuple(atEnd=0, offset=10.0, priority=0, classSortOrder=-20, isNotGrace=1, insertIndex=0)
    >>> s.sortTuple().add(n.sortTuple())
    SortTuple(atEnd=0, offset=20.0, priority=0, classSortOrder=0, isNotGrace=1, insertIndex=0)
    ```

    Note that atEnd and isNotGrace are equal to other’s value. are upper bounded at 1 and
    take the maxValue of either.

SortTuple.modify(*\*\*keywords*)[[source]](../_modules/music21/sorting.html#SortTuple.modify)
:   return a new SortTuple identical to the previous, except with
    the given keyword modified. Works only with keywords.

    ```python
    >>> st = sorting.SortTuple(atEnd=0, offset=1.0, priority=0, classSortOrder=20,
    ...           isNotGrace=1, insertIndex=32)
    >>> st2 = st.modify(offset=2.0)
    >>> st2.shortRepr()
    '2.0 <0.20.32>'
    >>> st2
    SortTuple(atEnd=0, offset=2.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=32)
    ```

    ```python
    >>> st3 = st2.modify(atEnd=1, isNotGrace=0)
    >>> st3.shortRepr()
    'End <0.20.[Grace].32>'
    ```

    The original tuple is never modified (hence tuple):

    ```python
    >>> st.offset
    1.0
    ```

    Changing offset, but nothing else, helps in creating .flatten() positions.

SortTuple.shortRepr()[[source]](../_modules/music21/sorting.html#SortTuple.shortRepr)
:   Returns a nice representation of a SortTuple

    ```python
    >>> st = sorting.SortTuple(atEnd=0, offset=1.0, priority=0, classSortOrder=20,
    ...           isNotGrace=1, insertIndex=323)
    >>> st.shortRepr()
    '1.0 <0.20.323>'
    ```

    ```python
    >>> st = sorting.SortTuple(atEnd=1, offset=1.0, priority=4, classSortOrder=7,
    ...           isNotGrace=0, insertIndex=200)
    >>> st.shortRepr()
    'End <4.7.[Grace].200>'
    ```

SortTuple.sub(*other*)[[source]](../_modules/music21/sorting.html#SortTuple.sub)
:   Subtract all attributes from to another. atEnd and isNotGrace take the min value of either.

    ```python
    >>> n = note.Note()
    >>> n.offset = 10
    >>> s = stream.Stream()
    >>> s.offset = 10
    >>> n.sortTuple()
    SortTuple(atEnd=0, offset=10.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=0)
    >>> s.sortTuple()
    SortTuple(atEnd=0, offset=10.0, priority=0, classSortOrder=-20, isNotGrace=1, insertIndex=0)
    >>> s.sortTuple().sub(n.sortTuple())
    SortTuple(atEnd=0, offset=0.0, priority=0, classSortOrder=-40, isNotGrace=1, insertIndex=0)
    ```

    Note that atEnd and isNotGrace are lower bounded at 0.
