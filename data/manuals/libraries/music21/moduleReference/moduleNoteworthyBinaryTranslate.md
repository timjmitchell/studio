Source: https://music21.org/music21docs/moduleReference/moduleNoteworthyBinaryTranslate.html

# music21.noteworthy.binaryTranslate

Attempts at reading pure .nwc files in music21

First will solve uncompressed .nwc then compressed .nwc

Thanks to Juria90 and the nwc2xml project for solving so many of the documentation problems.
No part of this code is taken from that project, but this project would have been impossible
without his work.

Translates .nwc into .nwctxt and then uses Jordi Guillen’s .nwctxt translator to go from
there to music21.

BETA – does not work for many file elements and is untested.

Demo, showing the extent of problems. The measure numbers are not set. Lyrics are missing.
Drum is still poorly handled.
This is very beta. Much better would be to convert the file into .xml or .nwctxt first.

```python
>>> c = converter.parse('/Users/Hildegard/Desktop/test1.nwc')
>>> c.show('text')
{0.0} <music21.metadata.Metadata object at ...>
{0.0} <music21.stream.Part ...>
    {0.0} <music21.instrument.Violin 'Violin'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.tempo.MetronomeMark animato Quarter=120>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note C>
        {2.0} <music21.note.Note C>
        {3.0} <music21.note.Note B>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note C>
{0.0} <music21.stream.Part ...>
    {0.0} <music21.instrument.Violin 'Violin'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.5} <music21.note.Note G>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note G>
{0.0} <music21.stream.Part ...>
    {0.0} <music21.instrument.Viola 'Viola'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.AltoClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D>
        {2.0} <music21.note.Note C#>
        {2.6667} <music21.note.Note D>
        {3.3333} <music21.note.Note E>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note E>
{0.0} <music21.stream.Part ...>
    {0.0} <music21.instrument.Violoncello 'Violoncello'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note G>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note C>

>>> c = converter.parse('/Users/Hildegard/Desktop/jingle1.nwc')
>>> c.show('text')
{0.0} <music21.metadata.Metadata object at 0x7fe8c0a5ffa0>
{0.0} <music21.stream.Part 0x7fe8c0920100>
    {0.0} <music21.instrument.Piano 'Piano'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.expressions.TextExpression 'Lively'>
        {0.0} <music21.expressions.TextExpression 'F'>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.tempo.MetronomeMark animato Quarter=120>
        {0.0} <music21.key.KeySignature of 1 flat>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Rest quarter>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Rest quarter>
    {8.0} <music21.stream.Measure 1 offset=8.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note C>
        {2.0} <music21.note.Note F>
        {3.5} <music21.note.Note G>
    {12.0} <music21.stream.Measure 2 offset=12.0>
        {0.0} <music21.note.Note A>
        {3.0} <music21.note.Rest quarter>
    {16.0} <music21.stream.Measure 3 offset=16.0>
        {0.0} <music21.expressions.TextExpression 'Bb'>
        {0.0} <music21.note.Note B->
        {1.0} <music21.note.Note B->
        {2.0} <music21.note.Note B->
        {3.5} <music21.note.Note B->
    {20.0} <music21.stream.Measure 4 offset=20.0>
        {0.0} <music21.expressions.TextExpression 'F'>
        {0.0} <music21.note.Note B->
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
        {3.5} <music21.note.Note A>
    {24.0} <music21.stream.Measure 5 offset=24.0>
        {0.0} <music21.expressions.TextExpression 'G'>
        {0.0} <music21.bar.Barline type=regular>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note G>
        {2.0} <music21.note.Note G>
        {3.0} <music21.note.Note A>
    {28.0} <music21.stream.Measure 6 offset=28.0>
        {0.0} <music21.expressions.TextExpression 'C7'>
        {0.0} <music21.note.Note G>
        {2.0} <music21.note.Note C>
        {4.0} <music21.bar.Repeat direction=end>
    {28.0} <music21.spanner.RepeatBracket 1
            <music21.stream.Measure 5 offset=24.0><music21.stream.Measure 6 offset=28.0>>
    {32.0} <music21.stream.Measure 7 offset=32.0>
        {0.0} <music21.expressions.TextExpression 'C7'>
        {0.0} <music21.bar.Barline type=regular>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note C>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note G>
    {36.0} <music21.stream.Measure 8 offset=36.0>
        {0.0} <music21.expressions.TextExpression 'F'>
        {0.0} <music21.note.Note F>
        {3.0} <music21.note.Rest quarter>
{0.0} <music21.stream.Part 0x7fe8c0921660>
    {0.0} <music21.instrument.Piano 'Piano'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.key.KeySignature of 1 flat>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.chord.Chord F3 A3 C4>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.chord.Chord F3 A3 C4>
    {8.0} <music21.stream.Measure 1 offset=8.0>
        {0.0} <music21.chord.Chord F3 A3 C4>
    {12.0} <music21.stream.Measure 2 offset=12.0>
        {0.0} <music21.chord.Chord F3 A3 C4>
        {1.0} <music21.note.Rest quarter>
        {2.0} <music21.chord.Chord F3 A3 C4>
        {3.0} <music21.note.Rest quarter>
    {16.0} <music21.stream.Measure 3 offset=16.0>
        {0.0} <music21.chord.Chord F3 B-3 D4>
    {20.0} <music21.stream.Measure 4 offset=20.0>
        {0.0} <music21.chord.Chord F3 A3 C4>
        {1.0} <music21.note.Rest quarter>
        {2.0} <music21.note.Rest half>
    {24.0} <music21.stream.Measure 5 offset=24.0>
        {0.0} <music21.bar.Barline type=regular>
        {0.0} <music21.chord.Chord G3 B3>
        {2.0} <music21.note.Rest half>
    {28.0} <music21.stream.Measure 6 offset=28.0>
        {0.0} <music21.chord.Chord E3 B-3 C4>
        {4.0} <music21.bar.Repeat direction=end>
    {28.0} <music21.spanner.RepeatBracket 1
             <music21.stream.Measure 5 offset=24.0><music21.stream.Measure 6 offset=28.0>>
    {32.0} <music21.stream.Measure 7 offset=32.0>
        {0.0} <music21.bar.Barline type=regular>
        {0.0} <music21.chord.Chord E3 B-3 C4>
        {1.0} <music21.note.Rest quarter>
        {2.0} <music21.note.Rest half>
    {36.0} <music21.stream.Measure 8 offset=36.0>
        {0.0} <music21.chord.Chord F3 A3 C4>
        {3.0} <music21.note.Rest quarter>
```

