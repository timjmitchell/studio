Source: https://music21.org/music21docs/moduleReference/moduleStreamMakeNotation.html

# music21.stream.makeNotation

## Functions

music21.stream.makeNotation.consolidateCompletedTuplets(*s: stream.Stream*, *\**, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *onlyIfTied: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#consolidateCompletedTuplets)
:   Locate consecutive notes or rests in s (or its substreams if recurse is True)
    that are unnecessarily expressed as tuplets and replace them with a single
    element. These groups must:

    > * be consecutive (with respect to [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote") objects)
    > * be all rests, or all `pitches`
    > * all have [`expressionIsInferred`](moduleDuration.html#music21.duration.Duration.expressionIsInferred "music21.duration.Duration.expressionIsInferred") = True.
    > * not begin during a tuplet
    > * sum to the tuplet’s total length
    > * if NotRest, all must be tied (if onlyIfTied is True)

    The groups are consolidated by prolonging the first note or rest in the group
    and removing the subsequent elements from the stream. (Destructive edit,
    so make a copy first if desired.)

    * New in v8.

    ```python
    >>> s = stream.Stream()
    >>> r = note.Rest(quarterLength=1/6)
    >>> s.repeatAppend(r, 5)
    >>> s.insert(5/6, note.Note(duration=r.duration))
    >>> from music21.stream.makeNotation import consolidateCompletedTuplets
    >>> consolidateCompletedTuplets(s)
    >>> [el.quarterLength for el in s.notesAndRests]
    [0.5, Fraction(1, 6), Fraction(1, 6), Fraction(1, 6)]
    ```

    onlyIfTied is True by default:

    ```python
    >>> s2 = stream.Stream()
    >>> n = note.Note(quarterLength=1/3)
    >>> s2.repeatAppend(n, 3)
    >>> consolidateCompletedTuplets(s)
    >>> [el.quarterLength for el in s2.notesAndRests]
    [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
    ```

    ```python
    >>> consolidateCompletedTuplets(s2, onlyIfTied=False)
    >>> [el.quarterLength for el in s2.notesAndRests]
    [1.0]
    ```

    Does nothing if tuplet definitions are not the same. (In which case, see
    [`TupletFixer`](moduleDuration.html#music21.duration.TupletFixer "music21.duration.TupletFixer") instead).

    ```python
    >>> s3 = stream.Stream([note.Rest(quarterLength=1/3), note.Rest(quarterLength=1/6)])
    >>> for my_rest in s3.notesAndRests:
    ...   print(my_rest.duration.tuplets)
    (<music21.duration.Tuplet 3/2/eighth>,)
    (<music21.duration.Tuplet 3/2/16th>,)
    >>> consolidateCompletedTuplets(s)
    >>> [el.quarterLength for el in s3.notesAndRests]
    [Fraction(1, 3), Fraction(1, 6)]
    ```

    Does nothing if there are multiple (nested) tuplets.

music21.stream.makeNotation.getTiePitchSet(*prior: [music21.note.NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")*) → [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#getTiePitchSet)
:   helper method for makeAccidentals to get the tie pitch set (or None)
    from the prior

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> n2.tie = tie.Tie('start')
    >>> n3 = note.Note('E4')
    >>> n3.tie = tie.Tie('stop')
    >>> n4 = note.Note('F4')
    >>> n4.tie = tie.Tie('continue')
    >>> c = chord.Chord([n1, n2, n3, n4])
    >>> tps = stream.makeNotation.getTiePitchSet(c)
    >>> isinstance(tps, set)
    True
    >>> sorted(tps)
    ['D4', 'F4']
    ```

    Non tie possessing objects return None

    ```python
    >>> r = bar.Repeat()
    >>> stream.makeNotation.getTiePitchSet(r) is None
    True
    ```

    Note or Chord without ties, returns an empty set:

    ```python
    >>> n = note.Note('F#5')
    >>> stream.makeNotation.getTiePitchSet(n)
    set()
    ```

    ```python
    >>> pChord = percussion.PercussionChord([note.Unpitched('D4'), note.Note('E5')])
    >>> stream.makeNotation.getTiePitchSet(pChord)
    set()
    ```

    Rest returns None

    ```python
    >>> r = note.Rest()
    >>> stream.makeNotation.getTiePitchSet(r) is None
    True
    ```

music21.stream.makeNotation.iterateBeamGroups(*s: StreamType*, *skipNoBeams=True*, *recurse=True*) → [Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/stream/makeNotation.html#iterateBeamGroups)
:   Generator that yields a List of NotRest objects that fall within a beam group.

    If skipNoBeams is True, then NotRest objects that have no beams are skipped.

    Recurse is True by default.

    Unclosed beam groups (like start followed by a Rest before a stop), currently
    will continue to yield until the first stop, but this behavior may change at any time in
    the future as beaming-over-barlines with multiple voices or beaming across
    Parts or PartStaffs is supported.

    ```python
    >>> from music21.stream.makeNotation import iterateBeamGroups
    >>> sc = converter.parse('tinyNotation: 3/4 c8 d e f g4   a4 b8 a16 g16 f4')
    >>> sc.makeBeams(inPlace=True)
    >>> for beamGroup in iterateBeamGroups(sc):
    ...     print(beamGroup)
    [<music21.note.Note C>, <music21.note.Note D>]
    [<music21.note.Note E>, <music21.note.Note F>]
    [<music21.note.Note B>, <music21.note.Note A>, <music21.note.Note G>]
    ```

    ```python
    >>> for beamGroup in iterateBeamGroups(sc, skipNoBeams=False):
    ...     print(beamGroup)
    [<music21.note.Note C>, <music21.note.Note D>]
    [<music21.note.Note E>, <music21.note.Note F>]
    [<music21.note.Note G>]
    [<music21.note.Note A>]
    [<music21.note.Note B>, <music21.note.Note A>, <music21.note.Note G>]
    [<music21.note.Note F>]
    ```

    If recurse is False, assumes a flat Score:

    ```python
    >>> for beamGroup in iterateBeamGroups(sc, recurse=False):
    ...     print(beamGroup)
    ```

    ```python
    >>> for beamGroup in iterateBeamGroups(sc.flatten(), recurse=False):
    ...     print(beamGroup)
    [<music21.note.Note C>, <music21.note.Note D>]
    [<music21.note.Note E>, <music21.note.Note F>]
    [<music21.note.Note B>, <music21.note.Note A>, <music21.note.Note G>]
    ```

    * New in v6.7.

music21.stream.makeNotation.makeAccidentalsInMeasureStream(*s: StreamType | [StreamIterator](moduleStreamIterator.html#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")*, *\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *useKeySignature: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") = True*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *tiePitchSet: [set](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#makeAccidentalsInMeasureStream)
:   Makes accidentals in place on a stream that contains Measures.
    Helper for Stream.makeNotation and Part.makeAccidentals.

    The function walks measures in order to update the values for the following keyword
    arguments of `makeAccidentals()` and calls
    that method on each Measure. (For this reason, the values supplied
    for these arguments in the method signature will be used on the first
    measure only, or in the case of useKeySignature, not at all if the first
    measure contains a KeySignature.):

    ```python
    pitchPastMeasure
    useKeySignature
    tiePitchSet
    ```

    Operates on the measures in place; make a copy first if this is not desired.

    * Changed in v8: the Stream may have other elements besides measures and the method
      :   will still work.

music21.stream.makeNotation.makeBeams(*s: StreamType*, *\**, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *setStemDirections: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *failOnNoTimeSignature: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → StreamType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#makeBeams)
:   Return a new Measure, or Stream of Measures, with beams applied to all
    notes. Measures with Voices will process voices independently.

    Note that makeBeams() is automatically called in show(‘musicxml’) and
    other formats if there is no beaming information in the piece (see
    haveBeamsBeenMade).

    If inPlace is True, this is done in-place; if inPlace is False,
    this returns a modified deep copy.

    Note

    Before Version 1.6, inPlace default was True; now False
    like most inPlace options in music21. Also, in 1.8, no tuplets are made
    automatically. Use makeTupletBrackets()

    See `getBeams()` for the algorithm used.

    ```python
    >>> aMeasure = stream.Measure()
    >>> aMeasure.timeSignature = meter.TimeSignature('4/4')
    >>> aNote = note.Note()
    >>> aNote.quarterLength = 0.25
    >>> aMeasure.repeatAppend(aNote, 16)
    >>> bMeasure = aMeasure.makeBeams(inPlace=False)
    ```

    ```python
    >>> for i in range(4):
    ...   print(f'{i} {bMeasure.notes[i].beams!r}')
    0 <music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>
    1 <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/stop>>
    2 <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/start>>
    3 <music21.beam.Beams <music21.beam.Beam 1/stop>/<music21.beam.Beam 2/stop>>
    ```

    This was formerly a bug – we could not have a partial-left beam at the start of a
    beam group. Now merges across the archetypeSpan

    ```python
    >>> aMeasure = stream.Measure()
    >>> aMeasure.timeSignature = meter.TimeSignature('4/4')
    >>> for i in range(4):
    ...     aMeasure.append(note.Rest(quarterLength=0.25))
    ...     aMeasure.repeatAppend(note.Note('C4', quarterLength=0.25), 3)
    >>> bMeasure = aMeasure.makeBeams(inPlace=False).notes
    >>> for i in range(6):
    ...   print(f'{i} {bMeasure[i].beams!r}')
    0 <music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>
    1 <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/continue>>
    2 <music21.beam.Beams <music21.beam.Beam 1/stop>/<music21.beam.Beam 2/stop>>
    3 <music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>
    4 <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/continue>>
    5 <music21.beam.Beams <music21.beam.Beam 1/stop>/<music21.beam.Beam 2/stop>>
    ```

    Grace notes no longer interfere with beaming:

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('3/4')
    >>> m.repeatAppend(note.Note(quarterLength=0.25), 4)
    >>> m.repeatAppend(note.Rest(), 2)
    >>> gn = note.Note(duration=duration.GraceDuration())
    >>> m.insert(0.25, gn)
    >>> m.makeBeams(inPlace=True)
    >>> [n.beams for n in m.notes]
    [<music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>,
    <music21.beam.Beams>,
    <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/stop>>,
    <music21.beam.Beams <music21.beam.Beam 1/continue>/<music21.beam.Beam 2/start>>,
    <music21.beam.Beams <music21.beam.Beam 1/stop>/<music21.beam.Beam 2/stop>>]
    ```

music21.stream.makeNotation.makeMeasures(*s: StreamType*, *\**, *meterStream=None*, *refStreamOrTimeRange=None*, *searchContext=False*, *innerBarline=None*, *finalBarline='final'*, *bestClef=False*, *inPlace=False*) → StreamType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#makeMeasures)
:   Takes a stream and places all of its elements into
    measures (`Measure` objects)
    based on the `TimeSignature` objects
    placed within
    the stream. If no TimeSignatures are found in the
    stream, a default of 4/4 is used.

    If inPlace is True, the original Stream is modified and lost
    if inPlace is False, this returns a modified deep copy.

    Many advanced features are available:

    (1) If a meterStream is given, the TimeSignatures in this
    stream are used instead of any found in the Stream.
    Alternatively, a single TimeSignature object
    can be provided in lieu of the stream. This feature lets you
    test out how a group of notes might be interpreted as measures
    in a number of different metrical schemes.

    (2) If refStreamOrTimeRange is provided, this Stream or List
    is used to give the span that you want to make measures as
    necessary to fill empty rests at the ends or beginnings of
    Streams, etc. Say for instance you’d like to make a complete
    score from a short ossia section, then you might use another
    Part from the Score as a refStreamOrTimeRange to make sure
    that the appropriate measures of rests are added at either side.

    (3) If innerBarline is not None, the specified Barline object
    or string-specification of Barline style will be used to create
    Barline objects between every created Measure. The default is None.

    (4) If finalBarline is not None, the specified Barline object or
    string-specification of Barline style will be used to create a Barline
    objects at the end of the last Measure. The default is ‘final’.

    The searchContext parameter determines whether context
    searches are used to find Clef and other notation objects.

    Here is a simple example of makeMeasures:

    A single measure of 4/4 is created from a Stream
    containing only three quarter notes:

    ```python
    >>> sSrc = stream.Stream()
    >>> sSrc.append(note.Note('C4', type='quarter'))
    >>> sSrc.append(note.Note('D4', type='quarter'))
    >>> sSrc.append(note.Note('E4', type='quarter'))
    >>> sMeasures = sSrc.makeMeasures()
    >>> sMeasures.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=final>
    ```

    Notice that the last measure is incomplete – makeMeasures
    does not fill up incomplete measures.

    We can also check that the measure created has
    the correct TimeSignature:

    ```python
    >>> sMeasures[0].timeSignature
    <music21.meter.TimeSignature 4/4>
    ```

    Now let’s redo this work in 2/4 by putting a TimeSignature
    of 2/4 at the beginning of the stream and rerunning
    makeMeasures. Now we will have two measures, each with
    correct measure numbers:

    ```python
    >>> sSrc.insert(0.0, meter.TimeSignature('2/4'))
    >>> sMeasuresTwoFour = sSrc.makeMeasures()
    >>> sMeasuresTwoFour.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
    {2.0} <music21.stream.Measure 2 offset=2.0>
        {0.0} <music21.note.Note E>
        {1.0} <music21.bar.Barline type=final>
    ```

    Let us put 10 quarter notes in a Part.

    ```python
    >>> sSrc = stream.Part()
    >>> n = note.Note('E-4')
    >>> n.quarterLength = 1
    >>> sSrc.repeatAppend(n, 10)
    ```

    After we run makeMeasures, we will have
    3 measures of 4/4 in a new Part object. This experiment
    demonstrates that running makeMeasures does not
    change the type of Stream you are using:

    ```python
    >>> sMeasures = sSrc.makeMeasures()
    >>> len(sMeasures.getElementsByClass(stream.Measure))
    3
    >>> sMeasures.__class__.__name__
    'Part'
    ```

    Demonstrate what makeMeasures will do with inPlace = True:

    ```python
    >>> sScr = stream.Score()
    >>> sPart = stream.Part()
    >>> sPart.insert(0, clef.TrebleClef())
    >>> sPart.insert(0, meter.TimeSignature('3/4'))
    >>> sPart.append(note.Note('C4', quarterLength = 3.0))
    >>> sPart.append(note.Note('D4', quarterLength = 3.0))
    >>> sScr.insert(0, sPart)
    >>> sScr.makeMeasures(inPlace=True)
    >>> sScr.show('text')
    {0.0} <music21.stream.Part 0x...>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 3/4>
            {0.0} <music21.note.Note C>
        {3.0} <music21.stream.Measure 2 offset=3.0>
            {0.0} <music21.note.Note D>
            {3.0} <music21.bar.Barline type=final>
    ```

    If after running makeMeasures you run makeTies, it will also split
    long notes into smaller notes with ties. Lyrics and articulations
    are attached to the first note. Expressions (fermatas,
    etc.) will soon be attached to the last note but this is not yet done:

    ```python
    >>> p1 = stream.Part()
    >>> p1.append(meter.TimeSignature('3/4'))
    >>> longNote = note.Note('D#4')
    >>> longNote.quarterLength = 7.5
    >>> longNote.articulations = [articulations.Staccato()]
    >>> longNote.lyric = 'hi'
    >>> p1.append(longNote)
    >>> partWithMeasures = p1.makeMeasures()
    >>> partWithMeasures is not p1
    True
    >>> dummy = partWithMeasures.makeTies(inPlace=True)
    >>> partWithMeasures.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note D#>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.note.Note D#>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.0} <music21.note.Note D#>
        {1.5} <music21.bar.Barline type=final>
    ```

    ```python
    >>> allNotes = partWithMeasures.flatten().notes
    >>> allNotes[0].articulations
    []
    ```

    ```python
    >>> allNotes[1].articulations
    []
    ```

    ```python
    >>> allNotes[2].articulations
    [<music21.articulations.Staccato>]
    ```

    ```python
    >>> [allNotes[0].lyric, allNotes[1].lyric, allNotes[2].lyric]
    ['hi', None, None]
    ```

    * Changed in v6: all but first attribute are keyword only
    * Changed in v7: now safe to call makeMeasures directly on a score containing parts

music21.stream.makeNotation.makeOrnamentalAccidentals(*noteOrChord: [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*, *\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/stream/makeNotation.html#makeOrnamentalAccidentals)
:   Makes accidentals for the ornamental pitches for any Ornaments on noteOrChord.
    This is very similar to the processing in pitch.updateAccidentalDisplay, except
    that there is no tie processing, since ornamental pitches cannot be tied.

music21.stream.makeNotation.makeRests(*s: StreamType*, *\**, *refStreamOrTimeRange=None*, *fillGaps=False*, *timeRangeFromBarDuration=False*, *inPlace=False*, *hideRests=False*) → StreamType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#makeRests)
:   Given a Stream with an offset not equal to zero,
    fill with one Rest preceding this offset.
    This can be called on any Stream,
    a Measure alone, or a Measure that contains
    Voices. This method recurses into Parts, Measures, and Voices,
    since users are unlikely to want “loose” rests outside sub-containers.

    If refStreamOrTimeRange is provided as a Stream, this
    Stream is used to get min and max offsets. If a list is provided,
    the list assumed to provide minimum and maximum offsets. Rests will
    be added to fill all time defined within refStream.

    If fillGaps is True, this will create rests in any
    time regions that have no active elements.

    If timeRangeFromBarDuration is True, and the calling Stream
    is a Measure with a TimeSignature (or a Part containing them),
    the time range will be determined
    by taking the `barDuration()` and subtracting
    `paddingLeft` and
    `paddingRight`.
    This keyword takes priority over refStreamOrTimeRange.
    If both are provided, timeRangeFromBarDuration
    prevails, unless no TimeSignature can be found, in which case, the function
    falls back to refStreamOrTimeRange.

    If inPlace is True, this is done in-place; if inPlace is False,
    this returns a modified deepcopy.

    ```python
    >>> a = stream.Stream()
    >>> a.insert(20, note.Note())
    >>> len(a)
    1
    >>> a.lowestOffset
    20.0
    >>> a.show('text')
    {20.0} <music21.note.Note C>
    ```

    Now make some rests:

    ```python
    >>> b = a.makeRests(inPlace=False)
    >>> len(b)
    2
    >>> b.lowestOffset
    0.0
    >>> b.show('text')
    {0.0} <music21.note.Rest 20ql>
    {20.0} <music21.note.Note C>
    >>> b[0].duration.quarterLength
    20.0
    ```

    Same thing, but this time, with gaps, and hidden rests:

    ```python
    >>> a = stream.Stream()
    >>> a.insert(20, note.Note('C4'))
    >>> a.insert(30, note.Note('D4'))
    >>> len(a)
    2
    >>> a.lowestOffset
    20.0
    >>> a.show('text')
    {20.0} <music21.note.Note C>
    {30.0} <music21.note.Note D>
    >>> b = a.makeRests(fillGaps=True, inPlace=False, hideRests=True)
    >>> len(b)
    4
    >>> b.lowestOffset
    0.0
    >>> b.show('text')
    {0.0} <music21.note.Rest 20ql>
    {20.0} <music21.note.Note C>
    {21.0} <music21.note.Rest 9ql>
    {30.0} <music21.note.Note D>
    >>> b[0].style.hideObjectOnPrint
    True
    ```

    Now with measures:

    ```python
    >>> a = stream.Part()
    >>> a.insert(4, note.Note('C4'))
    >>> a.insert(8, note.Note('D4'))
    >>> len(a)
    2
    >>> a.lowestOffset
    4.0
    >>> a.insert(0, meter.TimeSignature('4/4'))
    >>> a.makeMeasures(inPlace=True)
    >>> a.show('text', addEndTimes=True)
    {0.0 - 0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0 - 0.0} <music21.clef.TrebleClef>
        {0.0 - 0.0} <music21.meter.TimeSignature 4/4>
    {4.0 - 5.0} <music21.stream.Measure 2 offset=4.0>
        {0.0 - 1.0} <music21.note.Note C>
    {8.0 - 9.0} <music21.stream.Measure 3 offset=8.0>
        {0.0 - 1.0} <music21.note.Note D>
        {1.0 - 1.0} <music21.bar.Barline type=final>
    >>> a.makeRests(fillGaps=True, inPlace=True)
    >>> a.show('text', addEndTimes=True)
    {0.0 - 4.0} <music21.stream.Measure 1 offset=0.0>
        {0.0 - 0.0} <music21.clef.TrebleClef>
        {0.0 - 0.0} <music21.meter.TimeSignature 4/4>
        {0.0 - 4.0} <music21.note.Rest whole>
    {4.0 - 8.0} <music21.stream.Measure 2 offset=4.0>
        {0.0 - 1.0} <music21.note.Note C>
        {1.0 - 4.0} <music21.note.Rest dotted-half>
    {8.0 - 12.0} <music21.stream.Measure 3 offset=8.0>
        {0.0 - 1.0} <music21.note.Note D>
        {1.0 - 4.0} <music21.note.Rest dotted-half>
        {4.0 - 4.0} <music21.bar.Barline type=final>
    ```

    * Changed in v6: all but first attribute are keyword only
    * Changed in v7:
      - inPlace defaults False
      - Recurses into parts, measures, voices
      - Gave priority to timeRangeFromBarDuration over refStreamOrTimeRange
    * Changed in v8: scores (or other streams having parts) edited inPlace return None.

music21.stream.makeNotation.makeTies(*s: StreamType*, *\**, *meterStream=None*, *inPlace=False*, *displayTiedAccidentals=False*, *classFilterList=(<class 'music21.note.GeneralNote'>*, *)*) → StreamType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#makeTies)
:   Given a stream containing measures, examine each element in the
    Stream. If the element’s duration extends beyond the measure’s boundary,
    create a tied entity, placing the split Note in the next Measure.

    Note that this method assumes that there is appropriate space in the
    next Measure: this will not shift Note objects, but instead allocate
    them evenly over barlines.

    If inPlace is True, this is done in-place;
    if inPlace is False, this returns a modified deep copy.

    Put a 12-quarter-note-long note into a Stream w/ 4/4 as the duration.

    ```python
    >>> d = stream.Stream()
    >>> d.insert(0, meter.TimeSignature('4/4'))
    >>> n = note.Note('C4')
    >>> n.quarterLength = 12
    >>> d.insert(0, n)
    >>> d.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note C>
    ```

    After running makeMeasures, we get nice measures, a clef, but only one
    way-too-long note in Measure 1:

    ```python
    >>> x = d.makeMeasures()
    >>> x.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
    {4.0} <music21.stream.Measure 2 offset=4.0>

    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.bar.Barline type=final>
    >>> n2 = x.measure(1).notes[0]
    >>> n2.duration.quarterLength
    12.0
    >>> n2 is n
    False
    ```

    But after running makeTies, all is good:

    ```python
    >>> x.makeTies(inPlace=True)
    >>> x.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note C>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note C>
        {4.0} <music21.bar.Barline type=final>
    >>> m = x.measure(1).notes[0]
    >>> m.duration.quarterLength
    4.0
    >>> m is n
    False
    >>> m.tie
    <music21.tie.Tie start>
    >>> x.measure(2).notes[0].tie
    <music21.tie.Tie continue>
    >>> x.measure(3).notes[0].tie
    <music21.tie.Tie stop>
    ```

    Same experiment, but with rests:

    ```python
    >>> d = stream.Stream()
    >>> d.insert(0, meter.TimeSignature('4/4'))
    >>> r = note.Rest()
    >>> r.quarterLength = 12
    >>> d.insert(0, r)
    >>> x = d.makeMeasures()
    >>> x.makeTies(inPlace=True)
    >>> x.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Rest whole>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Rest whole>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Rest whole>
        {4.0} <music21.bar.Barline type=final>
    ```

    Notes: uses base.Music21Object.splitAtQuarterLength() once it has figured out
    what to split.

    * Changed in v4: inPlace = False by default.
    * Changed in v6: all but first attribute are keyword only
    * New in v7: classFilterList acts as a filter on what elements will
      be operated on (i.e. have durations split and/or ties made.)
      The default (note.GeneralNote,) includes Notes, Chords, and Rests.

    Here will we split and make ties only on Notes, leaving the too-long
    rest in measure 1 alone.

    ```python
    >>> p = stream.Part()
    >>> p.append(meter.TimeSignature('2/4'))
    >>> p.insert(0.0, note.Rest(quarterLength=3.0))
    >>> p.insert(3.0, note.Note(quarterLength=3.0))
    >>> p.makeMeasures(inPlace=True)
    >>> p.makeTies(classFilterList=[note.Note], inPlace=True)
    >>> p.show('text', addEndTimes=True)
    {0.0 - 3.0} <music21.stream.Measure 1 offset=0.0>
        {0.0 - 0.0} <music21.clef.TrebleClef>
        {0.0 - 0.0} <music21.meter.TimeSignature 2/4>
        {0.0 - 3.0} <music21.note.Rest dotted-half>
    {2.0 - 4.0} <music21.stream.Measure 2 offset=2.0>
        {1.0 - 2.0} <music21.note.Note C>
    {4.0 - 6.0} <music21.stream.Measure 3 offset=4.0>
        {0.0 - 2.0} <music21.note.Note C>
        {2.0 - 2.0} <music21.bar.Barline type=final>
    >>> p.measure(3).notes[0].tie
    <music21.tie.Tie stop>
    ```

music21.stream.makeNotation.makeTupletBrackets(*s: StreamType*, *\**, *inPlace=False*) → StreamType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#makeTupletBrackets)
:   Given a flat Stream of mixed durations, designates the first and last tuplet of any group
    of tuplets as the start or end of the tuplet, respectively.

    ```python
    >>> n = note.Note()
    >>> n.duration.quarterLength = 1/3
    >>> s = stream.Stream()
    >>> s.insert(0, meter.TimeSignature('2/4'))
    >>> s.repeatAppend(n, 6)
    >>> tupletTypes = [x.duration.tuplets[0].type for x in s.notes]
    >>> tupletTypes
    [None, None, None, None, None, None]
    >>> stream.makeNotation.makeTupletBrackets(s, inPlace=True)
    >>> tupletTypes = [x.duration.tuplets[0].type for x in s.notes]
    >>> tupletTypes
    ['start', None, 'stop', 'start', None, 'stop']
    ```

    The tuplets must already be coherent. See [`TupletFixer`](moduleDuration.html#music21.duration.TupletFixer "music21.duration.TupletFixer")
    for how to get that set up.

    TODO: does not handle nested tuplets

    * Changed in v1.8: inPlace is False by default
    * Changed in v7: Legacy behavior of taking in a list of durations removed.

music21.stream.makeNotation.moveNotesToVoices(*source: StreamType*, *classFilterList=('GeneralNote',)*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#moveNotesToVoices)
:   Move notes into voices. Happens inplace always. Returns None

music21.stream.makeNotation.ornamentalPitches(*s: StreamType*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/stream/makeNotation.html#ornamentalPitches)
:   Returns all ornamental [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects found in any
    ornaments in notes/chords in the stream (and substreams) as a Python list.

    Very much like the pitches property, except that instead of returning all
    the pitches found in notes and chords, it returns the ornamental pitches
    found in the ornaments on the notes and chords.

    If you want a list of \_all\_ the pitches in a stream, including the ornamental
    pitches, you can call s.pitches and makeNotation.ornamentalPitches(s),
    and then combine the two resulting lists into one big list.

music21.stream.makeNotation.realizeOrnaments(*s: StreamType*) → StreamType[[source]](../_modules/music21/stream/makeNotation.html#realizeOrnaments)
:   Realize all ornaments on a stream

    Creates a new stream that contains all realized ornaments in addition
    to other elements in the original stream.

    ```python
    >>> s1 = stream.Stream()
    >>> m1 = stream.Measure()
    >>> m1.number = 1
    >>> m1.append(meter.TimeSignature('4/4'))
    >>> n1 = note.Note('C4', type='whole')
    >>> n1.expressions.append(expressions.Mordent())
    >>> m1.append(n1)
    >>> m2 = stream.Measure()
    >>> m2.number = 2
    >>> n2 = note.Note('D4', type='whole')
    >>> m2.append(n2)
    >>> s1.append(m1)
    >>> s1.append(m2)
    >>> for x in s1.recurse(includeSelf=True):
    ...     x
    <music21.stream.Stream ...>
    <music21.stream.Measure 1 offset=0.0>
    <music21.meter.TimeSignature 4/4>
    <music21.note.Note C>
    <music21.stream.Measure 2 offset=4.0>
    <music21.note.Note D>
    ```

    ```python
    >>> s2 = stream.makeNotation.realizeOrnaments(s1)
    >>> for x in s2.recurse(includeSelf=True):
    ...     x
    <music21.stream.Stream ...>
    <music21.stream.Measure 1 offset=0.0>
    <music21.meter.TimeSignature 4/4>
    <music21.note.Note C>
    <music21.note.Note B>
    <music21.note.Note C>
    <music21.stream.Measure 2 offset=4.0>
    <music21.note.Note D>
    ```

    TODO: does not work for Gapful streams because it uses append rather
    :   than the offset of the original

music21.stream.makeNotation.saveAccidentalDisplayStatus(*s*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/stream/makeNotation.html#saveAccidentalDisplayStatus)
:   Restore accidental displayStatus on a Stream after an (inPlace) operation
    that sets accidental displayStatus (e.g. a transposition). Note that you
    should not do this unless you know that the displayStatus values will still
    be valid after the operation.

    ```python
    >>> sc = corpus.parse('bwv66.6')
    >>> intv = interval.Interval('P8')
    >>> classList = (key.KeySignature, note.Note)
    >>> with stream.makeNotation.saveAccidentalDisplayStatus(sc):
    ...     sc.transpose(intv, inPlace=True, classFilterList=classList)
    ```

    * New in v9.

music21.stream.makeNotation.setStemDirectionForBeamGroups(*s: StreamType*, *\**, *setNewStems=True*, *overrideConsistentStemDirections=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#setStemDirectionForBeamGroups)
:   Find all beam groups and set all the stemDirection tags for notes/chords
    in a beam group to point either up or down. If any other stem direction is
    encountered (‘double’, ‘noStem’, etc.) that note is skipped.

    If all notes have the same (non-unspecified) direction, then they are left alone unless
    overrideConsistentStemDirections is True (default: False). For instance,
    [`getStemDirectionForPitches()`](moduleClef.html#music21.clef.Clef.getStemDirectionForPitches "music21.clef.Clef.getStemDirectionForPitches") might say “down” but
    if everything in the beamGroup is either

    if setANewStems is True (as by default), then even notes with stemDirection
    of ‘unspecified’ get a stemDirection.

    The method currently assumes that the clef does not change within a beam group. This
    assumption may change in the future without notice.

    Operates in place. Run copy.deepcopy(s) beforehand for a non-inPlace version.

    * New in v6.7.

music21.stream.makeNotation.setStemDirectionOneGroup(*group: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")]*, *\**, *setNewStems=True*, *overrideConsistentStemDirections=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#setStemDirectionOneGroup)
:   Helper function to set stem directions for one beam group (or perhaps a beat, etc.)

    See setStemDirectionForBeamGroups for detailed information.

    * New in v6.7.

music21.stream.makeNotation.splitElementsToCompleteTuplets(*s: stream.Stream*, *\**, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *addTies: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/makeNotation.html#splitElementsToCompleteTuplets)
:   Split notes or rests if doing so will complete any incomplete tuplets.
    The element being split must have a duration that exceeds the
    remainder of the incomplete tuplet.

    The first note is edited; the additional notes are inserted in place.
    (Destructive edit, so make a copy first if desired.)
    Relies on `splitAtQuarterLength()`.

    * New in v8.

    ```python
    >>> from music21.stream.makeNotation import splitElementsToCompleteTuplets
    >>> s = stream.Stream(
    ...    [note.Note(quarterLength=1/3), note.Note(quarterLength=1), note.Note(quarterLength=2/3)]
    ... )
    >>> splitElementsToCompleteTuplets(s)
    >>> [el.quarterLength for el in s.notes]
    [Fraction(1, 3), Fraction(2, 3), Fraction(1, 3), Fraction(2, 3)]
    >>> [el.tie for el in s.notes]
    [None, <music21.tie.Tie start>, <music21.tie.Tie stop>, None]
    ```

    With recurse:

    ```python
    >>> m = stream.Measure([note.Note(quarterLength=1/6)])
    >>> m.insert(5/6, note.Note(quarterLength=1/6))
    >>> m.makeRests(inPlace=True, fillGaps=True)
    >>> p = stream.Part([m])
    >>> splitElementsToCompleteTuplets(p, recurse=True)
    >>> [el.quarterLength for el in p.recurse().notesAndRests]
    [Fraction(1, 6), Fraction(1, 3), Fraction(1, 3), Fraction(1, 6)]
    ```
