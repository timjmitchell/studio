Source: https://music21.org/music21docs/moduleReference/moduleRomanTextTsvConverter.html

# music21.romanText.tsvConverter

Converter for parsing the tabular representations of harmonic analysis such as the
DCMLab’s Annotated Beethoven Corpus (Neuwirth et al. 2018).

## M21toTSV

class music21.romanText.tsvConverter.M21toTSV(*m21Stream: [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")*, *dcml\_version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 2*)[[source]](../_modules/music21/romanText/tsvConverter.html#M21toTSV)
:   Conversion starting with a music21 stream.
    Exports to tabular data format and (optionally) writes the file.

    ```python
    >>> bachHarmony = corpus.parse('bach/choraleAnalyses/riemenschneider001.rntxt')
    >>> bachHarmony.parts[0].measure(1)[0].figure
    'I'
    ```

    The initialization includes the preparation of a list of lists, so

    ```python
    >>> initial = romanText.tsvConverter.M21toTSV(bachHarmony, dcml_version=2)
    >>> tsvData = initial.tsvData
    >>> from music21.romanText.tsvConverter import DCML_V2_HEADERS
    >>> tsvData[1][DCML_V2_HEADERS.index('chord')]
    'I'
    ```

[`M21toTSV`](#music21.romanText.tsvConverter.M21toTSV "music21.romanText.tsvConverter.M21toTSV") methods

M21toTSV.m21ToTsv() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[source]](../_modules/music21/romanText/tsvConverter.html#M21toTSV.m21ToTsv)
:   Converts a list of music21 chords to a list of lists
    which can then be written to a tsv file with toTsv(), or processed another way.

M21toTSV.write(*filePathAndName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*)[[source]](../_modules/music21/romanText/tsvConverter.html#M21toTSV.write)
:   Writes a list of lists (e.g. from m21ToTsv()) to a tsv file.

## TabChord

class music21.romanText.tsvConverter.TabChord[[source]](../_modules/music21/romanText/tsvConverter.html#TabChord)
:   An intermediate representation format for moving between tabular data in
    DCML v1 and music21 chords.

[`TabChord`](#music21.romanText.tsvConverter.TabChord "music21.romanText.tsvConverter.TabChord") bases

* [`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase")

[`TabChord`](#music21.romanText.tsvConverter.TabChord "music21.romanText.tsvConverter.TabChord") read/write properties

Read/write properties inherited from [`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`combinedChord`](#music21.romanText.tsvConverter.TabChordBase.combinedChord "music21.romanText.tsvConverter.TabChordBase.combinedChord") |  |  |

[`TabChord`](#music21.romanText.tsvConverter.TabChord "music21.romanText.tsvConverter.TabChord") methods

Methods inherited from [`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`populateFromRow()`](#music21.romanText.tsvConverter.TabChordBase.populateFromRow "music21.romanText.tsvConverter.TabChordBase.populateFromRow") | * [`tabToM21()`](#music21.romanText.tsvConverter.TabChordBase.tabToM21 "music21.romanText.tsvConverter.TabChordBase.tabToM21") |  |

## TabChordBase

class music21.romanText.tsvConverter.TabChordBase[[source]](../_modules/music21/romanText/tsvConverter.html#TabChordBase)
:   Abstract base class for intermediate representation format for moving
    between tabular data and music21 chords.

[`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase") read/write properties

TabChordBase.combinedChord
:   For easier interoperability with the DCML standards, we now use the
    column name ‘chord’ from the DCML file. But to preserve backwards-
    compatibility, we add this property, which is an alias for ‘chord’.

    ```python
    >>> tabCd = romanText.tsvConverter.TabChord()
    >>> tabCd.chord = 'viio7'
    >>> tabCd.combinedChord
    'viio7'
    >>> tabCd.combinedChord = 'IV+'
    >>> tabCd.chord
    'IV+'
    ```

[`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase") methods

TabChordBase.populateFromRow(*row: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *headIndices: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")]]*, *extraIndices: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#TabChordBase.populateFromRow)

TabChordBase.tabToM21() → [Harmony](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony")[[source]](../_modules/music21/romanText/tsvConverter.html#TabChordBase.tabToM21)
:   Creates and returns a music21.roman.RomanNumeral() object
    from a TabChord with all shared attributes.
    NB: call changeRepresentation() first if .representationType is not ‘m21’
    but you plan to process it with m21 (e.g. moving it into a stream).

    ```python
    >>> tabCd = romanText.tsvConverter.TabChord()
    >>> tabCd.numeral = 'vii'
    >>> tabCd.global_key = 'F'
    >>> tabCd.local_key = 'V'
    >>> tabCd.representationType = 'm21'
    >>> m21Ch = tabCd.tabToM21()
    ```

    Now we can check it’s a music21 RomanNumeral():

    ```python
    >>> m21Ch.figure
    'vii'
    ```

## TabChordV2

class music21.romanText.tsvConverter.TabChordV2[[source]](../_modules/music21/romanText/tsvConverter.html#TabChordV2)
:   An intermediate representation format for moving between tabular data in
    DCML v2 and music21 chords.

[`TabChordV2`](#music21.romanText.tsvConverter.TabChordV2 "music21.romanText.tsvConverter.TabChordV2") bases

* [`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase")

[`TabChordV2`](#music21.romanText.tsvConverter.TabChordV2 "music21.romanText.tsvConverter.TabChordV2") read/write properties

TabChordV2.beat: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
:   ‘beat’ has been removed from DCML v2 in favor of ‘mn\_onset’ and
    ‘mc\_onset’. ‘mn\_onset’ is equivalent to ‘beat’, except that ‘mn\_onset’
    is zero-indexed where ‘beat’ was 1-indexed, and ‘mn\_onset’ is in
    fractions of a whole-note rather than in quarter notes.

    ```python
    >>> tabCd = romanText.tsvConverter.TabChordV2()
    >>> tabCd.mn_onset = 0.0
    >>> tabCd.beat
    1.0
    ```

    ```python
    >>> tabCd.mn_onset = 0.5
    >>> tabCd.beat
    3.0
    ```

    ```python
    >>> tabCd.beat = 1.5
    >>> tabCd.beat
    1.5
    ```

TabChordV2.global\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
:   ‘global\_key’ has been renamed ‘globalkey’ in DCML v2. This property is
    provided as an alias for ‘globalkey’ so that TabChord and TabChordV2 can
    be used in the same way.

TabChordV2.local\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
:   ‘local\_key’ has been renamed ‘localkey’ in DCML v2. This property is
    provided as an alias for ‘localkey’ so that TabChord and TabChordV2 can
    be used in the same way.

TabChordV2.measure: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
:   ‘measure’ has been removed from DCML v2 in favor of ‘mn’ and ‘mc’. ‘mn’
    is equivalent to ‘measure’, so this property is provided as an alias.

Read/write properties inherited from [`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`combinedChord`](#music21.romanText.tsvConverter.TabChordBase.combinedChord "music21.romanText.tsvConverter.TabChordBase.combinedChord") |  |  |

[`TabChordV2`](#music21.romanText.tsvConverter.TabChordV2 "music21.romanText.tsvConverter.TabChordV2") methods

Methods inherited from [`TabChordBase`](#music21.romanText.tsvConverter.TabChordBase "music21.romanText.tsvConverter.TabChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`populateFromRow()`](#music21.romanText.tsvConverter.TabChordBase.populateFromRow "music21.romanText.tsvConverter.TabChordBase.populateFromRow") | * [`tabToM21()`](#music21.romanText.tsvConverter.TabChordBase.tabToM21 "music21.romanText.tsvConverter.TabChordBase.tabToM21") |  |

## TsvHandler

class music21.romanText.tsvConverter.TsvHandler(*tsvFile: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *dcml\_version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*)[[source]](../_modules/music21/romanText/tsvConverter.html#TsvHandler)
:   Conversion starting with a TSV file.

    First we need to get a score. (Don’t worry about this bit.)

    ```python
    >>> name = 'tsvEg_v1.tsv'
    >>> path = common.getSourceFilePath() / 'romanText' / name
    >>> handler = romanText.tsvConverter.TsvHandler(path)
    >>> handler.tsvToChords()
    ```

    These should be TabChords now.

    ```python
    >>> testTabChord1 = handler.chordList[0]
    >>> testTabChord1.combinedChord
    '.C.I6'
    ```

    Good. We can make them into music21 Roman-numerals.

    ```python
    >>> m21Chord1 = testTabChord1.tabToM21()
    >>> m21Chord1.figure
    'I'
    ```

    And for our last trick, we can put the whole collection in a music21 stream.

    ```python
    >>> out_stream = handler.toM21Stream()
    >>> out_stream.parts[0].measure(1)[roman.RomanNumeral][0].figure
    'I'
    ```

[`TsvHandler`](#music21.romanText.tsvConverter.TsvHandler "music21.romanText.tsvConverter.TsvHandler") methods

TsvHandler.prepStream() → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")[[source]](../_modules/music21/romanText/tsvConverter.html#TsvHandler.prepStream)
:   Prepares a music21 stream for the harmonic analysis to go into.
    Specifically: creates the score, part, and measure streams,
    as well as some (the available) metadata based on the original TSV data.
    Works like the .template() method,
    except that we don’t have a score to base the template on as such.

TsvHandler.toM21Stream() → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")[[source]](../_modules/music21/romanText/tsvConverter.html#TsvHandler.toM21Stream)
:   Takes a list of TabChords (self.chordList, prepared by .tsvToChords()),
    converts those TabChords in RomanNumerals
    (converting to the music21 representation format as necessary),
    creates a suitable music21 stream (by running .prepStream() using data from the TabChords),
    and populates that stream with the new RomanNumerals.

TsvHandler.tsvToChords() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#TsvHandler.tsvToChords)
:   Converts a list of lists (of the type imported by importTsv)
    into TabChords (i.e. a list of TabChords).

## Functions

music21.romanText.tsvConverter.characterSwaps(*preString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *minor: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *direction: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'm21-DCML'*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#characterSwaps)
:   Character swap function to coordinate between the two notational versions, for instance
    swapping between ‘%’ and ‘/o’ for the notation of half diminished (for example).

    ```python
    >>> testStr = 'ii%'
    >>> romanText.tsvConverter.characterSwaps(testStr, minor=False, direction='DCML-m21')
    'iiø'
    ```

music21.romanText.tsvConverter.getForm(*rn: [RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#getForm)
:   Takes a music21.roman.RomanNumeral object and returns the string indicating
    ‘form’ expected by the DCML standard.

    ```python
    >>> romanText.tsvConverter.getForm(roman.RomanNumeral('V'))
    ''
    >>> romanText.tsvConverter.getForm(roman.RomanNumeral('viio7'))
    'o'
    >>> romanText.tsvConverter.getForm(roman.RomanNumeral('IVM7'))
    'M'
    >>> romanText.tsvConverter.getForm(roman.RomanNumeral('III+'))
    '+'
    >>> romanText.tsvConverter.getForm(roman.RomanNumeral('IV+M7'))
    '+M'
    >>> romanText.tsvConverter.getForm(roman.RomanNumeral('viiø7'))
    '%'
    ```

music21.romanText.tsvConverter.getLocalKey(*local\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *global\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *convertDCMLToM21: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#getLocalKey)
:   Re-casts comparative local key (e.g. ‘V of G major’) in its own terms (‘D’).

    ```python
    >>> romanText.tsvConverter.getLocalKey('V', 'G')
    'D'
    ```

    ```python
    >>> romanText.tsvConverter.getLocalKey('ii', 'C')
    'd'
    ```

    ```python
    >>> romanText.tsvConverter.getLocalKey('i', 'C')
    'c'
    ```

    By default, assumes an m21 input, and operates as such:

    ```python
    >>> romanText.tsvConverter.getLocalKey('#vii', 'a')
    'g#'
    ```

    Set convert=True to convert from DCML to m21 formats. Hence;

    ```python
    >>> romanText.tsvConverter.getLocalKey('vii', 'a', convertDCMLToM21=True)
    'g'
    ```

music21.romanText.tsvConverter.getSecondaryKey(*rn: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *local\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#getSecondaryKey)
:   Separates comparative Roman-numeral for tonicizations like ‘V/vi’ into the component parts of
    a Roman-numeral (V) and
    a (very) local key (vi)
    and expresses that very local key in relation to the local key also called (DCML column 11).

    While .getLocalKey() work on the figure and key pair:

    ```python
    >>> romanText.tsvConverter.getLocalKey('vi', 'C')
    'a'
    ```

    With .getSecondaryKey(), we’re interested in the relative root of a secondaryRomanNumeral:

    ```python
    >>> romanText.tsvConverter.getSecondaryKey('V/vi', 'C')
    'a'
    ```

music21.romanText.tsvConverter.handleAddedTones(*dcmlChord: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#handleAddedTones)
:   Converts DCML added-tone syntax to music21.

    ```python
    >>> romanText.tsvConverter.handleAddedTones('V(64)')
    'Cad64'
    ```

    ```python
    >>> romanText.tsvConverter.handleAddedTones('i(4+2)')
    'i[no3][add4][add2]'
    ```

    ```python
    >>> romanText.tsvConverter.handleAddedTones('Viio7(b4-5)/V')
    'Viio7[no3][no5][addb4]/V'
    ```

    When in root position, 7 does not replace 8:

    ```python
    >>> romanText.tsvConverter.handleAddedTones('vi(#74)')
    'vi[no3][add#7][add4]'
    ```

    When not in root position, 7 does replace 8:

    ```python
    >>> romanText.tsvConverter.handleAddedTones('ii6(11#7b6)')
    'ii6[no8][no5][add11][add#7][addb6]'
    ```

    ‘0’ can be used to indicate root-replacement by 7 in a root-position chord.
    We need to change ‘0’ to ‘7’ because music21 changes the 0 to ‘o’ (i.e.,
    a diminished chord).

    ```python
    >>> romanText.tsvConverter.handleAddedTones('i(#0)')
    'i[no1][add#7]'
    ```

music21.romanText.tsvConverter.isMinor(*test\_key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#isMinor)
:   Checks whether a key is minor or not simply by upper vs lower case.

    ```python
    >>> romanText.tsvConverter.isMinor('F')
    False
    ```

    ```python
    >>> romanText.tsvConverter.isMinor('f')
    True
    ```

music21.romanText.tsvConverter.localKeyAsRn(*local\_key: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*, *global\_key: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/tsvConverter.html#localKeyAsRn)
:   Takes two music21.key.Key objects and returns the roman numeral for
    local\_key relative to global\_key.

    ```python
    >>> k1 = key.Key('C')
    >>> k2 = key.Key('e')
    >>> romanText.tsvConverter.localKeyAsRn(k1, k2)
    'VI'
    >>> k3 = key.Key('C#')
    >>> romanText.tsvConverter.localKeyAsRn(k3, k2)
    '#VI'
    >>> romanText.tsvConverter.localKeyAsRn(k2, k1)
    'iii'
    ```
