Source: https://music21.org/music21docs/moduleReference/moduleStreamFilters.html

# music21.stream.filters

The filter module contains [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter") objects
which are used by [`StreamIterator`](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator") objects to
decide whether a given element matches the list of elements that are being
filtered. Filters are used by methods on streams such as
`getElementsByClass()` to filter elements by classes.

## ClassFilter

class music21.stream.filters.ClassFilter(*classList=()*)[[source]](../_modules/music21/stream/filters.html#ClassFilter)
:   ClassFilter is used by .getElementsByClass() to
    find elements belonging to a class or a list of classes.

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('C'))
    >>> s.append(note.Rest())
    >>> s.append(note.Note('D'))
    >>> sI = iter(s)
    >>> sI
    <music21.stream.iterator.StreamIterator for Stream:0x104843828 @:0>
    >>> for x in sI:
    ...     print(x)
    <music21.note.Note C>
    <music21.note.Rest quarter>
    <music21.note.Note D>
    ```

    ```python
    >>> sI.filters.append(stream.filters.ClassFilter('Note'))
    >>> sI.filters
    [<music21.stream.filters.ClassFilter Note>]
    ```

    ```python
    >>> for x in sI:
    ...     print(x)
    <music21.note.Note C>
    <music21.note.Note D>
    ```

[`ClassFilter`](#music21.stream.filters.ClassFilter "music21.stream.filters.ClassFilter") bases

* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ClassFilter`](#music21.stream.filters.ClassFilter "music21.stream.filters.ClassFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ClassFilter`](#music21.stream.filters.ClassFilter "music21.stream.filters.ClassFilter") methods

ClassFilter.\_\_eq\_\_(*other*)[[source]](../_modules/music21/stream/filters.html#ClassFilter.__eq__)
:   Return self==value.

Methods inherited from [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter"):

|  |  |  |
| --- | --- | --- |
| * [`reset()`](#music21.stream.filters.StreamFilter.reset "music21.stream.filters.StreamFilter.reset") |  |  |

## ClassNotFilter

class music21.stream.filters.ClassNotFilter(*classList=()*)[[source]](../_modules/music21/stream/filters.html#ClassNotFilter)
:   Returns elements not of the class.

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('C'))
    >>> s.append(note.Rest())
    >>> s.append(note.Note('D'))
    >>> sI = iter(s)
    ```

    ```python
    >>> sI.filters.append(stream.filters.ClassNotFilter('Note'))
    >>> sI.filters
    [<music21.stream.filters.ClassNotFilter Note>]
    ```

    ```python
    >>> for x in sI:
    ...     print(x)
    <music21.note.Rest quarter>
    ```

[`ClassNotFilter`](#music21.stream.filters.ClassNotFilter "music21.stream.filters.ClassNotFilter") bases

* [`ClassFilter`](#music21.stream.filters.ClassFilter "music21.stream.filters.ClassFilter")
* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ClassNotFilter`](#music21.stream.filters.ClassNotFilter "music21.stream.filters.ClassNotFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ClassNotFilter`](#music21.stream.filters.ClassNotFilter "music21.stream.filters.ClassNotFilter") methods

Methods inherited from [`ClassFilter`](#music21.stream.filters.ClassFilter "music21.stream.filters.ClassFilter"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.stream.filters.ClassFilter.__eq__ "music21.stream.filters.ClassFilter.__eq__") |  |  |

Methods inherited from [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter"):

|  |  |  |
| --- | --- | --- |
| * [`reset()`](#music21.stream.filters.StreamFilter.reset "music21.stream.filters.StreamFilter.reset") |  |  |

## GroupFilter

class music21.stream.filters.GroupFilter(*groupFilterList=()*)[[source]](../_modules/music21/stream/filters.html#GroupFilter)
:   Returns elements with a certain group.

    ```python
    >>> n1 = note.Note('C')
    >>> n1.groups.append('trombone')
    >>> n2 = note.Note('D')
    >>> n2.groups.append('trombone')
    >>> n2.groups.append('tuba')
    >>> n3 = note.Note('E')
    >>> n3.groups.append('tuba')
    >>> s1 = stream.Stream()
    >>> s1.append(n1)
    >>> s1.append(n2)
    >>> s1.append(n3)
    >>> GF = stream.filters.GroupFilter
    ```

    ```python
    >>> for thisNote in iter(s1).addFilter(GF('trombone')):
    ...     print(thisNote.name)
    C
    D
    >>> for thisNote in iter(s1).addFilter(GF('tuba')):
    ...     print(thisNote.name)
    D
    E
    ```

[`GroupFilter`](#music21.stream.filters.GroupFilter "music21.stream.filters.GroupFilter") bases

* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GroupFilter`](#music21.stream.filters.GroupFilter "music21.stream.filters.GroupFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GroupFilter`](#music21.stream.filters.GroupFilter "music21.stream.filters.GroupFilter") methods

Methods inherited from [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter"):

|  |  |  |
| --- | --- | --- |
| * [`reset()`](#music21.stream.filters.StreamFilter.reset "music21.stream.filters.StreamFilter.reset") |  |  |

## IdFilter

class music21.stream.filters.IdFilter(*searchId=None*)[[source]](../_modules/music21/stream/filters.html#IdFilter)
:   filters on ids. used by stream.getElementById.
    No corresponding iterator call.

    Only a single ID can be passed in. Always returns a single item.

[`IdFilter`](#music21.stream.filters.IdFilter "music21.stream.filters.IdFilter") bases

* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`IdFilter`](#music21.stream.filters.IdFilter "music21.stream.filters.IdFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`IdFilter`](#music21.stream.filters.IdFilter "music21.stream.filters.IdFilter") methods

Methods inherited from [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter"):

|  |  |  |
| --- | --- | --- |
| * [`reset()`](#music21.stream.filters.StreamFilter.reset "music21.stream.filters.StreamFilter.reset") |  |  |

## IsFilter

class music21.stream.filters.IsFilter(*target=()*)[[source]](../_modules/music21/stream/filters.html#IsFilter)
:   filter on items where x IS y

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, key.KeySignature(-3))
    >>> n = note.Note('C#')
    >>> s.append(n)
    >>> s.append(note.Rest())
    >>> isFilter = stream.filters.IsFilter(n)
    >>> isFilter.derivationStr
    'is'
    >>> isFilter.target
    (<music21.note.Note C#>,)
    >>> isFilter.numToFind
    1
    ```

    .numToFind is used so that once all elements are found, the iterator can short circuit.

    ```python
    >>> for el in s.iter().addFilter(isFilter):
    ...     print(el is n)
    True
    ```

    Multiple elements can also be passed into the isFilter:

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, key.KeySignature(-3))
    >>> n = note.Note('C#')
    >>> s.append(n)
    >>> r = note.Rest()
    >>> s.append(r)
    >>> isFilter2 = stream.filters.IsFilter([n, r])
    >>> isFilter2.numToFind
    2
    ```

    ```python
    >>> for el in s.iter().addFilter(isFilter2):
    ...     print(el)
    <music21.note.Note C#>
    <music21.note.Rest quarter>
    ```

[`IsFilter`](#music21.stream.filters.IsFilter "music21.stream.filters.IsFilter") bases

* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`IsFilter`](#music21.stream.filters.IsFilter "music21.stream.filters.IsFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`IsFilter`](#music21.stream.filters.IsFilter "music21.stream.filters.IsFilter") methods

IsFilter.reset()[[source]](../_modules/music21/stream/filters.html#IsFilter.reset)

## IsNotFilter

class music21.stream.filters.IsNotFilter(*target=()*)[[source]](../_modules/music21/stream/filters.html#IsNotFilter)
:   Filter out everything but an item or list of items:

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, key.KeySignature(-3))
    >>> n = note.Note('C#')
    >>> s.append(n)
    >>> s.append(note.Rest())
    >>> for el in s.iter().addFilter(stream.filters.IsNotFilter(n)):
    ...     el
    <music21.key.KeySignature of 3 flats>
    <music21.note.Rest quarter>
    ```

    test that resetting works:

    ```python
    >>> for el in s.iter().addFilter(stream.filters.IsNotFilter(n)):
    ...     el
    <music21.key.KeySignature of 3 flats>
    <music21.note.Rest quarter>
    ```

    Using multiple filters:

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, key.KeySignature(-3))
    >>> n = note.Note('C#')
    >>> s.append(n)
    >>> r = note.Rest()
    >>> s.append(r)
    >>> for el in s.iter().addFilter(stream.filters.IsNotFilter([n, r])):
    ...     print(el)
    <music21.key.KeySignature of 3 flats>
    ```

[`IsNotFilter`](#music21.stream.filters.IsNotFilter "music21.stream.filters.IsNotFilter") bases

* [`IsFilter`](#music21.stream.filters.IsFilter "music21.stream.filters.IsFilter")
* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`IsNotFilter`](#music21.stream.filters.IsNotFilter "music21.stream.filters.IsNotFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`IsNotFilter`](#music21.stream.filters.IsNotFilter "music21.stream.filters.IsNotFilter") methods

IsNotFilter.reset()[[source]](../_modules/music21/stream/filters.html#IsNotFilter.reset)

## OffsetFilter

class music21.stream.filters.OffsetFilter(*offsetStart=0.0*, *offsetEnd=None*, *\**, *includeEndBoundary=True*, *mustFinishInSpan=False*, *mustBeginInSpan=True*, *includeElementsThatEndAtStart=True*, *stopAfterEnd=True*)[[source]](../_modules/music21/stream/filters.html#OffsetFilter)
:   see [`getElementsByOffset()`](moduleStreamIterator.html#music21.stream.iterator.StreamIterator.getElementsByOffset "music21.stream.iterator.StreamIterator.getElementsByOffset")
    for docs on this filter.

    Finds elements that match a given offset range.

    * Changed in v5.5: all arguments except offsetStart and offsetEnd are keyword only.
    * Changed in v6.5: stopAfterEnd can be set globally.

[`OffsetFilter`](#music21.stream.filters.OffsetFilter "music21.stream.filters.OffsetFilter") bases

* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OffsetFilter`](#music21.stream.filters.OffsetFilter "music21.stream.filters.OffsetFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OffsetFilter`](#music21.stream.filters.OffsetFilter "music21.stream.filters.OffsetFilter") methods

OffsetFilter.isElementOffsetInRange(*e*, *offset*, *\**, *stopAfterEnd=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/filters.html#OffsetFilter.isElementOffsetInRange)
:   Given an element, offset, and stream, return
    True, False, or raise StopIteration if the
    element is in the range, not in the range, or (if stopAfterEnd is True) is not
    and no future elements will be in the range.

    Factored out from \_\_call\_\_ to be used by OffsetHierarchyFilter, and it’s just
    a beast. :-)

Methods inherited from [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter"):

|  |  |  |
| --- | --- | --- |
| * [`reset()`](#music21.stream.filters.StreamFilter.reset "music21.stream.filters.StreamFilter.reset") |  |  |

## OffsetHierarchyFilter

class music21.stream.filters.OffsetHierarchyFilter(*offsetStart=0.0*, *offsetEnd=None*, *\**, *includeEndBoundary=True*, *mustFinishInSpan=False*, *mustBeginInSpan=True*, *includeElementsThatEndAtStart=True*, *stopAfterEnd=True*)[[source]](../_modules/music21/stream/filters.html#OffsetHierarchyFilter)
:   see [`getElementsByOffsetInHierarchy()`](moduleStreamIterator.html#music21.stream.iterator.RecursiveIterator.getElementsByOffsetInHierarchy "music21.stream.iterator.RecursiveIterator.getElementsByOffsetInHierarchy")
    for docs on this filter.

    Finds elements that match a given offset range in the hierarchy.

    Do not call .stream() afterwards or unstable results can occur.

[`OffsetHierarchyFilter`](#music21.stream.filters.OffsetHierarchyFilter "music21.stream.filters.OffsetHierarchyFilter") bases

* [`OffsetFilter`](#music21.stream.filters.OffsetFilter "music21.stream.filters.OffsetFilter")
* [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OffsetHierarchyFilter`](#music21.stream.filters.OffsetHierarchyFilter "music21.stream.filters.OffsetHierarchyFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OffsetHierarchyFilter`](#music21.stream.filters.OffsetHierarchyFilter "music21.stream.filters.OffsetHierarchyFilter") methods

Methods inherited from [`OffsetFilter`](#music21.stream.filters.OffsetFilter "music21.stream.filters.OffsetFilter"):

|  |  |  |
| --- | --- | --- |
| * [`isElementOffsetInRange()`](#music21.stream.filters.OffsetFilter.isElementOffsetInRange "music21.stream.filters.OffsetFilter.isElementOffsetInRange") |  |  |

Methods inherited from [`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter"):

|  |  |  |
| --- | --- | --- |
| * [`reset()`](#music21.stream.filters.StreamFilter.reset "music21.stream.filters.StreamFilter.reset") |  |  |

## StreamFilter

class music21.stream.filters.StreamFilter[[source]](../_modules/music21/stream/filters.html#StreamFilter)
:   A filter is an object that when called returns True or False
    about whether an element in the stream matches the filter.

    A lambda expression: lambda el, iterator: True if EXP else False can also be
    used as a very simple filter.

    Filters can also raise StopIteration if no other elements in this Stream
    can possibly fit.

    The StreamFilter object does nothing in itself but subclasses are crucial
    in filtering out elements according to different properties.

    Each subclass of StreamFilter should set its .derivationStr which is
    a string that determines which a derived Stream based on this filter should be called

    ```python
    >>> sf = stream.filters.StreamFilter()
    >>> sf
    <music21.stream.filters.StreamFilter object at 0x1051de828>
    >>> sf.derivationStr
    'streamFilter'
    ```

    StreamFilters also have these two properties, inherited from
    [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object") which help in certain debug operations

    ```python
    >>> 'StreamFilter' in sf.classSet
    True
    >>> sf.classes
    ('StreamFilter', 'ProtoM21Object', 'object')
    ```

[`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`StreamFilter`](#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter") methods

StreamFilter.reset()[[source]](../_modules/music21/stream/filters.html#StreamFilter.reset)
