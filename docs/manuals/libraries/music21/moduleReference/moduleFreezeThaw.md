Source: https://music21.org/music21docs/moduleReference/moduleFreezeThaw.html

# music21.freezeThaw

This module contains objects for storing complete Music21Objects, especially
Stream and Score objects on disk. Freezing (or “pickling”) refers to
writing the object to a file on disk (or to a string). Thawing (or
“unpickling”) refers to reading in a string or file and returning a Music21
object.

This module offers alternatives to writing a Score to MusicXML with
s.write(‘musicxml’). FreezeThaw has some advantages over using .write():
virtually every aspect of a music21 object is retained when Freezing. So
objects like roman.RomanNumeral, which aren’t supported by most formats, can be
stored with FreezeThaw and then read back again. Freezing is also much
faster than most conversion methods. But there’s a big downside: only
music21 and Python can use the Thaw side to get back Music21Objects
(though more information can be brought out of the JSONFreeze format through
any .json reader). In fact, there’s not even a guarantee that future versions
of music21 will be able to read a frozen version of a Stream. So the
advantages and disadvantages of this model definitely need to be kept in mind.

There are two formats that freezeThaw can produce: “Pickle” or JSON (for
JavaScript Object Notation – essentially a string representation of the
JavaScript equivalent of a Python dictionary).

Pickle is a Python-specific
idea for storing objects. The pickle module stores objects as a text file
that can’t be easily read by non-Python applications; it also isn’t guaranteed
to work across Python versions or even computers. However, it works well, is
fast, and is a standard part of python.

