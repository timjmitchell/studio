Source: https://music21.org/music21docs/moduleReference/moduleAbcFormatTranslate.html

# music21.abcFormat.translate

Functions for translating music21 objects and
[`ABCHandler`](moduleAbcFormat.html#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler") instances.
Mostly, these functions are for advanced, low level usage.
For basic importing of ABC files from a file or URL to a
`Stream`, use the music21 converter
module’s [`parse()`](moduleConverter.html#music21.converter.parse "music21.converter.parse") function.

## Functions

music21.abcFormat.translate.abcToStreamOpus(*abcHandler*, *inputM21=None*, *number=None*)[[source]](../_modules/music21/abcFormat/translate.html#abcToStreamOpus)
:   Convert a multi-work stream into one or more complete works packed into an Opus Stream.

    If a number argument is given, and a work is defined by
    that number, that work is returned.

music21.abcFormat.translate.abcToStreamPart(*abcHandler: [abcFormat.ABCHandler](moduleAbcFormat.html#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler")*, *inputM21: stream.Part | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *spannerBundle: [spanner.SpannerBundle](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → stream.Part[[source]](../_modules/music21/abcFormat/translate.html#abcToStreamPart)
:   Handler conversion of a single Part of a Score with multiple Parts.
    Results are added into the provided inputM21 object
    or a newly created Part object

    The part object is then returned.

music21.abcFormat.translate.abcToStreamScore(*abcHandler*, *inputM21=None*)[[source]](../_modules/music21/abcFormat/translate.html#abcToStreamScore)
:   Given an abcHandler object, build into a
    multi-part `Score` with metadata.

    This assumes that this ABCHandler defines a single work (with 1 or fewer reference numbers).

    if the optional parameter inputM21 is given a music21 Stream subclass, it will use that object
    as the outermost object. However, inner parts will
    always be made `Part` objects.

music21.abcFormat.translate.metadataToM21Object(*t: [abcFormat.ABCMetadata](moduleAbcFormat.html#music21.abcFormat.ABCMetadata "music21.abcFormat.ABCMetadata")*, *dst: stream.Measure | stream.Part*, *postTransposition: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *clefSet: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *useMeasures: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][[source]](../_modules/music21/abcFormat/translate.html#metadataToM21Object)
:   Parse a single ABCMetadata token, that does not represent what
    music21 considers metadata, such as a time signature, key signature,
    clef, or tempo, and put it in dst.

    This function uses coreAppend operations, so if called separately,
    dst.coreElementsChanged() should be called before accessing the stream.

    Returns the changed transposition and whether clef was set.

music21.abcFormat.translate.parseABCNote(*t: [abcFormat.ABCNote](moduleAbcFormat.html#music21.abcFormat.ABCNote "music21.abcFormat.ABCNote")*, *dst: stream.Measure | stream.Part*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat/translate.html#parseABCNote)
:   Parse an ABCNote object and add it to the destination stream.

music21.abcFormat.translate.parseTokens(*mh: [abcFormat.ABCHandler](moduleAbcFormat.html#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler")*, *dst: stream.Measure | stream.Part*, *p: stream.Part*, *useMeasures: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][[source]](../_modules/music21/abcFormat/translate.html#parseTokens)
:   parses all the tokens in a measure or part.

music21.abcFormat.translate.reBar(*music21Part*, *\**, *inPlace=False*)[[source]](../_modules/music21/abcFormat/translate.html#reBar)
:   Re-bar overflow measures using the last known time signature.

    ```python
    >>> irl2 = corpus.parse('irl', number=2)
    >>> irl2.metadata.title
    'Aililiu na Gamhna, S.35'
    >>> music21Part = irl2[1]
    ```

    The whole part is in 2/4 time, but there are some measures expressed in 4/4 time
    without an explicit time signature change, an error in abc parsing due to the
    omission of barlines. The method will split those measures such that they conform
    to the last time signature, in this case 2/4. The default is to reBar in place.
    The measure numbers are updated accordingly.

    (NOTE: reBar is called automatically in abcToStreamPart, hence not demonstrated below.)

    The key signature and clef are assumed to be the same in the second measure after the
    split, so both are omitted. If the time signature is not the same in the second measure,
    the new time signature is indicated, and the measure following returns to the last time
    signature, except in the case that a new time signature is indicated.

    ```python
    >>> music21Part.measure(15).show('text')
    {0.0} <music21.note.Note A>
    {1.0} <music21.note.Note A>
    ```

    ```python
    >>> music21Part.measure(16).show('text')
    {0.0} <music21.note.Note A>
    {0.5} <music21.note.Note B->
    {1.0} <music21.note.Note A>
    {1.5} <music21.note.Note G>
    ```

    An example where the time signature wouldn’t be the same. This score is
    mistakenly marked as 4/4, but has some measures that are longer.

    ```python
    >>> irl15 = corpus.parse('irl', number=15)
    >>> irl15.metadata.title
    'Esternowe, S. 60'
    >>> music21Part2 = irl15.parts.first()  # 4/4 time signature
    >>> music21Part2.measure(1).show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note A>
    {1.5} <music21.note.Note G>
    {2.0} <music21.note.Note E>
    {2.5} <music21.note.Note G>
    >>> music21Part2.measure(1)[-1].duration.quarterLength
    1.5
    ```

    ```python
    >>> music21Part2.measure(2).show('text')
    {0.0} <music21.meter.TimeSignature 1/8>
    {0.0} <music21.note.Note E>
    ```

    * Changed in v5: inPlace is False by default, and a keyword only argument.
