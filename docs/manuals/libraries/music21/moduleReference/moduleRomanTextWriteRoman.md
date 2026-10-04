Source: https://music21.org/music21docs/moduleReference/moduleRomanTextWriteRoman.html

# music21.romanText.writeRoman

Writer for the ‘RomanText’ format (Tymoczko, Gotham, Cuthbert, & Ariza ISMIR 2019)

## RnWriter

class music21.romanText.writeRoman.RnWriter(*obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/romanText/writeRoman.html#RnWriter)
:   Extracts the relevant information from a source
    (usually a `Stream` of
    [`RomanNumeral`](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral") objects) for
    writing to text files in the ‘RomanText’ format (rntxt).

    Writing rntxt is handled externally in the
    `WriteRoman()` so
    most users will never need to call this class directly, only invoking
    it indirectly through .write(‘rntxt’).
    Possible exceptions include users who want to convert Roman numerals into rntxt type
    strings and want to work with those strings directly, without writing to disk.

    For consistency with the
    [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") and [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write")
    methods across music21, this class is theoretically callable on
    any type of music21 object.
    Most relevant use cases will involve calling a
    stream containing one or more Roman numerals.
    This class supports any such stream:
    an `Opus` object of one or more scores,
    a `Score` with or without `Part` (s),
    a `Part`, or
    a `Measure`.

    ```python
    >>> scoreBach = corpus.parse('bach/choraleAnalyses/riemenschneider004.rntxt')
    >>> rnWriterFromScore = romanText.writeRoman.RnWriter(scoreBach)
    ```

    The strings are stored in the RnWriter’s combinedList variable, starting with the metadata:

    ```python
    >>> rnWriterFromScore.combinedList[0]
    'Composer: J. S. Bach'
    ```

    Composer and work metadata is inherited from score metadata wherever possible.
    A composer entry will register directly as will any entries for
    workTitle, movementNumber, and movementName
    (see [`prepTitle()`](#music21.romanText.writeRoman.RnWriter.prepTitle "music21.romanText.writeRoman.RnWriter.prepTitle") for details).

    ```python
    >>> rnWriterFromScore.combinedList[0] == 'Composer: ' + rnWriterFromScore.composer
    True
    ```

    As always, these metadata entries are user-settable.
    Make any adjustments to the metadata before calling this class.

    After the metadata, the list continues with strings for each measure in order.
    Here’s the last in our example:

    ```python
    >>> rnWriterFromScore.combinedList[-1]
    'm10 V6/V b2 V b3 I'
    ```

    In the case of the score, the top part is assumed to contain the Roman numerals.
    This is consistent with the parsing of rntxt which involves putting Roman numerals in a part
    (the top, and only part) within a score.

    In all other cases, the objects are iteratively inserted into larger streams until we end up
    with a part object (e.g. measure > part).

    ```python
    >>> rn = roman.RomanNumeral('viio64', 'a')
    >>> rnWriterFromRn = romanText.writeRoman.RnWriter(rn)
    >>> rnWriterFromRn.combinedList[0]
    'Composer: Composer unknown'
    ```

    ```python
    >>> rnWriterFromRn.combinedList[-1]
    'm0 a: viio64'
    ```

[`RnWriter`](#music21.romanText.writeRoman.RnWriter "music21.romanText.writeRoman.RnWriter") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RnWriter`](#music21.romanText.writeRoman.RnWriter "music21.romanText.writeRoman.RnWriter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RnWriter`](#music21.romanText.writeRoman.RnWriter "music21.romanText.writeRoman.RnWriter") methods

RnWriter.getChordString(*rn: [RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral")*)[[source]](../_modules/music21/romanText/writeRoman.html#RnWriter.getChordString)
:   Produce a string from a Roman numeral with the chord and
    the key if that key constitutes a change from the foregoing context.

    ```python
    >>> p = stream.Part()
    >>> m = stream.Measure()
    >>> m.insert(0, meter.TimeSignature('4/4'))
    >>> m.insert(0, roman.RomanNumeral('V', 'G'))
    >>> p.insert(0, m)
    >>> testCase = romanText.writeRoman.RnWriter(p)
    >>> sameKeyChord = testCase.getChordString(roman.RomanNumeral('I', 'G'))
    >>> sameKeyChord
    'I'
    ```

    ```python
    >>> changeKeyChord = testCase.getChordString(roman.RomanNumeral('V', 'D'))
    >>> changeKeyChord
    'D: V'
    ```

RnWriter.prepSequentialListOfLines()[[source]](../_modules/music21/romanText/writeRoman.html#RnWriter.prepSequentialListOfLines)
:   Prepares a sequential list of text lines, with time signatures and Roman numerals
    adding this to the (already prepared) metadata preamble ready for printing.

    ```python
    >>> p = stream.Part()
    >>> m = stream.Measure(number=1)
    >>> m.insert(0, meter.TimeSignature('4/4'))
    >>> m.insert(0, roman.RomanNumeral('V', 'G'))
    >>> p.insert(0, m)
    >>> testCase = romanText.writeRoman.RnWriter(p)
    >>> testCase.combinedList[-1]  # Last entry, after the metadata
    'm1 G: V'
    ```

    This follows the wider rntxt syntax in supporting
    Time Signature (`TimeSignature`) changes and
    Repeats marks ([`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat"))
    but only (currently) between measures.

    Let’s add a new measure to the stream we started,
    with a time signature change beforehand and
    both start and end repeats in it:

    ```python
    >>> m2 = stream.Measure(number=2)
    >>> m2.insert(0, meter.TimeSignature('3/4'))
    >>> m2.leftBarline = bar.Repeat(direction='start')
    >>> m2.rightBarline = bar.Repeat(direction='end')
    >>> m2.insert(0, roman.RomanNumeral('I', 'G'))
    >>> p.insert(0, m2)
    >>> testCase = romanText.writeRoman.RnWriter(p)
    ```

    The last line of the .combinedList gives the new measure:

    ```python
    >>> testCase.combinedList[-1]
    'm2 ||: I :||'
    ```

    The line before that gives the time signature change:

    ```python
    >>> testCase.combinedList[-2]
    'Time Signature: 3/4'
    ```

RnWriter.prepTitle(*md: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata")*)[[source]](../_modules/music21/romanText/writeRoman.html#RnWriter.prepTitle)
:   Attempt to prepare a single work title from the score metadata looking at each of
    the title, movementNumber and movementName attributes.
    Failing that, a placeholder ‘Title unknown’ stands in.

    ```python
    >>> s = stream.Score()
    >>> rnScore = romanText.writeRoman.RnWriter(s)
    >>> rnScore.title
    'Title unknown'
    ```

    ```python
    >>> s.insert(0, metadata.Metadata())
    >>> s.metadata.title = 'Fake title'
    >>> s.metadata.movementNumber = 123456789
    >>> s.metadata.movementName = 'Fake movementName'
    >>> rnScoreWithMD = romanText.writeRoman.RnWriter(s)
    >>> rnScoreWithMD.title
    'Fake title - No.123456789: Fake movementName'
    ```

## Functions

music21.romanText.writeRoman.intBeat(*beat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *roundValue: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 2*)[[source]](../_modules/music21/romanText/writeRoman.html#intBeat)
:   Converts beats to integers if possible, and otherwise to rounded decimals.
    Accepts input as string, int, float, or fractions.Fraction.

    ```python
    >>> testInt = romanText.writeRoman.intBeat(1, roundValue=2)
    >>> testInt
    1
    ```

    ```python
    >>> testFrac = romanText.writeRoman.intBeat(8 / 3, roundValue=2)
    >>> testFrac
    2.67
    ```

    ```python
    >>> testStr = romanText.writeRoman.intBeat('0.666666666', roundValue=2)
    >>> testStr
    0.67
    ```

    The roundValue sets the number of decimal places to round to. The default is two:

    ```python
    >>> testRound2 = romanText.writeRoman.intBeat(1.11111111, roundValue=2)
    >>> testRound2
    1.11
    ```

    But this can be set to any integer:

    ```python
    >>> testRound1 = romanText.writeRoman.intBeat(1.11111111, roundValue=1)
    >>> testRound1
    1.1
    ```

    Raises an error if called on a negative value.

music21.romanText.writeRoman.rnString(*measureNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *beat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *chordString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *inString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = ''*)[[source]](../_modules/music21/romanText/writeRoman.html#rnString)
:   Creates or extends a string of RomanText such that the output corresponds to a single
    measure line.

    If the inString is not given, None, or an empty string then this function starts a new line.

    ```python
    >>> lineStarter = romanText.writeRoman.rnString(14, 1, 'G: I')
    >>> lineStarter
    'm14 G: I'
    ```

    For any other inString, that string is the start of a measure line continued by the new values

    ```python
    >>> continuation = romanText.writeRoman.rnString(14, 2, 'viio6', 'm14 G: I')
    >>> continuation
    'm14 G: I b2 viio6'
    ```

    Naturally, this function requires the measure number of any such continuation to match
    that of the inString and raises an error where that is not the case.

    As these examples show, the chordString can be a Roman numeral alone (e.g. ‘viio6’)
    or one prefixed by a change of key (‘G: I’).