JSON was originally created to pass
JavaScript objects from a web server to a web browser, but its utility
(combining the power of XML with the ease of use of objects) has made it a
growing standard for other languages. (see
<https://docs.python.org/3/library/json.html>).
Music21 has two implementations of JSON (confusing, no?)
because we weren’t sure and are still not sure which will be best in the long-run:
the first approach
uses explicit lists of attributes that need to be stored and just saves those. This uses a
homemade set of methods that are specifically tailored for music21; but it misses some things that
may be important to you. The second approach uses the freely distributable
jsonpickle module. This approach probably stores more data than
a person not using music21 or python is likely to want, but can be used to get back an entire
music21 Stream with no conversion.

Both JSON and Pickle files can be huge, but freezeThaw can compress them with
gzip or ZipFile and thus they’re not that large at all.

Streams need to be run through .setupSerializationScaffold and .teardownSerializationScaffold
before and after either Pickle or jsonpickle in order to restore all the weakrefs that we use.

The name freezeThaw comes from Perl’s implementation of similar methods – I
like the idea of thawing something that’s frozen; “unpickling” just doesn’t
seem possible. In any event, I needed a name that wouldn’t already
exist in the Python namespace.

## StreamFreezeThawBase

class music21.freezeThaw.StreamFreezeThawBase[[source]](../_modules/music21/freezeThaw.html#StreamFreezeThawBase)
:   Contains a few methods that are used for both
    StreamFreezer and StreamThawer

[`StreamFreezeThawBase`](#music21.freezeThaw.StreamFreezeThawBase "music21.freezeThaw.StreamFreezeThawBase") methods

StreamFreezeThawBase.getJsonFp(*directory: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/freezeThaw.html#StreamFreezeThawBase.getJsonFp)

StreamFreezeThawBase.getPickleFp(*directory: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/freezeThaw.html#StreamFreezeThawBase.getPickleFp)

## StreamFreezer

class music21.freezeThaw.StreamFreezer(*streamObj=None*, *fastButUnsafe=False*, *topLevel=True*, *streamIds=None*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer)
:   This class is used to freeze a Stream, preparing it for serialization
    and providing conversion routines.

    In general, use [`freeze()`](moduleConverter.html#music21.converter.freeze "music21.converter.freeze")
    for serializing to a file.

    Use the `unfreeze()` to read from a
    serialized file

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note('C4'), 8)
    >>> temp = [s[n].transpose(n, inPlace=True) for n in range(len(s))]
    ```

    ```python
    >>> sf = freezeThaw.StreamFreezer(s)  # provide a Stream at init
    >>> data = sf.writeStr(fmt='pickle')  # pickle is default format
    ```

    ```python
    >>> st = freezeThaw.StreamThawer()
    >>> st.openStr(data)
    >>> s = st.stream
    >>> s.show('t')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C#>
    {2.0} <music21.note.Note D>
    {3.0} <music21.note.Note E->
    {4.0} <music21.note.Note E>
    {5.0} <music21.note.Note F>
    {6.0} <music21.note.Note F#>
    {7.0} <music21.note.Note G>
    ```

    ```python
    >>> sf2 = freezeThaw.StreamFreezer(s)  # do not reuse StreamFreezers
    >>> data2 = sf2.writeStr(fmt='jsonpickle')
    ```

    ```python
    >>> st2 = freezeThaw.StreamThawer()
    >>> st2.openStr(data2)
    >>> s2 = st2.stream
    >>> s2.show('t')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C#>
    {2.0} <music21.note.Note D>
    {3.0} <music21.note.Note E->
    {4.0} <music21.note.Note E>
    {5.0} <music21.note.Note F>
    {6.0} <music21.note.Note F#>
    {7.0} <music21.note.Note G>
    ```

    ```python
    >>> c = corpus.parse('luca/gloria')
    >>> sf = freezeThaw.StreamFreezer(c)
    >>> data = sf.writeStr(fmt='pickle')
    ```

    ```python
    >>> st = freezeThaw.StreamThawer()
    >>> st.openStr(data)
    >>> s2 = st.stream
    >>> len(s2.parts[0].measure(7).notes) == 6
    True
    ```

    JSONPickle is also an acceptable way of Freezing streams. Especially
    for going to music21j in Javascript:

    ```python
    >>> sf2 = freezeThaw.StreamFreezer(c)  # do not reuse StreamFreezers
    >>> data2 = sf2.writeStr(fmt='jsonpickle')
    >>> st2 = freezeThaw.StreamThawer()
    >>> st2.openStr(data2)
    >>> s3 = st2.stream
    >>> len(s3.parts[0].measure(7).notes) == 6
    True
    ```

    Or by writing to disk:

    ```python
    >>> sf2 = freezeThaw.StreamFreezer(c)  # do not reuse StreamFreezers
    >>> fp2 = sf2.write(fmt='jsonpickle')
    >>> st2 = freezeThaw.StreamThawer()
    >>> st2.open(fp2)
    >>> s3 = st2.stream
    >>> len(s3.parts[0].measure(7).notes) == 6
    True
    ```

[`StreamFreezer`](#music21.freezeThaw.StreamFreezer "music21.freezeThaw.StreamFreezer") bases

* [`StreamFreezeThawBase`](#music21.freezeThaw.StreamFreezeThawBase "music21.freezeThaw.StreamFreezeThawBase")

[`StreamFreezer`](#music21.freezeThaw.StreamFreezer "music21.freezeThaw.StreamFreezer") methods

StreamFreezer.findActiveStreamIdsInHierarchy(*hierarchyObject=None*, *getSpanners=True*, *getVariants=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/freezeThaw.html#StreamFreezer.findActiveStreamIdsInHierarchy)
:   Return a list of all Stream ids anywhere in the hierarchy. By id,
    we mean id(s) not s.id – so they are memory locations and unique.

    Stores them in .streamIds.

    if hierarchyObject is None, uses self.stream.

    ```python
    >>> sc = stream.Score()
    >>> p1 = stream.Part()
    >>> p2 = stream.Part()
    >>> m1 = stream.Measure()
    >>> v1 = stream.Voice()
    >>> m1.insert(0, v1)
    >>> p2.insert(0, m1)
    >>> sc.insert(0, p1)
    >>> sc.insert(0, p2)
    >>> shouldFindIds = [id(sc), id(p1), id(p2), id(m1), id(v1)]
    ```

    fastButUnsafe is needed because it does not make a deepcopy
    and thus lets you compare ids before and after.

    ```python
    >>> sf = freezeThaw.StreamFreezer(sc, fastButUnsafe=True)
    >>> foundIds = sf.findActiveStreamIdsInHierarchy()
    >>> for thisId in shouldFindIds:
    ...     if thisId not in foundIds:
    ...         raise ValueError('Missing Id')
    >>> for thisId in foundIds:
    ...     if thisId not in shouldFindIds:
    ...         raise ValueError('Additional Id Found')
    ```

    Spanners are included unless getSpanners is False

    ```python
    >>> staffGroup = layout.StaffGroup([p1, p2])
    >>> sc.insert(0, staffGroup)
    ```

    [`StaffGroup`](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup") is a spanner, so
    it should be found

    ```python
    >>> sf2 = freezeThaw.StreamFreezer(sc, fastButUnsafe=True)
    >>> foundIds = sf2.findActiveStreamIdsInHierarchy()
    ```

    But you won’t find the id of the spanner itself in
    the foundIds:

    ```python
    >>> id(staffGroup) in foundIds
    False
    ```

    instead it’s the id of the storage object:

    ```python
    >>> id(staffGroup.spannerStorage) in foundIds
    True
    ```

    Variants are treated similarly:

    ```python
    >>> s = stream.Stream()
    >>> m = stream.Measure()
    >>> m.append(note.Note(type='whole'))
    >>> s.append(m)
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> m2 = stream.Measure()
    >>> n2 = note.Note('D#4')
    >>> n2.duration.type = 'whole'
    >>> m2.append(n2)
    >>> s2.append(m2)
    >>> v = variant.Variant(s2.elements)
    >>> s.insert(0, v)
    >>> sf = freezeThaw.StreamFreezer(s, fastButUnsafe=True)
    >>> allIds = sf.findActiveStreamIdsInHierarchy()
    >>> len(allIds)
    4
    >>> for streamElement in [s, m, m2, v._stream]:
    ...    if id(streamElement) not in allIds:
    ...        print('this should not happen!', allIds, id(streamElement))
    ```

    N.B. with variants:

    ```python
    >>> id(s2) == id(v._stream)
    False
    ```

    The method also sets self.streamIds to the returned list:

    ```python
    >>> sf.streamIds is allIds
    True
    ```

StreamFreezer.packStream(*streamObj=None*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.packStream)
:   Prepare the passed in Stream in place, return storage
    dictionary format.

    ```python
    >>> from pprint import pprint
    >>> s = stream.Stream()
    >>> n = note.Note('D#4')
    >>> s.append(n)
    >>> sf = freezeThaw.StreamFreezer(s)
    >>> pprint(sf.packStream())
    {'m21Version': (...), 'stream': <music21.stream.Stream 0x1289212>}
    ```

StreamFreezer.parseWriteFmt(*fmt*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.parseWriteFmt)
:   Parse a passed-in write format

    ```python
    >>> sf = freezeThaw.StreamFreezer()
    >>> sf.parseWriteFmt(None)
    'pickle'
    >>> sf.parseWriteFmt('JSON')
    'jsonpickle'
    ```

    Anything else returns ‘pickle’ as a default:

    ```python
    >>> sf.parseWriteFmt('inconceivable')
    'pickle'
    ```

StreamFreezer.recursiveClearSites(*startObj*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.recursiveClearSites)
:   recursively clear all sites, including activeSites, taking into account
    that spanners and variants behave differently.

    Called by setupSerializationScaffold.

    To be run after setupStoredElementOffsetTuples() has been run

    ```python
    >>> n = note.Note('D#4')
    >>> len(n.sites)
    1
    >>> s = stream.Stream()
    >>> s.id = 'stream s'
    >>> s.insert(10, n)
    >>> len(n.sites)
    2
    >>> s2 = stream.Stream()
    >>> s2.insert(20, n)
    >>> s2.id = 'stream s2'
    >>> len(n.sites)
    3
    ```

    ```python
    >>> n.getOffsetBySite(s)
    10.0
    >>> n.getOffsetBySite(s2)
    20.0
    ```

    ```python
    >>> sf = freezeThaw.StreamFreezer()
    ```

    This will remove n from s but leave the rest of the sites intact:

    ```python
    >>> sf.setupStoredElementOffsetTuples(s)
    >>> len(n.sites)
    2
    >>> n.getOffsetBySite(s)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object <music21.note.Note D#>
           is not stored in stream <music21.stream.Stream stream s>
    >>> n.getOffsetBySite(s2)
    20.0
    ```

    After recursiveClearSites n will be not know its location anywhere:

    ```python
    >>> sf.recursiveClearSites(s)
    >>> len(n.sites)  # just the None site
    1
    ```

    This leaves n and s2 in strange positions, because n is in s2.elements still:

    ```python
    >>> n in s2.elements
    True
    ```

    This predicament is why when the standard freezeThaw call is made, what is frozen is a
    deepcopy of the Stream so that nothing is left in an unusable position

StreamFreezer.removeStreamStatusClient(*streamObj*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.removeStreamStatusClient)
:   if s is a stream then

    s.streamStatus.\_client is s

    this can be hard to pickle, so this method removes the streamStatus.\_client from the
    streamObj (not recursive). Called by setupSerializationScaffold.

StreamFreezer.setupSerializationScaffold(*streamObj=None*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.setupSerializationScaffold)
:   Prepare this stream and all of its contents for pickle/pickling, that
    is, serializing and storing an object representation on file or as a string.

    The topLevel and streamIdsFound arguments are used to keep track of recursive calls.

    Note that this is a destructive process: elements contained within this Stream
    will have their sites cleared of all contents not in the hierarchy
    of the Streams. Thus, when doing a normal .write(‘pickle’)
    the Stream is deepcopied before this method is called. The
    attribute fastButUnsafe = True setting of StreamFreezer ignores the destructive
    effects of these processes and skips the deepcopy.

    ```python
    >>> a = stream.Stream()
    >>> n = note.Note()
    >>> n.duration.type = 'whole'
    >>> a.repeatAppend(n, 10)
    >>> sf = freezeThaw.StreamFreezer(a)
    >>> sf.setupSerializationScaffold()
    ```

StreamFreezer.setupStoredElementOffsetTuples(*streamObj*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.setupStoredElementOffsetTuples)
:   move all elements from .\_elements and .\_endElements
    to a new attribute .\_storedElementOffsetTuples
    which contains a list of tuples of the form
    (el, offset or ‘end’).

    Called by setupSerializationScaffold.

    ```python
    >>> s = stream.Measure()
    >>> n1 = note.Note('C#')
    >>> n2 = note.Note('E-')
    >>> bl1 = bar.Barline()
    >>> s.insert(0.0, n1)
    >>> s.insert(1.0, n2)
    >>> s.storeAtEnd(bl1)
    ```

    ```python
    >>> sFreeze = freezeThaw.StreamFreezer()
    >>> sFreeze.setupStoredElementOffsetTuples(s)
    >>> s._elements, s._endElements
    ([], [])
    >>> s._storedElementOffsetTuples
    [(<music21.note.Note C#>, 0.0),
     (<music21.note.Note E->, 1.0),
     (<music21.bar.Barline type=regular>, 'end')]
    >>> n1.getOffsetBySite(s)
    Traceback (most recent call last):
    music21.sites.SitesException: an entry for this object <music21.note.Note C#> is
         not stored in stream <music21.stream.Measure 0 offset=0.0>
    ```

    Trying it again, but now with substreams:

    ```python
    >>> s2 = stream.Measure()
    >>> n1 = note.Note('C#')
    >>> n2 = note.Note('E-')
    >>> bl1 = bar.Barline()
    >>> v1 = stream.Voice()
    >>> n3 = note.Note('F#')
    >>> v1.insert(2.0, n3)
    >>> s2.insert(0.0, n1)
    >>> s2.insert(1.0, n2)
    >>> s2.storeAtEnd(bl1)
    >>> s2.insert(2.0, v1)
    >>> sFreeze.setupStoredElementOffsetTuples(s2)
    ```

    ```python
    >>> v1._storedElementOffsetTuples
    [(<music21.note.Note F#>, 2.0)]
    >>> s2._storedElementOffsetTuples
    [(<music21.note.Note C#>, 0.0),
     (<music21.note.Note E->, 1.0),
     (<music21.stream.Voice ...>, 2.0),
     (<music21.bar.Barline type=regular>, 'end')]
    >>> s2._storedElementOffsetTuples[2][0] is v1
    True
    ```

StreamFreezer.write(*fmt='pickle'*, *fp=None*, *zipType=None*, *\*\*keywords*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.write)
:   For a supplied Stream, write a serialized version to
    disk in either ‘pickle’ or ‘jsonpickle’ format and
    return the filepath to the file.

    jsonpickle is the better format for transporting from
    one computer to another, but slower and may have some bugs.

    If zipType == ‘zlib’ then zlib compression is done after serializing.
    No other compression types are currently supported.

StreamFreezer.writeStr(*fmt=None*, *\*\*keywords*)[[source]](../_modules/music21/freezeThaw.html#StreamFreezer.writeStr)
:   Convert the object to a pickled/jsonpickled string
    and return the string

Methods inherited from [`StreamFreezeThawBase`](#music21.freezeThaw.StreamFreezeThawBase "music21.freezeThaw.StreamFreezeThawBase"):

|  |  |  |
| --- | --- | --- |
| * [`getJsonFp()`](#music21.freezeThaw.StreamFreezeThawBase.getJsonFp "music21.freezeThaw.StreamFreezeThawBase.getJsonFp") | * [`getPickleFp()`](#music21.freezeThaw.StreamFreezeThawBase.getPickleFp "music21.freezeThaw.StreamFreezeThawBase.getPickleFp") |  |

## StreamThawer

class music21.freezeThaw.StreamThawer[[source]](../_modules/music21/freezeThaw.html#StreamThawer)
:   This class is used to thaw a data string into a Stream

    In general user [`parse()`](moduleConverter.html#music21.converter.parse "music21.converter.parse") to read from a
    serialized file.

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note('C4'), 8)
    >>> temp = [s[n].transpose(n, inPlace=True) for n in range(len(s))]
    ```

    ```python
    >>> sf = freezeThaw.StreamFreezer(s)  # provide a Stream at init
    >>> data = sf.writeStr(fmt='pickle')  # pickle is default format
    ```

    ```python
    >>> sfOut = freezeThaw.StreamThawer()
    >>> sfOut.openStr(data)
    >>> s = sfOut.stream
    >>> s.show('t')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C#>
    {2.0} <music21.note.Note D>
    {3.0} <music21.note.Note E->
    {4.0} <music21.note.Note E>
    {5.0} <music21.note.Note F>
    {6.0} <music21.note.Note F#>
    {7.0} <music21.note.Note G>
    ```

[`StreamThawer`](#music21.freezeThaw.StreamThawer "music21.freezeThaw.StreamThawer") bases

* [`StreamFreezeThawBase`](#music21.freezeThaw.StreamFreezeThawBase "music21.freezeThaw.StreamFreezeThawBase")

[`StreamThawer`](#music21.freezeThaw.StreamThawer "music21.freezeThaw.StreamThawer") methods

StreamThawer.open(*fp*, *zipType=None*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.open)
:   For a supplied file path to a pickled stream, unpickle

StreamThawer.openStr(*fileData: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *pickleFormat=None*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.openStr)
:   Take bytes representing a Frozen(pickled/jsonpickled)
    Stream and convert it to a normal Stream.

    if format is None then the format is automatically
    determined from the bytes contents.

    The name of the function is a legacy of Py2. With
    pickle (not jsonpickle), it works on bytes, not strings.

StreamThawer.parseOpenFmt(*storage*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.parseOpenFmt)
:   Look at the file and determine the format

StreamThawer.restoreElementsFromTuples(*streamObj*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.restoreElementsFromTuples)
:   Take a Stream with elements and offsets stored in
    a list of tuples (element, offset or ‘end’) at
    \_storedElementOffsetTuples
    and restore it to the .\_elements and .\_endElements lists
    in the proper locations:

    ```python
    >>> s = stream.Measure()
    >>> s._elements, s._endElements
    ([], [])
    ```

    ```python
    >>> n1 = note.Note('C#')
    >>> n2 = note.Note('E-')
    >>> bl1 = bar.Barline()
    >>> tupleList = [(n1, 0.0), (n2, 1.0), (bl1, 'end')]
    >>> s._storedElementOffsetTuples = tupleList
    ```

    ```python
    >>> sThaw = freezeThaw.StreamThawer()
    >>> sThaw.restoreElementsFromTuples(s)
    >>> s.show('text')
    {0.0} <music21.note.Note C#>
    {1.0} <music21.note.Note E->
    {2.0} <music21.bar.Barline type=regular>
    >>> s._endElements
    [<music21.bar.Barline type=regular>]
    >>> s[1].getOffsetBySite(s)
    1.0
    ```

    Trying it again, but now with substreams:

    ```python
    >>> s2 = stream.Measure()
    >>> v1 = stream.Voice()
    >>> n3 = note.Note('F#')
    >>> v1._storedElementOffsetTuples = [(n3, 2.0)]
    >>> tupleList = [(n1, 0.0), (n2, 1.0), (bl1, 'end'), (v1, 2.0)]
    >>> s2._storedElementOffsetTuples = tupleList
    >>> sThaw.restoreElementsFromTuples(s2)
    >>> s2.show('text')
    {0.0} <music21.note.Note C#>
    {1.0} <music21.note.Note E->
    {2.0} <music21.stream.Voice ...>
        {2.0} <music21.note.Note F#>
    {5.0} <music21.bar.Barline type=regular>
    ```

StreamThawer.restoreStreamStatusClient(*streamObj*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.restoreStreamStatusClient)
:   Restore the streamStatus client to point to the Stream
    (do we do this for derivations? No: there should not be derivations stored.
    Other objects? Unclear at present.)

StreamThawer.teardownSerializationScaffold(*streamObj=None*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.teardownSerializationScaffold)
:   After rebuilding this Stream from pickled storage, prepare this as a normal Stream.

    If streamObj is None, runs it on the embedded stream

    ```python
    >>> a = stream.Stream()
    >>> n = note.Note()
    >>> n.duration.type = 'whole'
    >>> a.repeatAppend(n, 10)
    >>> sf = freezeThaw.StreamFreezer(a)
    >>> sf.setupSerializationScaffold()
    ```

    ```python
    >>> st = freezeThaw.StreamThawer()
    >>> st.teardownSerializationScaffold(a)
    ```

StreamThawer.unpackStream(*storage*)[[source]](../_modules/music21/freezeThaw.html#StreamThawer.unpackStream)
:   Convert from storage dictionary to Stream.

Methods inherited from [`StreamFreezeThawBase`](#music21.freezeThaw.StreamFreezeThawBase "music21.freezeThaw.StreamFreezeThawBase"):

|  |  |  |
| --- | --- | --- |
| * [`getJsonFp()`](#music21.freezeThaw.StreamFreezeThawBase.getJsonFp "music21.freezeThaw.StreamFreezeThawBase.getJsonFp") | * [`getPickleFp()`](#music21.freezeThaw.StreamFreezeThawBase.getPickleFp "music21.freezeThaw.StreamFreezeThawBase.getPickleFp") |  |
