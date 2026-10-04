Source: https://music21.org/music21docs/moduleReference/moduleOmrEvaluators.html

# music21.omr.evaluators

This module takes two XML files and displays the number of measures that
differ between the two before and after running the combined correction models

## OmrGroundTruthPair

class music21.omr.evaluators.OmrGroundTruthPair(*omr=None*, *ground=None*)[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair)
:   Object for making comparisons between an OMR score and the GroundTruth

    Takes in a path to the OMR and a path to the groundTruth
    (or a pair of music21.stream.Score objects).

    See below for examples.

[`OmrGroundTruthPair`](#music21.omr.evaluators.OmrGroundTruthPair "music21.omr.evaluators.OmrGroundTruthPair") read/write properties

OmrGroundTruthPair.debug
:   Returns either the debug value set for this
    evaluator, or globalDebug

[`OmrGroundTruthPair`](#music21.omr.evaluators.OmrGroundTruthPair "music21.omr.evaluators.OmrGroundTruthPair") methods

OmrGroundTruthPair.deleteCost(*x*)[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.deleteCost)
:   define the deletion cost for x and y (1)

OmrGroundTruthPair.getDifferences()[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.getDifferences)
:   Returns the total edit distance as an Int between
    the two scores

    This function is based on James H. Martin’s minimum edit distance.

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> ground = omr.correctors.K525groundTruthShortPath
    >>> omrGTP = omr.evaluators.OmrGroundTruthPair(omr=omrPath, ground=ground)
    >>> differences = omrGTP.getDifferences()
    >>> differences
    32
    ```

OmrGroundTruthPair.getGroundScore()[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.getGroundScore)
:   Returns a ScoreCorrector object of the Ground truth score

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> ground = omr.correctors.K525groundTruthShortPath
    >>> omrGTP = omr.evaluators.OmrGroundTruthPair(omr=omrPath, ground=ground)
    >>> ssGT = omrGTP.getGroundScore()
    >>> ssGT
    <music21.omr.correctors.ScoreCorrector object at 0x...>
    ```

OmrGroundTruthPair.getOmrScore()[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.getOmrScore)
:   Returns a ScoreCorrector object of the OMR score. does not store it anywhere

    ```python
    >>> omrPath = omr.correctors.K525omrShortPath
    >>> ground = omr.correctors.K525groundTruthShortPath
    >>> omrGTP = omr.evaluators.OmrGroundTruthPair(omr=omrPath, ground=ground)
    >>> ssOMR = omrGTP.getOmrScore()
    >>> ssOMR
    <music21.omr.correctors.ScoreCorrector object at 0x...>
    ```

OmrGroundTruthPair.hashAll()[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.hashAll)
:   store the Hashes for both scores.

OmrGroundTruthPair.insertCost(*x*)[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.insertCost)
:   define the insertion cost for x and y (1)

OmrGroundTruthPair.minEditDist(*target*, *source*)[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.minEditDist)
:   Computes the min edit distance from target to source. Figure 3.25

OmrGroundTruthPair.parseAll()[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.parseAll)
:   Parse both scores.

OmrGroundTruthPair.substCost(*x*, *y*)[[source]](../_modules/music21/omr/evaluators.html#OmrGroundTruthPair.substCost)
:   define the substitution cost for x and y (2 if x and y are unequal else 0)

## Functions

music21.omr.evaluators.autoCorrelationBestMeasure(*inputScore*)[[source]](../_modules/music21/omr/evaluators.html#autoCorrelationBestMeasure)
:   Essentially it’s the ratio of amount of rhythmic similarity within a piece, which
    gives an upper bound on what the omr.corrector.prior measure should be able to
    achieve for the flagged measures. If a piece has low rhythmic similarity in general, then
    there’s no way for a correct match to be found within the unflagged measures in the piece.

    Returns a tuple of the total number of NON-flagged measures and the total number
    of those measures that have a rhythmic match.

    Takes in a stream.Score.

    ```python
    >>> c = converter.parse(omr.correctors.K525omrShortPath)  # first 21 measures
    >>> totalUnflagged, totalUnflaggedWithMatches = omr.evaluators.autoCorrelationBestMeasure(c)
    >>> (totalUnflagged, totalUnflaggedWithMatches)
    (71, 64)
    >>> print( float(totalUnflaggedWithMatches) / totalUnflagged )
    0.901...
    ```

    Schoenberg has low autoCorrelation.

    ```python
    >>> c = corpus.parse('schoenberg/opus19/movement6')
    >>> totalUnflagged, totalUnflaggedWithMatches = omr.evaluators.autoCorrelationBestMeasure(c)
    >>> (totalUnflagged, totalUnflaggedWithMatches)
    (18, 6)
    >>> print( float(totalUnflaggedWithMatches) / totalUnflagged )
    0.333...
    ```

music21.omr.evaluators.evaluateCorrectingModel(*omrPath*, *groundTruthPath*, *debug=None*, *originalDifferences=None*, *runOnePart=False*)[[source]](../_modules/music21/omr/evaluators.html#evaluateCorrectingModel)
:   Get a dictionary showing the efficacy of the omr.correctors.ScoreCorrector on an OMR Score
    by comparing it to the GroundTruth.

    Set debug to True to see a lot of intermediary steps.

    ```python
    >>> omrFilePath = omr.correctors.K525omrShortPath
    >>> groundTruthFilePath = omr.correctors.K525groundTruthShortPath
    >>> returnDict = omr.evaluators.evaluateCorrectingModel(omrFilePath, groundTruthFilePath)
    >>> for name in sorted(list(returnDict.keys())):
    ...     (name, returnDict[name])
    ('newEditDistance', 20)
    ('numberOfFlaggedMeasures', 13)
    ('originalEditDistance', 32)
    ('totalNumberOfMeasures', 84)
    ```
