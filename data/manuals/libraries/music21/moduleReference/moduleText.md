Source: https://music21.org/music21docs/moduleReference/moduleText.html

# music21.text

Utility routines for processing text in scores and other musical objects.

## TextBox

class music21.text.TextBox(*content=None*, *x=500*, *y=500*, *\*\*keywords*)[[source]](../_modules/music21/text.html#TextBox)
:   A TextBox is arbitrary text that might be positioned anywhere on a page,
    independent of notes or staffs. A page attribute specifies what page this text is found on;
    style.absoluteY and style.absoluteX position the text from the bottom left corner in
    units of tenths.

    This object is similar to the TextExpression object, but does not have as many position
    parameters, enclosure attributes, and the ability to convert to
    RepeatExpressions and TempoTexts.

    ```python
    >>> y = 1000  # set a fixed vertical distance
    >>> s = stream.Stream()
    ```

    Specify character, x position, y position

    ```python
    >>> tb = text.TextBox('m', 250, y)
    >>> tb.style.fontSize = 40
    >>> tb.style.alignVertical = 'bottom'
    >>> s.append(tb)
    ```

    ```python
    >>> tb = text.TextBox('u', 300, y)
    >>> tb.style.fontSize = 60
    >>> tb.style.alignVertical = 'bottom'
    >>> s.append(tb)
    ```

    ```python
    >>> tb = text.TextBox('s', 550, y)
    >>> tb.style.fontSize = 120
    >>> tb.style.alignVertical = 'bottom'
    >>> s.append(tb)
    ```

    ```python
    >>> tb = text.TextBox('ic', 700, y)
    >>> tb.style.alignVertical = 'bottom'
    >>> tb.style.fontSize = 20
    >>> tb.style.fontStyle = 'italic'
    >>> s.append(tb)
    ```

    ```python
    >>> tb = text.TextBox('21', 850, y)
    >>> tb.style.alignVertical = 'bottom'
    >>> tb.style.fontSize = 80
    >>> tb.style.fontWeight = 'bold'
    >>> tb.style.fontStyle = 'italic'
    >>> s.append(tb)
    ```

    ```python
    >>> s.show()
    ```

    [![../_images/textBoxes-01.png](../_images/textBoxes-01.png)](../_images/textBoxes-01.png)

[`TextBox`](#music21.text.TextBox "music21.text.TextBox") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TextBox`](#music21.text.TextBox "music21.text.TextBox") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TextBox`](#music21.text.TextBox "music21.text.TextBox") read/write properties

TextBox.content
:   Get or set the content.

    ```python
    >>> te = text.TextBox('Con fuoco')
    >>> te.content
    'Con fuoco'
    >>> te.style.justify = 'center'
    >>> te.style.justify
    'center'
    ```

TextBox.page
:   Get or set the page number. The first page (page 1) is the default.

    ```python
    >>> te = text.TextBox('Great Score')
    >>> te.content
    'Great Score'
    >>> te.page
    1
    >>> te.page = 2
    >>> te.page
    2
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TextBox`](#music21.text.TextBox "music21.text.TextBox") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TextBox`](#music21.text.TextBox "music21.text.TextBox") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## LanguageDetector

class music21.text.LanguageDetector(*text=None*)[[source]](../_modules/music21/text.html#LanguageDetector)
:   Attempts to detect language on the basis of trigrams.

    ```python
    >>> ld = text.LanguageDetector()
    >>> ld.mostLikelyLanguage('Guten Morgen Frau Wieck. Ich bin Robert.')
    'de'
    ```

    Note that accuracy improves with longer texts, and that the trigrams are
    case sensitive. Putting “Morgen” in lowercase evaluates the text as Dutch.

    Supported languages are currently:

    ```python
    >>> text.LanguageDetector.languageLong
    {'en': 'English',
     'fr': 'French',
     'it': 'Italian',
     'de': 'German',
     'cn': 'Chinese',
     'la': 'Latin',
     'nl': 'Dutch'}
    ```

    See also, documentation for [`Trigram`](#music21.text.Trigram "music21.text.Trigram").

[`LanguageDetector`](#music21.text.LanguageDetector "music21.text.LanguageDetector") methods

LanguageDetector.mostLikelyLanguage(*excerpt: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/text.html#LanguageDetector.mostLikelyLanguage)
:   Returns the code of the most likely language for a passage, works on
    unicode or ascii. Current languages are:

    ```python
    >>> text.LanguageDetector.languageCodes
    ['en', 'fr', 'it', 'de', 'cn', 'la', 'nl']
    ```

    or None if no language is detected.

    ```python
    >>> ld = text.LanguageDetector()
    >>> ld.mostLikelyLanguage('Hello there, how are you doing today? '
    ...                       + "I haven't seen you in a while.")
    'en'
    >>> ld.mostLikelyLanguage('Ciao come stai? Sono molto lento oggi, ma non so perche.')
    'it'
    >>> ld.mostLikelyLanguage('Credo in unum deum. Patrem omnipotentem. Factorum celi')
    'la'
    ```

    ```python
    >>> ld = text.LanguageDetector()
    >>> ld.mostLikelyLanguage('') is None
    True
    ```

LanguageDetector.mostLikelyLanguageNumeric(*excerpt=None*)[[source]](../_modules/music21/text.html#LanguageDetector.mostLikelyLanguageNumeric)
:   returns a number representing the most likely language for a passage
    or 0 if there is no text.

    Useful for feature extraction.

    The codes are the index of the language name in LanguageDetector.languageCodes + 1

    ```python
    >>> ld = text.LanguageDetector()
    >>> for index in range(len(ld.languageCodes)):
    ...    print(str(index + 1) + ' ' +  ld.languageCodes[index])
    1 en
    2 fr
    3 it
    4 de
    5 cn
    6 la
    7 nl
    >>> numLang = ld.mostLikelyLanguageNumeric('Hello there, how are you doing today? '
    ...                + "I haven't seen you in a while.")
    >>> numLang
    1
    >>> ld.languageCodes[numLang - 1]
    'en'
    ```

classmethod LanguageDetector.readExcerpts()[[source]](../_modules/music21/text.html#LanguageDetector.readExcerpts)
:   Read the stored trigrams once and store them for later.

    Called on first LanguageDectector read.

## Trigram

class music21.text.Trigram(*excerptList=None*)[[source]](../_modules/music21/text.html#Trigram)
:   See LanguageDetector above.
    From <https://code.activestate.com/recipes/326576-language-detection-using-character-trigrams/>

    The frequency of three character
    sequences is calculated. When treated as a vector, this information
    can be compared to other trigrams, and the difference between them
    seen as an angle. The cosine of this angle varies between 1 for
    complete similarity, and 0 for utter difference. Since letter
    combinations are characteristic to a language, this can be used to
    determine the language of a body of text. For example:

    ```python
    >>> reference_en = Trigram('/path/to/reference/text/english')
    >>> reference_de = Trigram('/path/to/reference/text/german')
    >>> unknown = Trigram('url://pointing/to/unknown/text')
    >>> unknown.similarity(reference_de)
    #_DOCS_SHOW 0.4
    >>> unknown.similarity(reference_en)
    #_DOCS_SHOW 0.95
    ```

    would indicate the unknown text is almost certainly English. As
    syntax sugar, the minus sign is overloaded to return the difference
    between texts, so the above objects would give you:

    #\_DOCS\_SHOW >>> unknown - reference\_de
    #\_DOCS\_SHOW 0.6
    #\_DOCS\_SHOW >>> reference\_en - unknown # order doesn’t matter.
    #\_DOCS\_SHOW 0.05

    As it stands, the Trigram ignores character set information, which
    means you can only accurately compare within a single encoding
    (iso-8859-1 in the examples). A more complete implementation might
    convert to unicode first.

    As an extra bonus, there is a method to make up nonsense words in the
    style of the Trigram’s text.

    ```python
    >>> reference_en.makeWords(30)
    My withillonquiver and ald, by now wittlectionsurper, may sequia,
    tory, I ad my notter. Marriusbabilly She lady for rachalle spen hat knong al elf
    ```

[`Trigram`](#music21.text.Trigram "music21.text.Trigram") read-only properties

Trigram.length

[`Trigram`](#music21.text.Trigram "music21.text.Trigram") methods

Trigram.likely(*k*)[[source]](../_modules/music21/text.html#Trigram.likely)
:   Returns a character likely to follow the given string
    two character string, or a space if nothing is found.

Trigram.makeWords(*count*)[[source]](../_modules/music21/text.html#Trigram.makeWords)
:   returns a string of made-up words based on the known text.

Trigram.measure()[[source]](../_modules/music21/text.html#Trigram.measure)
:   calculates the scalar length of the trigram vector and
    stores it in self.length.

Trigram.parseExcerpt(*excerpt*)[[source]](../_modules/music21/text.html#Trigram.parseExcerpt)

Trigram.similarity(*other: [Trigram](#music21.text.Trigram "music21.text.Trigram")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/text.html#Trigram.similarity)
:   returns a number between 0 and 1 indicating similarity between
    two trigrams.

    1.0 means an identical ratio of trigrams;
    0.0 means no trigrams in common.

## Functions

music21.text.assembleAllLyrics(*streamIn*, *maxLyrics=10*, *lyricSeparation='\n'*, *\**, *wordSeparator=' '*)[[source]](../_modules/music21/text.html#assembleAllLyrics)
:   Concatenate all Lyrics text from a stream separated by lyricSeparation.
    The Stream is automatically recursed.

    uses assembleLyrics to do the heavy work.

    maxLyrics just determines how many times we should parse through the score, since it is
    not easy to determine what the maximum number of lyrics exist in the score.

    Here is a demo with one note and five lyrics.

    ```python
    >>> f = corpus.parse('demos/multiple-verses.xml')
    >>> text.assembleLyrics(f, 1)
    '1. First'
    >>> text.assembleLyrics(f, 2)
    '2. Second'
    >>> l = text.assembleAllLyrics(f)
    >>> l
    '1. First\n2. Second\n3. Third\n4. Fourth\n5. Fifth'
    ```

    * Changed in v8: no lyric separator appears at the beginning.

music21.text.assembleLyrics(*streamIn*, *lineNumber=1*, *\**, *wordSeparator=' '*)[[source]](../_modules/music21/text.html#assembleLyrics)
:   Concatenate text from a stream. The Stream is automatically flattened.

    The lineNumber parameter determines which line of text is assembled,
    as a ONE-indexed identifier in the .lyrics array.
    (To be changed in v8 to go with an identifier.). This means that
    lineNumber=0 will retrieve the last line of text.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note()
    >>> n1.lyric = 'Hi'
    >>> n2 = note.Note()
    >>> n2.lyric = 'there'
    >>> s.append(n1)
    >>> s.append(n2)
    >>> text.assembleLyrics(s)
    'Hi there'
    ```

    Composite lyrics can also be assembled.

    ```python
    >>> composite = note.Lyric()
    >>> composite0 = note.Lyric(text="He'", syllabic='begin')
    >>> composite1 = note.Lyric(text="ya", syllabic='end')
    >>> composite1.elisionBefore = '_'
    >>> composite.components = [composite0, composite1]
    >>> n1.lyrics[0] = composite
    >>> text.assembleLyrics(s)
    "He'_ya there"
    ```

    To get the lyrics from another line, set the lineNumber attribute.
    (see also [`assembleAllLyrics()`](#music21.text.assembleAllLyrics "music21.text.assembleAllLyrics") to get all
    lyrics).

    ```python
    >>> n1.addLyric('Bye')
    >>> n2.addLyric('Now')
    >>> text.assembleLyrics(s, lineNumber=2)
    'Bye Now'
    ```

music21.text.postpendArticle(*src*, *language=None*)[[source]](../_modules/music21/text.html#postpendArticle)
:   Given a text string, if an article is found in a leading position,
    place it at the end with a comma.

    ```python
    >>> text.postpendArticle('The Ale is Dear')
    'Ale is Dear, The'
    >>> text.postpendArticle('The Ale is Dear', 'en')
    'Ale is Dear, The'
    >>> text.postpendArticle('The Ale is Dear', 'it')
    'The Ale is Dear'
    >>> text.postpendArticle('Il Combattimento di Tancredi e Clorinda', 'it')
    'Combattimento di Tancredi e Clorinda, Il'
    ```

music21.text.prependArticle(*src*, *language=None*)[[source]](../_modules/music21/text.html#prependArticle)
:   Given a text string, if an article is found in a trailing position with a comma,
    place the article in front and remove the comma.

    ```python
    >>> text.prependArticle('Ale is Dear, The')
    'The Ale is Dear'
    >>> text.prependArticle('Ale is Dear, The', 'en')
    'The Ale is Dear'
    >>> text.prependArticle('Ale is Dear, The', 'it')
    'Ale is Dear, The'
    >>> text.prependArticle('Combattimento di Tancredi e Clorinda, Il', 'it')
    'Il Combattimento di Tancredi e Clorinda'
    ```
