Source: https://music21.org/music21docs/moduleReference/moduleMusedata.html

# music21.musedata

**N.B. in Dec. 2014 MuseData access was removed from music21 because the rights conflicted with
access computationally from music21. This module is retained for anyone who has such access,
however it is completely untested now and errors cannot and will not be fixed.**

Objects and resources for processing MuseData.

MuseData conversion from a file or URL to a `Stream` is available through
the music21 converter module’s [`parse()`](moduleConverter.html#music21.converter.parse "music21.converter.parse") function.

```python
>>> from music21 import *
>>> abcScore = converter.parse('d:/data/musedata/myScore.stage2')
```

Low level MuseData conversion is facilitated by the objects in this module and
`music21.musedata.translate.museDataToStreamScore()`.

## MuseDataWork

class music21.musedata.MuseDataWork[[source]](../_modules/music21/musedata.html#MuseDataWork)
:   A work might consist of one or more files.

[`MuseDataWork`](#music21.musedata.MuseDataWork "music21.musedata.MuseDataWork") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MuseDataWork`](#music21.musedata.MuseDataWork "music21.musedata.MuseDataWork") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MuseDataWork`](#music21.musedata.MuseDataWork "music21.musedata.MuseDataWork") methods

MuseDataWork.addFile(*fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musedata.html#MuseDataWork.addFile)
:   Open and read this file path or list of paths as MuseDataFile objects
    and set self.files

MuseDataWork.addString(*input\_str*)[[source]](../_modules/music21/musedata.html#MuseDataWork.addString)
:   Add a string representation acting like a part file

    ```python
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addString('WK#:581       MV#:3c\nBreitkopf & Hartel, Vol. 13\n' +
    ...               'Clarinet Quintet\n' +
    ...               'Trio II\n' +
    ...               '$  K:0   Q:6   T:3/4   X:-11   C:4\n' +
    ...               'C5     3        e     d  [     (&0p\n' +
    ...               'E5     3        e     d  ]')
    ```

    # TODO: Okay, so what? did we test this or demo anything?

MuseDataWork.getParts()[[source]](../_modules/music21/musedata.html#MuseDataWork.getParts)
:   Get all parts contained in all files associated with this work.
    A list of MuseDataPart objects that were created in a MuseDataFile.

## MuseDataDirectory

class music21.musedata.MuseDataDirectory(*dirOrList*)[[source]](../_modules/music21/musedata.html#MuseDataDirectory)
:   This class manages finding musedata files stored in a directory,
    comparing file names and examining subdirectories to determine which files are parts.

    Once found, a MuseDataWork, or a list of paths, can be returned

    A directory, or a list of file path stubs, such as that obtained within a zip file,
    can both be provided.

[`MuseDataDirectory`](#music21.musedata.MuseDataDirectory "music21.musedata.MuseDataDirectory") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MuseDataDirectory`](#music21.musedata.MuseDataDirectory "music21.musedata.MuseDataDirectory") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MuseDataDirectory`](#music21.musedata.MuseDataDirectory "music21.musedata.MuseDataDirectory") methods

MuseDataDirectory.getPaths(*group=None*)[[source]](../_modules/music21/musedata.html#MuseDataDirectory.getPaths)
:   Return sorted paths for a group, or None

MuseDataDirectory.isMusedataFile(*fp*)[[source]](../_modules/music21/musedata.html#MuseDataDirectory.isMusedataFile)

## MuseDataFile

class music21.musedata.MuseDataFile[[source]](../_modules/music21/musedata.html#MuseDataFile)
:   A MuseDataFile file may describe one or more MuseDataPart;
    a Score might need multiple files for complete definition.
    A MuseDataFile object can be created from a string.

    When read, one or more MuseDataPart objects are created and stored on self.parts.

[`MuseDataFile`](#music21.musedata.MuseDataFile "music21.musedata.MuseDataFile") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MuseDataFile`](#music21.musedata.MuseDataFile "music21.musedata.MuseDataFile") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MuseDataFile`](#music21.musedata.MuseDataFile "music21.musedata.MuseDataFile") methods

MuseDataFile.close()[[source]](../_modules/music21/musedata.html#MuseDataFile.close)

MuseDataFile.open(*fp*)[[source]](../_modules/music21/musedata.html#MuseDataFile.open)

MuseDataFile.read()[[source]](../_modules/music21/musedata.html#MuseDataFile.read)

MuseDataFile.readstr(*input\_str*)[[source]](../_modules/music21/musedata.html#MuseDataFile.readstr)
:   Read a string, dividing it into individual parts.

## MuseDataMeasure

class music21.musedata.MuseDataMeasure(*src=None*, *parent=None*)[[source]](../_modules/music21/musedata.html#MuseDataMeasure)
:   A MuseDataMeasure is an abstraction of the data contained within a measure definitions.

    This needs to be an object to gracefully handle the following cases.
    Some Measures do not have any notes, for example, and the end of encoding where a
    final bar line is defined. Some measures do not have numbers or barlin definitions,
    such as pickup notes. Some measures define barline characteristics.
    Backup and forward presumably only is contained within a measure.

[`MuseDataMeasure`](#music21.musedata.MuseDataMeasure "music21.musedata.MuseDataMeasure") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MuseDataMeasure`](#music21.musedata.MuseDataMeasure "music21.musedata.MuseDataMeasure") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MuseDataMeasure`](#music21.musedata.MuseDataMeasure "music21.musedata.MuseDataMeasure") methods

MuseDataMeasure.getBarObject()[[source]](../_modules/music21/musedata.html#MuseDataMeasure.getBarObject)
:   Return a configured music21 bar object. This can be used with the current
    Measure or applied to a previous Measure.

MuseDataMeasure.getMeasureObject()[[source]](../_modules/music21/musedata.html#MuseDataMeasure.getMeasureObject)
:   Return a configured music21 `Measure`.

MuseDataMeasure.getRecords()[[source]](../_modules/music21/musedata.html#MuseDataMeasure.getRecords)
:   Return a list of all records stored in this measure as MuseDataRecord.

MuseDataMeasure.hasNotes()[[source]](../_modules/music21/musedata.html#MuseDataMeasure.hasNotes)
:   Return True of if this Measure has Notes

MuseDataMeasure.hasVoices()[[source]](../_modules/music21/musedata.html#MuseDataMeasure.hasVoices)
:   Return True of if this Measure defines one or more ‘back’ indication.

    Note: this does not instantiate MuseDataRecord instances.

## MuseDataMeasureIterator

class music21.musedata.MuseDataMeasureIterator(*src*, *boundaries*, *parent*)[[source]](../_modules/music21/musedata.html#MuseDataMeasureIterator)
:   Create MuseDataMeasure objects on demand, in order

## MuseDataPart

class music21.musedata.MuseDataPart(*src=None*, *stage=None*)[[source]](../_modules/music21/musedata.html#MuseDataPart)
:   A MuseData part is defined by collection of lines

[`MuseDataPart`](#music21.musedata.MuseDataPart "music21.musedata.MuseDataPart") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MuseDataPart`](#music21.musedata.MuseDataPart "music21.musedata.MuseDataPart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MuseDataPart`](#music21.musedata.MuseDataPart "music21.musedata.MuseDataPart") methods

MuseDataPart.getClefObject(*voice=1*)[[source]](../_modules/music21/musedata.html#MuseDataPart.getClefObject)
:   Return a music21 clef object based on a two character clef definition.

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getClefObject().sign
    'G'
    ```

MuseDataPart.getDirective()[[source]](../_modules/music21/musedata.html#MuseDataPart.getDirective)
:   The directive field is generally used to store tempo indications.
    This indication, however, is frequently not provided.

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getDirective() is None
    True
    ```

MuseDataPart.getDivisionsPerQuarterNote()[[source]](../_modules/music21/musedata.html#MuseDataPart.getDivisionsPerQuarterNote)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getDivisionsPerQuarterNote()
    6
    ```

MuseDataPart.getGroupMembershipNumber(*membership='score'*)[[source]](../_modules/music21/musedata.html#MuseDataPart.getGroupMembershipNumber)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getGroupMembershipNumber()
    1
    ```

MuseDataPart.getGroupMemberships()[[source]](../_modules/music21/musedata.html#MuseDataPart.getGroupMemberships)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getGroupMemberships()
    ['sound', 'score']
    ```

MuseDataPart.getGroupMembershipsTotal(*membership='score'*)[[source]](../_modules/music21/musedata.html#MuseDataPart.getGroupMembershipsTotal)
:   ```python
    >>> fp1 = str(common.getSourceFilePath() /'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getGroupMembershipsTotal()
    5
    ```

MuseDataPart.getKeyParameters()[[source]](../_modules/music21/musedata.html#MuseDataPart.getKeyParameters)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                   / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getKeyParameters()
    0
    ```

MuseDataPart.getKeySignature()[[source]](../_modules/music21/musedata.html#MuseDataPart.getKeySignature)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getKeySignature()
    <music21.key.KeySignature of no sharps or flats>
    ```

MuseDataPart.getMeasures()[[source]](../_modules/music21/musedata.html#MuseDataPart.getMeasures)
:   Return a list of all measures stored in this part as MuseDataMeasure objects.

MuseDataPart.getMovementNumber()[[source]](../_modules/music21/musedata.html#MuseDataPart.getMovementNumber)
:   Returns a string, not an int.

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getMovementNumber()
    '3'
    ```

MuseDataPart.getMovementTitle()[[source]](../_modules/music21/musedata.html#MuseDataPart.getMovementTitle)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getMovementTitle()
    'Trio II'
    ```

MuseDataPart.getPartName()[[source]](../_modules/music21/musedata.html#MuseDataPart.getPartName)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getPartName()
    'Clarinet in A'
    ```

MuseDataPart.getSource()[[source]](../_modules/music21/musedata.html#MuseDataPart.getSource)
:   Return the source (original print encoding) for the score.

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '03.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getSource()
    'Breitkopf & Härtel, Vol. 13'
    ```

    Note that the publisher is Härtel. MuseData predates the standardization
    of encoding as UTF-8, so many
    MuseData files are in Windows (ISO-8859-1) encodings.
    Music21 tries first
    in utf-8 and if there are errors will try again in ISO-8859-1, and if it
    fails it will try to read ignoring any errors (leaving “Hrtel”).
    In this case, both UTF-8 and ISO-8859-1 support this character (Latin-1 space
    in Unicode).

    If you know the encoding you can pass that to MuseDataWork or MuseDataFile.
    It is not yet a property you can specify in converter.

    ```python
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.encoding = 'ISO-8859-1'
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getSource()
    'Breitkopf & Härtel, Vol. 13'
    ```

MuseDataPart.getTimeSignatureObject()[[source]](../_modules/music21/musedata.html#MuseDataPart.getTimeSignatureObject)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getTimeSignatureObject()
    <music21.meter.TimeSignature 3/4>
    ```

MuseDataPart.getTimeSignatureParameters()[[source]](../_modules/music21/musedata.html#MuseDataPart.getTimeSignatureParameters)
:   ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                   / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getTimeSignatureParameters()
    '3/4'
    ```

MuseDataPart.getTranspositionIntervalObject()[[source]](../_modules/music21/musedata.html#MuseDataPart.getTranspositionIntervalObject)
:   If this part defines a transposition, return a corresponding Interval object.

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> fp2 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '02.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.addFile(fp2)
    >>> mdw.getParts()[0].getTranspositionIntervalObject()
    <music21.interval.Interval m-3>
    ```

MuseDataPart.getWorkNumber()[[source]](../_modules/music21/musedata.html#MuseDataPart.getWorkNumber)
:   Returns a String not an int, representing an opus number

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getWorkNumber()
    '581'
    ```

MuseDataPart.getWorkTitle()[[source]](../_modules/music21/musedata.html#MuseDataPart.getWorkTitle)
:   For stage 1 just gets the catalogue number

    ```python
    >>> fp1 = (common.getSourceFilePath() / 'musedata' / 'testPrimitive'
    ...                    / 'test01' / '01.md')
    >>> mdw = musedata.MuseDataWork()
    >>> mdw.addFile(fp1)
    >>> mdw.getParts()[0].getWorkTitle()
    'Clarinet Quintet'
    ```

MuseDataPart.update()[[source]](../_modules/music21/musedata.html#MuseDataPart.update)
:   After setting the source string, this method must be called to configure
    the \_measureNumberToLine method and set additional attributes.

## MuseDataRecord

class music21.musedata.MuseDataRecord(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *parent=None*)[[source]](../_modules/music21/musedata.html#MuseDataRecord)
:   Object for extracting data from a Note or other related record, or a
    single line of musedata data.

[`MuseDataRecord`](#music21.musedata.MuseDataRecord "music21.musedata.MuseDataRecord") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MuseDataRecord`](#music21.musedata.MuseDataRecord "music21.musedata.MuseDataRecord") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MuseDataRecord`](#music21.musedata.MuseDataRecord "music21.musedata.MuseDataRecord") methods

MuseDataRecord.getArticulationObjects()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getArticulationObjects)
:   Return a list of 0 or more music21 Articulation objects

    ```python
    >>> mdr = musedata.MuseDataRecord('C4    12        e     u  [      .p')
    >>> mdr.getArticulationObjects()
    [<music21.articulations.Staccato>]
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('C4    12        e     u  [      .p>')
    >>> mdr.getArticulationObjects()
    [<music21.articulations.Staccato>, <music21.articulations.Accent>]
    ```

MuseDataRecord.getBeams()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getBeams)
:   Return complete span of characters defining beams.

    ```python
    >>> mdr = musedata.MuseDataRecord('E2     1        s     u  =')
    >>> mdr.getBeams()
    '='
    >>> mdr = musedata.MuseDataRecord('E2     1        s     u  ]')
    >>> mdr.getBeams()
    ']'
    >>> mdr = musedata.MuseDataRecord('E2     4        q     u')
    >>> mdr.getBeams() is None
    True
    ```

MuseDataRecord.getDots()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getDots)

MuseDataRecord.getDynamicObjects()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getDynamicObjects)
:   Return a list of 0 or more music21 Dynamic objects

    ```python
    >>> mdr = musedata.MuseDataRecord('C5    12        e     u         ff')
    >>> mdr.getDynamicObjects()
    [<music21.dynamics.Dynamic ff>]
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('E4    48        h     u        (pp')
    >>> mdr.getDynamicObjects()
    [<music21.dynamics.Dynamic pp>]
    ```

MuseDataRecord.getExpressionObjects()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getExpressionObjects)
:   Return a list of 0 or more music21 Articulation objects

    ```python
    >>> mdr = musedata.MuseDataRecord('C4    12        e     u  [      t')
    >>> mdr.getExpressionObjects()
    [<music21.expressions.Trill>]
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('C4    12        e     u  [      .p>F')
    >>> mdr.getExpressionObjects()
    [<music21.expressions.Fermata>]
    ```

MuseDataRecord.getLyrics()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getLyrics)
:   Return lyrics as a list.

    ```python
    >>> mdr = musedata.MuseDataRecord('D4     2        e     u                    con-')
    >>> mdr.stage = 2
    >>> mdr.getLyrics()
    ['con-']
    ```

MuseDataRecord.getPitchObject()[[source]](../_modules/music21/musedata.html#MuseDataRecord.getPitchObject)
:   Get the Pitch object defined by this record. This may be a note, chord, or grace pitch.

    ```python
    >>> mdr = musedata.MuseDataRecord('Ef4    1        s     d  ==')
    >>> p = mdr.getPitchObject()
    >>> p.nameWithOctave
    'E-4'
    >>> mdr = musedata.MuseDataRecord('F#4    1        s #   d  ==')
    >>> p = mdr.getPitchObject()
    >>> p.nameWithOctave
    'F#4'
    >>> p.accidental.displayStatus
    True
    ```

    Double sharps were giving octave problems.

    ```python
    >>> mdr = musedata.MuseDataRecord('F##5   2        e x   d')
    >>> p = mdr.getPitchObject()
    >>> p.nameWithOctave
    'F##5'
    ```

MuseDataRecord.getQuarterLength(*divisionsPerQuarterNote=None*)[[source]](../_modules/music21/musedata.html#MuseDataRecord.getQuarterLength)
:   Gets the quarterLength of the note given the prevailing divisionsPerQuarterNote

    Here there is one division:

    ```python
    >>> mdr = musedata.MuseDataRecord('Ef4    1        s     d  ==')
    >>> mdr.getQuarterLength(4)
    0.25
    >>> mdr.getQuarterLength(8)
    0.125
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('Ef4    6        s     d  ==')
    >>> mdr.getQuarterLength(4)
    1.5
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('back   4')
    >>> mdr.getQuarterLength(4)
    1.0
    ```

MuseDataRecord.hasCautionaryAccidental()[[source]](../_modules/music21/musedata.html#MuseDataRecord.hasCautionaryAccidental)
:   Return a boolean if this note has a cautionary accidental.

    ```python
    >>> mdr = musedata.MuseDataRecord('F5     3        t n   d  ==[   (+')
    >>> mdr.hasCautionaryAccidental()
    True
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('C4    12        e     u  [')
    >>> mdr.hasCautionaryAccidental()
    False
    ```

MuseDataRecord.isBack()[[source]](../_modules/music21/musedata.html#MuseDataRecord.isBack)
:   ```python
    >>> mdr = musedata.MuseDataRecord('back   4')
    >>> mdr.isBack()
    True
    ```

MuseDataRecord.isChord()[[source]](../_modules/music21/musedata.html#MuseDataRecord.isChord)
:   Chords are specified as additional note records following a main chord tone.
    The blank space defines this as chord tone.

MuseDataRecord.isCueOrGrace()[[source]](../_modules/music21/musedata.html#MuseDataRecord.isCueOrGrace)

MuseDataRecord.isNote()[[source]](../_modules/music21/musedata.html#MuseDataRecord.isNote)

MuseDataRecord.isRest() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musedata.html#MuseDataRecord.isRest)
:   Return a boolean if this record is a rest.

    ```python
    >>> mdr = musedata.MuseDataRecord('D4     1        s     d  ]]')
    >>> mdr.isRest()
    False
    >>> mdr = musedata.MuseDataRecord('measure 1       A')
    >>> mdr.isRest()
    False
    ```

MuseDataRecord.isTied()[[source]](../_modules/music21/musedata.html#MuseDataRecord.isTied)
:   Return a boolean if this record is tied.

    ```python
    >>> mdr = musedata.MuseDataRecord('D4     8-       h     d        -')
    >>> mdr.isTied()
    True
    ```

    ```python
    >>> mdr = musedata.MuseDataRecord('C4     1        s     u  [[')
    >>> mdr.isTied()
    False
    ```

## MuseDataRecordIterator

class music21.musedata.MuseDataRecordIterator(*src*, *parent*)[[source]](../_modules/music21/musedata.html#MuseDataRecordIterator)
:   Create MuseDataRecord objects on demand, in order