## FontDict

class music21.noteworthy.binaryTranslate.FontDict[[source]](../_modules/music21/noteworthy/binaryTranslate.html#FontDict)

## NWCConverter

class music21.noteworthy.binaryTranslate.NWCConverter(*\*\*keywords*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter)
:   A converter object for binary .nwc files. Do not normally use directly; use converter.parse.

    ```python
    >>> nwcc = noteworthy.binaryTranslate.NWCConverter()
    >>> nwcc
    <music21.noteworthy.binaryTranslate.NWCConverter object at 0x...>
    >>> nwcc.fileContents
    b''
    >>> nwcc.parsePosition
    0
    >>> nwcc.version  # version of nwc file to be parsed
    200
    >>> nwcc.numberOfStaves
    0
    >>> nwcc.staves
    []
    ```

[`NWCConverter`](#music21.noteworthy.binaryTranslate.NWCConverter "music21.noteworthy.binaryTranslate.NWCConverter") methods

NWCConverter.advanceToNotNUL(*nul: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") = b'\x00'*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.advanceToNotNUL)

NWCConverter.byteToInt(*updateParsePosition=True*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.byteToInt)
:   changes a byte into an unsigned int
    (i.e., if the byte is > 127 then it’s subtracted from 256)

NWCConverter.byteToSignedInt(*updateParsePosition=True*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.byteToSignedInt)
:   changes a byte into a signed int
    (i.e., if the byte is > 127 then it’s subtracted from 256)

NWCConverter.dumpToNWCText() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.dumpToNWCText)

NWCConverter.fileVersion(*updateParsePosition=True*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.fileVersion)

NWCConverter.isValidNWCFile(*updateParsePosition=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.isValidNWCFile)

NWCConverter.parse()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.parse)
:   the main parse routine called by parseFile() or parseString()

NWCConverter.parseFile(*fp: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.parseFile)
:   Parse a file (calls .toStream)

    ```python
    >>> fp = '/Users/cuthbert/desktop/cuthbert_test1.nwc'
    >>> nwcc = noteworthy.binaryTranslate.NWCConverter()
    >>> nwcc.fileContents
    b''
    >>> streamObj = nwcc.parseFile(fp)
    >>> len(nwcc.fileContents)  # binary
    1139
    >>> nwcc.fileContents[0:80]
    b'[NoteWorthy ArtWare]\x00\x00\x00[NoteWorthy
             Composer]\x00\x01\x02\x02\x00\x00\x00N/A\x000_JldRQMSKq6M5a3FQqK_g\x00\x00\x00'
    >>> streamObj
    <music21.stream.Score ...>
    ```

NWCConverter.parseHeader() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.parseHeader)
:   Sets a ton of information from the header, and advances the parse position.

