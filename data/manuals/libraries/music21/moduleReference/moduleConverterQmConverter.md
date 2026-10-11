Source: https://music21.org/music21docs/moduleReference/moduleConverterQmConverter.html

# music21.converter.qmConverter

This is an example of how converter.subConverters.SubConverter
can be subclassed in order to parse and write an unsupported format
in this case, the format, .qm, consists of a line of letters separated
by spaces:

> C E G D F

and turns each of them into a quarter note in octave 4 in 4/4.

Consult the code to see how it works. To use, call
converter.registerSubConverter(converter.qmConverter.QMConverter)
then myStream = converter.parse(‘quarterMusic: C E G D F’)

## QMConverter

class music21.converter.qmConverter.QMConverter(*\*\*keywords*)[[source]](../_modules/music21/converter/qmConverter.html#QMConverter)

[`QMConverter`](#music21.converter.qmConverter.QMConverter "music21.converter.qmConverter.QMConverter") bases

* [`SubConverter`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")

[`QMConverter`](#music21.converter.qmConverter.QMConverter "music21.converter.qmConverter.QMConverter") read/write properties

Read/write properties inherited from [`SubConverter`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.stream "music21.converter.subConverters.SubConverter.stream") |  |  |

[`QMConverter`](#music21.converter.qmConverter.QMConverter "music21.converter.qmConverter.QMConverter") methods

QMConverter.parseData(*strData*, *number=None*)[[source]](../_modules/music21/converter/qmConverter.html#QMConverter.parseData)
:   Parse the data. The number attribute is not used.

    ```python
    >>> from music21.converter.qmConverter import QMConverter
    >>> qmc = QMConverter()
    >>> qmc.parseData('C D E G C')
    >>> q_stream = qmc.stream
    >>> q_stream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note G>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.bar.Barline type=final>
    ```

QMConverter.parseFile(*filePath*, *number=None*, *\*\*keywords*)[[source]](../_modules/music21/converter/qmConverter.html#QMConverter.parseFile)
:   parse a file from disk. If QMConverter is registered, then any
    file ending in .qm will automatically be parsed.

    ```python
    >>> import os
    >>> parserPath = common.getSourceFilePath() / 'converter'
    >>> testPath = parserPath / 'quarterMusicTestIn.qm'
    ```

    ```python
    >>> from music21.converter.qmConverter import QMConverter
    >>> qmc = QMConverter()
    >>> qmc.parseFile(testPath)
    >>> s = qmc.stream
    >>> s.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note G>
        {3.0} <music21.note.Note F>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note C>
        {3.0} <music21.bar.Barline type=final>
    ```

QMConverter.write(*obj*, *fmt*, *fp=None*, *subformats=()*, *\*\*keywords*)[[source]](../_modules/music21/converter/qmConverter.html#QMConverter.write)
:   Calls .writeDataStream on the repr of obj, and returns the fp returned by it.

Methods inherited from [`SubConverter`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter"):

|  |  |  |
| --- | --- | --- |
| * [`checkShowAbility()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.checkShowAbility "music21.converter.subConverters.SubConverter.checkShowAbility") * [`getExtensionForSubformats()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.getExtensionForSubformats "music21.converter.subConverters.SubConverter.getExtensionForSubformats") * [`getTemporaryFile()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.getTemporaryFile "music21.converter.subConverters.SubConverter.getTemporaryFile") | * [`launch()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.launch "music21.converter.subConverters.SubConverter.launch") * [`show()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.show "music21.converter.subConverters.SubConverter.show") | * [`toData()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.toData "music21.converter.subConverters.SubConverter.toData") * [`writeDataStream()`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter.writeDataStream "music21.converter.subConverters.SubConverter.writeDataStream") |
