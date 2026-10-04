Source: https://music21.org/music21docs/moduleReference/moduleConverterSubConverters.html

# music21.converter.subConverters

SubConverters parse or display a single format.

Each subConverter should inherit from the base SubConverter object and have at least a
parseData method that sets self.stream.

## ConverterABC

class music21.converter.subConverters.ConverterABC(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterABC)
:   Simple class wrapper for parsing ABC.

    Input only

[`ConverterABC`](#music21.converter.subConverters.ConverterABC "music21.converter.subConverters.ConverterABC") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterABC`](#music21.converter.subConverters.ConverterABC "music21.converter.subConverters.ConverterABC") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterABC`](#music21.converter.subConverters.ConverterABC "music21.converter.subConverters.ConverterABC") methods

ConverterABC.parseData(*strData*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterABC.parseData)
:   Get ABC data, as token list, from a string representation.
    If more than one work is defined in the ABC data, a
    `Opus` object will be returned;
    otherwise, a `Score` is returned.

ConverterABC.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterABC.parseFile)
:   Get ABC data from a file path. If more than one work is defined in the ABC
    data, a `Opus` object will be returned;
    otherwise, a `Score` is returned.

    If number is provided, and this ABC file defines multiple works
    with an X: tag, just the specified work will be returned.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterBraille

class music21.converter.subConverters.ConverterBraille(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterBraille)

[`ConverterBraille`](#music21.converter.subConverters.ConverterBraille "music21.converter.subConverters.ConverterBraille") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterBraille`](#music21.converter.subConverters.ConverterBraille "music21.converter.subConverters.ConverterBraille") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterBraille`](#music21.converter.subConverters.ConverterBraille "music21.converter.subConverters.ConverterBraille") methods

ConverterBraille.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterBraille.show)
:   Write the data, then show the generated data, using .launch() or printing
    to a console.

    Some simple formats that do not need launching, may skip .launch() and
    simply return the output.

ConverterBraille.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterBraille.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterCapella

class music21.converter.subConverters.ConverterCapella(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterCapella)
:   Simple class wrapper for parsing Capella .capx XML files. See capella/fromCapellaXML.

