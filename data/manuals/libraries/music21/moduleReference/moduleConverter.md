Source: https://music21.org/music21docs/moduleReference/moduleConverter.html

# music21.converter

music21.converter contains tools for loading music from various file formats,
whether from disk, from the web, or from text, into
music21.stream.:class:~music21.stream.Score objects (or
other similar stream objects).

The most powerful and easy to use tool is the [`parse()`](#music21.converter.parse "music21.converter.parse")
function. Simply provide a filename, URL, or text string and, if the format
is supported, a `Score` will be returned.

This is the most general, public interface for all formats. Programmers
adding their own formats to the system should provide an interface here to
their own parsers (such as humdrum, musicxml, etc.)

The second and subsequent times that a file is loaded it will likely be much
faster since we store a parsed version of each file as a “pickle” object in
the temp folder on the disk.

```python
>>> s = converter.parse('D:/myDocs/schubert.krn')
>>> s
<music21.stream.Score ...>
```

## Converter

class music21.converter.Converter[[source]](../_modules/music21/converter.html#Converter)
:   A class used for converting all supported data formats into music21 objects.

    Not a subclass, but a wrapper for different converter objects based on format.

[`Converter`](#music21.converter.Converter "music21.converter.Converter") read-only properties

Converter.stream
:   Returns the .subConverter.stream object.

[`Converter`](#music21.converter.Converter "music21.converter.Converter") methods

static Converter.defaultSubConverters() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")]][[source]](../_modules/music21/converter.html#Converter.defaultSubConverters)
:   return an alphabetical list of the default subConverters: those in converter.subConverters
    with the class SubConverter.

    Do not use generally. Use Converter.subConvertersList()

    ```python
    >>> c = converter.Converter()
    >>> for sc in c.defaultSubConverters():
    ...     print(sc)
    <class 'music21.converter.subConverters.ConverterABC'>
    <class 'music21.converter.subConverters.ConverterBraille'>
    <class 'music21.converter.subConverters.ConverterCapella'>
    <class 'music21.converter.subConverters.ConverterClercqTemperley'>
    <class 'music21.converter.subConverters.ConverterHumdrum'>
    <class 'music21.converter.subConverters.ConverterIPython'>
    <class 'music21.converter.subConverters.ConverterLilypond'>
    <class 'music21.converter.subConverters.ConverterMEI'>
    <class 'music21.converter.subConverters.ConverterMidi'>
    <class 'music21.converter.subConverters.ConverterMuseData'>
    <class 'music21.converter.subConverters.ConverterMusicXML'>
    <class 'music21.converter.subConverters.ConverterNoteworthy'>
    <class 'music21.converter.subConverters.ConverterNoteworthyBinary'>
    <class 'music21.converter.subConverters.ConverterRomanText'>
    <class 'music21.converter.subConverters.ConverterScala'>
    <class 'music21.converter.subConverters.ConverterText'>
    <class 'music21.converter.subConverters.ConverterTextLine'>
    <class 'music21.converter.subConverters.ConverterTinyNotation'>
    <class 'music21.converter.subConverters.ConverterVexflow'>
    <class 'music21.converter.subConverters.ConverterVolpiano'>
    <class 'music21.converter.subConverters.SubConverter'>
    ```

Converter.formatFromHeader(*dataStr: \_StrOrBytes*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), \_StrOrBytes][[source]](../_modules/music21/converter.html#Converter.formatFromHeader)
:   if dataStr begins with a text header such as “tinyNotation:” then
    return that format plus the dataStr with the head removed.

    Else, return (None, dataStr) where dataStr is the original untouched.

    The header is not detected case-sensitive.

    ```python
    >>> c = converter.Converter()
    >>> c.formatFromHeader('tinynotation: C4 E2')
    ('tinynotation', 'C4 E2')
    ```

    Note that the format is always returned in lower case:

    ```python
    >>> c.formatFromHeader('romanText: m1: a: I b2 V')
    ('romantext', 'm1: a: I b2 V')
    ```

    If there is no header then the format is None and the original is
    returned unchanged:

    ```python
    >>> c.formatFromHeader('C4 E2')
    (None, 'C4 E2')
    >>> c.formatFromHeader(b'binary-data')
    (None, b'binary-data')
    ```

    New formats can register new headers, like this old Amiga format:

    ```python
    >>> class ConverterSonix(converter.subConverters.SubConverter):
    ...    registerFormats = ('sonix',)
    ...    registerInputExtensions = ('mus',)
    >>> converter.registerSubConverter(ConverterSonix)
    >>> c.formatFromHeader('sonix: AIFF data')
    ('sonix', 'AIFF data')
    ```

    If bytes are passed in, the data is returned as bytes, but the
    header format is still converted to a string:

    ```python
    >>> c.formatFromHeader(b'romanText: m1: a: I b2 V')
    ('romantext', b'm1: a: I b2 V')
    ```

    Anything except string or bytes raises a ValueError:

    ```python
    >>> c.formatFromHeader(23)
    Traceback (most recent call last):
    ValueError: Cannot parse a format from <class 'int'>.
    ```

Converter.getFormatFromFileExtension(*fp*)[[source]](../_modules/music21/converter.html#Converter.getFormatFromFileExtension)
:   gets the format from a file extension.

    ```python
    >>> fp = common.getSourceFilePath() / 'musedata' / 'testZip.zip'
    >>> c = converter.Converter()
    >>> c.getFormatFromFileExtension(fp)
    'musedata'
    ```

static Converter.getSubConverterFormats() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")]][[source]](../_modules/music21/converter.html#Converter.getSubConverterFormats)
:   Get a dictionary of subConverters for various formats.

    (staticmethod: call on an instance or the class itself)

    ```python
    >>> scf = converter.Converter.getSubConverterFormats()
    >>> scf['abc']
    <class 'music21.converter.subConverters.ConverterABC'>
    >>> for x in sorted(scf):
    ...     x, scf[x]
    ('abc', <class 'music21.converter.subConverters.ConverterABC'>)
    ('braille', <class 'music21.converter.subConverters.ConverterBraille'>)
    ('capella', <class 'music21.converter.subConverters.ConverterCapella'>)
    ('clercqtemperley', <class 'music21.converter.subConverters.ConverterClercqTemperley'>)
    ('cttxt', <class 'music21.converter.subConverters.ConverterClercqTemperley'>)
    ('har', <class 'music21.converter.subConverters.ConverterClercqTemperley'>)
    ('humdrum', <class 'music21.converter.subConverters.ConverterHumdrum'>)
    ('ipython', <class 'music21.converter.subConverters.ConverterIPython'>)
    ('jupyter', <class 'music21.converter.subConverters.ConverterIPython'>)
    ('lily', <class 'music21.converter.subConverters.ConverterLilypond'>)
    ('lilypond', <class 'music21.converter.subConverters.ConverterLilypond'>)
    ('mei', <class 'music21.converter.subConverters.ConverterMEI'>)
    ('midi', <class 'music21.converter.subConverters.ConverterMidi'>)
    ('musedata', <class 'music21.converter.subConverters.ConverterMuseData'>)
    ('musicxml', <class 'music21.converter.subConverters.ConverterMusicXML'>)
    ('noteworthy', <class 'music21.converter.subConverters.ConverterNoteworthyBinary'>)
    ('noteworthytext', <class 'music21.converter.subConverters.ConverterNoteworthy'>)
    ('rntext', <class 'music21.converter.subConverters.ConverterRomanText'>)
    ('romantext', <class 'music21.converter.subConverters.ConverterRomanText'>)
    ('scala', <class 'music21.converter.subConverters.ConverterScala'>)
    ('t', <class 'music21.converter.subConverters.ConverterText'>)
    ('text', <class 'music21.converter.subConverters.ConverterText'>)
    ('textline', <class 'music21.converter.subConverters.ConverterTextLine'>)
    ('tinynotation', <class 'music21.converter.subConverters.ConverterTinyNotation'>)
    ('txt', <class 'music21.converter.subConverters.ConverterText'>)
    ('vexflow', <class 'music21.converter.subConverters.ConverterVexflow'>)
    ('volpiano', <class 'music21.converter.subConverters.ConverterVolpiano'>)
    ('xml', <class 'music21.converter.subConverters.ConverterMusicXML'>)
    ```

static Converter.getSubConverterFromFormat(*converterFormat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")[[source]](../_modules/music21/converter.html#Converter.getSubConverterFromFormat)
:   Return a particular subConverter class based on the format
    of the converterFormat string.

    Static method: call on the class itself or an instance:

    ```python
    >>> converter.Converter.getSubConverterFromFormat('musicxml')
    <music21.converter.subConverters.ConverterMusicXML object at 0x...>
    ```

Converter.parseData(*dataStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *number=None*, *format=None*, *forceSource=False*, *\*\*keywords*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter.html#Converter.parseData)
:   Given raw data, determine format and parse into a music21 Stream,
    set as self.stream.

Converter.parseFile(*fp*, *number=None*, *format=None*, *forceSource=False*, *storePickle=True*, *\*\*keywords*)[[source]](../_modules/music21/converter.html#Converter.parseFile)
:   Given a file path, parse and store a music21 Stream, set as self.stream.

    If format is None then look up the format from the file
    extension using common.findFormatFile.

    Will load from a pickle unless forceSource is True
    Will store as a pickle unless storePickle is False

Converter.parseFileNoPickle(*fp: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *format: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *forceSource: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/converter.html#Converter.parseFileNoPickle)
:   Given a file path, parse and store a music21 Stream.

    If format is None then look up the format from the file
    extension using common.findFormatFile.

    Does not use or store pickles in any circumstance.

Converter.parseURL(*url: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *format: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *forceSource: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter.html#Converter.parseURL)
:   Given a url, download and parse the file
    into a music21 Stream stored in the stream
    property of the converter object.

    Note that this checks the user Environment
    autoDownload setting before downloading.

    Use forceSource=True to download every time rather than
    re-reading from a cached file.

    ```python
    >>> joplinURL = ('https://github.com/cuthbertLab/music21/raw/master'
    ...              + '/music21/corpus/joplin/maple_leaf_rag.mxl')
    >>> c = converter.Converter()
    >>> c.parseURL(joplinURL)
    >>> joplinStream = c.stream
    ```

    * Changed in v7: made keyword-only and added forceSource option.

Converter.regularizeFormat(*fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter.html#Converter.regularizeFormat)
:   Take in a string representing a format, a file extension (w/ or without leading dot)
    etc. and find the format string that best represents the format that should be used.

    Searches SubConverter.registerFormats first, then SubConverter.registerInputExtensions,
    then SubConverter.registerOutputExtensions

    Returns None if no format applies:

    ```python
    >>> c = converter.Converter()
    >>> c.regularizeFormat('mxl')
    'musicxml'
    >>> c.regularizeFormat('t')
    'text'
    >>> c.regularizeFormat('abc')
    'abc'
    >>> c.regularizeFormat('lily.png')
    'lilypond'
    >>> c.regularizeFormat('blah') is None
    True
    ```

Converter.setSubConverterFromFormat(*converterFormat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](../_modules/music21/converter.html#Converter.setSubConverterFromFormat)
:   sets the .subConverter according to the format of converterFormat:

    ```python
    >>> convObj = converter.Converter()
    >>> convObj.setSubConverterFromFormat('humdrum')
    >>> convObj.subConverter
    <music21.converter.subConverters.ConverterHumdrum object at 0x...>
    ```

static Converter.subConvertersList(*converterType: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['any', 'input', 'output'] = 'any'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")]][[source]](../_modules/music21/converter.html#Converter.subConvertersList)
:   Gives a list of all the subConverter classes that are registered.

    If converterType is ‘any’ (true), then input or output
    subConverters are listed.

    Otherwise, ‘input’, or ‘output’ can be used to filter.

    ```python
    >>> c = converter.Converter()
    >>> scl = c.subConvertersList()
    >>> defaultScl = c.defaultSubConverters()
    >>> tuple(scl) == tuple(defaultScl)
    True
    ```

    ```python
    >>> sclInput = c.subConvertersList('input')
    >>> sclInput
    [<class 'music21.converter.subConverters.ConverterABC'>,
     <class 'music21.converter.subConverters.ConverterCapella'>,
     <class 'music21.converter.subConverters.ConverterClercqTemperley'>,
     <class 'music21.converter.subConverters.ConverterHumdrum'>,
     <class 'music21.converter.subConverters.ConverterMEI'>,
     <class 'music21.converter.subConverters.ConverterMidi'>,
     <class 'music21.converter.subConverters.ConverterMuseData'>,
     <class 'music21.converter.subConverters.ConverterMusicXML'>,
     <class 'music21.converter.subConverters.ConverterNoteworthy'>,
     <class 'music21.converter.subConverters.ConverterNoteworthyBinary'>,
     <class 'music21.converter.subConverters.ConverterRomanText'>,
     <class 'music21.converter.subConverters.ConverterScala'>,
     <class 'music21.converter.subConverters.ConverterTinyNotation'>,
     <class 'music21.converter.subConverters.ConverterVolpiano'>]
    ```

    Get those that can output (note that this is also a static method
    on converter)

    ```python
    >>> sclOutput = converter.Converter.subConvertersList('output')
    >>> sclOutput
    [<class 'music21.converter.subConverters.ConverterBraille'>,
     <class 'music21.converter.subConverters.ConverterLilypond'>,
     <class 'music21.converter.subConverters.ConverterMidi'>,
     <class 'music21.converter.subConverters.ConverterMusicXML'>,
     <class 'music21.converter.subConverters.ConverterRomanText'>,
     <class 'music21.converter.subConverters.ConverterScala'>,
     <class 'music21.converter.subConverters.ConverterText'>,
     <class 'music21.converter.subConverters.ConverterTextLine'>,
     <class 'music21.converter.subConverters.ConverterVexflow'>,
     <class 'music21.converter.subConverters.ConverterVolpiano'>]
    ```

    ```python
    >>> class ConverterSonix(converter.subConverters.SubConverter):
    ...    registerFormats = ('sonix',)
    ...    registerInputExtensions = ('mus',)
    >>> converter.registerSubConverter(ConverterSonix)
    >>> ConverterSonix in c.subConvertersList()
    True
    ```

    Newly registered subConverters appear first, so they will be used instead
    of any default subConverters that work on the same format or extension.

    ```python
    >>> class BadMusicXMLConverter(converter.subConverters.SubConverter):
    ...    registerFormats = ('musicxml',)
    ...    registerInputExtensions = ('xml', 'mxl', 'musicxml')
    ...    def parseData(self, strData, number=None):
    ...        self.stream = stream.Score(id='empty')
    ```

    ```python
    >>> converter.registerSubConverter(BadMusicXMLConverter)
    >>> c.subConvertersList()
    [<class '...BadMusicXMLConverter'>,
     ...
     <class 'music21.converter.subConverters.ConverterMusicXML'>,
     ...]
    ```

    Show that this musicxml file by Amy Beach is now parsed by BadMusicXMLConverter:

    ```python
    >>> s = corpus.parse('beach/prayer_of_a_tired_child')
    >>> s.id
    'empty'
    >>> len(s.parts)
    0
    ```

    Note that if the file has already been parsed by another subConverter format
    the parameter forceSource is required to force the file to be parsed by the
    newly registered subConverter:

    ```python
    >>> converter.unregisterSubConverter(BadMusicXMLConverter)
    >>> s = corpus.parse('beach/prayer_of_a_tired_child')
    >>> s.id
    'empty'
    >>> len(s.parts)
    0
    >>> s = corpus.parse('beach/prayer_of_a_tired_child', forceSource=True)
    >>> len(s.parts)
    6
    ```

[`Converter`](#music21.converter.Converter "music21.converter.Converter") instance variables

Converter.subConverter
:   a [`SubConverter`](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter") object
    that will do the actual converting.

## ArchiveManager

class music21.converter.ArchiveManager(*fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *archiveType='zip'*)[[source]](../_modules/music21/converter.html#ArchiveManager)
:   Before opening a file path, this class can check if this is an
    archived file collection, such as a .zip or .mxl file. This will return the
    data from the archive.

    ```python
    >>> fnCorpus = corpus.getWork('bwv66.6', fileExtensions=('.xml',))
    ```

    This is likely a unicode string

    ```python
    >>> fnCorpus
    '/Users/cuthbert/git/music21base/music21/corpus/bach/bwv66.6.mxl'
    >>> am = converter.ArchiveManager(fnCorpus)
    >>> am.isArchive()
    True
    >>> am.getNames()
    ['bwv66.6.xml', 'META-INF/container.xml']
    >>> data = am.getData()
    >>> data[0:70]
    '<?xml version="1.0" encoding="UTF-8"?>\r<!DOCTYPE score-partwise PUBLIC'
    ```

    The only archive type supported now is zip. But .mxl is zip so that covers almost
    everything.

[`ArchiveManager`](#music21.converter.ArchiveManager "music21.converter.ArchiveManager") methods

ArchiveManager.getData(*dataFormat='musicxml'*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[source]](../_modules/music21/converter.html#ArchiveManager.getData)
:   Return data from the archive.

    For ‘musedata’ format this will be a list of strings.
    For ‘musicxml’ this will be a single string.

    * Changed in v8: name is not used.

ArchiveManager.getNames() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/converter.html#ArchiveManager.getNames)
:   Return a list of all names contained in this archive.

ArchiveManager.isArchive() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/converter.html#ArchiveManager.isArchive)
:   Return True or False if the filepath is an
    archive of the supplied archiveType.

## PickleFilter

class music21.converter.PickleFilter(*fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *forceSource: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/converter.html#PickleFilter)
:   Before opening a file path, this class checks to see if there is an up-to-date
    version of the file pickled and stored in the scratch directory.

    If forceSource is True, then a pickle path will not be created.

    Provide a file path to check if there is pickled version.

    If forceSource is True, pickled files, if available, will not be
    returned.

[`PickleFilter`](#music21.converter.PickleFilter "music21.converter.PickleFilter") methods

PickleFilter.getPickleFp(*directory: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *zipType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter.html#PickleFilter.getPickleFp)
:   Returns the file path of the pickle file for this file.

    Returns a pathlib.Path

PickleFilter.removePickle() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter.html#PickleFilter.removePickle)
:   If a compressed pickled file exists, remove it from disk.

    Generally not necessary to call, since we can just overwrite obsolete pickles,
    but useful elsewhere.

PickleFilter.status() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/converter.html#PickleFilter.status)
:   Given a file path specified with \_\_init\_\_, look for an up-to-date pickled
    version of this file path. If it exists, return its fp, otherwise return the
    original file path.

    Return arguments are file path to load, boolean whether to write a pickle, and
    the file path of the pickle. All file paths can be pathlib.Path objects or None

    Does not check that fp exists or create the pickle file.

    ```python
    >>> fp = '/Users/Cuthbert/Desktop/musicFile.mxl'
    >>> pickFilter = converter.PickleFilter(fp)
    >>> pickFilter.status()
    (PosixPath('/Users/Cuthbert/Desktop/musicFile.mxl'), True,
          PosixPath('/tmp/music21/m21-10.0.0-py3.13-18b8c5a5f07826bd67ea0f20462f0b8d.p.gz'))
    ```

## Functions

music21.converter.parse(*value: [MetadataEntry](moduleMetadataBundles.html#music21.metadata.bundles.MetadataEntry "music21.metadata.bundles.MetadataEntry") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*, *\**, *forceSource: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *format: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/converter.html#parse)
:   Given a file path, encoded data in a Python string, or a URL, attempt to
    parse the item into a Stream. Note: URL downloading will not happen
    automatically unless the user has set their Environment “autoDownload”
    preference to “allow”.

    Keywords can include number which specifies a piece number in a file of
    multi-piece file. (Otherwise, a particular score from an
    `Opus` can also be extracted by providing a
    two-element list or tuple of the form (path, number) to the value argument.)

    format specifies the format to parse the line of text or the file as.

    quantizePost specifies whether to quantize a stream resulting from MIDI conversion.
    By default, MIDI streams are quantized to the nearest sixteenth or triplet-eighth
    (i.e. smaller durations will not be preserved).
    quarterLengthDivisors sets the quantization units explicitly.

    A string of text is first checked to see if it is a filename that exists on
    disk. If not it is searched to see if it looks like a URL. If not it is
    processed as data.

    PC File:

    ```python
    >>> s = converter.parse(r'c:\users\myke\desktop\myFile.xml')
    ```

    Mac File:

    ```python
    >>> s = converter.parse('/Users/cuthbert/Desktop/myFile.xml')
    ```

    URL:

    ```python
    >>> s = converter.parse('https://midirepository.org/file220/file.mid')
    ```

    Data is preceded by an identifier such as “tinynotation:”

    ```python
    >>> s = converter.parse("tinyNotation: 3/4 E4 r f# g=lastG trip{b-8 a g} c", makeNotation=False)
    >>> s[meter.TimeSignature].first()
    <music21.meter.TimeSignature 3/4>
    ```

    or the format can be passed directly:

    ```python
    >>> s = converter.parse("2/16 E4 r f# g=lastG trip{b-8 a g} c", format='tinyNotation')
    >>> s[meter.TimeSignature].first()
    <music21.meter.TimeSignature 2/16>
    ```

    * Changed in v8: passing a list of tinyNotation strings was never documented as a
      :   possibility and has been removed.

music21.converter.parseFile(*fp*, *number=None*, *format=None*, *forceSource=False*, *\*\*keywords*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/converter.html#parseFile)
:   Given a file path, attempt to parse the file into a Stream.

music21.converter.parseData(*dataStr*, *number=None*, *format=None*, *\*\*keywords*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/converter.html#parseData)
:   Given musical data represented within a Python string, attempt to parse the
    data into a Stream.

music21.converter.parseURL(*url*, *\**, *format=None*, *number=None*, *forceSource=False*, *\*\*keywords*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/converter.html#parseURL)
:   Given a URL, attempt to download and parse the file into a Stream. Note:
    URL downloading will not happen automatically unless the user has set their
    Environment “autoDownload” preference to “allow”.

    * Changed in v7: made keyword-only.

music21.converter.freeze(*streamObj*, *fmt=None*, *fp=None*, *fastButUnsafe=False*, *zipType='zlib'*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter.html#freeze)
:   Given a StreamObject and a file path, serialize and store the Stream to a file.

    This function is based on the `StreamFreezer` object.

    The serialization format is defined by the fmt argument; ‘pickle’ (the default) is only one
    presently supported. ‘json’ or ‘jsonnative’ will be used once jsonpickle is good enough.

    If no file path is given, a temporary file is used.

    The file path is returned.

    ```python
    >>> c = converter.parse('tinynotation: 4/4 c4 d e f')
    >>> c.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note F>
        {4.0} <music21.bar.Barline type=final>
    >>> fp = converter.freeze(c, fmt='pickle')
    >>> fp
    PosixPath('/tmp/music21/sjiwoe.p.gz')
    ```

    The file can then be “thawed” back into a Stream using the
    [`thaw()`](#music21.converter.thaw "music21.converter.thaw") method.

    ```python
    >>> d = converter.thaw(fp)
    >>> d.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note F>
        {4.0} <music21.bar.Barline type=final>
    ```

music21.converter.thaw(*fp*, *zipType='zlib'*)[[source]](../_modules/music21/converter.html#thaw)
:   Given a file path of a serialized Stream, defrost the file into a Stream.

    This function is based on the `StreamFreezer` object.

    See the documentation for [`freeze()`](#music21.converter.freeze "music21.converter.freeze") for demos.

music21.converter.freezeStr(*streamObj*, *fmt=None*)[[source]](../_modules/music21/converter.html#freezeStr)
:   Given a StreamObject
    serialize and return a serialization string.

    This function is based on the
    `StreamFreezer` object.

    The serialization format is defined by
    the fmt argument; ‘pickle’ (the default),
    is the only one presently supported.

    ```python
    >>> c = converter.parse('tinyNotation: 4/4 c4 d e f', makeNotation=False)
    >>> c.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    {2.0} <music21.note.Note E>
    {3.0} <music21.note.Note F>
    >>> data = converter.freezeStr(c, fmt='pickle')
    >>> len(data) > 20  # pickle implementation dependent
    True
    >>> d = converter.thawStr(data)
    >>> d.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    {2.0} <music21.note.Note E>
    {3.0} <music21.note.Note F>
    ```

music21.converter.thawStr(*strData*)[[source]](../_modules/music21/converter.html#thawStr)
:   Given a serialization string, defrost into a Stream.

    This function is based on the `StreamFreezer` object.

music21.converter.registerSubConverter(*newSubConverter: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter.html#registerSubConverter)
:   Add a SubConverter to the list of registered subConverters.

    Example, register a converter for the obsolete Amiga composition software Sonix (so fun!)

    ```python
    >>> class ConverterSonix(converter.subConverters.SubConverter):
    ...    registerFormats = ('sonix',)
    ...    registerInputExtensions = ('mus',)
    ```

    ```python
    >>> converter.registerSubConverter(ConverterSonix)
    >>> scf = converter.Converter().getSubConverterFormats()
    >>> for x in sorted(scf):
    ...     x, scf[x]
    ('abc', <class 'music21.converter.subConverters.ConverterABC'>)
    ...
    ('sonix', <class '...ConverterSonix'>)
    ...
    ```

    See converter.qmConverter for an example of an extended subConverter.

    Changed in v.9 – custom subConverters are registered above default subConverters.

music21.converter.unregisterSubConverter(*removeSubConverter: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['all'] | [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/converter.html#unregisterSubConverter)
:   Remove a SubConverter from the list of registered subConverters.

    (Note that the list is a shared list across all Converters currently –
    that has long been considered a feature, but with multiprocessing, this
    could change in the future.)

    ```python
    >>> mxlConverter = converter.subConverters.ConverterMusicXML
    ```

    ```python
    >>> c = converter.Converter()
    >>> mxlConverter in c.subConvertersList()
    True
    >>> converter.unregisterSubConverter(mxlConverter)
    >>> mxlConverter in c.subConvertersList()
    False
    ```

    If there is no such subConverter registered, and it is not a default subConverter,
    then a converter.ConverterException is raised:

    ```python
    >>> class ConverterSonix(converter.subConverters.SubConverter):
    ...    registerFormats = ('sonix',)
    ...    registerInputExtensions = ('mus',)
    ```

    ```python
    >>> converter.unregisterSubConverter(ConverterSonix)
    Traceback (most recent call last):
    music21.converter.ConverterException: Could not remove <class '...ConverterSonix'> from
                registered subConverters
    ```

    The special command “all” removes everything including the default converters:

    ```python
    >>> converter.unregisterSubConverter('all')
    >>> c.subConvertersList()
    []
    ```

    Housekeeping: let’s reset our subconverters and check things are okay again.

    ```python
    >>> converter.resetSubConverters()
    >>> c = converter.Converter()
    >>> mxlConverter in c.subConvertersList()
    True
    ```

music21.converter.resetSubConverters()[[source]](../_modules/music21/converter.html#resetSubConverters)
:   Reset state to default (removing all registered and deregistered subConverters).

music21.converter.toData(*obj: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\*\*keywords*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/converter.html#toData)
:   Convert obj to the given format fmt and return the information retrieved.

    Currently, this is somewhat inefficient: it calls SubConverter.toData which
    calls write() on the object and reads back the value of the file.

    ```python
    >>> tiny = converter.parse('tinyNotation: 4/4 C4 D E F G1')
    >>> data = converter.toData(tiny, 'braille.ascii')
    >>> type(data)
    <class 'str'>
    >>> print(data)
        #D4
    #A _?:$] (<K
    ```
