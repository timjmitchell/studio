Source: https://music21.org/music21docs/moduleReference/moduleDerivation.html

# music21.derivation

This module defines objects for tracking the derivation of one
`Stream` from another.

## Derivation

class music21.derivation.Derivation(*client: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/derivation.html#Derivation)
:   A Derivation object keeps track of which Streams (or perhaps other Music21Objects)
    a Stream or other music21 object has come from and how.

    Derivation is automatically updated by many methods:

    ```python
    >>> import copy
    >>> sOrig = stream.Stream(id='orig')
    >>> sNew = copy.deepcopy(sOrig)
    >>> sNew.id = 'copy'
    >>> sNew.derivation
    <Derivation of <music21.stream.Stream copy>
        from <music21.stream.Stream orig> via '__deepcopy__'>
    ```

    ```python
    >>> sNew.derivation.client
    <music21.stream.Stream copy>
    >>> sNew.derivation.client is sNew
    True
    >>> sNew.derivation.origin
    <music21.stream.Stream orig>
    >>> sNew.derivation.method
    '__deepcopy__'
    ```

    ```python
    >>> s1 = stream.Stream()
    >>> s1.id = 'DerivedStream'
    >>> d1 = derivation.Derivation(s1)
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> s2.id = 'OriginalStream'
    ```

    ```python
    >>> d1.method = 'manual'
    >>> d1.origin = s2
    >>> d1
    <Derivation of <music21.stream.Stream DerivedStream> from
        <music21.stream.Stream OriginalStream> via 'manual'>
    >>> d1.origin is s2
    True
    ```

    ```python
    >>> d1.client is s1
    True
    ```

    ```python
    >>> import copy
    >>> d2 = copy.deepcopy(d1)
    >>> d2.origin is s2
    True
    ```

    ```python
    >>> d1.method = 'measure'
    >>> d1.method
    'measure'
    ```

    Deleting the origin stream does not change the Derivation, since origin is held by strong ref:

    ```python
    >>> import gc  # Garbage collection
    >>> del s2
    >>> unused = gc.collect()  # ensure Garbage collection is run
    >>> d1
    <Derivation of <music21.stream.Stream DerivedStream>
        from <music21.stream.Stream OriginalStream> via 'measure'>
    ```

    But deleting the client stream changes the Derivation, since client is held by weak ref,
    and will also delete the origin (so long as client was ever set)

    ```python
    >>> del s1
    >>> unused = gc.collect()  # ensure Garbage collection is run
    >>> d1
    <Derivation of None from None via 'measure'>
    ```

[`Derivation`](#music21.derivation.Derivation "music21.derivation.Derivation") bases

* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Derivation`](#music21.derivation.Derivation "music21.derivation.Derivation") read-only properties

Derivation.originId
:   Return the Python id (=memory location) of the origin.
    (Same as id(derivation.origin). Not the same as derivation.origin.ind)

Derivation.rootDerivation
:   Return a reference to the oldest source of this Stream; that is, chain
    calls to `derivesFrom` until we get to a
    Stream that cannot be further derived.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.repeatAppend(note.Note(), 10)
    >>> s1.repeatAppend(note.Rest(), 10)
    >>> s2 = s1.notesAndRests.stream()
    >>> s3 = s2.getElementsByClass(note.Note).stream()
    >>> s3.derivation.rootDerivation is s1
    True
    ```

[`Derivation`](#music21.derivation.Derivation "music21.derivation.Derivation") read/write properties

Derivation.client

Derivation.method
:   Returns or sets the string of the method that was used to generate this
    Stream.

    ```python
    >>> s = stream.Stream()
    >>> s.derivation.method is None
    True
    ```

    ```python
    >>> sNotes = s.notes.stream()
    >>> sNotes.derivation.method
    'notes'
    ```

    Some examples are ‘getElementsByClass’ etc.

    ```python
    >>> s = stream.Stream()
    >>> s.id = 'lonelyStream'
    >>> s.append(clef.TrebleClef())
    >>> s.append(note.Note())
    >>> sNotes = s.notes.stream()
    >>> sNotes.derivation
    <Derivation of <music21.stream.Stream lonelyStream>
        from <music21.stream.Stream lonelyStream> via 'notes'>
    ```

    ```python
    >>> derived = sNotes.derivation
    >>> derived.method
    'notes'
    ```

    ```python
    >>> derived.method = 'blah'
    >>> derived.method
    'blah'
    ```

    ```python
    >>> derived is sNotes.derivation
    True
    >>> sNotes.derivation.method
    'blah'
    ```

Derivation.origin

[`Derivation`](#music21.derivation.Derivation "music21.derivation.Derivation") methods

Derivation.chain() → Generator[[base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/derivation.html#Derivation.chain)
:   Iterator/Generator

    Yields the Streams which this Derivation’s client Stream was derived
    from. This provides a way to obtain all Streams that the client passed
    through, such as those created by
    `getElementsByClass()` or
    `flatten()`.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.id = 's1'
    >>> s1.repeatAppend(note.Note(), 10)
    >>> s1.repeatAppend(note.Rest(), 10)
    >>> s2 = s1.notesAndRests.stream()
    >>> s2.id = 's2'
    >>> s3 = s2.getElementsByClass(note.Note).stream()
    >>> s3.id = 's3'
    >>> for y in s3.derivation.chain():
    ...     print(y)
    <music21.stream.Stream s2>
    <music21.stream.Stream s1>
    ```

    ```python
    >>> list(s3.derivation.chain()) == [s2, s1]
    True
    ```

## Functions

music21.derivation.derivationMethod(*function*)[[source]](../_modules/music21/derivation.html#derivationMethod)
:   This decorator can be used for creating a function that returns a new
    derivation. But is currently unused, since it does not take into account inPlace=True.
    Stream.cloneEmpty(derivationMethod=’derivationMethod’) is preferred for
    Streams.

    ```python
    >>> from copy import deepcopy
    >>> @derivation.derivationMethod
    ... def allGreen(n):
    ...     n2 = deepcopy(n)
    ...     n2.style.color = 'green'
    ...     return n2
    ```

    ```python
    >>> n = note.Note('C#')
    >>> n2 = allGreen(n)
    >>> n2.style.color
    'green'
    ```

    ```python
    >>> n2.name = 'D-'
    >>> n2.derivation
    <Derivation of <music21.note.Note D-> from <music21.note.Note C#> via 'allGreen'>
    ```
