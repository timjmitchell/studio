Source: https://music21.org/music21docs/moduleReference/moduleStreamTools.html

# music21.stream.tools

## Functions

music21.stream.tools.removeDuplicates(*thisStream: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *classesToRemove: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") = (<class 'music21.meter.base.TimeSignature'>*, *<class 'music21.key.KeySignature'>*, *<class 'music21.clef.Clef'>)*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/stream/tools.html#removeDuplicates)
:   The repetition of some classes like notes is common.
    By contrast, the explicit repetition of certain other objects like clefs
    usually indicates an error e.g., resulting from a copy’n’paste.
    This function serves to remove those that are likely in error and make no change.

    Use the classesToRemove argument to specify which music21 classes to check and remove.
    The classes currently supported are: time signatures, key signatures, and clefs.
    The classesToRemove argument defaults all three.
    Sometimes there are legitimate reasons to duplicate even these classes.
    In that case, override the default by specifying the list of which of the three of classes.
    More classes may be added, but for now they will simply raise a ValueError.

    So let’s create an example part with an initial set of
    time signature, key signature, and clef.

    ```python
    >>> p = stream.Part()
    >>> p.append(meter.TimeSignature('3/4'))  # first TS
    >>> p.append(key.KeySignature(6))  # first KS
    >>> p.append(clef.TrebleClef())  # first Clef
    ```

    Then a few notes, followed by a duplicates of the
    key signature, and clef.

    ```python
    >>> p.append(note.Note('C'))
    >>> p.append(note.Note('C'))
    >>> p.append(note.Note('D'))
    ```

    ```python
    >>> p.append(meter.TimeSignature('3/4'))  # duplicate
    >>> p.append(key.KeySignature(6))  # duplicate
    >>> p.append(clef.TrebleClef())  # duplicate
    ```

    Finally, a few more notes, followed by a
    change of time signature, key signature, and clef.

    ```python
    >>> p.append(note.Note('E'))
    >>> p.append(note.Note('F'))
    >>> p.append(note.Note('G'))
    ```

    ```python
    >>> p.append(meter.TimeSignature('2/4'))
    >>> p.append(key.KeySignature(-5))
    >>> p.append(clef.BassClef())
    ```

    ```python
    >>> p.append(note.Note('A'))
    >>> p.append(note.Note('B'))
    >>> p.append(note.Note('C5'))
    ```

    Now we’ll make it into a proper part with measures and see
    how it looks in its original, unaltered form:

    ```python
    >>> p.makeMeasures(inPlace=True)
    >>> p.show('t')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.key.KeySignature of 6 sharps>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note C>
        {2.0} <music21.note.Note D>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.key.KeySignature of 6 sharps>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note G>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.key.KeySignature of 5 flats>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
    {8.0} <music21.stream.Measure 4 offset=8.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.bar.Barline type=final>
    ```

    Calling removeDuplicates should remove the duplicates
    even with those changes now stored within measures,
    not directly on the part.
    Specifically, in our example,
    the duplicates entries are removed from measure 2
    and the actual changes in measure 3 remain.

    ```python
    >>> testInPlace = stream.tools.removeDuplicates(p)
    >>> testInPlace.show('t')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.key.KeySignature of 6 sharps>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note C>
        {2.0} <music21.note.Note D>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note G>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.key.KeySignature of 5 flats>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
    {8.0} <music21.stream.Measure 4 offset=8.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.bar.Barline type=final>
    ```

    As the example shows, this function defaults to working on a stream inPlace.

    ```python
    >>> testInPlace == p
    True
    ```

    To avoid this, set inPlace to False.

    ```python
    >>> testNotInPlace = stream.tools.removeDuplicates(p, inPlace=False)
    >>> testNotInPlace == p
    False
    ```

    This function is primarily designed and intended for use on a stream.Part object.
    If called on a steam.Score, it will simply be applied to each of that score’s parts in turn.

    ```python
    >>> s = stream.Score()
    >>> s.append(p)
    >>> t = stream.tools.removeDuplicates(s, inPlace=False)
    >>> s.parts[0] == testInPlace
    True
    ```
