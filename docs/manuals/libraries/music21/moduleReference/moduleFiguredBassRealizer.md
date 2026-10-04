Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassRealizer.html

# music21.figuredBass.realizer

This module, the heart of fbRealizer, is all about realizing
a bass line of (bassNote, notationString)
pairs. All it takes to create well-formed realizations of a
bass line is a few lines of music21 code,
from start to finish. See [`FiguredBassLine`](#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine") for more details.

```python
>>> from music21.figuredBass import realizer
>>> fbLine = realizer.FiguredBassLine()
>>> fbLine.addElement(note.Note('C3'))
>>> fbLine.addElement(note.Note('D3'), '4,3')
>>> fbLine.addElement(note.Note('C3', quarterLength = 2.0))
>>> allSols = fbLine.realize()
>>> allSols.getNumSolutions()
30
>>> allSols.generateRandomRealizations(14).show()
```

> [![../_images/fbRealizer_intro.png](../_images/fbRealizer_intro.png)](../_images/fbRealizer_intro.png)

The same can be accomplished by taking the notes and notations
from a `Stream`.
See [`figuredBassFromStream()`](#music21.figuredBass.realizer.figuredBassFromStream "music21.figuredBass.realizer.figuredBassFromStream") for more details.

```python
>>> s = converter.parse('tinynotation: C4 D4_4,3 C2', makeNotation=False)
>>> fbLine = realizer.figuredBassFromStream(s)
>>> allSols2 = fbLine.realize()
>>> allSols2.getNumSolutions()
30
```

## FiguredBassLine

class music21.figuredBass.realizer.FiguredBassLine(*inKey=None*, *inTime=None*)[[source]](../_modules/music21/figuredBass/realizer.html#FiguredBassLine)
:   A FiguredBassLine is an interface for realization of a line of (bassNote, notationString) pairs.
    Currently, only 1:1 realization is supported, meaning that every bassNote is realized and the
    `quarterLength` or duration of a realization above a bassNote
    is identical to that of the bassNote.

    inKey defaults to C major.

    inTime defaults to 4/4.

    ```python
    >>> from music21.figuredBass import realizer
    >>> fbLine = realizer.FiguredBassLine(key.Key('B'), meter.TimeSignature('3/4'))
    >>> fbLine.inKey
    <music21.key.Key of B major>
    >>> fbLine.inTime
    <music21.meter.TimeSignature 3/4>
    ```

[`FiguredBassLine`](#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine") methods

FiguredBassLine.addElement(*bassObject: [Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *notationString=None*)[[source]](../_modules/music21/figuredBass/realizer.html#FiguredBassLine.addElement)
:   Use this method to add (bassNote, notationString) pairs to the bass line. Elements
    are realized in the order they are added.

    ```python
    >>> from music21.figuredBass import realizer
    >>> fbLine = realizer.FiguredBassLine(key.Key('B'), meter.TimeSignature('3/4'))
    >>> fbLine.addElement(note.Note('B2'))
    >>> fbLine.addElement(note.Note('C#3'), '6')
    >>> fbLine.addElement(note.Note('D#3'), '6')
    >>> fbLine.generateBassLine().show()
    ```

    [![../_images/fbRealizer_bassLine.png](../_images/fbRealizer_bassLine.png)](../_images/fbRealizer_bassLine.png)

FiguredBassLine.generateBassLine()[[source]](../_modules/music21/figuredBass/realizer.html#FiguredBassLine.generateBassLine)
:   Generates the bass line as a `Score`.

    ```python
    >>> from music21.figuredBass import realizer
    >>> fbLine = realizer.FiguredBassLine(key.Key('B'), meter.TimeSignature('3/4'))
    >>> fbLine.addElement(note.Note('B2'))
    >>> fbLine.addElement(note.Note('C#3'), '6')
    >>> fbLine.addElement(note.Note('D#3'), '6')
    >>> fbLine.generateBassLine().show()
    ```

    [![../_images/fbRealizer_bassLine.png](../_images/fbRealizer_bassLine.png)](../_images/fbRealizer_bassLine.png)

    ```python
    >>> sBach = corpus.parse('bach/bwv307')
    >>> sBach.parts.last().measure(0).show('text')
    {0.0} ...
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.key.Key of B- major>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note B->
    {0.5} <music21.note.Note C>
    ```

    ```python
    >>> fbLine = realizer.figuredBassFromStream(sBach.parts.last())
    >>> fbLine.generateBassLine().measure(1).show('text')
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.key.KeySignature of 2 flats>
    {0.0} <music21.meter.TimeSignature 4/4>
    {3.0} <music21.note.Note B->
    {3.5} <music21.note.Note C>
    ```

FiguredBassLine.overlayPart(*music21Part*)[[source]](../_modules/music21/figuredBass/realizer.html#FiguredBassLine.overlayPart)

FiguredBassLine.realize(*fbRules=None*, *numParts=4*, *maxPitch=None*)[[source]](../_modules/music21/figuredBass/realizer.html#FiguredBassLine.realize)
:   Creates a [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment")
    for each (bassNote, notationString) pair
    added using [`addElement()`](#music21.figuredBass.realizer.FiguredBassLine.addElement "music21.figuredBass.realizer.FiguredBassLine.addElement").
    Each Segment is associated
    with the [`Rules`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") object provided, meaning that rules are
    universally applied across all Segments. The number of parts in a realization
    (including the bass) can be controlled through numParts, and the maximum pitch can
    likewise be controlled through maxPitch.
    Returns a [`Realization`](#music21.figuredBass.realizer.Realization "music21.figuredBass.realizer.Realization").

    If this method is called without having provided any (bassNote, notationString) pairs,
    a FiguredBassLineException is raised. If only one pair is provided, the Realization will
    contain [`allCorrectConsecutivePossibilities()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities")
    for the one note.

    if fbRules is None, creates a new rules.Rules() object

    if maxPitch is None, uses pitch.Pitch(‘B5’)

    ```python
    >>> from music21.figuredBass import realizer
    >>> from music21.figuredBass import rules
    >>> fbLine = realizer.FiguredBassLine(key.Key('B'), meter.TimeSignature('3/4'))
    >>> fbLine.addElement(note.Note('B2'))
    >>> fbLine.addElement(note.Note('C#3'), '6')
    >>> fbLine.addElement(note.Note('D#3'), '6')
    >>> fbRules = rules.Rules()
    >>> r1 = fbLine.realize(fbRules)
    >>> r1.getNumSolutions()
    208
    >>> fbRules.forbidVoiceOverlap = False
    >>> r2 = fbLine.realize(fbRules)
    >>> r2.getNumSolutions()
    7908
    ```

FiguredBassLine.retrieveSegments(*fbRules=None*, *numParts=4*, *maxPitch=None*)[[source]](../_modules/music21/figuredBass/realizer.html#FiguredBassLine.retrieveSegments)
:   generates the segmentList from an fbList, including any overlaid Segments

    if fbRules is None, creates a new rules.Rules() object

    if maxPitch is None, uses pitch.Pitch(‘B5’)

[`FiguredBassLine`](#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine") instance variables

FiguredBassLine.inKey
:   A [`Key`](moduleKey.html#music21.key.Key "music21.key.Key") which implies a scale value,
    scale mode, and key signature for a
    [`FiguredBassScale`](moduleFiguredBassRealizerScale.html#music21.figuredBass.realizerScale.FiguredBassScale "music21.figuredBass.realizerScale.FiguredBassScale").

FiguredBassLine.inTime
:   A `TimeSignature` which specifies the
    time signature of realizations outputted to a
    `Score`.

## Realization

class music21.figuredBass.realizer.Realization(*\*\*fbLineOutputs*)[[source]](../_modules/music21/figuredBass/realizer.html#Realization)
:   Returned by [`FiguredBassLine`](#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine") after calling
    [`realize()`](#music21.figuredBass.realizer.FiguredBassLine.realize "music21.figuredBass.realizer.FiguredBassLine.realize"). Allows for the
    generation of realizations as a `Score`.

    * See the [`examples`](moduleFiguredBassExamples.html#module-music21.figuredBass.examples "music21.figuredBass.examples") module for examples on the generation
      of realizations.
    * A possibility progression is a valid progression through a string of
      [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment") instances.
      See [`possibility`](moduleFiguredBassPossibility.html#module-music21.figuredBass.possibility "music21.figuredBass.possibility") for more details on possibilities.

[`Realization`](#music21.figuredBass.realizer.Realization "music21.figuredBass.realizer.Realization") methods

Realization.generateAllRealizations()[[source]](../_modules/music21/figuredBass/realizer.html#Realization.generateAllRealizations)
:   Generates all unique realizations as a `Score`.

    Warning

    This method is unoptimized, and may take a prohibitive amount
    of time for a Realization which has more than 100 solutions.

Realization.generateRandomRealization()[[source]](../_modules/music21/figuredBass/realizer.html#Realization.generateRandomRealization)
:   Generates a random unique realization as a `Score`.

Realization.generateRandomRealizations(*amountToGenerate=20*)[[source]](../_modules/music21/figuredBass/realizer.html#Realization.generateRandomRealizations)
:   Generates *amountToGenerate* unique realizations as a `Score`.

    Warning

    This method is unoptimized, and may take a prohibitive amount
    of time if amountToGenerate is more than 100.

Realization.generateRealizationFromPossibilityProgression(*possibilityProgression*)[[source]](../_modules/music21/figuredBass/realizer.html#Realization.generateRealizationFromPossibilityProgression)
:   Generates a realization as a `Score` given a possibility progression.

Realization.getAllPossibilityProgressions()[[source]](../_modules/music21/figuredBass/realizer.html#Realization.getAllPossibilityProgressions)
:   Compiles each unique possibility progression, adding
    it to a master list. Returns the master list.

    Warning

    This method is unoptimized, and may take a prohibitive amount
    of time for a Realization which has more than 200,000 solutions.

Realization.getNumSolutions()[[source]](../_modules/music21/figuredBass/realizer.html#Realization.getNumSolutions)
:   Returns the number of solutions (unique realizations) to a Realization by calculating
    the total number of paths through a string of [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment")
    movements. This is faster and more efficient than compiling each unique realization into a
    list, adding it to a master list, and then taking the length of the master list.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.exampleB()
    >>> fbRealization = fbLine.realize()
    >>> fbRealization.getNumSolutions()
    422
    >>> fbLine2 = examples.exampleC()
    >>> fbRealization2 = fbLine2.realize()
    >>> fbRealization2.getNumSolutions()
    833
    ```

Realization.getRandomPossibilityProgression()[[source]](../_modules/music21/figuredBass/realizer.html#Realization.getRandomPossibilityProgression)
:   Returns a random unique possibility progression.

[`Realization`](#music21.figuredBass.realizer.Realization "music21.figuredBass.realizer.Realization") instance variables

Realization.keyboardStyleOutput
:   True by default. If True, generated realizations
    are represented in keyboard style, with two staves. If False,
    realizations are represented in chorale style with n staves,
    where n is the number of parts. SATB if n = 4.

## Functions

music21.figuredBass.realizer.figuredBassFromStream(*streamPart: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*) → [FiguredBassLine](#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine")[[source]](../_modules/music21/figuredBass/realizer.html#figuredBassFromStream)
:   Takes a `Part` (or another `Stream` subclass)
    and returns a [`FiguredBassLine`](#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine") object whose bass notes
    have notations taken from the lyrics in the source stream. This method along with the
    [`realize()`](#music21.figuredBass.realizer.FiguredBassLine.realize "music21.figuredBass.realizer.FiguredBassLine.realize") method provide the easiest
    way of converting from a notated version of a figured bass (such as in a MusicXML file) to
    a realized version of the same line.

    ```python
    >>> s = converter.parse('tinynotation: 4/4 C4 D8_6 E8_6 F4 G4_7 c1', makeNotation=False)
    >>> fb = figuredBass.realizer.figuredBassFromStream(s)
    >>> fb
    <music21.figuredBass.realizer.FiguredBassLine object at 0x...>
    ```

    ```python
    >>> fbRules = figuredBass.rules.Rules()
    >>> fbRules.partMovementLimits = [(1, 2), (2, 12), (3, 12)]
    >>> fbRealization = fb.realize(fbRules)
    >>> fbRealization.getNumSolutions()
    13
    >>> fbRealization.generateRandomRealizations(8).show()
    ```

    [![../_images/fbRealizer_fbStreamPart.png](../_images/fbRealizer_fbStreamPart.png)](../_images/fbRealizer_fbStreamPart.png)

    * Changed in v7.3: multiple figures in same lyric (e.g. ‘64’) now supported.

music21.figuredBass.realizer.addLyricsToBassNote(*bassNote*, *notationString=None*)[[source]](../_modules/music21/figuredBass/realizer.html#addLyricsToBassNote)
:   Takes in a bassNote and a corresponding notationString as arguments.
    Adds the parsed notationString as lyrics to the bassNote, which is
    useful when displaying the figured bass in external software.

    ```python
    >>> from music21.figuredBass import realizer
    >>> n1 = note.Note('G3')
    >>> realizer.addLyricsToBassNote(n1, '6,4')
    >>> n1.lyrics[0].text
    '6'
    >>> n1.lyrics[1].text
    '4'
    >>> n1.show()
    ```

    [![../_images/fbRealizer_lyrics.png](../_images/fbRealizer_lyrics.png)](../_images/fbRealizer_lyrics.png)