[`ConverterCapella`](#music21.converter.subConverters.ConverterCapella "music21.converter.subConverters.ConverterCapella") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterCapella`](#music21.converter.subConverters.ConverterCapella "music21.converter.subConverters.ConverterCapella") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterCapella`](#music21.converter.subConverters.ConverterCapella "music21.converter.subConverters.ConverterCapella") methods

ConverterCapella.parseData(*strData*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterCapella.parseData)
:   parse a data stream of uncompressed capella xml

    N.B. for web parsing, it gets more complex.

ConverterCapella.parseFile(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterCapella.parseFile)
:   Parse a Capella file

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterClercqTemperley

class music21.converter.subConverters.ConverterClercqTemperley(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterClercqTemperley)
:   Wrapper for parsing harmonic definitions in Trevor de Clercq and
    David Temperley’s format.

[`ConverterClercqTemperley`](#music21.converter.subConverters.ConverterClercqTemperley "music21.converter.subConverters.ConverterClercqTemperley") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterClercqTemperley`](#music21.converter.subConverters.ConverterClercqTemperley "music21.converter.subConverters.ConverterClercqTemperley") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterClercqTemperley`](#music21.converter.subConverters.ConverterClercqTemperley "music21.converter.subConverters.ConverterClercqTemperley") methods

ConverterClercqTemperley.parseData(*strData: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterClercqTemperley.parseData)
:   Called when a string (or binary) data is encountered.

    This method MUST be implemented to do anything in parsing.

    Return self.stream in the end

ConverterClercqTemperley.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number=None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterClercqTemperley.parseFile)
:   Called when a file is encountered. If all that needs to be done is
    loading the file and putting the data into parseData then there is no need
    to implement this method. Just set self.readBinary to True | False.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterHumdrum

class music21.converter.subConverters.ConverterHumdrum(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterHumdrum)
:   Simple class wrapper for parsing Humdrum data provided in a file or in a string.

[`ConverterHumdrum`](#music21.converter.subConverters.ConverterHumdrum "music21.converter.subConverters.ConverterHumdrum") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterHumdrum`](#music21.converter.subConverters.ConverterHumdrum "music21.converter.subConverters.ConverterHumdrum") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterHumdrum`](#music21.converter.subConverters.ConverterHumdrum "music21.converter.subConverters.ConverterHumdrum") methods

ConverterHumdrum.parseData(*humdrumString*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterHumdrum.parseData)
:   Open Humdrum data from a string – calls
    [`parse()`](moduleHumdrumSpineParser.html#music21.humdrum.spineParser.HumdrumDataCollection.parse "music21.humdrum.spineParser.HumdrumDataCollection.parse").

    ```python
    >>> humData = ('**kern\n*M2/4\n=1\n24r\n24g#\n24f#\n24e\n24c#\n' +
    ...     '24f\n24r\n24dn\n24e-\n24gn\n24e-\n24dn\n*-')
    >>> c = converter.subConverters.ConverterHumdrum()
    >>> s = c.parseData(humData)
    >>> c.stream.show('text')
    {0.0} <music21.metadata.Metadata object at 0x7f33545027b8>
    {0.0} <music21.stream.Part spine_0>
        {0.0} <music21.humdrum.spineParser.MiscTandem **kern>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.meter.TimeSignature 2/4>
            {0.0} <music21.note.Rest 1/6ql>
            {0.1667} <music21.note.Note G#>
            {0.3333} <music21.note.Note F#>
            {0.5} <music21.note.Note E>
            {0.6667} <music21.note.Note C#>
            {0.8333} <music21.note.Note F>
            {1.0} <music21.note.Rest 1/6ql>
            {1.1667} <music21.note.Note D>
            {1.3333} <music21.note.Note E->
            {1.5} <music21.note.Note G>
            {1.6667} <music21.note.Note E->
            {1.8333} <music21.note.Note D>
    ```

ConverterHumdrum.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterHumdrum.parseFile)
:   Open Humdrum data from a file path.

    Calls humdrum.parseFile on filepath.

    Number is ignored here.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterIPython

class music21.converter.subConverters.ConverterIPython(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterIPython)
:   Meta-subConverter for displaying image data in a Notebook
    using either png (via MuseScore or LilyPond) or directly via
    Vexflow/music21j, or MIDI using music21j.

[`ConverterIPython`](#music21.converter.subConverters.ConverterIPython "music21.converter.subConverters.ConverterIPython") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterIPython`](#music21.converter.subConverters.ConverterIPython "music21.converter.subConverters.ConverterIPython") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterIPython`](#music21.converter.subConverters.ConverterIPython "music21.converter.subConverters.ConverterIPython") methods

ConverterIPython.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterIPython.show)
:   show a specialized for Jupyter Notebook using the appropriate subformat.

    For MusicXML runs it through MuseScore and returns the PNG data.
    (use multipageWidget to get an experimental interactive page display).

    For MIDI: loads a music21j-powered MIDI player in to the Notebook.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterLilypond

class music21.converter.subConverters.ConverterLilypond(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterLilypond)
:   Convert to Lilypond and from there usually to png, pdf, or svg.

    Note: that the proper format for displaying Lilypond in Jupyter
    notebook in v9 is ipython.lily.png and not lily.ipython.png

[`ConverterLilypond`](#music21.converter.subConverters.ConverterLilypond "music21.converter.subConverters.ConverterLilypond") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterLilypond`](#music21.converter.subConverters.ConverterLilypond "music21.converter.subConverters.ConverterLilypond") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterLilypond`](#music21.converter.subConverters.ConverterLilypond "music21.converter.subConverters.ConverterLilypond") methods

ConverterLilypond.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterLilypond.show)
:   Call .write (write out the lilypond (.ly) file; convert to .png/.pdf, etc.)
    then launch the appropriate viewer for .png/.pdf (graphicsPath) or .svg
    (vectorPath)

ConverterLilypond.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\**, *coloredVariants: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterLilypond.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterMEI

class music21.converter.subConverters.ConverterMEI(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMEI)
:   Converter for MEI. You must use an “.mei” file extension for MEI files because music21 will
    parse “.xml” files as MusicXML.

[`ConverterMEI`](#music21.converter.subConverters.ConverterMEI "music21.converter.subConverters.ConverterMEI") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterMEI`](#music21.converter.subConverters.ConverterMEI "music21.converter.subConverters.ConverterMEI") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterMEI`](#music21.converter.subConverters.ConverterMEI "music21.converter.subConverters.ConverterMEI") methods

ConverterMEI.checkShowAbility(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMEI.checkShowAbility)
:   MEI export is not yet implemented.

ConverterMEI.parseData(*dataString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number=None*) → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/converter/subConverters.html#ConverterMEI.parseData)
:   Convert a string with an MEI document into its corresponding music21 elements.

    * dataString: The string with XML to convert.
    * number: Unused in this class. Default is `None`.

    Returns the music21 objects corresponding to the MEI file.

ConverterMEI.parseFile(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*) → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/converter/subConverters.html#ConverterMEI.parseFile)
:   Convert a file with an MEI document into its corresponding music21 elements.

    * filePath: Full pathname to the file containing MEI data as a string or Path.
    * number: Unused in this class. Default is `None`.

    Returns the music21 objects corresponding to the MEI file.

ConverterMEI.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMEI.show)
:   Write the data, then show the generated data, using .launch() or printing
    to a console.

    Some simple formats that do not need launching, may skip .launch() and
    simply return the output.

ConverterMEI.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMEI.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterMidi

class music21.converter.subConverters.ConverterMidi(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMidi)
:   Simple class wrapper for parsing MIDI and sending MIDI data out.

[`ConverterMidi`](#music21.converter.subConverters.ConverterMidi "music21.converter.subConverters.ConverterMidi") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterMidi`](#music21.converter.subConverters.ConverterMidi "music21.converter.subConverters.ConverterMidi") read-only properties

ConverterMidi.encoding

[`ConverterMidi`](#music21.converter.subConverters.ConverterMidi "music21.converter.subConverters.ConverterMidi") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterMidi`](#music21.converter.subConverters.ConverterMidi "music21.converter.subConverters.ConverterMidi") methods

ConverterMidi.parseData(*strData*, *number=None*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMidi.parseData)
:   Get MIDI data from a binary string representation.

    Calls midi.translate.midiStringToStream.

    Keywords to control quantization:
    quantizePost controls whether to quantize the output. (Default: True)
    quarterLengthDivisors allows for overriding the default quantization units
    in defaults.quantizationQuarterLengthDivisors. (Default: (4, 3)).

    If encoding is not provided use the encoding of the Converter
    (default “utf-8”)

ConverterMidi.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMidi.parseFile)
:   Get MIDI data from a file path.

    Calls midi.translate.midiFilePathToStream.

    Keywords to control quantization:
    quantizePost controls whether to quantize the output. (Default: True)
    quarterLengthDivisors allows for overriding the default quantization units
    in defaults.quantizationQuarterLengthDivisors. (Default: (4, 3)).

    If encoding is not provided use the encoding of the Converter
    (default “utf-8”)

ConverterMidi.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\**, *addStartDelay: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMidi.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterMuseData

class music21.converter.subConverters.ConverterMuseData(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMuseData)
:   Simple class wrapper for parsing MuseData.

[`ConverterMuseData`](#music21.converter.subConverters.ConverterMuseData "music21.converter.subConverters.ConverterMuseData") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterMuseData`](#music21.converter.subConverters.ConverterMuseData "music21.converter.subConverters.ConverterMuseData") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterMuseData`](#music21.converter.subConverters.ConverterMuseData "music21.converter.subConverters.ConverterMuseData") methods

ConverterMuseData.parseData(*strData*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMuseData.parseData)
:   Get musedata from a string representation.

ConverterMuseData.parseFile(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMuseData.parseFile)
:   parse fp (a pathlib.Path()) and number

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterMusicXML

class music21.converter.subConverters.ConverterMusicXML(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMusicXML)
:   Converter for MusicXML using the 2015 ElementTree system.

    Users should not need this Object. Call converter.parse directly

[`ConverterMusicXML`](#music21.converter.subConverters.ConverterMusicXML "music21.converter.subConverters.ConverterMusicXML") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterMusicXML`](#music21.converter.subConverters.ConverterMusicXML "music21.converter.subConverters.ConverterMusicXML") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterMusicXML`](#music21.converter.subConverters.ConverterMusicXML "music21.converter.subConverters.ConverterMusicXML") methods

ConverterMusicXML.parseData(*xmlString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMusicXML.parseData)
:   Open MusicXML data from a string.

ConverterMusicXML.parseFile(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMusicXML.parseFile)
:   Open from a file path; check to see if there is a pickled
    version available and up to date; if so, open that, otherwise
    open source.

ConverterMusicXML.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMusicXML.show)
:   Override to do something with png

ConverterMusicXML.write(*obj: music21.Music21Object*, *fmt*, *fp=None*, *subformats=()*, *\**, *makeNotation=True*, *compress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterMusicXML.write)
:   Write to a .musicxml file.

    Set makeNotation=False to prevent fixing up the notation, and where possible,
    to prevent making additional deepcopies. (This option cannot be used if obj is not a
    `Score`.) makeNotation=True generally solves common notation
    issues, whereas makeNotation=False is intended for advanced users facing
    special cases where speed is a priority or making notation reverses user choices.

    Set compress=True to immediately compress the output to a .mxl file. Set
    to True automatically if format=’mxl’ or if fp is given and ends with .mxl

ConverterMusicXML.writeDataStream(*fp*, *dataStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *\*\*keywords*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#ConverterMusicXML.writeDataStream)
:   Writes dataStr which must be bytes to fp.
    Adds .musicxml suffix to fp if it does not already contain some suffix.

    * Changed in v7: returns a pathlib.Path

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") | * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") |

## ConverterNoteworthy

class music21.converter.subConverters.ConverterNoteworthy(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterNoteworthy)
:   Simple class wrapper for parsing NoteworthyComposer data provided in a
    file or in a string.

    Gets data with the file format .nwctxt

    Users should not need this routine. The basic format is converter.parse(‘file.nwctxt’)

    ```python
    >>> paertPath = converter.parse(r'd:/desktop/arvo_part_o_weisheit.nwctxt')
    >>> paertStream = converter.parse(paertPath)
    >>> len(paertStream.parts)
    4
    ```

    For developers: see the documentation for [`parseData()`](#music21.converter.subConverters.ConverterNoteworthy.parseData "music21.converter.subConverters.ConverterNoteworthy.parseData") and [`parseFile()`](#music21.converter.subConverters.ConverterNoteworthy.parseFile "music21.converter.subConverters.ConverterNoteworthy.parseFile")
    to see the low-level usage.

[`ConverterNoteworthy`](#music21.converter.subConverters.ConverterNoteworthy "music21.converter.subConverters.ConverterNoteworthy") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterNoteworthy`](#music21.converter.subConverters.ConverterNoteworthy "music21.converter.subConverters.ConverterNoteworthy") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterNoteworthy`](#music21.converter.subConverters.ConverterNoteworthy "music21.converter.subConverters.ConverterNoteworthy") methods

ConverterNoteworthy.parseData(*nwcData*)[[source]](../_modules/music21/converter/subConverters.html#ConverterNoteworthy.parseData)
:   Open Noteworthy data from a string or list

    ```python
    >>> nwcData = ('!NoteWorthyComposer(2.0)\n|AddStaff\n|Clef|' +
    ...     'Type:Treble\n|Note|Dur:Whole|Pos:1^')
    >>> c = converter.subConverters.ConverterNoteworthy()
    >>> c.parseData(nwcData)
    >>> c.stream.show('text')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.note.Note C>
    ```

ConverterNoteworthy.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterNoteworthy.parseFile)
:   Open Noteworthy data (as nwctxt) from a file path.

    ```python
    >>> paertPath = converter.parse('d:/desktop/arvo_part_o_weisheit.nwctxt')
    >>> c = converter.subConverters.ConverterNoteworthy()
    >>> c.parseFile(filePath)
    >>> c.stream.show()
    ```

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterNoteworthyBinary

class music21.converter.subConverters.ConverterNoteworthyBinary(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterNoteworthyBinary)
:   Simple class wrapper for parsing NoteworthyComposer binary data
    provided in a file or in a string.

    Gets data with the file format .nwc

    Users should not need this routine. Call converter.parse directly

[`ConverterNoteworthyBinary`](#music21.converter.subConverters.ConverterNoteworthyBinary "music21.converter.subConverters.ConverterNoteworthyBinary") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterNoteworthyBinary`](#music21.converter.subConverters.ConverterNoteworthyBinary "music21.converter.subConverters.ConverterNoteworthyBinary") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterNoteworthyBinary`](#music21.converter.subConverters.ConverterNoteworthyBinary "music21.converter.subConverters.ConverterNoteworthyBinary") methods

ConverterNoteworthyBinary.parseData(*nwcData*)[[source]](../_modules/music21/converter/subConverters.html#ConverterNoteworthyBinary.parseData)
:   Called when a string (or binary) data is encountered.

    This method MUST be implemented to do anything in parsing.

    Return self.stream in the end

ConverterNoteworthyBinary.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterNoteworthyBinary.parseFile)
:   Called when a file is encountered. If all that needs to be done is
    loading the file and putting the data into parseData then there is no need
    to implement this method. Just set self.readBinary to True | False.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") | * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterRomanText

class music21.converter.subConverters.ConverterRomanText(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterRomanText)
:   Simple class wrapper for parsing roman text harmonic definitions.

[`ConverterRomanText`](#music21.converter.subConverters.ConverterRomanText "music21.converter.subConverters.ConverterRomanText") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterRomanText`](#music21.converter.subConverters.ConverterRomanText "music21.converter.subConverters.ConverterRomanText") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterRomanText`](#music21.converter.subConverters.ConverterRomanText "music21.converter.subConverters.ConverterRomanText") methods

ConverterRomanText.parseData(*strData*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterRomanText.parseData)
:   Called when a string (or binary) data is encountered.

    This method MUST be implemented to do anything in parsing.

    Return self.stream in the end

ConverterRomanText.parseFile(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterRomanText.parseFile)
:   Called when a file is encountered. If all that needs to be done is
    loading the file and putting the data into parseData then there is no need
    to implement this method. Just set self.readBinary to True | False.

ConverterRomanText.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterRomanText.write)
:   Writes ‘RomanText’ files (using the extension .rntxt) from a music21.stream.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterScala

class music21.converter.subConverters.ConverterScala(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterScala)

[`ConverterScala`](#music21.converter.subConverters.ConverterScala "music21.converter.subConverters.ConverterScala") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterScala`](#music21.converter.subConverters.ConverterScala "music21.converter.subConverters.ConverterScala") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterScala`](#music21.converter.subConverters.ConverterScala "music21.converter.subConverters.ConverterScala") methods

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") | * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterText

class music21.converter.subConverters.ConverterText(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterText)
:   standard text presentation has line breaks, is printed.

    Two keyword options are allowed: addEndTimes=Boolean and useMixedNumerals=Boolean

[`ConverterText`](#music21.converter.subConverters.ConverterText "music21.converter.subConverters.ConverterText") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterText`](#music21.converter.subConverters.ConverterText "music21.converter.subConverters.ConverterText") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterText`](#music21.converter.subConverters.ConverterText "music21.converter.subConverters.ConverterText") methods

ConverterText.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterText.show)
:   Write the data, then show the generated data, using .launch() or printing
    to a console.

    Some simple formats that do not need launching, may skip .launch() and
    simply return the output.

ConverterText.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterText.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterTextLine

class music21.converter.subConverters.ConverterTextLine(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterTextLine)
:   a text line compacts the complete recursive representation into a
    single line of text; most for debugging. returned, not printed

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> s.measures(1, 4).show('textline')
    "{0.0} <music21.stream.Part Soprano> / {0.0} <music21.instrument.Instrument '... 1'>..."
    ```

[`ConverterTextLine`](#music21.converter.subConverters.ConverterTextLine "music21.converter.subConverters.ConverterTextLine") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterTextLine`](#music21.converter.subConverters.ConverterTextLine "music21.converter.subConverters.ConverterTextLine") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterTextLine`](#music21.converter.subConverters.ConverterTextLine "music21.converter.subConverters.ConverterTextLine") methods

ConverterTextLine.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterTextLine.show)
:   Write the data, then show the generated data, using .launch() or printing
    to a console.

    Some simple formats that do not need launching, may skip .launch() and
    simply return the output.

ConverterTextLine.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterTextLine.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterTinyNotation

class music21.converter.subConverters.ConverterTinyNotation(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterTinyNotation)
:   Simple class wrapper for parsing TinyNotation data provided in a file or
    in a string.

    Input only for now.

[`ConverterTinyNotation`](#music21.converter.subConverters.ConverterTinyNotation "music21.converter.subConverters.ConverterTinyNotation") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterTinyNotation`](#music21.converter.subConverters.ConverterTinyNotation "music21.converter.subConverters.ConverterTinyNotation") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterTinyNotation`](#music21.converter.subConverters.ConverterTinyNotation "music21.converter.subConverters.ConverterTinyNotation") methods

ConverterTinyNotation.parseData(*tnData*, *number=None*)[[source]](../_modules/music21/converter/subConverters.html#ConverterTinyNotation.parseData)
:   Open TinyNotation data from a string

    ```python
    >>> tnData = "3/4 E4 r f# g=lastG trip{b-8 a g} c"
    >>> c = converter.subConverters.ConverterTinyNotation()
    >>> s = c.parseData(tnData)
    >>> c.stream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Rest quarter>
        {2.0} <music21.note.Note F#>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note B->
        {1.3333} <music21.note.Note A>
        {1.6667} <music21.note.Note G>
        {2.0} <music21.note.Note C>
        {2.5} <music21.bar.Barline type=final>
    ```

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`write()`](#music21.converter.subConverters.SubConverter.write "music21.converter.subConverters.SubConverter.write") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterVexflow

class music21.converter.subConverters.ConverterVexflow(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVexflow)

[`ConverterVexflow`](#music21.converter.subConverters.ConverterVexflow "music21.converter.subConverters.ConverterVexflow") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterVexflow`](#music21.converter.subConverters.ConverterVexflow "music21.converter.subConverters.ConverterVexflow") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterVexflow`](#music21.converter.subConverters.ConverterVexflow "music21.converter.subConverters.ConverterVexflow") methods

ConverterVexflow.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\**, *local: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVexflow.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseData()`](#music21.converter.subConverters.SubConverter.parseData "music21.converter.subConverters.SubConverter.parseData") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`show()`](#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## ConverterVolpiano

class music21.converter.subConverters.ConverterVolpiano(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVolpiano)
:   Reads or writes volpiano (Chant encoding).

    Normally, just use ‘converter’ and .show()/.write()

    ```python
    >>> p = converter.parse('volpiano: 1---c-d-ef----4')
    >>> p.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note F>
        {4.0} <music21.volpiano.Neume <music21.note.Note E><music21.note.Note F>>
        {4.0} <music21.bar.Barline type=double>
    >>> p.show('volpiano')
    1---c-d-ef----4
    ```

[`ConverterVolpiano`](#music21.converter.subConverters.ConverterVolpiano "music21.converter.subConverters.ConverterVolpiano") bases

* [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`ConverterVolpiano`](#music21.converter.subConverters.ConverterVolpiano "music21.converter.subConverters.ConverterVolpiano") read/write properties

Read/write properties inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`ConverterVolpiano`](#music21.converter.subConverters.ConverterVolpiano "music21.converter.subConverters.ConverterVolpiano") methods

ConverterVolpiano.getDataStr(*obj*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVolpiano.getDataStr)
:   Get the raw data, for storing as a variable.

ConverterVolpiano.parseData(*dataString*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *breaksToLayout: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVolpiano.parseData)
:   Called when a string (or binary) data is encountered.

    This method MUST be implemented to do anything in parsing.

    Return self.stream in the end

ConverterVolpiano.show(*obj*, *fmt*, *app=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVolpiano.show)
:   Write the data, then show the generated data, using .launch() or printing
    to a console.

    Some simple formats that do not need launching, may skip .launch() and
    simply return the output.

ConverterVolpiano.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#ConverterVolpiano.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`parseFile()`](#music21.converter.subConverters.SubConverter.parseFile "music21.converter.subConverters.SubConverter.parseFile") | * [`toData()`](#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |

## SubConverter

class music21.converter.subConverters.SubConverter(*\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#SubConverter)
:   Class wrapper for parsing data or outputting data.

    All other Converter types should inherit from this and
    have ways of dealing with various data formats.

    Attributes that should be set:

    ```python
    readBinary = True or False (default False)
    registerFormats = tuple of formats that can be handled; eg: ('musicxml',)
    registerShowFormats = tuple of format calls that can be handled in .show() and .write()
    registerInputExtensions = tuple of input extensions that should be handled in converter
    registerOutputExtensions = tuple of output extensions that can be written. Order matters:
        the first will be used in calls to .write()
    canBePickled = True or False (default True; does not do anything yet)
    codecWrite = True or False (default False) if encodings need to be used to write
    stringEncoding = string (default 'utf-8'). If codecWrite is True, this specifies what
        encoding to use
    ```

[`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter") read/write properties

SubConverter.stream
:   Returns or sets the stream in the converter. Must be defined for subConverter to work.

[`SubConverter`](#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter") methods

SubConverter.checkShowAbility(*\*\*keywords*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#SubConverter.checkShowAbility)
:   return bool on whether the *system* is
    equipped to show in this format.

    Default True. Might be False if, say
    a Lilypond converter is used and Lilypond
    is not installed.

SubConverter.getExtensionForSubformats(*subformats: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#SubConverter.getExtensionForSubformats)
:   Given a default format or subformats, give the file extension it should have:

    ```python
    >>> c = converter.subConverters.ConverterMidi()
    >>> c.getExtensionForSubformats()
    '.mid'
    ```

SubConverter.getTemporaryFile(*subformats: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*) → [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#SubConverter.getTemporaryFile)
:   Return a temporary file with an extension appropriate for the format.

    ```python
    >>> c = corpus.parse('bwv66.6')
    >>> lpConverter = converter.subConverters.ConverterLilypond()
    >>> tf = str(lpConverter.getTemporaryFile(subformats=['png']))
    >>> tf.endswith('.png')
    True
    ```

    * Changed in v6: returns pathlib.Path

SubConverter.launch(*filePath: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *fmt=None*, *options: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *app: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *launchKey=None*)[[source]](../_modules/music21/converter/subConverters.html#SubConverter.launch)
:   Opens the appropriate viewer for the file generated by .write()

    app is the path to an application to launch. Specify it and/or a launchKey.
    launchKey is the specific key in .music21rc (such as graphicsPath), etc.
    to search for the application. If it’s not specified then there might be
    a default one for the converter in self.launchKey. If it can’t find it
    there then environLocal.formatToApp(fmt) will be used.

    Not needed for formats for which .show() just prints to the console.

SubConverter.parseData(*dataString*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/converter/subConverters.html#SubConverter.parseData)
:   Called when a string (or binary) data is encountered.

    This method MUST be implemented to do anything in parsing.

    Return self.stream in the end

SubConverter.parseFile(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#SubConverter.parseFile)
:   Called when a file is encountered. If all that needs to be done is
    loading the file and putting the data into parseData then there is no need
    to implement this method. Just set self.readBinary to True | False.

SubConverter.show(*obj*, *fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *app=None*, *subformats=()*, *\*\*keywords*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#SubConverter.show)
:   Write the data, then show the generated data, using .launch() or printing
    to a console.

    Some simple formats that do not need launching, may skip .launch() and
    simply return the output.

SubConverter.toData(*obj*, *fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *subformats: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\*\*keywords*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#SubConverter.toData)
:   Write the object out in the given format and then read it back in
    and return the object (str or bytes) returned.

SubConverter.write(*obj: [music21.base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | IOBase | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *subformats: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\*\*keywords*)[[source]](../_modules/music21/converter/subConverters.html#SubConverter.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

SubConverter.writeDataStream(*fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [IOBase](https://docs.python.org/3/library/io.html#io.IOBase "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *dataStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *\*\*keywords*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter/subConverters.html#SubConverter.writeDataStream)
:   Writes the data stream to fp or to a temporary file and returns the
    Path object of the filename written.
