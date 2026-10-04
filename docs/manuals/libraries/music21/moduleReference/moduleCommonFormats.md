Source: https://music21.org/music21docs/moduleReference/moduleCommonFormats.html

# music21.common.formats

Utilities for working with file formats.

almost everything here is deprecated.

## Functions

music21.common.formats.findFormat(*fmt*)[[source]](../_modules/music21/common/formats.html#findFormat)
:   Given a format defined either by a format name, abbreviation, or
    an extension, return the regularized format name as well as
    the output extensions.

    DEPRECATED May 2014 – moving to converter

    All but the first element of the tuple are deprecated for use, since
    the extension can vary by subConverter (e.g., lily.png)

    ```python
    >>> common.findFormat('.mxl')
    ('musicxml', '.musicxml')
    >>> common.findFormat('musicxml')
    ('musicxml', '.musicxml')
    >>> common.findFormat('lily')
    ('lilypond', '.ly')
    >>> common.findFormat('lily.png')
    ('lilypond', '.ly')
    >>> common.findFormat('humdrum')
    ('humdrum', '.krn')
    >>> common.findFormat('txt')
    ('text', '.txt')
    >>> common.findFormat('textline')
    ('textline', '.txt')
    >>> common.findFormat('midi')
    ('midi', '.mid')
    >>> common.findFormat('abc')
    ('abc', '.abc')
    >>> common.findFormat('scl')
    ('scala', '.scl')
    >>> common.findFormat('braille')
    ('braille', '.txt')
    >>> common.findFormat('vexflow')
    ('vexflow', '.html')
    >>> common.findFormat('capx')
    ('capella', '.capx')
    ```

    Works the same whether you have a leading dot or not:

    ```python
    >>> common.findFormat('md')
    ('musedata', '.md')
    >>> common.findFormat('.md')
    ('musedata', '.md')
    ```

    If you give something we can’t deal with, returns a Tuple of None, None:

    ```python
    >>> common.findFormat('wpd')
    (None, None)
    ```

music21.common.formats.findFormatExtFile(*fp*)[[source]](../_modules/music21/common/formats.html#findFormatExtFile)
:   Given a file path (relative or absolute)
    find format and extension used (not the output extension)

    DEPRECATED May 2014 – moving to converter

    ```python
    >>> common.findFormatExtFile('test.mxl')
    ('musicxml', '.mxl')
    >>> common.findFormatExtFile('long/file/path/test-2009.03.02.xml')
    ('musicxml', '.xml')
    >>> common.findFormatExtFile('long/file/path.intermediate.png/test-2009.03.xml')
    ('musicxml', '.xml')
    ```

    ```python
    >>> common.findFormatExtFile('test')
    (None, None)
    ```

    Windows drive
    >>> common.findFormatExtFile(‘d:/long/file/path/test.xml’)
    (‘musicxml’, ‘.xml’)

    On a windows networked filesystem
    >>> common.findFormatExtFile(r’\longfilepathtest.krn’)
    (‘humdrum’, ‘.krn’)

music21.common.formats.findFormatExtURL(*url*)[[source]](../_modules/music21/common/formats.html#findFormatExtURL)
:   Given a URL, attempt to find the extension.
    This may scrub arguments in a URL, or simply look at the last characters.

    DEPRECATED May 2014 – moving to converter

    ```python
    >>> urlA = 'http://somesite.com/?l=cc/schubert/piano/d0576&file=d0576-06.krn&f=xml'
    >>> urlB = 'http://somesite.com/cgi-bin/ksdata?l=cc/schubert/d0576&file=d0576-06.krn&f=kern'
    >>> urlC = 'http://somesite.com/cgi-bin/ksdata?l=cc/bach/cello&file=bwv1007-01.krn&f=xml'
    >>> urlF = 'https://junk'
    >>> urlM = 'http://somesite.com/files/mid001.mid'
    ```

    ```python
    >>> common.findFormatExtURL(urlA)
    ('musicxml', '.xml')
    >>> common.findFormatExtURL(urlB)
    ('humdrum', '.krn')
    >>> common.findFormatExtURL(urlC)
    ('musicxml', '.xml')
    >>> common.findFormatExtURL(urlF)
    (None, None)
    >>> common.findFormatExtURL(urlM)
    ('midi', '.mid')
    ```

music21.common.formats.findFormatFile(*fp*)[[source]](../_modules/music21/common/formats.html#findFormatFile)
:   Given a file path (relative or absolute) return the format

    DEPRECATED May 2014 – moving to converter

    ```python
    >>> common.findFormatFile('test.xml')
    'musicxml'
    >>> common.findFormatFile('long/file/path/test-2009.03.02.xml')
    'musicxml'
    >>> common.findFormatFile('long/file/path.intermediate.png/test-2009.03.xml')
    'musicxml'
    ```

    On a windows networked filesystem
    >>> common.findFormatFile(r’\longfilepathtest.krn’)
    ‘humdrum’

music21.common.formats.findSubConverterForFormat(*fmt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[SubConverter](moduleConverterSubConverters.html#music21.converter.subConverters.SubConverter "music21.converter.subConverters.SubConverter")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/common/formats.html#findSubConverterForFormat)
:   return a converter.subConverter.SubConverter subclass
    for a given format – this is a music21 format name,
    not a file extension. Or returns None

    ```python
    >>> common.findSubConverterForFormat('musicxml')
    <class 'music21.converter.subConverters.ConverterMusicXML'>
    ```

    ```python
    >>> common.findSubConverterForFormat('text')
    <class 'music21.converter.subConverters.ConverterText'>
    ```

    ```python
    >>> common.findSubConverterForFormat('romantext')
    <class 'music21.converter.subConverters.ConverterRomanText'>
    ```

    Some subConverters have format aliases

    ```python
    >>> common.findSubConverterForFormat('t')
    <class 'music21.converter.subConverters.ConverterText'>
    ```
