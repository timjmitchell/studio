Source: https://music21.org/music21docs/moduleReference/moduleOmrCorrectors.html

# music21.omr.correctors

## MeasureHash

class music21.omr.correctors.MeasureHash(*measureObject=None*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash)
:   Able to do a number of matching, substitution and hashing operations on
    a given measure object

[`MeasureHash`](#music21.omr.correctors.MeasureHash "music21.omr.correctors.MeasureHash") methods

MeasureHash.differenceProbabilityForOneOpCode(*opCodeTuple*, *source*, *destination=None*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.differenceProbabilityForOneOpCode)
:   Given an opCodeTuple and a source, differenceProbabilityForOneOpCode
    returns the difference probability for one type of op-code
    (replace, insert, delete, or equal).
    Here, the destination is in the set F of flagged measures and the
    source is in the set C of correcting measures.
    Source and destination are both hashStrings

    ```python
    >>> source = 'PFPFFF'
    >>> destination = 'PFPFGF'
    >>> ops = ('equal', 0, 4, 0, 4)
    >>> mh = omr.correctors.MeasureHash()
    >>> mh.differenceProbabilityForOneOpCode(ops, source, destination)
    0.8762013031640626
    ```

    Omission

    ```python
    >>> ops2 = ('insert', 4, 4, 4, 5)
    >>> mh2 = omr.correctors.MeasureHash()
    >>> mh2.differenceProbabilityForOneOpCode(ops2, source, destination)
    0.009
    ```

    ```python
    >>> ops3 = ('replace', 2, 4, 2, 4)
    >>> mh3 = omr.correctors.MeasureHash()
    >>> mh3.differenceProbabilityForOneOpCode(ops3, 'PPPPP', 'PPVZP')
    0.0001485
    ```

    Five deletes in a row:

    ```python
    >>> ops4 = ('delete', 0, 5, 0, 0)
    >>> mh3 = omr.correctors.MeasureHash()
    >>> mh3.differenceProbabilityForOneOpCode(ops4, 'e', 'GFPGF')
    1.024e-12
    ```

    Example of Violin II vs. Viola in K525 I, m. 17

    ```python
    >>> vlnII = converter.parse('tinynotation: 4/4 e4 e8. e8 c4 c8 c8').flatten().notes.stream()
    >>> viola = converter.parse('tinynotation: 4/4 c4 c8  c8 A4 A8 A8').flatten().notes.stream()
    >>> vlnIIMH = omr.correctors.MeasureHash(vlnII)
    >>> violaMH = omr.correctors.MeasureHash(viola)
    >>> vlnIIMH.hashString
    'PLFPFF'
    >>> violaMH.hashString
    'PFFPFF'
    >>> opCodes = vlnIIMH.getOpCodes(violaMH.hashString)
    >>> for oc in opCodes:
    ...     prob = vlnIIMH.differenceProbabilityForOneOpCode(
    ...         oc,
    ...         violaMH.hashString,
    ...     )
    ...     print(f'{oc!r:>30} : {prob:.3f}')
             ('equal', 0, 1, 0, 1) : 0.968
           ('replace', 1, 2, 1, 2) : 0.009
             ('equal', 2, 6, 2, 6) : 0.876
    ```

MeasureHash.getHashString()[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getHashString)
:   takes a stream and returns a hashed string for searching on
    and stores it in self.hashString

    If a measure object has multiple voices, use the first voice.

    ```python
    >>> m = stream.Measure()
    >>> m.append(note.Note('C', quarterLength=1.5))
    >>> m.append(note.Note('C', quarterLength=0.5))
    >>> m.append(note.Rest(quarterLength=1.5))
    >>> m.append(note.Note('B', quarterLength=0.5))
    ```

    ```python
    >>> hasher = omr.correctors.MeasureHash(m)
    >>> hasher.getHashString()
    'VFUF'
    >>> hasher.hashString == 'VFUF'
    True
    ```

MeasureHash.getMeasureDifference(*hashString*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getMeasureDifference)
:   Returns the difference ratio between two measures
    b is the “correct” measure that we want to replace the flagged measure with

    Takes a hashString

    ```python
    >>> m = stream.Measure()
    >>> m.append(note.Note('C', quarterLength=1.5))
    >>> m.append(note.Note('C', quarterLength=0.5))
    >>> m.append(note.Rest(quarterLength=1.5))
    >>> m.append(note.Note('B', quarterLength=0.5))
    ```

    ```python
    >>> hasher = omr.correctors.MeasureHash(m)
    >>> hasher.setSequenceMatcher()
    >>> hasher.getMeasureDifference('VGUF')
    0.25
    ```

    ```python
    >>> m = stream.Measure()
    >>> m.append(note.Note('C', quarterLength=1.5))
    >>> m.append(note.Note('C', quarterLength=0.5))
    >>> m.append(note.Rest(quarterLength=1.5))
    >>> m.append(note.Note('B', quarterLength=0.5))
    ```

    ```python
    >>> hasher = omr.correctors.MeasureHash(m)
    >>> hasher.setSequenceMatcher()
    >>> hasher.getMeasureDifference('VFUF')
    1.0
    ```

MeasureHash.getOpCodes(*otherHash=None*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getOpCodes)
:   Gets the opcodes from a simple sequenceMatcher for the current measureHash

    Example of Violin II vs. Viola and Cello in K525 I, m. 17

    ```python
    >>> vlnII = converter.parse('tinynotation: 4/4 e4 e8. e8 c4 c8 c8').flatten().notes.stream()
    >>> viola = converter.parse('tinynotation: 4/4 c4 c8  c8 A4 A8 A8').flatten().notes.stream()
    >>> cello = converter.parse('tinynotation: 4/4 C4 C4     D4 D4   ').flatten().notes.stream()
    >>> vlnII_MH = omr.correctors.MeasureHash(vlnII)
    >>> viola_MH = omr.correctors.MeasureHash(viola)
    >>> cello_MH = omr.correctors.MeasureHash(cello)
    >>> vlnII_MH.getOpCodes(viola_MH.hashString)
    [('equal', 0, 1, 0, 1), ('replace', 1, 2, 1, 2), ('equal', 2, 6, 2, 6)]
    >>> vlnII_MH.getOpCodes(cello_MH.hashString)
    [('equal', 0, 1, 0, 1), ('delete', 1, 3, 1, 1),
     ('equal', 3, 4, 1, 2), ('replace', 4, 6, 2, 4)]
    ```

MeasureHash.getProbabilityBasedOnChanges(*otherHash*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getProbabilityBasedOnChanges)
:   Takes a hash string and gets the probability based on changes.

    ```python
    >>> otherHash = 'e'
    >>> hashString = 'GFPGF'
    >>> mh = omr.correctors.MeasureHash()
    >>> mh.hashString = hashString
    >>> mh.getProbabilityBasedOnChanges(otherHash)
    2.9472832125e-14
    ```

    Example of Violin II vs. Viola and Cello in K525 I, m. 17

    ```python
    >>> vlnII = converter.parse('tinynotation: 4/4 e4 e8. e8 c4 c8 c8').flatten().notes.stream()
    >>> viola = converter.parse('tinynotation: 4/4 c4 c8  c8 A4 A8 A8').flatten().notes.stream()
    >>> cello = converter.parse('tinynotation: 4/4 C4 C4     D4 D4   ').flatten().notes.stream()
    >>> vlnII_MH = omr.correctors.MeasureHash(vlnII)
    >>> viola_MH = omr.correctors.MeasureHash(viola)
    >>> cello_MH = omr.correctors.MeasureHash(cello)
    >>> vlnII_MH.getProbabilityBasedOnChanges(viola_MH.hashString)
    0.0076295...
    >>> vlnII_MH.getProbabilityBasedOnChanges(cello_MH.hashString)
    4.077...e-09
    ```

MeasureHash.getProbabilityFromOneCharSub(*source*, *destination*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getProbabilityFromOneCharSub)
:   Source and destination are strings of one character

    ```python
    >>> mh = omr.correctors.MeasureHash()
    ```

    Eighth note to eighth rest:

    ```python
    >>> mh.getProbabilityFromOneCharSub('F', 'G')
    0.003
    ```

    Eighth note to quarter note:

    ```python
    >>> mh.getProbabilityFromOneCharSub('F', 'P')
    0.0165
    ```

    Eighth note to half note:

    ```python
    >>> mh.getProbabilityFromOneCharSub('F', 'Z')
    0.0002722...
    ```

    Quarter note to dotted quarter note:

    ```python
    >>> mh.getProbabilityFromOneCharSub('P', 'V')
    0.009
    ```

    Dotted quarter note to quarter note:

    ```python
    >>> mh.getProbabilityFromOneCharSub('V', 'P')
    0.004
    ```

    ```python
    >>> mh.getProbabilityFromOneCharSub('A', 'Y')
    3.6e-05
    ```

MeasureHash.getProbabilityOnAddition()[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getProbabilityOnAddition)
:   In order for the source to be correct,
    the destination added a symbol
    Associated with type ‘insert’

    ```python
    >>> omr.correctors.MeasureHash().getProbabilityOnAddition()
    0.004
    ```

MeasureHash.getProbabilityOnEquality()[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getProbabilityOnEquality)
:   Parts or the whole of a string were equal.

    ```python
    >>> omr.correctors.MeasureHash().getProbabilityOnEquality()
    0.9675
    ```

MeasureHash.getProbabilityOnOmission()[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getProbabilityOnOmission)
:   In order for the source to be correct,
    the destination omitted a symbol.
    Associated with type ‘delete’ and in the case of replacement of
    a dotted version of a note with an undotted version (or double dot with dotted, etc.)

    ```python
    >>> omr.correctors.MeasureHash().getProbabilityOnOmission()
    0.009
    ```

MeasureHash.getProbabilityOnSubstitute(*source*, *destination*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.getProbabilityOnSubstitute)
:   Source and destination are measureHash strings
    Source is in set C of correcting measures.
    Destination is in set F of flagged measures.

    (Rossant & Bloch)

    * value change: 50.77% of all errors (inverse: 0.0197)
    * confusions: 9.23% of all errors (inverse: 0.108)
      :   Note: these get the most probability, because they are the rarest
    * omission: 27.69% of all errors (inverse: 0.0361)
    * addition: 12.31% of all errors (inverse: 0.08125)

    ```python
    >>> mh = omr.correctors.MeasureHash()
    ```

    Replacement of eighth note (F) for quarter note (P) = shift of one value:

    ```python
    >>> mh.getProbabilityOnSubstitute('F', 'P')
    0.0165
    ```

    Replacement of eighth note (F) for eighth rest (G) = shift of one type:

    ```python
    >>> mh.getProbabilityOnSubstitute('F', 'G')
    0.003
    ```

    Omission of any symbol, less common so costs more
    The proposed correction assumes that the incorrect measure omitted a symbol

    ```python
    >>> mh.getProbabilityOnSubstitute('', 'P')
    0.009
    ```

    Addition of any symbol, less common so costs more
    The proposed correction assumes that the incorrect measure added a symbol

    ```python
    >>> mh.getProbabilityOnSubstitute('P', '')
    0.004
    ```

    Combination of value shift and an addition:

    ```python
    >>> mh.getProbabilityOnSubstitute('F', 'PP')
    0.0001485
    ```

    Take minimum length. Compare index to index. Any additional letters
    in the flagged measure get graded as additions. Any additional letters
    in the comparison measure get graded as omissions.

MeasureHash.hashGrace(*n*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.hashGrace)
:   Gives a Grace Note a duration of a 128th note

MeasureHash.hashNote(*n*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.hashNote)
:   Encodes a note

    ```python
    >>> hasher = omr.correctors.MeasureHash()
    ```

    ```python
    >>> n = note.Note('C')
    >>> n.duration.type = 'quarter'
    >>> hasher.hashNote(n)
    'P'
    >>> n2 = note.Note('C')
    >>> n2.duration.type = 'half'
    >>> hasher.hashNote(n2)
    'Z'
    >>> n3 = note.Note('C', quarterLength=1.5)
    >>> hasher.hashNote(n3)
    'V'
    ```

MeasureHash.hashQuarterLength(*ql*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.hashQuarterLength)
:   Turns a QuarterLength duration into an integer from 1 to 127

    ```python
    >>> hasher = omr.correctors.MeasureHash()
    >>> hasher.hashQuarterLength(1.0)
    80
    ```

    ```python
    >>> hasher.hashQuarterLength(2.0)
    90
    ```

MeasureHash.hashRest(*r*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.hashRest)
:   Encodes a rest

    ```python
    >>> r = note.Rest(1.0)
    >>> hasher = omr.correctors.MeasureHash()
    >>> hasher.hashRest(r)
    'Q'
    ```

MeasureHash.setSequenceMatcher(*hashes=None*)[[source]](../_modules/music21/omr/correctors.html#MeasureHash.setSequenceMatcher)

## MeasureRelationship

class music21.omr.correctors.MeasureRelationship(*flaggedMeasurePart*, *flaggedMeasureIndex*, *correctMeasurePart*, *correctMeasureIndex*, *correctionProbability*)

## MeasureSlice

class music21.omr.correctors.MeasureSlice(*score*, *i*)[[source]](../_modules/music21/omr/correctors.html#MeasureSlice)
:   represents a single measure from all parts

[`MeasureSlice`](#music21.omr.correctors.MeasureSlice "music21.omr.correctors.MeasureSlice") methods

MeasureSlice.getSliceHashes()[[source]](../_modules/music21/omr/correctors.html#MeasureSlice.getSliceHashes)
:   ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> omrScore = converter.parse(omrPath)
    >>> ssOMR = omr.correctors.ScoreCorrector(omrScore)
    >>> ssOMR
    <music21.omr.correctors.ScoreCorrector object at 0x...>
    >>> measureSlice = ssOMR.getMeasureSlice(2)
    >>> measureSlice
    <music21.omr.correctors.MeasureSlice object at 0x...>
    ```

MeasureSlice.runSliceSearch(*incorrectPartIndex*)[[source]](../_modules/music21/omr/correctors.html#MeasureSlice.runSliceSearch)
:   Takes in an incorrectPartIndex and returns an array
    of the measure indices within the slice that have the
    maximum probability to correct a given flagged measures.

    Returns a namedtuple (MeasureRelationship)

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> omrScore = converter.parse(omrPath)
    >>> ssOMR = omr.correctors.ScoreCorrector(omrScore)
    >>> measureSlice = ssOMR.getMeasureSlice(2)
    >>> measureSlice
    <music21.omr.correctors.MeasureSlice object at 0x...>
    >>> measureSlice.runSliceSearch(1)
    MeasureRelationship(flaggedMeasurePart=1, flaggedMeasureIndex=2,
        correctMeasurePart=3, correctMeasureIndex=2, correctionProbability=0.0054...)
    ```

    ```python
    >>> measureSlice = ssOMR.getMeasureSlice(3)
    >>> measureSlice.runSliceSearch(0)
    MeasureRelationship(flaggedMeasurePart=0,
        flaggedMeasureIndex=3, correctMeasurePart=1, correctMeasureIndex=3,
        correctionProbability=2.41...e-14)
    ```

## PriorsIntegrationScore

class music21.omr.correctors.PriorsIntegrationScore(*total*, *horizontal*, *vertical*, *ignored*)

## ScoreCorrector

class music21.omr.correctors.ScoreCorrector(*score=None*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector)
:   takes in a music21.stream.Score object and runs OMR correction on it.

[`ScoreCorrector`](#music21.omr.correctors.ScoreCorrector "music21.omr.correctors.ScoreCorrector") methods

ScoreCorrector.generateCorrectedScore(*horizontalArray*, *verticalArray*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.generateCorrectedScore)
:   Given two correcting arrays (one from the horizontal model and one from
    the vertical model),
    which offer source measures for each flagged measure in each part,
    this method compares the probabilities of proposed
    source measures for each flagged measure,
    and replaces the flagged measures contents with the more probable source measure
    using substituteOneMeasureContentsForAnother.
    It then rehashes the score so that a new difference comparison can be run.

    Returns a collections.namedtuple of the total number of flagged measures, the total number
    corrected by the horizontal (Prior based on Distance) and the
    vertical (Prior based on Parts)
    methods.

ScoreCorrector.getAllHashes()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.getAllHashes)
:   Returns an array of arrays, each of which is the hashed notes for a part

    ```python
    >>> p1 = stream.Part()
    >>> p1.insert(0, meter.TimeSignature('4/4'))
    >>> p1.append(note.Note('C', type = 'half'))
    >>> p1.append(note.Rest(type='half'))
    >>> p1.append(note.Note('C', type = 'half'))
    >>> p1.append(note.Rest(type='half'))
    >>> p1.makeMeasures(inPlace=True)
    >>> p2 = stream.Part()
    >>> p2.insert(0, meter.TimeSignature('4/4'))
    >>> p2.repeatAppend(note.Note('C', type='quarter'), 8)
    >>> p2.makeMeasures(inPlace=True)
    >>> s = stream.Score()
    >>> s.insert(0, p1)
    >>> s.insert(0, p2)
    >>> ss = omr.correctors.ScoreCorrector(s)
    >>> ss.getAllHashes()
    [['Z[', 'Z['], ['PPPP', 'PPPP']]
    ```

ScoreCorrector.getAllIncorrectMeasures()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.getAllIncorrectMeasures)
:   Returns an array of the incorrect measure indices arrays for each part.
    This is used in the MeasureSlice object to make sure we’re not comparing a flagged
    measure to other flagged measures in its slice

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> omrScore = converter.parse(omrPath)
    >>> ssOMR = omr.correctors.ScoreCorrector(omrScore)
    >>> ssOMR
    <music21.omr.correctors.ScoreCorrector object at 0x...>
    >>> ssOMR.getAllIncorrectMeasures()
    [[1, 3, 9, 10, 12, 17, 20], [2, 12, 14, 17], [1, 9], []]
    ```

ScoreCorrector.getMeasureSlice(*i*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.getMeasureSlice)
:   Given an index, i, returns a MeasureSlice object at that index

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> omrScore = converter.parse(omrPath)
    >>> ssOMR = omr.correctors.ScoreCorrector(omrScore)
    >>> ssOMR.getMeasureSlice(4)
    <music21.omr.correctors.MeasureSlice object at 0x...>
    ```

ScoreCorrector.getSinglePart(*pn*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.getSinglePart)
:   returns a NEW SinglePart object for part number pn from the score

ScoreCorrector.getVerticalProbabilityDistributionSinglePart(*pn*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.getVerticalProbabilityDistributionSinglePart)
:   Returns the Vertical Probability Distribution (PrP) for a single part.

    Get the Priors for the Violin II part (first 20 measures only)

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> omrScore = converter.parse(omrPath)
    >>> ssOMR = omr.correctors.ScoreCorrector(omrScore)
    >>> allDists = ssOMR.getVerticalProbabilityDistributionSinglePart(1)
    >>> [f'{p:0.3f}' for p in allDists]
    ['0.571', '1.000', '0.667', '0.714']
    ```

ScoreCorrector.getVerticalProbabilityDistributionSinglePartSingleMeasure(*pn*, *measureIndex*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.getVerticalProbabilityDistributionSinglePartSingleMeasure)

ScoreCorrector.run()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.run)
:   Run all known models for OMR correction on
    this score

ScoreCorrector.runHorizontalCorrectionModel()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.runHorizontalCorrectionModel)
:   runs for sp in self.singleParts:
    :   sp.runHorizontalCorrectionModel()

    returns correctingArrayAllParts

ScoreCorrector.runPriorModel()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.runPriorModel)
:   run the horizontal and vertical correction models
    on the score. Returns the new self.score object.

ScoreCorrector.runVerticalCorrectionModel()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.runVerticalCorrectionModel)
:   Runs a basic vertical correction model on a ScoreCorrector object.
    That is, for each flagged measure, this method replaces the rhythm in that flagged measure
    with the rhythm of a measure with the least difference.

ScoreCorrector.runVerticalSearch(*i*, *pn*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.runVerticalSearch)
:   Returns an array of the minimum distance measure indices
    given a measure (with index i) within a part pn to compare to

ScoreCorrector.substituteOneMeasureContentsForAnother(*sourceHorizontalIndex*, *sourceVerticalIndex*, *destinationHorizontalIndex*, *destinationVerticalIndex*)[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.substituteOneMeasureContentsForAnother)
:   Takes a destination measure, deletes its contents, and replaces them
    with the contents of a source measure but retains as many pitches as possible

    The destination measure would normally be in the set F of flagged measures
    (having an incorrect number of beats)
    while the source measure is in the set C of correcting measures.

    ```python
    >>> s = corpus.parse('bwv66.6').measures(1, 2)
    >>> s.show('text')
    {0.0} <music21.stream.Part Soprano>
        ...
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note A>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note C#>
            {3.0} <music21.note.Note E>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note C#>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note A>
            {3.0} <music21.note.Note C#>
    {0.0} <music21.stream.Part Alto>
         ...
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note F#>
            {1.0} <music21.note.Note E>
            {2.0} <music21.note.Note E>
            {3.0} <music21.note.Note E>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note E>
            {0.5} <music21.note.Note A>
            {1.0} <music21.note.Note G#>
            {2.0} <music21.note.Note E>
            {3.0} <music21.note.Note G#>
    ...
    ```

    Replace part 1, measure 2 (index 1) with part 0, measure 1 (index 0) while retaining
    as many pitches as possible. The eighth-notes will become quarters:

    ```python
    >>> scOMR = omr.correctors.ScoreCorrector(s)
    >>> scOMR.substituteOneMeasureContentsForAnother(0, 0, 1, 1)
    >>> s2 = scOMR.score
    >>> s2.show('text')
    {0.0} <music21.stream.Part Soprano>
        ...
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note A>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note C#>
            {3.0} <music21.note.Note E>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note C#>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note A>
            {3.0} <music21.note.Note C#>
    {0.0} <music21.stream.Part Alto>
         ...
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note F#>
            {1.0} <music21.note.Note E>
            {2.0} <music21.note.Note E>
            {3.0} <music21.note.Note E>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note E>
            {1.0} <music21.note.Note A>
            {2.0} <music21.note.Note G#>
            {3.0} <music21.note.Note E>
    ...
    ```

ScoreCorrector.verticalProbabilityDist()[[source]](../_modules/music21/omr/correctors.html#ScoreCorrector.verticalProbabilityDist)
:   Uses a score and returns an array of probabilities.
    For n in the array, n is the probability that the nth part

## SinglePart

class music21.omr.correctors.SinglePart(*part=None*, *pn=None*)[[source]](../_modules/music21/omr/correctors.html#SinglePart)

[`SinglePart`](#music21.omr.correctors.SinglePart "music21.omr.correctors.SinglePart") methods

SinglePart.getIncorrectMeasureIndices(*runFast=False*)[[source]](../_modules/music21/omr/correctors.html#SinglePart.getIncorrectMeasureIndices)
:   Returns an array of all the measures that OMR software would flag - that is,
    measures that do
    not have the correct number of beats given the current time signature

    if runFast is True (by default), assumes that the initial TimeSignature
    is the TimeSignature for the entire piece.

    ```python
    >>> p = stream.Part()
    >>> ts = meter.TimeSignature('6/8')
    >>> m1 = stream.Measure()
    >>> m1.number = 1
    >>> m1.append(ts)
    >>> m1.append(note.Note('C4', quarterLength = 3.0))
    >>> p.append(m1)
    >>> m2 = stream.Measure()
    >>> m2.number = 2
    >>> m2.append(note.Note('C4', quarterLength = 1.5))
    >>> p.append(m2)
    ```

    ```python
    >>> sp = omr.correctors.SinglePart(p, pn = 0)
    >>> sp.getIncorrectMeasureIndices()
    [1]
    ```

    ```python
    >>> p[1]
    <music21.stream.Measure 2 offset=3.0>
    >>> p[1].insert(0, meter.TimeSignature('3/8'))
    >>> sp.getIncorrectMeasureIndices(runFast=False)
    []
    ```

SinglePart.getMeasures()[[source]](../_modules/music21/omr/correctors.html#SinglePart.getMeasures)

SinglePart.getProbabilityDistribution(*sourceIndex*, *destinationIndex*)[[source]](../_modules/music21/omr/correctors.html#SinglePart.getProbabilityDistribution)

SinglePart.getSequenceHashesFromMeasureStream()[[source]](../_modules/music21/omr/correctors.html#SinglePart.getSequenceHashesFromMeasureStream)
:   takes in a measure stream of a part
    returns an array of hashed strings

SinglePart.horizontalProbabilityDist(*regenerate=False*)[[source]](../_modules/music21/omr/correctors.html#SinglePart.horizontalProbabilityDist)
:   Uses (takes?) an array of hashed measures and returns an array of probabilities.
    For n in the array, n is the probability that the measure (n-(length of score)) away
    from a flagged measure will offer a rhythmic solution.

    These are the probabilities that, within a part, a measure offers a solution, given its
    distance from a flagged measure.

SinglePart.runHorizontalCorrectionModel()[[source]](../_modules/music21/omr/correctors.html#SinglePart.runHorizontalCorrectionModel)
:   Runs a basic horizontal correction model on a score.
    That is, for each flagged measure, this method replaces the rhythm in that flagged measure
    with the rhythm of a measure with the least difference.

SinglePart.runHorizontalSearch(*i*)[[source]](../_modules/music21/omr/correctors.html#SinglePart.runHorizontalSearch)
:   Returns an array of the indices of the minimum distance measures
    given a measure (with index i) to compare to.
