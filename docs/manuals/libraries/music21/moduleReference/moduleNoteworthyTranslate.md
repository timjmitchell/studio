Source: https://music21.org/music21docs/moduleReference/moduleNoteworthyTranslate.html

# music21.noteworthy.translate

Module to translate Noteworthy Composer’s NWCTXT format to music21.

## NoteworthyTranslator

class music21.noteworthy.translate.NoteworthyTranslator[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator)
:   stores all the data about the current parse context (whether we’re in a slur, tuplet, etc.)

[`NoteworthyTranslator`](#music21.noteworthy.translate.NoteworthyTranslator "music21.noteworthy.translate.NoteworthyTranslator") methods

NoteworthyTranslator.createBarlines(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createBarlines)
:   Translates bar lines into music21.

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentPart = stream.Part()
    >>> nwt.currentMeasure = stream.Measure()
    >>> nwt.createBarlines({'Style':'MasterRepeatOpen'})
    >>> nwt.currentMeasure
    <music21.stream.Measure 0 offset=0.0>
    >>> nwt.currentMeasure.leftBarline
    <music21.bar.Repeat direction=start>
    ```

NoteworthyTranslator.createClef(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createClef)
:   Add a new clef to the current measure and return the currentClef.

    Clef lines should look like: |Clef|Type:ClefType or
    |Clef|Type:ClefType|OctaveShift:Octave Down (or Up)

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = stream.Measure()
    >>> nwt.createClef({'Type': 'Treble'})
    >>> nwt.currentMeasure.show('text')
    {0.0} <music21.clef.TrebleClef>
    >>> nwt.currentClef
    'TREBLE'
    >>> nwt.createClef({'Type' : 'Bass', 'OctaveShift' : 'Octave Down'})
    >>> nwt.currentMeasure.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.clef.Bass8vbClef>
    >>> nwt.createClef({'Type' : 'Percussion'})
    >>> nwt.currentMeasure.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.clef.Bass8vbClef>
    {0.0} <music21.clef.PercussionClef>
    ```

    If no clef can be found then it raises a NoteworthyTranslate exception

    ```python
    >>> nwt.createClef({'Type' : 'OrangeClef'})
    Traceback (most recent call last):
    music21.noteworthy.translate.NoteworthyTranslateException: Did
        not find a proper clef in type, OrangeClef
    ```

NoteworthyTranslator.createDynamicVariance(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createDynamicVariance)
:   Adding dynamics like “crescendo” to the measure.

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = stream.Measure()
    >>> nwt.createDynamicVariance({'Style' : 'Crescendo', 'Pos': '-6'})
    >>> nwt.currentMeasure.show('text')
    {0.0} <music21.dynamics.Crescendo>
    ```

NoteworthyTranslator.createDynamics(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createDynamics)
:   Adding dynamics like “fff”, “pp”, … to the measure.

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = stream.Measure()
    >>> nwt.createDynamics({'Style': 'fff', 'Pos': '-8'})
    >>> nwt.currentMeasure[0]
    <music21.dynamics.Dynamic fff>
    ```

NoteworthyTranslator.createEnding(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createEnding)

NoteworthyTranslator.createKey(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createKey)
:   Adds a new key signature to the given measure.
    Returns the number of sharps (negative for flats)

    ```python
    >>> measureIn = stream.Measure()
    >>> measureIn.append(note.Rest(quarterLength=3.0))
    ```

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = measureIn
    >>> nwt.createKey({'Signature':'F#,C#,G#,D#'})
    >>> nwt.currentKey.sharps
    4
    >>> measureIn.show('text')
    {0.0} <music21.note.Rest dotted-half>
    {3.0} <music21.key.KeySignature of 4 sharps>
    ```

NoteworthyTranslator.createLyrics(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createLyrics)
:   Get a list of lyrics from a Lyric line

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> lyricsList = nwt.createLyrics({'Text': '"Hello world"'})
    >>> lyricsList[0]
    'Hello'
    ```

NoteworthyTranslator.createOtherRepetitions(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createOtherRepetitions)
:   Repetitions like ‘Coda’, ‘Segno’ and some others.

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = stream.Measure()
    >>> nwt.createOtherRepetitions({'Style' : 'ToCoda', 'Pos': '8',
    ...                             'Wide':'Y', 'Placement': 'BestFitForward'})
    >>> isinstance(nwt.currentMeasure[0], repeat.Coda)
    True
    ```

NoteworthyTranslator.createPart()[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createPart)
:   Add a new part to the score.

NoteworthyTranslator.createSongInfo(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createSongInfo)

NoteworthyTranslator.createStaff(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createStaff)

NoteworthyTranslator.createStaffInstrument(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createStaffInstrument)

NoteworthyTranslator.createTempo(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createTempo)

NoteworthyTranslator.createText(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createText)

NoteworthyTranslator.createTimeSignature(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.createTimeSignature)
:   Adding a time signature in the score.

    ```python
    >>> measure = stream.Measure()
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = measure
    >>> nwt.createTimeSignature({'Signature':'4/4'})
    >>> measure[0]
    <music21.meter.TimeSignature 4/4>
    ```

NoteworthyTranslator.getMultiplePitchesFromPositionInfo(*posInfo*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.getMultiplePitchesFromPositionInfo)
:   returns a list of pitch objects given the Pos:… info
    for a chord.

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentClef = 'BASS'
    >>> pList = nwt.getMultiplePitchesFromPositionInfo('1,b3,5^')
    >>> pList
    [<music21.pitch.Pitch E3>, <music21.pitch.Pitch G-3>, <music21.pitch.Pitch B3>]
    ```

NoteworthyTranslator.getOnePitchFromPosition(*pos*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.getOnePitchFromPosition)
:   Get one pitch from a position:

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentClef = 'BASS'
    >>> p = nwt.getOnePitchFromPosition('b3')
    >>> p
    <music21.pitch.Pitch G-3>
    >>> p.ps
    54.0
    ```

NoteworthyTranslator.getPitchFromPositionInfo(*posInfo*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.getPitchFromPositionInfo)
:   returns a pitch object given the Pos: info

    removes ties and alteration signs. Otherwise
    is same as getOnePitchFromPosition()

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentClef = 'BASS'
    >>> p = nwt.getPitchFromPositionInfo('b3^')  # removes ties
    >>> p
    <music21.pitch.Pitch G-3>
    ```

NoteworthyTranslator.getShortestStream()[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.getShortestStream)

NoteworthyTranslator.getStepAndOctaveFromPosition(*positionNote*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.getStepAndOctaveFromPosition)
:   Given an int representing the position on the staff for the
    current clef,
    returns a string for the step and an int for the octave

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentClef = 'BASS'
    >>> (step, octave) = nwt.getStepAndOctaveFromPosition(3)
    >>> (step, octave)
    ('G', 3)
    ```

NoteworthyTranslator.parseFile(*filePath*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.parseFile)

NoteworthyTranslator.parseList(*dataList*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.parseList)
:   Parses a list where each element is a line from a nwctxt file.

    Returns a `Score` object

    ```python
    >>> data = []
    >>> data.append('!NoteWorthyComposer(2.0)\n')
    >>> data.append('|AddStaff|\n')
    >>> data.append('|Clef|Type:Bass\n')
    >>> data.append('|TimeSig|Signature:4/4\n')
    >>> data.append('|Note|Dur:Whole|Pos:1\n')
    ```

    ```python
    >>>
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> s = nwt.parseList(data)
    >>> s.show('text')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note E>
    ```

NoteworthyTranslator.parseString(*data*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.parseString)

NoteworthyTranslator.setDurationForObject(*generalNote*, *durationInfo*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.setDurationForObject)
:   generalNote could be a Note, Chord, or Rest

    DurationInfo is a string like:

    > Whole,Dotted,Slur

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> n = note.Note()
    >>> nwt.setDurationForObject(n, 'Half')
    >>> n.duration
    <music21.duration.Duration 2.0>
    ```

NoteworthyTranslator.setTieFromPitchInfo(*noteOrChord*, *pitchInfo*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.setTieFromPitchInfo)
:   sets the tie status for a noteOrChord from the pitchInfo

NoteworthyTranslator.translateChord(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.translateChord)
:   Translation of a music21 chord from a NWC one.

    ```python
    >>> measure = stream.Measure()
    ```

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = measure
    >>> nwt.translateChord({'Dur': ['Half'], 'Pos': ['1,3,#5']})
    >>> measure[0]
    <music21.chord.Chord C5 E5 G#5>
    ```

    Chords also inherit accidentals:
    >>> nwt.translateChord({‘Dur’: [‘Half’], ‘Pos’: [‘1,3,5’]})
    >>> measure[1]
    <music21.chord.Chord C5 E5 G#5>

NoteworthyTranslator.translateNote(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.translateNote)
:   Translation of a music21 note from a NWC note.

    ```python
    >>> measure = stream.Measure()
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = measure
    >>> nwt.translateNote({'Dur': 'Half', 'Pos': '#-3'})
    >>> measure[0]
    <music21.note.Note F#>
    ```

    Note that the next note in the measure with the same position should
    inherit the last position’s accidental:

    ```python
    >>> nwt.translateNote({'Dur': 'Half', 'Pos': '-3'})
    >>> measure[1]
    <music21.note.Note F#>
    ```

NoteworthyTranslator.translateRest(*attributes*)[[source]](../_modules/music21/noteworthy/translate.html#NoteworthyTranslator.translateRest)
:   Translation of a music21 rest. Adds the rest to the given measure.

    ```python
    >>> measureIn = stream.Measure()
    >>> measureIn.append(note.Note('C#4', type='half'))
    ```

    ```python
    >>> nwt = noteworthy.translate.NoteworthyTranslator()
    >>> nwt.currentMeasure = measureIn
    >>> nwt.translateRest({'Dur': '8th,Dotted'})
    >>> nwt.translateRest({'Dur': '4th'})
    >>> measureIn.show('text')
    {0.0} <music21.note.Note C#>
    {2.0} <music21.note.Rest dotted-eighth>
    {2.75} <music21.note.Rest quarter>
    ```
