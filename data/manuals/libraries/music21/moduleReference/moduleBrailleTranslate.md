Source: https://music21.org/music21docs/moduleReference/moduleBrailleTranslate.html

# music21.braille.translate

Functions for exporting music21 data as braille.

This module was made in consultation with the manual “Introduction to Braille
Music Transcription, Second Edition” by Mary Turner De Garmo, 2005. It is
available from the Library of Congress
[here](https://www.loc.gov/nls/services-and-resources/music-service-and-materials/),
and will henceforth be referred to as BMTM.

The most important function, and the only one that is needed to translate music
into braille, is [`objectToBraille()`](#music21.braille.translate.objectToBraille "music21.braille.translate.objectToBraille"). This function,
as well as the others, accepts keyword arguments that serve to modify the output.
If no keyword arguments are needed, then using the function is equivalent to
calling [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") on the music.

Keywords:

* **inPlace** (False): If False, then [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") is called
  on all `Measure`, `Part`, and
  `PartStaff` instances. Copies of those objects are then
  used to transcribe the music. If True, the transcription is done “as is.”
  This is useful for strict transcription because
  sometimes [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation")
  introduces some unwanted artifacts in the music. However, the music needs
  to be organized into measures for transcription to work.
* **debug** (False): If True, a braille-english representation of the music is returned. Useful
  for knowing how the music was interpreted by the braille transcriber.

The rest of the keywords are segment keywords. A segment is “a group of measures occupying
more than one braille line.” Music is divided into segments to “present the music to
the reader in a meaningful manner and to give him convenient reference points to use in
memorization” (BMTM, 71). Some of these keywords are changed automatically in context.

* **cancelOutgoingKeySig** (True): If True, whenever a key signature change is
  :   encountered, the new signature should be preceded by the old one.
* **descendingChords** (True): If True, then chords are spelled around the highest note.
  :   If False, then chords are spelled around the lowest note. This keyword is
      overridden by any valid clefs present in the music.
* **dummyRestLength** (None) For a given positive integer n, adds n “dummy rests”
  :   near the beginning of a segment. Designed for test purposes, as the rests
      are used to demonstrate measure division at the end of braille lines.
* **maxLineLength** (40): The maximum amount of braille characters
  :   that should be present in a line of braille.
* **segmentBreaks** (None): A list consisting of (measure number, offset start)
  :   tuples indicating where the music should be broken into segments.

      Warning

      Not currently implemented
* **showClefSigns** (False): If True, then clef signs are displayed.
  :   Since braille does not use clefs or staves to represent music, they would
      instead be shown for referential or historical purposes.
* **showFirstMeasureNumber** (True): If True, then a measure number is shown
  :   following the heading (if applicable) and preceding the music.
* **showHand** (None): If set to “right” or “left”, the corresponding
  :   hand sign is shown before the music. In keyboard music,
      the hand signs are shown automatically.
* **showHeading** (True): If True, then a braille heading is created above
  :   the initial segment. A heading consists
      of an initial [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature"), `TimeSignature`,
      [`TempoText`](moduleTempo.html#music21.tempo.TempoText "music21.tempo.TempoText"), and [`MetronomeMark`](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark"),
      or any subset thereof. The heading
      is centered above the music automatically.
* **showLongSlursAndTiesTogether** (None), **showShortSlursAndTiesTogether** (False):
  :   If False, then the slur on either side of the phrase is reduced by the amount
      that ties are present. If True, then slurs and ties are shown together
      (i.e. the note can have both a slur and a tie). If showLongSlursAndTiesTogether
      is None (default), its value is programmatically set to be the value of
      `slurLongPhraseWithBrackets`, described next.
* **slurLongPhraseWithBrackets** (True): If True, then the slur of a
  :   long phrase (4+ consecutive notes) is brailled using the bracket slur.
      If False, the double slur is used instead.
* **suppressOctaveMarks** (False): If True, then all octave marks are suppressed.
  :   Designed for test purposes, as octave marks were not presented in BMTM until Chapter 7.
* **upperFirstInNoteFingering** (True): If True, then whenever
  :   there is a choice fingering (i.e. 5|4), the upper
      number is transcribed before the lower number. If False, the reverse is the case.

## Functions

music21.braille.translate.objectToBraille(*music21Obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#objectToBraille)
:   Translates an arbitrary object to braille.

    ```python
    >>> from music21.braille import translate
    >>> samplePart = converter.parse('tinynotation: 3/4 C4 D16 E F G# r4 e2.')
    >>> samplePart.show()
    ```

    > [![../_images/objectToBraille.png](../_images/objectToBraille.png)](../_images/objectToBraille.png)

    ```python
    >>> print(translate.objectToBraille(samplePart))
    ⠀⠀⠀⠀⠀⠀⠀⠼⠉⠲⠀⠀⠀⠀⠀⠀⠀
    ⠼⠁⠀⠸⠹⠵⠋⠛⠩⠓⠧⠀⠐⠏⠄⠣⠅
    ```

    For normal users, you’ll just call this, which starts a text editor:

    ```python
    >>> samplePart.show('braille')
    ⠀⠀⠀⠀⠀⠀⠀⠼⠉⠲⠀⠀⠀⠀⠀⠀⠀
    ⠼⠁⠀⠸⠹⠵⠋⠛⠩⠓⠧⠀⠐⠏⠄⠣⠅
    ```

    Other examples:

    ```python
    >>> sampleNote = note.Note('C3')
    >>> print(translate.objectToBraille(sampleNote))
    ⠸⠹
    ```

    ```python
    >>> sampleDynamic = dynamics.Dynamic('fff')
    >>> print(translate.objectToBraille(sampleDynamic))
    ⠜⠋⠋⠋
    ```

    ```python
    >>> sample_voice = stream.Voice([note.Note()])
    >>> sample_measure = stream.Measure([sample_voice])
    >>> print(translate.objectToBraille(sample_measure))
    ⠀⠼⠁⠲⠀
    ⠼⠚⠀⠐⠹
    ```

    ```python
    >>> empty_measure = stream.Measure()
    >>> print(translate.objectToBraille(empty_measure))
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠙⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠼⠚
    ```

    Not currently supported: generic stream.Stream objects or stream.Voice objects:

    ```python
    >>> sample_generic_stream = stream.Stream([note.Note()])
    >>> translate.objectToBraille(sample_generic_stream)
    Traceback (most recent call last):
    music21.braille.translate.BrailleTranslateException: Stream cannot be translated to Braille.
    ```

music21.braille.translate.keyboardPartsToBraille(*keyboardScore*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#keyboardPartsToBraille)
:   Translates a Score object containing two `Part` instances to braille,
    an upper part and a lower
    part. Assumes that the two parts are aligned and well constructed. Bar over bar format is used.

music21.braille.translate.measureToBraille(*music21Measure*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=False*, *showHand=None*, *showHeading=False*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#measureToBraille)
:   Translates a `Measure` to braille.

    ```python
    >>> p = stream.Part()
    >>> p.append(note.Note('C4', type='whole'))
    >>> p.makeMeasures(inPlace=True)
    >>> p.show('t')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {4.0} <music21.bar.Barline type=final>
    >>> print(braille.translate.objectToBraille(p))
    ⠀⠀⠼⠙⠲⠀⠀
    ⠼⠁⠀⠐⠽⠣⠅
    >>> print(braille.translate.measureToBraille(p.measure(1)))
    ⠼⠙⠲⠀⠐⠽⠣⠅
    ```

music21.braille.translate.metadataToString(*music21Metadata: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata")*, *returnBrailleUnicode=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/braille/translate.html#metadataToString)
:   Convert a Metadata format to a format for BRF.

    ```python
    >>> from music21.braille import translate
    >>> corelli = corpus.parse('monteverdi/madrigal.3.1.rntxt')
    >>> mdObject = corelli.getElementsByClass(metadata.Metadata).first()
    >>> mdObject.__class__
    <class 'music21.metadata.Metadata'>
    ```

    The default is very close to ascii.

    ```python
    >>> print(translate.metadataToString(mdObject))
    Alternative Title: 3.1
    Composer: Claudio Monteverdi
    Title: La Giovinetta Pianta
    ```

    And in Braille Unicode.

    ```python
    >>> unicodeVersion = translate.metadataToString(mdObject, returnBrailleUnicode=True)
    >>> print(unicodeVersion)
    ⠠⠁⠇⠞⠑⠗⠝⠁⠞⠊⠧⠑⠀⠠⠞⠊⠞⠇⠑⠒⠀⠼⠉⠲⠁
    ⠠⠉⠕⠍⠏⠕⠎⠑⠗⠒⠀⠠⠉⠇⠁⠥⠙⠊⠕⠀⠠⠍⠕⠝⠞⠑⠧⠑⠗⠙⠊
    ⠠⠞⠊⠞⠇⠑⠒⠀⠠⠇⠁⠀⠠⠛⠊⠕⠧⠊⠝⠑⠞⠞⠁⠀⠠⠏⠊⠁⠝⠞⠁
    ```

    Note the difference between the first and then translating back to ASCII Braille:

    ```python
    >>> print(braille.basic.brailleUnicodeToBrailleAscii(unicodeVersion))
    ,ALTERNATIVE ,TITLE3 #C4A
    ,COMPOSER3 ,CLAUDIO ,MONTEVERDI
    ,TITLE3 ,LA ,GIOVINETTA ,PIANTA
    ```

music21.braille.translate.opusToBraille(*music21Opus*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#opusToBraille)
:   Translates an `Opus` to braille.

music21.braille.translate.partToBraille(*music21Part*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#partToBraille)
:   Translates a `Part` to braille.

    This is one of two (w/ keyboardPartsToBraille) main routines. Runs segment.findSegments
    and then for each segment runs transcribe on it.

music21.braille.translate.scoreToBraille(*music21Score*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#scoreToBraille)
:   Translates a `Score` to braille.

music21.braille.translate.streamToBraille(*music21Stream: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure") | [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")*, *\**, *inPlace=False*, *debug=False*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/translate.html#streamToBraille)
:   Translates a `Measure`.
    `Part`,
    `Score`, or
    `Opus` to braille.

    Note: generic `Stream` instances are not supported.

    ```python
    >>> s = stream.Stream(note.Note())
    >>> braille.translate.streamToBraille(s)
    Traceback (most recent call last):
    music21.braille.translate.BrailleTranslateException: Stream cannot be translated to Braille.
    ```
