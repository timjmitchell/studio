Source: https://music21.org/music21docs/moduleReference/moduleRomanTextClercqTemperley.html

# music21.romanText.clercqTemperley

Parses the de Clercq-Temperley popular music flavor of RomanText.
The Clercq-Temperley file format and additional rock corpus analysis
information may be located at <https://rockcorpus.midside.com>

## CTSong

class music21.romanText.clercqTemperley.CTSong(*textFile: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") = ''*, *\*\*keywords*)[[source]](../_modules/music21/romanText/clercqTemperley.html#CTSong)
:   This parser is an object-oriented approach to parsing clercqTemperley text files into music.
    It is an advanced method. Most people should just run:

    ```python
    >>> p = converter.parse('clercqTemperley/dt/BrownEyedGirl.cttxt')
    ```

    or if the file ends in .txt then give the format explicitly as either ‘clerqTemperley’
    or ‘cttxt’:

    ```python
    >>> p = converter.parse('BrownEyedGirl.txt', format='clercqTemperley')
    ```

    Advanced: if you want access to a CTSong object itself (for manipulating the input before
    converting to a string, etc. then create a CTSong object with one of the following inputs:

    1. by passing in the string, with newline characters (\n) at the end of each line
    2. by passing in the filename as a string or path, and have Python
       open the file and read the text

    Given this file, you could create a CTSong object with:

    ```python
    >>> exampleClercqTemperley = '''
    ... % Brown-Eyed Girl
    ... VP: I | IV | I | V |
    ... In: $VP*2
    ... Vr: $VP*4 IV | V | I | vi | IV | V | I | V | % Second half could be called chorus
    ... Ch: V | | $VP*2 I |*4
    ... Ch2: V | | $VP*3     % Fadeout
    ... S: [G] $In $Vr $Vr $Ch $VP $Vr $Ch2
    ... '''
    ```

    Or:

    ```python
    >>> s = romanText.clercqTemperley.CTSong('C:/Brown-Eyed_Girl.txt')
    ```

    When you call the .toPart() method on the newly created CTSong object,
    the code extracts meaningful properties (such as title, text, comments,
    year, rules, home time Signature, and home Key Signature) from the text file
    and returns a new Part object. It also makes these properties available on the
    CTSong object.

    The toPart() method has two optional labeling parameters, labelRomanNumerals and
    labelSubsectionsOnScore. Both are set to True by default. Thus, the created score
    will have labels (on the chord’s lyric) for each roman numeral as well as for each
    section in the song (LHS). In case of a recursive definition (a rule contains a reference
    to another rule), both labels are printed, with the deepest
    reference on the smallest lyric line.

    ```python
    >>> p = s.toPart()
    >>> p.show()
    ```

    [![../_images/ClercqTemperleyExbrown-eyed_girl.png](../_images/ClercqTemperleyExbrown-eyed_girl.png)](../_images/ClercqTemperleyExbrown-eyed_girl.png)

    ```python
    >>> firstRN = p[roman.RomanNumeral][0]
    >>> firstRN.lyric
    'I\nVP\nIn'
    ```

    All roman numerals mark which formal division they are in:

    ```python
    >>> 'formalDivision' in firstRN.editorial
    True
    >>> firstRN.editorial.formalDivision
    ['VP', 'In']
    ```

    The second RomanNumeral is at the start of no formal divisions

    ```python
    >>> secondRN = p[roman.RomanNumeral][1]
    >>> secondRN.lyric
    'IV'
    >>> secondRN.editorial.formalDivision
    []
    ```

    ```python
    >>> s.title
    'Brown-Eyed Girl'
    ```

    ```python
    >>> s.homeTimeSig
    <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> s.homeKey
    <music21.key.Key of G major>
    ```

    ```python
    >>> s.comments
    [['Vr:', 'Second half could be called chorus'], ['Ch2:', 'Fadeout']]
    ```

    Year is not defined as part of the Clercq-Temperley format, but it will be helpful
    to have it as a property. So let’s assign a year to this song:

    ```python
    >>> s.year = 1967
    >>> s.year
    1967
    ```

    Upon calling toPart(), CTRule objects are also created. CTRule objects are
    the individual rules that make up the song object. For example,

    ```python
    >>> s.rules
    OrderedDict([('VP', <music21.romanText.clercqTemperley.CTRule
                         text='VP: I | IV | I | V |'>),
                 ('In', <music21.romanText.clercqTemperley.CTRule text='In: $VP*2'>),
                 ('Vr', <music21.romanText.clercqTemperley.CTRule
                         text='Vr: $VP*4 IV | V | I | vi | IV | V | I | V |
                                     % Second half could be called chorus'>),
                 ('Ch', <music21.romanText.clercqTemperley.CTRule
                         text='Ch: V | | $VP*2 I |*4'>),
                 ('Ch2', <music21.romanText.clercqTemperley.CTRule
                         text='Ch2: V | | $VP*3     % Fadeout'>),
                 ('S', <music21.romanText.clercqTemperley.CTRule
                         text='S: [G] $In $Vr $Vr $Ch $VP $Vr $Ch2'>)])
    ```

    The parser extracts meaningful properties to each rule, such as sectionName,
    home time signature of that rule, home key of that rule, and of course the individual
    stream from the song corresponding to the rule.

    The following examples display the instantiated properties of the second rule (list indexes
    start at one) as created above.

    ```python
    >>> rule = s.rules['In']
    >>> rule.text
    'In: $VP*2'
    ```

    ```python
    >>> rule.sectionName
    'Introduction'
    ```

    With this object-oriented approach to parsing the clercq-temperley text file format,
    we now have the ability to analyze a large corpus (200 files) of popular music
    using the full suite of harmonic tools of music21. We can not only analyze each
    song as a whole, as presented in Clercq and Temperley’s research, but we can also analyze each
    individual section (or rule) of a song. This may provide interesting insight
    into popular music beyond our current understanding.

    Examples used throughout this class utilize the following Clercq-Temperley text file

    ```python
    >>> BlitzkriegBopCT = '''
    ... % Blitzkrieg Bop
    ... BP: I | IV V | %THIS IS A COMMENT
    ... In: $BP*3 I IV | I | $BP*3 I IV | I | R |*4 I |*4
    ... Vr: $BP*3 I IV | I |
    ... Br: IV | | I | IV I | IV | | ii | IV V |
    ... Co: R |*4 I |*4
    ... S: [A] $In $Vr $Vr $Br $Vr $Vr $Br $Vr $Vr $Co
    ... '''
    ```

    Another example using a different Clercq-Temperley file

    RockClockCT =
    % Rock Around the Clock
    % just a general comment
    In: I | | | | | | V | |
    Vr: I | | | | IVd7 | | I | | V7 | | I | | %a comment on verse
    Vrf: I | | | | IVd7 | | I | | V7 | | I | IV iv | V | . I |
    S: [A] $In $Vr $Vr $Vr $Vr $Vr $Vr $Vrf % 3rd and 6th verses are instrumental

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.RockClockCT)
    >>> part = s.toPart()
    >>> part.highestTime
    376.0
    ```

    ```python
    >>> s.title
    'Rock Around the Clock'
    ```

    ```python
    >>> s.homeTimeSig
    <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> s.homeKey
    <music21.key.Key of A major>
    ```

    ```python
    >>> s.comments
    [['just a general comment'],
     ['Vr:', 'a comment on verse'],
     ['S:', '3rd and 6th verses are instrumental']]
    ```

    ```python
    >>> s.year = 1952
    >>> s.year
    1952
    ```

    ```python
    >>> s.rules
    OrderedDict([('In', <music21.romanText.clercqTemperley.CTRule
                            text='In: I | | | | | | V | |'>),
                 ('Vr', <music21.romanText.clercqTemperley.CTRule
                         text='Vr: I | | | | IVd7 | | I | | V7 | | I | | %a comment on verse'>),
                 ('Vrf', <music21.romanText.clercqTemperley.CTRule
                         text='Vrf: I | | | | IVd7 | | I | | V7 | | I | IV iv | V | . I |'>),
                 ('S', <music21.romanText.clercqTemperley.CTRule
                         text='S: [A] $In $Vr $Vr $Vr $Vr $Vr $Vr $Vrf
                                     % 3rd and 6th verses are instrumental'>)])
    ```

    ```python
    >>> rule = s.rules['In']
    >>> rule.text
    'In: I | | | | | | V | |'
    ```

    ```python
    >>> rule.sectionName
    'Introduction'
    ```

[`CTSong`](#music21.romanText.clercqTemperley.CTSong "music21.romanText.clercqTemperley.CTSong") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`CTSong`](#music21.romanText.clercqTemperley.CTSong "music21.romanText.clercqTemperley.CTSong") read-only properties

CTSong.comments
:   Get the comments list of all CTRule objects.

    comments are stored as a list of comments, each comment on a line as a list. If the
    comment is on a rule line, the list contains both the line’s LHS (like “In:”)
    and the comment if the comment is on a line of its own, only the comment is
    appended as a list of length one.

    The title is not a comment. The title is stored under self.title

    > textString = ‘’’
    >
    > %Simple Gifts
    >
    > % A wonderful shaker melody
    >
    > Vr: I | I | %incomplete verse
    >
    > S: [A] $Vr % Not quite finished!’’’

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.textString)
    >>> s
    <music21.romanText.clercqTemperley.CTSong title='Simple Gifts' year=None>
    >>> s.comments
    [['A wonderful shaker melody'], ['Vr:', 'incomplete verse'], ['S:', 'Not quite finished!']]
    ```

CTSong.homeKey
:   gets the initial, or ‘home’, Key by looking at the music text and locating
    the key signature at the start of the S: rule.

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.textString)
    >>> s.homeKey
    <music21.key.Key of A major>
    ```

CTSong.homeTimeSig
:   gets the initial, or ‘home’, time signature in a song by looking at the ‘S’ substring
    and returning the provided time signature. If not present, returns a default music21
    time signature of 4/4

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.textString)
    >>> s.homeTimeSig
    <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> change = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.changeIsGonnaCome)
    >>> change.homeTimeSig
    <music21.meter.TimeSignature 12/8>
    >>> change.homeTimeSig.beatSequence
    <music21.meter.core.MeterSequence {{1/8+1/8+1/8}+{1/8+1/8+1/8}+{1/8+1/8+1/8}+{1/8+1/8+1/8}}>
    ```

CTSong.rules
:   Get the rules of a CTSong. the Rules is an OrderedDict of
    objects of type CTRule. If only a text file
    provided, this goes through text file and creates the
    rule object out of each line containing
    an LHS including the Song line, which should always be last.

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.BlitzkriegBopCT)
    >>> len(s.rules)
    6
    >>> for rule in s.rules:
    ...   (rule, s.rules[rule])
    ('BP', <music21.romanText.clercqTemperley.CTRule
                text='BP: I | IV V | %THIS IS A COMMENT'>)
    ('In', <music21.romanText.clercqTemperley.CTRule
                text='In: $BP*3 I IV | I | $BP*3 I IV | I | R |*4 I |*4'>)
    ('Vr', <music21.romanText.clercqTemperley.CTRule
                text='Vr: $BP*3 I IV | I |'>)
    ('Br', <music21.romanText.clercqTemperley.CTRule
                text='Br: IV | | I | IV I | IV | | ii | IV V |'>)
    ('Co', <music21.romanText.clercqTemperley.CTRule
                text='Co: R |*4 I |*4'>)
    ('S', <music21.romanText.clercqTemperley.CTRule
                text='S: [A] $In $Vr $Vr $Br $Vr $Vr $Br $Vr $Vr $Co'>)
    ```

    Rules S is where we begin:

    ```python
    >>> s.rules['S']
    <music21.romanText.clercqTemperley.CTRule
        text='S: [A] $In $Vr $Vr $Br $Vr $Vr $Br $Vr $Vr $Co'>
    ```

CTSong.title
:   Get or set the title of the CTSong. If not specified
    explicitly but the clercq-Temperley text exists,
    this attribute searches first few lines of text file for title (a string preceded by a ‘%’)
    if found, sets title attribute to this string and returns this title)

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.textString)
    >>> s.title
    'Simple Gifts'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`CTSong`](#music21.romanText.clercqTemperley.CTSong "music21.romanText.clercqTemperley.CTSong") methods

CTSong.parse(*textFile: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*)[[source]](../_modules/music21/romanText/clercqTemperley.html#CTSong.parse)
:   Called when a CTSong is created by passing a string or filename;
    in the second case, it opens the file
    and removes all blank lines, and adds in new line characters
    returns pieceString that CTSong can call .expand() on.

    ```python
    >>> exCT = romanText.clercqTemperley.exampleClercqTemperley
    ```

    This calls parse implicitly:

    ```python
    >>> s = romanText.clercqTemperley.CTSong(exCT)
    ```

    ```python
    >>> print(s.text)
    % Brown-Eyed Girl
    VP: I | IV | I | V |
    In: $VP*2
    Vr: $VP*4 IV | V | I | vi | IV | V | I | V |       % Second half could be called chorus
    Ch: V | | $VP*2 I |*4
    Ch2: V | | $VP*3     % Fadeout
    S: [G] $In $Vr $Vr $Ch $VP $Vr $Ch2
    ```

    ```python
    >>> s.lines[0]
    '% Brown-Eyed Girl'
    ```

    ```python
    >>> s.lines[-1]
    'S: [G] $In $Vr $Vr $Ch $VP $Vr $Ch2'
    ```

CTSong.toPart(*labelRomanNumerals=True*, *labelSubsectionsOnScore=True*) → [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTSong.toPart)
:   creates a Part object out of a from CTSong and also creates CTRule objects in the process,
    filling their .streamFromCTSong attribute with the corresponding smaller inner stream.
    Individual attributes of a rule are defined by the entire CTSong, such as
    meter and time signature, so creation of CTRule objects typically occurs
    only from this method and directly from the clercqTemperley text.

    ```python
    >>> s = romanText.clercqTemperley.CTSong(romanText.clercqTemperley.BlitzkriegBopCT)
    >>> partObj = s.toPart()
    >>> partObj.highestOffset
    380.0
    ```

CTSong.toScore(*labelRomanNumerals=True*, *labelSubsectionsOnScore=True*) → [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTSong.toScore)
:   DEPRECATED: use .toPart() instead. This method will be removed in v.10

[`CTSong`](#music21.romanText.clercqTemperley.CTSong "music21.romanText.clercqTemperley.CTSong") instance variables

CTSong.year
:   The year of the CTSong; not formally defined
    by the Clercq-Temperley format.

## CTRule

class music21.romanText.clercqTemperley.CTRule(*text=''*, *parent: [CTSong](#music21.romanText.clercqTemperley.CTSong "music21.romanText.clercqTemperley.CTSong") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule)
:   CTRule objects correspond to the individual lines defined in a
    [`CTSong`](#music21.romanText.clercqTemperley.CTSong "music21.romanText.clercqTemperley.CTSong") object. They are typically
    created by the parser after a CTSong object has been created and the .toPart() method
    has been called on that object. The usefulness of each CTRule object is that each
    has a `streamFromCTSong()` attribute,
    which is the stream from the entire score that the rule corresponds to.

    To parse, put the text into the

[`CTRule`](#music21.romanText.clercqTemperley.CTRule "music21.romanText.clercqTemperley.CTRule") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`CTRule`](#music21.romanText.clercqTemperley.CTRule "music21.romanText.clercqTemperley.CTRule") read-only properties

CTRule.comment
:   Get the comment of a CTRule object.

    ```python
    >>> rs = 'In: $BP*3 I IV | I | $BP*3 I IV | I | R |*4 I |*4 % This is a comment'
    >>> s = romanText.clercqTemperley.CTRule(rs)
    >>> s.comment
    'This is a comment'
    ```

CTRule.sectionName
:   Returns the expanded version of the Left-hand side (LHS) such as
    Introduction, Verse, etc. if
    text is present (uses LHS to expand)

    Currently supported abbreviations:

    * In: Introduction
    * Br: Bridge
    * Vr: Verse
    * Ch: Chorus
    * Fadeout: Fadeout
    * S: Song

    ```python
    >>> s = romanText.clercqTemperley.CTRule('Vr2: $BP*3 I IV | I |')
    >>> s.sectionName
    'Verse2'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`CTRule`](#music21.romanText.clercqTemperley.CTRule "music21.romanText.clercqTemperley.CTRule") read/write properties

CTRule.LHS
:   Get the LHS (Left Hand Side) of the CTRule.
    If not specified explicitly but CTtext present, searches
    first characters up until ‘:’ for rule and returns string)

    ```python
    >>> rs = 'In: $BP*3 I IV | R |*4 I |*4 % This is a comment'
    >>> s = romanText.clercqTemperley.CTRule(rs)
    >>> s.LHS
    'In'
    ```

CTRule.musicText
:   Gets just the music text of the CTRule, excluding the left hand side and comments

    ```python
    >>> rs = 'In: $BP*3 I IV | I | $BP*3 I IV | I | R |*4 I |*4 % This is a comment'
    >>> s = romanText.clercqTemperley.CTRule(rs)
    >>> s.text
    'In: $BP*3 I IV | I | $BP*3 I IV | I | R |*4 I |*4 % This is a comment'
    >>> s.musicText
    '$BP*3 I IV | I | $BP*3 I IV | I | R |*4 I |*4'
    ```

CTRule.parent
:   A reference to the CTSong object housing the CTRule if any.

[`CTRule`](#music21.romanText.clercqTemperley.CTRule "music21.romanText.clercqTemperley.CTRule") methods

CTRule.addOptionalTieAndLyrics(*rn: [roman.RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral")*, *lastChord: [chord.Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.addOptionalTieAndLyrics)
:   Adds ties to chords that are the same. Adds lyrics to chords that change.

CTRule.expand(*tsContext: [TimeSignature](moduleMeterBase.html#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *keyContext: [Key](moduleKey.html#music21.key.Key "music21.key.Key") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")][[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.expand)
:   The meat of it all – expand one rule completely and return a list of Measure objects.

    Parses within the local time signature context and key context.

CTRule.expandExpansionContent(*content: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *numReps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.expandExpansionContent)
:   Expand a rule that contains an expansion (i.e., a $) in it.

    Requires CTSong parent to be set.

CTRule.expandSimpleContent(*content: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *numReps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.expandSimpleContent)

CTRule.fixupChordAtom(*atom: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.fixupChordAtom)
:   changes some CT values into music21 values

    ```python
    >>> s = romanText.clercqTemperley.CTRule()
    >>> s.fixupChordAtom('iix')
    'iio'
    >>> s.fixupChordAtom('viih7')
    'vii/o7'
    >>> s.fixupChordAtom('iia')
    'ii+'
    ```

CTRule.insertKsTs(*m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*, *ts: [TimeSignature](moduleMeterBase.html#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature")*, *keyObj: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.insertKsTs)
:   Insert a new time signature or Key into measure m, if it’s
    not already in the stream somewhere.

    Note that the name “ks” is slightly misnamed. It requires a Key,
    not KeySignature object.

CTRule.isSame(*rn: [roman.RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral")*, *lastChord: [chord.Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/romanText/clercqTemperley.html#CTRule.isSame)
:   Returns True if the pitches of the RomanNumeral are the same as the pitches
    of lastChord. Returns False if lastChord is None.

[`CTRule`](#music21.romanText.clercqTemperley.CTRule "music21.romanText.clercqTemperley.CTRule") instance variables

CTRule.text
:   The full text of the CTRule, including the LHS, chords, and comments.