NWCConverter.parseString(*bytesIn: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") = b''*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.parseString)
:   same as parseFile but takes a string (in Py3, bytes) of binary data instead.

NWCConverter.readBytes(*bytesToRead=1*, *updateParsePosition=True*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.readBytes)
:   reads the next bytesToRead bytes and then (optionally) updates self.parsePosition

NWCConverter.readLEShort(*updateParsePosition=True*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.readLEShort)
:   Helper module: read a little-endian short value to an integer

    ```python
    >>> nwcc = noteworthy.binaryTranslate.NWCConverter()
    >>> nwcc.fileContents = b''
    >>> nwcc.parsePosition
    0
    >>> nwcc.readLEShort()
    258
    >>> nwcc.parsePosition
    2
    >>> nwcc.readLEShort()
    259
    >>> nwcc.parsePosition
    4
    ```

    Or to not update the parsePosition, send False:
    >>> nwcc.parsePosition = 0
    >>> nwcc.readLEShort(False)
    258
    >>> nwcc.readLEShort(False)
    258
    >>> nwcc.parsePosition
    0

NWCConverter.readToNUL(*updateParsePosition=True*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.readToNUL)
:   reads self.fileContents up to, but not including, the next position of x00.

    updates the parsePosition unless updateParsePosition is False

NWCConverter.skipBytes(*numBytes=1*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.skipBytes)

NWCConverter.toStream()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCConverter.toStream)

## NWCObject

class music21.noteworthy.binaryTranslate.NWCObject(*staffParent: [NWCStaff](#music21.noteworthy.binaryTranslate.NWCStaff "music21.noteworthy.binaryTranslate.NWCStaff")*, *parserParent: [NWCConverter](#music21.noteworthy.binaryTranslate.NWCConverter "music21.noteworthy.binaryTranslate.NWCConverter")*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject)
:   NWCObject class is a union that can be used for each type of object contained in a staff.

    An object binary blob starts with its type.
    The parse() method calls the appropriate method depending on the object type.
    Each parsing method should set up the ‘dumpMethod’ method that return the nwctxt version
    of the object.

[`NWCObject`](#music21.noteworthy.binaryTranslate.NWCObject "music21.noteworthy.binaryTranslate.NWCObject") methods

NWCObject.barline()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.barline)
:   Bar line
    2 bytes

NWCObject.clef()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.clef)
:   clef info,
    4 bytes

NWCObject.dynamic()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.dynamic)
:   dynamics
    7 bytes

NWCObject.dynamicVariation()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.dynamicVariation)
:   Dynamic variation
    3 bytes

NWCObject.ending()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.ending)
:   Endings
    2 bytes

NWCObject.flowDir()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.flowDir)
:   Flow
    4 bytes

NWCObject.instrument()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.instrument)
:   Instrument
    8 bytes

NWCObject.keySig()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.keySig)
:   Key signature
    10 bytes

NWCObject.mpc()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.mpc)
:   Midi Instructions
    34 bytes

NWCObject.note()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.note)
:   Note
    8 bytes

NWCObject.noteChordMember()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.noteChordMember)
:   Chord member
    8 bytes + n Note objects

NWCObject.parse()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.parse)
:   determine what type of object I am, and set things accordingly

NWCObject.pedal()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.pedal)
:   Pedal
    3 bytes

NWCObject.performance()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.performance)
:   Performance
    3 bytes

NWCObject.rest()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.rest)
:   Rest
    8 bytes

NWCObject.restChordMember()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.restChordMember)
:   Rest chord
    10 bytes

NWCObject.setDurationForObject()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.setDurationForObject)
:   get duration string for note or rest

NWCObject.tempo()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.tempo)
:   Tempo indications
    5 bytes + null terminated string

NWCObject.tempoVariation()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.tempoVariation)
:   Tempo variation
    4 bytes

NWCObject.textObj()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.textObj)
:   Text
    3 bytes + null terminated string

NWCObject.timeSig()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCObject.timeSig)
:   Time signature
    6 bytes

## NWCStaff

class music21.noteworthy.binaryTranslate.NWCStaff(*parent: [NWCConverter](#music21.noteworthy.binaryTranslate.NWCConverter "music21.noteworthy.binaryTranslate.NWCConverter")*)[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCStaff)
:   A NWCStaff is a list of NWCObjects (see [`parseObjects()`](#music21.noteworthy.binaryTranslate.NWCStaff.parseObjects "music21.noteworthy.binaryTranslate.NWCStaff.parseObjects")) associated to metadata
    (see [`parseHeader()`](#music21.noteworthy.binaryTranslate.NWCStaff.parseHeader "music21.noteworthy.binaryTranslate.NWCStaff.parseHeader")). It may also contain some lyrics (see [`parseLyrics()`](#music21.noteworthy.binaryTranslate.NWCStaff.parseLyrics "music21.noteworthy.binaryTranslate.NWCStaff.parseLyrics")).
    It defines a [`dump()`](#music21.noteworthy.binaryTranslate.NWCStaff.dump "music21.noteworthy.binaryTranslate.NWCStaff.dump") method that return a list of string containing the
    nwctxt-formatted content of each object of the staff.

[`NWCStaff`](#music21.noteworthy.binaryTranslate.NWCStaff "music21.noteworthy.binaryTranslate.NWCStaff") methods

NWCStaff.dump() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCStaff.dump)

NWCStaff.parse()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCStaff.parse)

NWCStaff.parseHeader()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCStaff.parseHeader)

NWCStaff.parseLyrics()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCStaff.parseLyrics)

NWCStaff.parseObjects()[[source]](../_modules/music21/noteworthy/binaryTranslate.html#NWCStaff.parseObjects)
