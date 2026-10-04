Source: https://music21.org/music21docs/moduleReference/moduleAbcFormat.html

# music21.abcFormat

ABC is a music format that, while being able to encode all sorts of scores, is especially
strong at representing monophonic music, and folk music in particular.

Modules in the music21.abcFormat package deal with importing ABC into music21. Most people
working with ABC data won’t need to use this package. To convert ABC from a file or URL
to a `Stream` use the [`parse()`](moduleConverter.html#music21.converter.parse "music21.converter.parse") function of
the converter module:

```python
>>> from music21 import *
>>> abcScore = converter.parse('/users/ariza/myScore.abc')
```

For users who will be editing ABC extensively or need a way to have music21 output ABC
(which it doesn’t do natively), we suggest using the open source EasyABC package:
<https://easyabc.sourceforge.net> . You can set it up as a MusicXML reader through:

```python
>>> us = environment.UserSettings()
>>> us['musicxmlPath'] = '/Applications/EasyABC.app'
```

or wherever you have downloaded EasyABC to
(PC users might need: ‘c:/program files (x86)/easyabc/easyabc.exe’)
(Thanks to Norman Schmidt for the heads-up)

There is a two-step process in converting ABC files to music21 Streams. First this module
reads in the text-based .abc file and converts all the information into ABCToken objects. Then
the function [`music21.abcFormat.translate.abcToStreamScore()`](moduleAbcFormatTranslate.html#music21.abcFormat.translate.abcToStreamScore "music21.abcFormat.translate.abcToStreamScore") of
the [music21.abcFormat.translate](moduleAbcFormatTranslate.html#moduleabcformattranslate) module
translates those Tokens into music21 objects.

Music21 implements the entire v1.6 ABC standard (January 1997) found at
<https://abcnotation.com/standard/abc_v1.6.txt> . The system aims to support the
v2.1 ABC standard (December 2011) found at
<https://abcnotation.com/wiki/abc:standard:v2.1> but some parts (e.g. 4.10 Variant Endings) are not
implemented. No support is yet given for the draft 2.2 standard.

## ABCFile

class music21.abcFormat.ABCFile(*abcVersion: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = (1, 3, 0)*)[[source]](../_modules/music21/abcFormat.html#ABCFile)
:   ABC File or String access

    The abcVersion attribution optionally specifies the (major, minor, patch)
    version of ABC to process– e.g., (2, 1, 0).

    If not set, default ABC 1.3 parsing is performed.

[`ABCFile`](#music21.abcFormat.ABCFile "music21.abcFormat.ABCFile") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ABCFile`](#music21.abcFormat.ABCFile "music21.abcFormat.ABCFile") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCFile`](#music21.abcFormat.ABCFile "music21.abcFormat.ABCFile") methods

ABCFile.close()[[source]](../_modules/music21/abcFormat.html#ABCFile.close)

static ABCFile.extractReferenceNumber(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCFile.extractReferenceNumber)
:   Extract the string data relating to a single reference number
    from a file that defines multiple songs or pieces.

    This method permits loading a single work from a collection/opus
    without parsing the entire file.

    Here is sample data that is not correct ABC but demonstrates the basic concept:

    ```python
    >>> fileData = """
    ...   X:1
    ...   Hello
    ...   X:2
    ...   Aloha
    ...   X:3
    ...   Goodbye
    ...   """
    ```

    ```python
    >>> file2 = abcFormat.ABCFile.extractReferenceNumber(fileData, 2)
    >>> print(file2)
    X:2
    Aloha
    ```

    If the number does not exist, raises an ABCFileException:

    ```python
    >>> abcFormat.ABCFile.extractReferenceNumber(fileData, 99)
    Traceback (most recent call last):
    music21.abcFormat.ABCFileException: cannot find requested
        reference number in source file: 99
    ```

    If the same number is defined twice in one file (should not be) only
    the first data is returned.

    * Changed in v6.2: now a static method.

ABCFile.open(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*)[[source]](../_modules/music21/abcFormat.html#ABCFile.open)
:   Open a file for reading

ABCFile.openFileLike(*fileLike*)[[source]](../_modules/music21/abcFormat.html#ABCFile.openFileLike)
:   Assign a file-like object, such as those provided by
    StringIO, as an open file object.

    ```python
    >>> from io import StringIO
    >>> fileLikeOpen = StringIO()
    ```

ABCFile.read(*number=None*)[[source]](../_modules/music21/abcFormat.html#ABCFile.read)
:   Read a file. Note that this calls readstr,
    which processes all tokens.

    If number is given, a work number will be extracted if possible.

ABCFile.readstr(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [ABCHandler](#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler")[[source]](../_modules/music21/abcFormat.html#ABCFile.readstr)
:   Read a string and process all Tokens.
    Returns a ABCHandler instance.

## ABCHandler

class music21.abcFormat.ABCHandler(*abcVersion: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...] = (1, 3, 0)*, *lineBreaksDefinePhrases=False*)[[source]](../_modules/music21/abcFormat.html#ABCHandler)
:   An ABCHandler is able to divide elements of a character stream into objects and handle
    store in a list, and passes global information to components

    Optionally, specify the (major, minor, patch) version of ABC to process–
    e.g., (1.2.0). If not set, default ABC 1.3 parsing is performed.

    If lineBreaksDefinePhrases is True then new lines within music elements
    define new phrases. This is useful for parsing extra information from
    the Essen Folksong repertory

    * New in v6.3: lineBreaksDefinePhrases – does not yet do anything

[`ABCHandler`](#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler") methods

static ABCHandler.barlineTokenFilter(*token: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ABCBar](#music21.abcFormat.ABCBar "music21.abcFormat.ABCBar")][[source]](../_modules/music21/abcFormat.html#ABCHandler.barlineTokenFilter)
:   Some single barline tokens are better replaced
    with two tokens. This method, given a token,
    returns a list of tokens. If there is no change
    necessary, the provided token will be returned within
    the list.

    A staticmethod. Call on the class itself.

    ```python
    >>> abcFormat.ABCHandler.barlineTokenFilter('::')
    [<music21.abcFormat.ABCBar ':|'>, <music21.abcFormat.ABCBar '|:'>]
    ```

    ```python
    >>> abcFormat.ABCHandler.barlineTokenFilter('|2')
    [<music21.abcFormat.ABCBar '|'>, <music21.abcFormat.ABCBar '[2'>]
    ```

    ```python
    >>> abcFormat.ABCHandler.barlineTokenFilter(':|1')
    [<music21.abcFormat.ABCBar ':|'>, <music21.abcFormat.ABCBar '[1'>]
    ```

    If nothing matches, the original token is returned as an ABCBar object:

    ```python
    >>> abcFormat.ABCHandler.barlineTokenFilter('hi')
    [<music21.abcFormat.ABCBar 'hi'>]
    ```

ABCHandler.definesMeasures()[[source]](../_modules/music21/abcFormat.html#ABCHandler.definesMeasures)
:   Returns True if this token structure defines Measures in a normal Measure form.
    Otherwise False

    ```python
    >>> abcStr = ('M:6/8\nL:1/8\nK:G\nV:1 name="Whistle" ' +
    ...     'snm="wh"\nB3 A3 | G6 | B3 A3 | G6 ||\nV:2 name="violin" ' +
    ...     'snm="v"\nBdB AcA | GAG D3 | BdB AcA | GAG D6 ||\nV:3 name="Bass" ' +
    ...     'snm="b" clef=bass\nD3 D3 | D6 | D3 D3 | D6 ||')
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStr)
    >>> ah.definesMeasures()
    True
    ```

    ```python
    >>> abcStr = 'M:6/8\nL:1/8\nK:G\nB3 A3 G6 B3 A3 G6'
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStr)
    >>> ah.definesMeasures()
    False
    ```

ABCHandler.definesReferenceNumbers()[[source]](../_modules/music21/abcFormat.html#ABCHandler.definesReferenceNumbers)
:   Return True if this token structure defines more than 1 reference number,
    usually implying multiple pieces encoded in one file.

    ```python
    >>> abcStr = 'X:5\nM:6/8\nL:1/8\nK:G\nB3 A3 | G6 | B3 A3 | G6 ||'
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStr)
    >>> ah.definesReferenceNumbers()  # only one returns False
    False
    ```

    ```python
    >>> abcStr = 'X:5\nM:6/8\nL:1/8\nK:G\nB3 A3 | G6 | B3 A3 | G6 ||\n'
    >>> abcStr += 'X:6\nM:6/8\nL:1/8\nK:G\nB3 A3 | G6 | B3 A3 | G6 ||'
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStr)
    ```

    There are two tokens, so this returns True

    ```python
    >>> ah.definesReferenceNumbers()
    True
    ```

ABCHandler.getReferenceNumber()[[source]](../_modules/music21/abcFormat.html#ABCHandler.getReferenceNumber)
:   If tokens are processed, get the first
    reference number defined.

    ```python
    >>> abcStr = 'X:5\nM:6/8\nL:1/8\nK:G\nB3 A3 | G6 | B3 A3 | G6 ||'
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStr)
    >>> ah.getReferenceNumber()
    '5'
    ```

ABCHandler.getTitle() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.getTitle)
:   Get the first title tag. Used for testing.

    Requires tokens to have been processed.

ABCHandler.hasNotes() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.hasNotes)
:   If tokens are processed, return True if ABCNote or
    ABCChord classes are defined

    ```python
    >>> abcStr = 'M:6/8\nL:1/8\nK:G\n'
    >>> ah1 = abcFormat.ABCHandler()
    >>> junk = ah1.process(abcStr)
    >>> ah1.hasNotes()
    False
    ```

    ```python
    >>> abcStr = 'M:6/8\nL:1/8\nK:G\nc1D2'
    >>> ah2 = abcFormat.ABCHandler()
    >>> junk = ah2.process(abcStr)
    >>> ah2.hasNotes()
    True
    ```

ABCHandler.parseHeaderForVersionInformation(*inputSearch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.parseHeaderForVersionInformation)
:   Search a line of text for a comment abc version number

    ```python
    >>> ah = abcFormat.ABCHandler()
    >>> ah.abcVersion
    (1, 3, 0)
    ```

    ```python
    >>> ah.parseHeaderForVersionInformation('%abc-2.3.2')
    >>> ah.abcVersion
    (2, 3, 2)
    ```

    Changed in v9: abcVersion defaults to (1, 3, 0) as documented.

ABCHandler.process(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.process)

ABCHandler.processComment()[[source]](../_modules/music21/abcFormat.html#ABCHandler.processComment)
:   Processes the comment at self.pos in self.strSrc, setting self.skipAhead
    and self.abcDirectives for the directiveKey.

    ```python
    >>> from textwrap import dedent
    >>> ah = abcFormat.ABCHandler()
    >>> data = dedent("""
    ...    Hello % this is a comment
    ...    Bye
    ...    """)
    >>> ah.strSrc = data
    >>> ah.pos = 6
    >>> ah.processComment()
    >>> ah.skipAhead
    19
    >>> len(' this is a comment\n')
    19
    ```

    Directives get stored in the handler:

    ```python
    >>> data = '%%abc-hello world'
    >>> ah = abcFormat.ABCHandler()
    >>> ah.strSrc = data
    >>> ah.pos = 0
    >>> ah.processComment()
    >>> ah.abcDirectives
    {'abc-hello': 'world'}
    >>> ah.abcDirectives['abc-hello']
    'world'
    ```

    * Changed in v9: version is not parsed by this method.

static ABCHandler.returnAbcVersionFromMatch(*verMats: [Match](https://docs.python.org/3/library/re.html#re.Match "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/abcFormat.html#ABCHandler.returnAbcVersionFromMatch)
:   Given a match from a regular expression return the parsed ABC version

    ```python
    >>> import re
    >>> match = re.match(r'(\d+).(\d+).(\d+)', '2.3.4')
    >>> ah = abcFormat.ABCHandler()
    >>> ah.returnAbcVersionFromMatch(match)
    (2, 3, 4)
    ```

    ```python
    >>> match = re.match(r'(\d+).(\d+).?(\d?)', '1.7')
    >>> ah.returnAbcVersionFromMatch(match)
    (1, 7, 0)
    ```

ABCHandler.splitByMeasure() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ABCHandlerBar](#music21.abcFormat.ABCHandlerBar "music21.abcFormat.ABCHandlerBar")][[source]](../_modules/music21/abcFormat.html#ABCHandler.splitByMeasure)
:   Divide a token list by Measures, also
    defining start and end bars of each Measure.

    If a component does not have notes, leave
    as an empty bar. This is often done with leading metadata.

    Returns a list of ABCHandlerBar instances.
    The first usually defines only Metadata

    TODO: Test and examples

ABCHandler.splitByReferenceNumber() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [ABCHandler](#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler")][[source]](../_modules/music21/abcFormat.html#ABCHandler.splitByReferenceNumber)
:   Split tokens by reference numbers.

    Returns a dictionary of ABCHandler instances, where the reference number
    is used to access the music. If no reference numbers are defined,
    the tune is available under the dictionary entry None.

    ```python
    >>> abcStr = 'X:5\nM:6/8\nL:1/8\nK:G\nB3 A3 | G6 | B3 A3 | G6 ||'
    >>> abcStr += 'X:6\nM:6/8\nL:1/8\nK:G\nB3 A3 | G6 | B3 A3 | G6 ||'
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStr)
    >>> len(ah)
    28
    >>> ahDict = ah.splitByReferenceNumber()
    >>> 5 in ahDict
    True
    >>> 6 in ahDict
    True
    >>> 7 in ahDict
    False
    ```

    Each entry is its own ABCHandler object.

    ```python
    >>> ahDict[5]
    <music21.abcFormat.ABCHandler object at 0x10b0cf5f8>
    >>> len(ahDict[5].tokens)
    14
    ```

    Header information (except for comments) should be appended to all pieces.

    ```python
    >>> from textwrap import dedent
    >>> abcEarly = dedent("""X:4
    ...    M:6/8
    ...    L:1/8
    ...    K:F
    ...    I:abc-version 1.6
    ...    B=3 B3 | G6 | B3 A3 | G6 ||
    ...    """)
    >>> abcStrWHeader = '%abc-2.1\nO: Irish\n' + abcEarly + abcStr
    ```

    ```python
    >>> ah = abcFormat.ABCHandler()
    >>> junk = ah.process(abcStrWHeader)
    >>> len(ah)
    44
    >>> ahDict = ah.splitByReferenceNumber()
    ```

    Did we get the origin header in each score?

    ```python
    >>> ahDict[5].tokens[0]
    <music21.abcFormat.ABCMetadata 'O: Irish'>
    >>> ahDict[6].tokens[0]
    <music21.abcFormat.ABCMetadata 'O: Irish'>
    ```

    Before parsing all the tokens should have the 2.1 version:

    ```python
    >>> ahDict[4].abcVersion
    (2, 1, 0)
    >>> ahDict[5].abcVersion
    (2, 1, 0)
    ```

    After parsing, the abcVersion should be set for score 4 and
    revert for score 5.

    ```python
    >>> for f in ahDict:
    ...    _ = abcFormat.translate.abcToStreamScore(ahDict[f])
    >>> ahDict[4].abcVersion
    (1, 6, 0)
    >>> ahDict[5].abcVersion
    (2, 1, 0)
    ```

ABCHandler.splitByVoice() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ABCHandler](#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler")][[source]](../_modules/music21/abcFormat.html#ABCHandler.splitByVoice)
:   Given a processed token list, look for voices. If voices exist,
    split into parts: common metadata, then next voice, next voice, etc.

    Each part is returned as a ABCHandler instance.

    ```python
    >>> abcStr = ('M:6/8\nL:1/8\nK:G\nV:1 name="Whistle" ' +
    ...     'snm="wh"\nB3 A3 | G6 | B3 A3 | G6 ||\nV:2 name="violin" ' +
    ...     'snm="v"\nBdB AcA | GAG D3 | BdB AcA | GAG D6 ||\nV:3 name="Bass" ' +
    ...     'snm="b" clef=bass\nD3 D3 | D6 | D3 D3 | D6 ||')
    >>> ah = abcFormat.ABCHandler()
    >>> ah.process(abcStr)
    >>> tokenColls = ah.splitByVoice()
    >>> tokenColls[0]
    <music21.abcFormat.ABCHandler object at 0x...>
    ```

    Common headers are first

    ```python
    >>> [token.src for token in tokenColls[0].tokens]
    ['M:6/8', 'L:1/8', 'K:G']
    ```

    Then each voice

    ```python
    >>> [token.src for token in tokenColls[1].tokens]
    ['V:1 name="Whistle" snm="wh"',
     'B3', 'A3', '|', 'G6', '|', 'B3', 'A3', '|', 'G6', '||']
    >>> [token.src for token in tokenColls[2].tokens]
    ['V:2 name="violin" snm="v"',
     'B', 'd', 'B', 'A', 'c', 'A', '|',
     'G', 'A', 'G', 'D3', '|',
     'B', 'd', 'B', 'A', 'c', 'A', '|',
     'G', 'A', 'G', 'D6', '||']
    >>> [token.src for token in tokenColls[3].tokens]
    ['V:3 name="Bass" snm="b" clef=bass',
     'D3', 'D3', '|', 'D6', '|',
     'D3', 'D3', '|', 'D6', '||']
    ```

    Then later the metadata can be merged at the start of each voice:

    ```python
    >>> mergedTokens = tokenColls[0] + tokenColls[1]
    >>> mergedTokens
    <music21.abcFormat.ABCHandler object at 0x...>
    >>> [token.src for token in mergedTokens.tokens]
    ['M:6/8', 'L:1/8', 'K:G', 'V:1 name="Whistle" snm="wh"',
     'B3', 'A3', '|', 'G6', '|',
     'B3', 'A3', '|', 'G6', '||']
    ```

static ABCHandler.startsMetadata(*c: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *cNext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *cNextNext: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.startsMetadata)
:   Returns True if this context describes the start of a metadata section, like

    A:something

    Metadata: capital letter, with next char as ‘:’ and some following character

    ```python
    >>> ah = abcFormat.ABCHandler
    >>> ah.startsMetadata('A', ':', 's')
    True
    ```

    lowercase w: is a special case for lyric defs

    ```python
    >>> ah.startsMetadata('w', ':', 's')
    True
    ```

    Following char must be “:”

    ```python
    >>> ah.startsMetadata('A', ' ', 's')
    False
    ```

    Pipe after colon indicates not metadata (bar info).
    For example need to not misinterpret repeat bars as metadata
    e.g. dAG FED:|2 dAG FGA|

    this is incorrect, but we can avoid it by
    looking for a leading pipe and returning False

    ```python
    >>> ah.startsMetadata('A', ':', '|')
    False
    ```

    ```python
    >>> ah.startsMetadata('A', ':', None)
    False
    ```

ABCHandler.tokenProcess() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.tokenProcess)
:   Process all token objects. First, calls preParse(), then
    does context assignments, then calls parse().

ABCHandler.tokenize(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCHandler.tokenize)
:   Walk the abc string, creating ABC objects along the way.

    This may be called separately from process(), in the case
    that pre-/post-parse processing is not needed.

    ```python
    >>> abch = abcFormat.ABCHandler()
    >>> abch.tokens
    []
    >>> abch.tokenize('X: 1')
    >>> abch.tokens
    [<music21.abcFormat.ABCMetadata 'X: 1'>]
    ```

    ```python
    >>> abch = abcFormat.ABCHandler()
    >>> abch.tokenize('(6f')
    >>> abch.tokens
    [<music21.abcFormat.ABCTuplet '(6'>, <music21.abcFormat.ABCNote 'f'>]
    ```

    ```python
    >>> abch = abcFormat.ABCHandler()
    >>> abch.tokenize('(6:4f')
    >>> abch.tokens
    [<music21.abcFormat.ABCTuplet '(6:4'>, <music21.abcFormat.ABCNote 'f'>]
    ```

    ```python
    >>> abch = abcFormat.ABCHandler()
    >>> abch.tokenize('(6:4:2f')
    >>> abch.tokens
    [<music21.abcFormat.ABCTuplet '(6:4:2'>, <music21.abcFormat.ABCNote 'f'>]
    ```

    ```python
    >>> abch = abcFormat.ABCHandler()
    >>> abch.tokenize('(6::2f')
    >>> abch.tokens
    [<music21.abcFormat.ABCTuplet '(6::2'>, <music21.abcFormat.ABCNote 'f'>]
    ```

ABCHandler.tokensToBarIndices() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/abcFormat.html#ABCHandler.tokensToBarIndices)
:   Return a list of indices indicating which tokens in self.tokens are
    bar lines or the last piece of metadata before a note or chord.

## ABCHandlerBar

class music21.abcFormat.ABCHandlerBar[[source]](../_modules/music21/abcFormat.html#ABCHandlerBar)
:   A Handler specialized for storing bars. All left
    and right bars are collected and assigned to their respective attributes.

[`ABCHandlerBar`](#music21.abcFormat.ABCHandlerBar "music21.abcFormat.ABCHandlerBar") bases

* [`ABCHandler`](#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler")

[`ABCHandlerBar`](#music21.abcFormat.ABCHandlerBar "music21.abcFormat.ABCHandlerBar") methods

Methods inherited from [`ABCHandler`](#music21.abcFormat.ABCHandler "music21.abcFormat.ABCHandler"):

|  |  |  |
| --- | --- | --- |
| * [`barlineTokenFilter()`](#music21.abcFormat.ABCHandler.barlineTokenFilter "music21.abcFormat.ABCHandler.barlineTokenFilter") * [`definesMeasures()`](#music21.abcFormat.ABCHandler.definesMeasures "music21.abcFormat.ABCHandler.definesMeasures") * [`definesReferenceNumbers()`](#music21.abcFormat.ABCHandler.definesReferenceNumbers "music21.abcFormat.ABCHandler.definesReferenceNumbers") * [`getReferenceNumber()`](#music21.abcFormat.ABCHandler.getReferenceNumber "music21.abcFormat.ABCHandler.getReferenceNumber") * [`getTitle()`](#music21.abcFormat.ABCHandler.getTitle "music21.abcFormat.ABCHandler.getTitle") * [`hasNotes()`](#music21.abcFormat.ABCHandler.hasNotes "music21.abcFormat.ABCHandler.hasNotes") | * [`parseHeaderForVersionInformation()`](#music21.abcFormat.ABCHandler.parseHeaderForVersionInformation "music21.abcFormat.ABCHandler.parseHeaderForVersionInformation") * [`process()`](#music21.abcFormat.ABCHandler.process "music21.abcFormat.ABCHandler.process") * [`processComment()`](#music21.abcFormat.ABCHandler.processComment "music21.abcFormat.ABCHandler.processComment") * [`returnAbcVersionFromMatch()`](#music21.abcFormat.ABCHandler.returnAbcVersionFromMatch "music21.abcFormat.ABCHandler.returnAbcVersionFromMatch") * [`splitByMeasure()`](#music21.abcFormat.ABCHandler.splitByMeasure "music21.abcFormat.ABCHandler.splitByMeasure") * [`splitByReferenceNumber()`](#music21.abcFormat.ABCHandler.splitByReferenceNumber "music21.abcFormat.ABCHandler.splitByReferenceNumber") | * [`splitByVoice()`](#music21.abcFormat.ABCHandler.splitByVoice "music21.abcFormat.ABCHandler.splitByVoice") * [`startsMetadata()`](#music21.abcFormat.ABCHandler.startsMetadata "music21.abcFormat.ABCHandler.startsMetadata") * [`tokenProcess()`](#music21.abcFormat.ABCHandler.tokenProcess "music21.abcFormat.ABCHandler.tokenProcess") * [`tokenize()`](#music21.abcFormat.ABCHandler.tokenize "music21.abcFormat.ABCHandler.tokenize") * [`tokensToBarIndices()`](#music21.abcFormat.ABCHandler.tokensToBarIndices "music21.abcFormat.ABCHandler.tokensToBarIndices") |

## ABCAccent

class music21.abcFormat.ABCAccent(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCAccent)
:   ABCAccent tokens “K” precede a note or chord;
    they are a property of that note/chord.
    These appear as “>” in the output.

[`ABCAccent`](#music21.abcFormat.ABCAccent "music21.abcFormat.ABCAccent") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCAccent`](#music21.abcFormat.ABCAccent "music21.abcFormat.ABCAccent") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCAccent`](#music21.abcFormat.ABCAccent "music21.abcFormat.ABCAccent") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCBar

class music21.abcFormat.ABCBar(*src*)[[source]](../_modules/music21/abcFormat.html#ABCBar)
:   An ABCBar token represents a barline, possibly with repeat information.

    Currently 4.10 Variant

[`ABCBar`](#music21.abcFormat.ABCBar "music21.abcFormat.ABCBar") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCBar`](#music21.abcFormat.ABCBar "music21.abcFormat.ABCBar") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCBar`](#music21.abcFormat.ABCBar "music21.abcFormat.ABCBar") methods

ABCBar.getBarObject() → [bar.Barline](moduleBar.html#music21.bar.Barline "music21.bar.Barline") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCBar.getBarObject)
:   Return a music21 bar object

    ```python
    >>> ab = abcFormat.ABCBar('|:')
    >>> ab.parse()
    >>> barObject = ab.getBarObject()
    >>> barObject
     <music21.bar.Repeat direction=start>
    ```

ABCBar.isRegular() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCBar.isRegular)
:   Return True if this is a regular, single, light bar line.

    ```python
    >>> ab = abcFormat.ABCBar('|')
    >>> ab.parse()
    >>> ab.isRegular()
    True
    ```

ABCBar.isRepeat() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCBar.isRepeat)

ABCBar.isRepeatBracket() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False][[source]](../_modules/music21/abcFormat.html#ABCBar.isRepeatBracket)
:   Return a number if this defines a repeat bracket for an alternate ending
    otherwise returns False.

    ```python
    >>> ab = abcFormat.ABCBar('[2')
    >>> ab.parse()
    >>> ab.isRepeat()
    False
    >>> ab.isRepeatBracket()
    2
    ```

ABCBar.parse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCBar.parse)
:   Assign the bar-type based on the source string.

    ```python
    >>> ab = abcFormat.ABCBar('|')
    >>> ab.parse()
    >>> ab
    <music21.abcFormat.ABCBar '|'>
    ```

    ```python
    >>> ab.barType
    'barline'
    >>> ab.barStyle
    'regular'
    ```

    ```python
    >>> ab = abcFormat.ABCBar('||')
    >>> ab.parse()
    >>> ab.barType
    'barline'
    >>> ab.barStyle
    'light-light'
    ```

    ```python
    >>> ab = abcFormat.ABCBar('|:')
    >>> ab.parse()
    >>> ab.barType
    'repeat'
    >>> ab.barStyle
    'heavy-light'
    >>> ab.repeatForm
    'start'
    ```

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |  |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCBrokenRhythmMarker

class music21.abcFormat.ABCBrokenRhythmMarker(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCBrokenRhythmMarker)
:   Marks that rhythm is broken with ‘>>>’

[`ABCBrokenRhythmMarker`](#music21.abcFormat.ABCBrokenRhythmMarker "music21.abcFormat.ABCBrokenRhythmMarker") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCBrokenRhythmMarker`](#music21.abcFormat.ABCBrokenRhythmMarker "music21.abcFormat.ABCBrokenRhythmMarker") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCBrokenRhythmMarker`](#music21.abcFormat.ABCBrokenRhythmMarker "music21.abcFormat.ABCBrokenRhythmMarker") methods

ABCBrokenRhythmMarker.preParse()[[source]](../_modules/music21/abcFormat.html#ABCBrokenRhythmMarker.preParse)
:   Called before context adjustments: need to have access to data

    ```python
    >>> brokenRhythm = abcFormat.ABCBrokenRhythmMarker('>>>')
    >>> brokenRhythm.preParse()
    >>> brokenRhythm.data
    '>>>'
    ```

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |  |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCChord

class music21.abcFormat.ABCChord(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCChord)
:   A representation of an ABC Chord, which contains within its delimiters individual notes.

    A subclass of ABCNote.

[`ABCChord`](#music21.abcFormat.ABCChord "music21.abcFormat.ABCChord") bases

* [`ABCNote`](#music21.abcFormat.ABCNote "music21.abcFormat.ABCNote")
* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCChord`](#music21.abcFormat.ABCChord "music21.abcFormat.ABCChord") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCChord`](#music21.abcFormat.ABCChord "music21.abcFormat.ABCChord") methods

ABCChord.parse(*forceKeySignature=None*, *forceDefaultQuarterLength=None*)[[source]](../_modules/music21/abcFormat.html#ABCChord.parse)
:   Handles the following types of chords:

    * Chord without length modifier: [ceg]
    * Chords with outer length modifier: [ceg]2, [ceg]/2
    * Chords with inner length modifier: [c2e2g2], [c2eg]
    * Chords with inner and outer length modifier: [c2e2g2]/2, [c/2e/2g/2]2

Methods inherited from [`ABCNote`](#music21.abcFormat.ABCNote "music21.abcFormat.ABCNote"):

|  |  |  |
| --- | --- | --- |
| * [`getPitchName()`](#music21.abcFormat.ABCNote.getPitchName "music21.abcFormat.ABCNote.getPitchName") | * [`getQuarterLength()`](#music21.abcFormat.ABCNote.getQuarterLength "music21.abcFormat.ABCNote.getQuarterLength") |  |

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |  |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCCrescStart

class music21.abcFormat.ABCCrescStart(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCCrescStart)
:   ABCCrescStart tokens always precede the notes in a crescendo.
    These tokens coincide with the string “!crescendo(“;
    the closing string “!crescendo)” counts as an ABCParenStop.

[`ABCCrescStart`](#music21.abcFormat.ABCCrescStart "music21.abcFormat.ABCCrescStart") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCCrescStart`](#music21.abcFormat.ABCCrescStart "music21.abcFormat.ABCCrescStart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCCrescStart`](#music21.abcFormat.ABCCrescStart "music21.abcFormat.ABCCrescStart") methods

ABCCrescStart.fillCresc() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCCrescStart.fillCresc)

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCDimStart

class music21.abcFormat.ABCDimStart(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCDimStart)
:   ABCDimStart tokens always precede the notes in a diminuendo.
    They function identically to ABCCrescStart tokens.

[`ABCDimStart`](#music21.abcFormat.ABCDimStart "music21.abcFormat.ABCDimStart") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCDimStart`](#music21.abcFormat.ABCDimStart "music21.abcFormat.ABCDimStart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCDimStart`](#music21.abcFormat.ABCDimStart "music21.abcFormat.ABCDimStart") methods

ABCDimStart.fillDim()[[source]](../_modules/music21/abcFormat.html#ABCDimStart.fillDim)

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCDownbow

class music21.abcFormat.ABCDownbow(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCDownbow)
:   ABCDownbow tokens “v” precede a note or chord;
    they are a property of that note/chord.

[`ABCDownbow`](#music21.abcFormat.ABCDownbow "music21.abcFormat.ABCDownbow") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCDownbow`](#music21.abcFormat.ABCDownbow "music21.abcFormat.ABCDownbow") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCDownbow`](#music21.abcFormat.ABCDownbow "music21.abcFormat.ABCDownbow") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCGraceStart

class music21.abcFormat.ABCGraceStart(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCGraceStart)
:   Grace note start

[`ABCGraceStart`](#music21.abcFormat.ABCGraceStart "music21.abcFormat.ABCGraceStart") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCGraceStart`](#music21.abcFormat.ABCGraceStart "music21.abcFormat.ABCGraceStart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCGraceStart`](#music21.abcFormat.ABCGraceStart "music21.abcFormat.ABCGraceStart") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCGraceStop

class music21.abcFormat.ABCGraceStop(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCGraceStop)
:   Grace note end

[`ABCGraceStop`](#music21.abcFormat.ABCGraceStop "music21.abcFormat.ABCGraceStop") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCGraceStop`](#music21.abcFormat.ABCGraceStop "music21.abcFormat.ABCGraceStop") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCGraceStop`](#music21.abcFormat.ABCGraceStop "music21.abcFormat.ABCGraceStop") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCMetadata

class music21.abcFormat.ABCMetadata(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCMetadata)
:   Defines a token of metadata in ABC.

    ```python
    >>> md = abcFormat.ABCMetadata('I:linebreak')
    >>> md.src
    'I:linebreak'
    ```

    Has two attributes, tag and data which are strings.
    Initially both are set to ‘’:

    ```python
    >>> md.tag
    ''
    ```

    After calling preParse(), these are separated:

    ```python
    >>> md.preParse()
    >>> md.tag
    'I'
    >>> md.data
    'linebreak'
    ```

[`ABCMetadata`](#music21.abcFormat.ABCMetadata "music21.abcFormat.ABCMetadata") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCMetadata`](#music21.abcFormat.ABCMetadata "music21.abcFormat.ABCMetadata") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCMetadata`](#music21.abcFormat.ABCMetadata "music21.abcFormat.ABCMetadata") methods

ABCMetadata.getClefObject() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[clef.Clef](moduleClef.html#music21.clef.Clef "music21.clef.Clef") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/abcFormat.html#ABCMetadata.getClefObject)
:   Extract any clef parameters stored in the key metadata token.
    Assume that a clef definition suggests a transposition.
    Return both the Clef and the transposition.

    Returns a two-element tuple of clefObj and transposition in semitones

    ```python
    >>> am = abcFormat.ABCMetadata('K:Eb Lydian bass')
    >>> am.preParse()
    >>> am.getClefObject()
    (<music21.clef.BassClef>, -24)
    ```

ABCMetadata.getDefaultQuarterLength() → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.getDefaultQuarterLength)
:   If there is a quarter length representation available, return it as a floating point value

    ```python
    >>> am = abcFormat.ABCMetadata('L:1/2')
    >>> am.preParse()
    >>> am.getDefaultQuarterLength()
    2.0
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('L:1/8')
    >>> am.preParse()
    >>> am.getDefaultQuarterLength()
    0.5
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M:C|')
    >>> am.preParse()
    >>> am.getDefaultQuarterLength()
    0.5
    ```

    If taking from meter, find the “fraction” and if < 0.75 use sixteenth notes.
    If >= 0.75 use eighth notes.

    ```python
    >>> am = abcFormat.ABCMetadata('M:2/4')
    >>> am.preParse()
    >>> am.getDefaultQuarterLength()
    0.25
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M:3/4')
    >>> am.preParse()
    >>> am.getDefaultQuarterLength()
    0.5
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M:6/8')
    >>> am.preParse()
    >>> am.getDefaultQuarterLength()
    0.5
    ```

    Meter is only used for default length if there is no L:

    ```python
    >>> x = 'L:1/4\nM:3/4\n\nf'
    >>> sc = converter.parse(x, format='abc')
    >>> sc.recurse().notes.first().duration.type
    'quarter'
    ```

ABCMetadata.getKeySignatureObject() → t.Union[[key.Key](moduleKey.html#music21.key.Key "music21.key.Key"), [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/abcFormat.html#ABCMetadata.getKeySignatureObject)
:   Return a music21 [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") or [`Key`](moduleKey.html#music21.key.Key "music21.key.Key")
    object for this metadata tag.

    ```python
    >>> am = abcFormat.ABCMetadata('K:G')
    >>> am.preParse()
    >>> ks = am.getKeySignatureObject()
    >>> ks
    <music21.key.Key of G major>
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:Gmin')
    >>> am.preParse()
    >>> ks = am.getKeySignatureObject()
    >>> ks
    <music21.key.Key of g minor>
    >>> ks.sharps
    -2
    ```

    Note that capitalization does not matter
    (<http://abcnotation.com/wiki/abc:standard:v2.1#kkey>)
    so this should still be minor.

    ```python
    >>> am = abcFormat.ABCMetadata('K:GM')
    >>> am.preParse()
    >>> ks = am.getKeySignatureObject()
    >>> ks
    <music21.key.Key of g minor>
    ```

ABCMetadata.getKeySignatureParameters() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/abcFormat.html#ABCMetadata.getKeySignatureParameters)
:   Extract key signature parameters,
    returning the number of sharps and the mode.

    ```python
    >>> am = abcFormat.ABCMetadata('K:Eb Lydian')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (-2, 'lydian')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:APhry')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (-1, 'phrygian')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:G Mixolydian')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (0, 'mixolydian')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K: Edor')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (2, 'dorian')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K: F')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (-1, 'major')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:G')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (1, 'major')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:Gm')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (-2, 'minor')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:Hp')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (2, None)
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:G ionian')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (1, 'ionian')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('K:G aeol')
    >>> am.preParse()
    >>> am.getKeySignatureParameters()
    (-2, 'aeolian')
    ```

ABCMetadata.getMetronomeMarkObject() → [tempo.MetronomeMark](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.getMetronomeMarkObject)
:   Extract any tempo parameters stored in a tempo metadata token.

    ```python
    >>> am = abcFormat.ABCMetadata('Q: "Allegro" 1/4=120')
    >>> am.preParse()
    >>> am.getMetronomeMarkObject()
    <music21.tempo.MetronomeMark Allegro Quarter=120>
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('Q: 3/8=50 "Slowly"')
    >>> am.preParse()
    >>> am.getMetronomeMarkObject()
    <music21.tempo.MetronomeMark Slowly Dotted Quarter=50>
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('Q:1/2=120')
    >>> am.preParse()
    >>> am.getMetronomeMarkObject()
    <music21.tempo.MetronomeMark animato Half=120>
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('Q:1/4 3/8 1/4 3/8=40')
    >>> am.preParse()
    >>> am.getMetronomeMarkObject()
    <music21.tempo.MetronomeMark grave Whole tied to Quarter (5 total QL)=40>
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('Q:90')
    >>> am.preParse()
    >>> am.getMetronomeMarkObject()
    <music21.tempo.MetronomeMark maestoso Quarter=90>
    ```

ABCMetadata.getTimeSignatureObject() → meter.TimeSignature | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.getTimeSignatureObject)
:   Return a music21 `TimeSignature`
    object for this metadata tag, if isMeter is True, otherwise raise exception.

    ```python
    >>> am = abcFormat.ABCMetadata('M:2/2')
    >>> am.preParse()
    >>> ts = am.getTimeSignatureObject()
    >>> ts
    <music21.meter.TimeSignature 2/2>
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('Q:40')
    >>> am.getTimeSignatureObject()
    Traceback (most recent call last):
    music21.abcFormat.ABCTokenException: no time signature associated with
        this non-metrical metadata.
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M:none')
    >>> am.preParse()
    >>> ts = am.getTimeSignatureObject()
    >>> ts is None
    True
    ```

ABCMetadata.getTimeSignatureParameters() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.getTimeSignatureParameters)
:   If there is a time signature representation available,
    get a numerator, denominator and an abbreviation symbol.
    To get a music21 `TimeSignature` object, use
    the [`getTimeSignatureObject()`](#music21.abcFormat.ABCMetadata.getTimeSignatureObject "music21.abcFormat.ABCMetadata.getTimeSignatureObject") method.

    ```python
    >>> am = abcFormat.ABCMetadata('M:2/2')
    >>> am.preParse()
    >>> am.isMeter()
    True
    >>> am.getTimeSignatureParameters()
    (2, 2, 'normal')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M:C|')
    >>> am.preParse()
    >>> am.getTimeSignatureParameters()
    (2, 2, 'cut')
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M: none')
    >>> am.preParse()
    >>> am.getTimeSignatureParameters() is None
    True
    ```

    ```python
    >>> am = abcFormat.ABCMetadata('M: FREI4/4')
    >>> am.preParse()
    >>> am.getTimeSignatureParameters()
    (4, 4, 'normal')
    ```

ABCMetadata.isComposer() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isComposer)
:   Returns True if the tag is “C” for composer, False otherwise.

ABCMetadata.isDefaultNoteLength() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isDefaultNoteLength)
:   Returns True if the tag is “L”, False otherwise.

ABCMetadata.isKey() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isKey)
:   Returns True if the tag is “K”, False otherwise.
    Note that in some cases a Key will encode clef information.

    (example from corpus: josquin/laDeplorationDeLaMorteDeJohannesOckeghem.abc)

ABCMetadata.isMeter() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isMeter)
:   Returns True if the tag is “M” for meter, False otherwise.

ABCMetadata.isOrigin() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isOrigin)
:   Returns True if the tag is “O” for origin, False otherwise.
    This value is set in the Metadata localOfComposition of field.

ABCMetadata.isReferenceNumber() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isReferenceNumber)
:   Returns True if the tag is “X”, False otherwise.

    ```python
    >>> x = abcFormat.ABCMetadata('X:5')
    >>> x.preParse()
    >>> x.tag
    'X'
    >>> x.isReferenceNumber()
    True
    ```

ABCMetadata.isTempo() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isTempo)
:   Returns True if the tag is “Q” for tempo, False otherwise.

ABCMetadata.isTitle() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isTitle)
:   Returns True if the tag is “T” for title, False otherwise.

ABCMetadata.isVersion() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isVersion)
:   Returns True if the tag is “I” for “Information” and
    the data is “abc-version”, False otherwise.

    ```python
    >>> x = abcFormat.ABCMetadata('I:abc-version 2.1')
    >>> x.preParse()
    >>> x.tag
    'I'
    >>> x.isVersion()
    True
    ```

    ```python
    >>> deer = abcFormat.ABCMetadata('I:abc-venison yummy')
    >>> deer.preParse()
    >>> deer.tag
    'I'
    >>> deer.isVersion()
    False
    ```

ABCMetadata.isVoice() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.isVoice)
:   Returns True if the tag is “V”, False otherwise.

ABCMetadata.parse()[[source]](../_modules/music21/abcFormat.html#ABCMetadata.parse)
:   Dummy method that reads self.src and loads attributes.
    It is called after contextual adjustments.

    It is designed to be subclassed or overridden.

ABCMetadata.preParse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCMetadata.preParse)
:   Called before contextual adjustments and needs
    to have access to data. Divides a token into
    .tag (a single capital letter or w) and .data representations.

    ```python
    >>> x = abcFormat.ABCMetadata('T:tagData')
    >>> x.preParse()
    >>> x.tag
    'T'
    >>> x.data
    'tagData'
    ```

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |  |  |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCNote

class music21.abcFormat.ABCNote(*src=''*, *carriedAccidental: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCNote)
:   A model of an ABCNote.

    General usage requires multi-pass processing. After being tokenized,
    each ABCNote needs a number of attributes updates. Attributes to
    be updated after tokenizing, and based on the linear sequence of
    tokens: inBar, inBeam (not used), inGrace,
    activeDefaultQuarterLength, brokenRhythmMarker, and
    activeKeySignature.

    The chordSymbols list stores one or more chord symbols (ABC calls
    these guitar chords) associated with this note. This attribute is
    updated when parse() is called.

[`ABCNote`](#music21.abcFormat.ABCNote "music21.abcFormat.ABCNote") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCNote`](#music21.abcFormat.ABCNote "music21.abcFormat.ABCNote") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCNote`](#music21.abcFormat.ABCNote "music21.abcFormat.ABCNote") methods

ABCNote.getPitchName(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *forceKeySignature=None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/abcFormat.html#ABCNote.getPitchName)
:   Given a note or rest string without a chord symbol,
    return a music21 pitch string or None (if a rest),
    and the accidental display status. This value is paired
    with an accidental display status. Pitch alterations, and
    accidental display status, are adjusted if a key is
    declared in the Note.

    ```python
    >>> an = abcFormat.ABCNote()
    >>> an.getPitchName('e2')
    ('E5', None)
    >>> an.getPitchName('C')
    ('C4', None)
    >>> an.getPitchName('B,,')
    ('B2', None)
    >>> an.getPitchName('C,')
    ('C3', None)
    >>> an.getPitchName('c')
    ('C5', None)
    >>> an.getPitchName("c'")
    ('C6', None)
    >>> an.getPitchName("c''")
    ('C7', None)
    >>> an.getPitchName("^g")
    ('G#5', True)
    >>> an.getPitchName("_g''")
    ('G-7', True)
    >>> an.getPitchName('=c')
    ('Cn5', True)
    ```

    If pitch is a rest (z) then the Pitch name is None:

    ```python
    >>> an.getPitchName('z4')
    (None, None)
    ```

    Grace note:

    ```python
    >>> an.getPitchName('{c}')
    ('C5', None)
    ```

    Given an active KeySignature object, the pitch name might
    change:

    ```python
    >>> an.activeKeySignature = key.KeySignature(3)
    >>> an.getPitchName('c')
    ('C#5', False)
    ```

    Illegal pitch names raise an ABCHandlerException

    ```python
    >>> an.getPitchName('x')
    Traceback (most recent call last):
    music21.abcFormat.ABCHandlerException: cannot find any pitch information in: 'x'
    ```

ABCNote.getQuarterLength(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *forceDefaultQuarterLength: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCNote.getQuarterLength)
:   Called with parse(), after context processing, to calculate duration

    ```python
    >>> an = abcFormat.ABCNote()
    >>> an.activeDefaultQuarterLength = 0.5
    >>> an.getQuarterLength('e2')
    1.0
    >>> an.getQuarterLength('G')
    0.5
    >>> an.getQuarterLength('=c/2')
    0.25
    >>> an.getQuarterLength('A3/2')
    0.75
    >>> an.getQuarterLength('A/')
    0.25
    ```

    ```python
    >>> an.getQuarterLength('A//')
    0.125
    >>> an.getQuarterLength('A///')
    0.0625
    ```

    ```python
    >>> an = abcFormat.ABCNote()
    >>> an.activeDefaultQuarterLength = 0.5
    >>> an.brokenRhythmMarker = ('>', 'left')
    >>> an.getQuarterLength('A')
    0.75
    >>> an.brokenRhythmMarker = ('>', 'right')
    >>> an.getQuarterLength('A')
    0.25
    ```

    ```python
    >>> an.brokenRhythmMarker = ('<<', 'left')
    >>> an.getQuarterLength('A')
    0.125
    >>> an.brokenRhythmMarker = ('<<', 'right')
    >>> an.getQuarterLength('A')
    0.875
    ```

    ```python
    >>> an.brokenRhythmMarker = ('<<<', 'left')
    >>> an.getQuarterLength('A')
    0.0625
    >>> an.brokenRhythmMarker = ('<<<', 'right')
    >>> an.getQuarterLength('A')
    0.9375
    ```

    ```python
    >>> an.getQuarterLength('A', forceDefaultQuarterLength=1.0)
    1.875
    ```

ABCNote.parse(*forceDefaultQuarterLength: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *forceKeySignature: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCNote.parse)
:   Dummy method that reads self.src and loads attributes.
    It is called after contextual adjustments.

    It is designed to be subclassed or overridden.

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |  |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCParenStop

class music21.abcFormat.ABCParenStop(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCParenStop)
:   A general parenthesis stop;
    comes at the end of a tuplet, slur, or dynamic marking.

[`ABCParenStop`](#music21.abcFormat.ABCParenStop "music21.abcFormat.ABCParenStop") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCParenStop`](#music21.abcFormat.ABCParenStop "music21.abcFormat.ABCParenStop") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCParenStop`](#music21.abcFormat.ABCParenStop "music21.abcFormat.ABCParenStop") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCSlurStart

class music21.abcFormat.ABCSlurStart(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCSlurStart)
:   ABCSlurStart tokens always precede the notes in a slur.
    For nested slurs, each open parenthesis gets its own token.

[`ABCSlurStart`](#music21.abcFormat.ABCSlurStart "music21.abcFormat.ABCSlurStart") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCSlurStart`](#music21.abcFormat.ABCSlurStart "music21.abcFormat.ABCSlurStart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCSlurStart`](#music21.abcFormat.ABCSlurStart "music21.abcFormat.ABCSlurStart") methods

ABCSlurStart.fillSlur()[[source]](../_modules/music21/abcFormat.html#ABCSlurStart.fillSlur)
:   Creates a spanner object for each open paren associated with a slur;
    these slurs are filled with notes until end parens are read.

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCStaccato

class music21.abcFormat.ABCStaccato(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCStaccato)
:   ABCStaccato tokens “.” precede a note or chord;
    they are a property of that note/chord.

[`ABCStaccato`](#music21.abcFormat.ABCStaccato "music21.abcFormat.ABCStaccato") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCStaccato`](#music21.abcFormat.ABCStaccato "music21.abcFormat.ABCStaccato") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCStaccato`](#music21.abcFormat.ABCStaccato "music21.abcFormat.ABCStaccato") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCStraccent

class music21.abcFormat.ABCStraccent(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCStraccent)
:   ABCStraccent tokens “k” precede a note or chord;
    they are a property of that note/chord.
    These appear as “^” in the output.

[`ABCStraccent`](#music21.abcFormat.ABCStraccent "music21.abcFormat.ABCStraccent") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCStraccent`](#music21.abcFormat.ABCStraccent "music21.abcFormat.ABCStraccent") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCStraccent`](#music21.abcFormat.ABCStraccent "music21.abcFormat.ABCStraccent") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCTenuto

class music21.abcFormat.ABCTenuto(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCTenuto)
:   ABCTenuto tokens “M” precede a note or chord;
    they are a property of that note/chord.

[`ABCTenuto`](#music21.abcFormat.ABCTenuto "music21.abcFormat.ABCTenuto") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCTenuto`](#music21.abcFormat.ABCTenuto "music21.abcFormat.ABCTenuto") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCTenuto`](#music21.abcFormat.ABCTenuto "music21.abcFormat.ABCTenuto") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCTie

class music21.abcFormat.ABCTie(*src=''*)[[source]](../_modules/music21/abcFormat.html#ABCTie)
:   Handles instances of ties ‘-’ between notes in an ABC score.
    Ties are treated as an attribute of the note before the ‘-‘;
    the note after is marked as the end of the tie.

[`ABCTie`](#music21.abcFormat.ABCTie "music21.abcFormat.ABCTie") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCTie`](#music21.abcFormat.ABCTie "music21.abcFormat.ABCTie") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCTie`](#music21.abcFormat.ABCTie "music21.abcFormat.ABCTie") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCToken

class music21.abcFormat.ABCToken(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCToken)
:   ABC processing works with a multi-pass procedure. The first pass
    breaks the data stream into a list of ABCToken objects. ABCToken
    objects are specialized in subclasses.

    The multi-pass procedure is conducted by an ABCHandler object.
    The ABCHandler.tokenize() method breaks the data stream into
    ABCToken objects. The [`tokenProcess()`](#music21.abcFormat.ABCHandler.tokenProcess "music21.abcFormat.ABCHandler.tokenProcess") method first
    calls the [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") method on each token,
    then does contextual
    adjustments to all tokens, then calls [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") on all tokens.

    The source ABC string itself is stored in self.src.

    Because of how copying ABCTokens works, all tokens must have default parameters in their
    initializers

[`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken") methods

ABCToken.parse()[[source]](../_modules/music21/abcFormat.html#ABCToken.parse)
:   Dummy method that reads self.src and loads attributes.
    It is called after contextual adjustments.

    It is designed to be subclassed or overridden.

ABCToken.preParse()[[source]](../_modules/music21/abcFormat.html#ABCToken.preParse)
:   Dummy method that is called before contextual adjustments.
    Designed to be subclassed or overridden.

static ABCToken.stripComment(*strSrc: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCToken.stripComment)
:   removes ABC-style comments from a string:

    ```python
    >>> ao = abcFormat.ABCToken()
    >>> ao.stripComment('asdf')
    'asdf'
    >>> ao.stripComment('asdf%234')
    'asdf'
    >>> ao.stripComment('asdf  %     234')
    'asdf  '
    >>> ao.stripComment('[ceg]% this chord appears 50% more often than other chords do')
    '[ceg]'
    ```

    This is a static method, so it can also be called on the class itself:

    ```python
    >>> abcFormat.ABCToken.stripComment('b1 % a b-flat actually')
    'b1 '
    ```

    * Changed in v6.2: made a staticmethod

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCTuplet

class music21.abcFormat.ABCTuplet(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCTuplet)
:   ABCTuplet tokens always precede the notes they describe.

    In ABCHandler.tokenProcess(), rhythms are adjusted.

[`ABCTuplet`](#music21.abcFormat.ABCTuplet "music21.abcFormat.ABCTuplet") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCTuplet`](#music21.abcFormat.ABCTuplet "music21.abcFormat.ABCTuplet") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCTuplet`](#music21.abcFormat.ABCTuplet "music21.abcFormat.ABCTuplet") methods

ABCTuplet.updateNoteCount() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCTuplet.updateNoteCount)
:   Update the note count of notes that are
    affected by this tuplet. Can be set by p:q:r style tuplets.
    Also creates a tuplet object.

    ```python
    >>> at = abcFormat.ABCTuplet('(6')
    >>> at.updateRatio()
    >>> at.updateNoteCount()
    >>> at.noteCount
    6
    >>> at.tupletObj
    <music21.duration.Tuplet 6/2>
    ```

    ```python
    >>> at = abcFormat.ABCTuplet('(6:4:12')
    >>> at.updateRatio()
    >>> at.updateNoteCount()
    >>> at.noteCount
    12
    >>> at.tupletObj
    <music21.duration.Tuplet 6/4>
    ```

    ```python
    >>> at = abcFormat.ABCTuplet('(6::18')
    >>> at.updateRatio()
    >>> at.updateNoteCount()
    >>> at.noteCount
    18
    ```

ABCTuplet.updateRatio(*timeSignatureObj: meter.TimeSignature | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/abcFormat.html#ABCTuplet.updateRatio)
:   Cannot be called until local meter context
    is established.

    ```python
    >>> at = abcFormat.ABCTuplet('(3')
    >>> at.updateRatio()
    >>> at.numberNotesActual, at.numberNotesNormal
    (3, 2)
    ```

    Generally a 5:n tuplet is 5 in the place of 2.

    ```python
    >>> at = abcFormat.ABCTuplet('(5')
    >>> at.updateRatio()
    >>> at.numberNotesActual, at.numberNotesNormal
    (5, 2)
    ```

    Unless it’s in a meter.TimeSignature compound (triple) context:

    ```python
    >>> at = abcFormat.ABCTuplet('(5')
    >>> at.updateRatio(meter.TimeSignature('6/8'))
    >>> at.numberNotesActual, at.numberNotesNormal
    (5, 3)
    ```

    Six is 6:2, not 6:4!

    ```python
    >>> at = abcFormat.ABCTuplet('(6')
    >>> at.updateRatio()
    >>> at.numberNotesActual, at.numberNotesNormal
    (6, 2)
    ```

    ```python
    >>> at = abcFormat.ABCTuplet('(6:4')
    >>> at.updateRatio()
    >>> at.numberNotesActual, at.numberNotesNormal
    (6, 4)
    ```

    ```python
    >>> at = abcFormat.ABCTuplet('(6::6')
    >>> at.updateRatio()
    >>> at.numberNotesActual, at.numberNotesNormal
    (6, 2)
    ```

    2 is 2 in 3…

    ```python
    >>> at = abcFormat.ABCTuplet('(2')
    >>> at.updateRatio()
    >>> at.numberNotesActual, at.numberNotesNormal
    (2, 3)
    ```

    Some other types:

    ```python
    >>> for n in 1, 2, 3, 4, 5, 6, 7, 8, 9:
    ...     at = abcFormat.ABCTuplet(f'({n}')
    ...     at.updateRatio()
    ...     print(at.numberNotesActual, at.numberNotesNormal)
    1 1
    2 3
    3 2
    4 3
    5 2
    6 2
    7 2
    8 3
    9 2
    ```

    Tuplets > 9 raise an exception:

    ```python
    >>> at = abcFormat.ABCTuplet('(10')
    >>> at.updateRatio()
    Traceback (most recent call last):
    music21.abcFormat.ABCTokenException: cannot handle tuplet of form: '(10'
    ```

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## ABCUpbow

class music21.abcFormat.ABCUpbow(*src: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/abcFormat.html#ABCUpbow)
:   ABCUpbow tokens “u” precede a note or chord;
    they are a property of that note/chord.

[`ABCUpbow`](#music21.abcFormat.ABCUpbow "music21.abcFormat.ABCUpbow") bases

* [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`ABCUpbow`](#music21.abcFormat.ABCUpbow "music21.abcFormat.ABCUpbow") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ABCUpbow`](#music21.abcFormat.ABCUpbow "music21.abcFormat.ABCUpbow") methods

Methods inherited from [`ABCToken`](#music21.abcFormat.ABCToken "music21.abcFormat.ABCToken"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.abcFormat.ABCToken.parse "music21.abcFormat.ABCToken.parse") | * [`preParse()`](#music21.abcFormat.ABCToken.preParse "music21.abcFormat.ABCToken.preParse") | * [`stripComment()`](#music21.abcFormat.ABCToken.stripComment "music21.abcFormat.ABCToken.stripComment") |

Methods inherited from [`EqualSlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleCommonObjects.html#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## Functions

music21.abcFormat.mergeLeadingMetaData(*barHandlers: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ABCHandlerBar](#music21.abcFormat.ABCHandlerBar "music21.abcFormat.ABCHandlerBar")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ABCHandlerBar](#music21.abcFormat.ABCHandlerBar "music21.abcFormat.ABCHandlerBar")][[source]](../_modules/music21/abcFormat.html#mergeLeadingMetaData)
:   Given a list of ABCHandlerBar objects, return a list of ABCHandlerBar
    objects where leading metadata is merged, if possible,
    with the bar data following.

    This consolidates all metadata in bar-like entities.
