Source: https://music21.org/music21docs/moduleReference/moduleAnalysisFloatingKey.html

# music21.analysis.floatingKey

The floatingKey analyzer will give an approximation of the key at any point in
a score down to the measure level using a fixed window. It helps smooth out
measures emphasizing non-chord tones, etc.

## KeyAnalyzer

class music21.analysis.floatingKey.KeyAnalyzer(*s=None*)[[source]](../_modules/music21/analysis/floatingKey.html#KeyAnalyzer)
:   KeyAnalyzer is the main object to use for floating analysis.

    The windowSize attribute (default 4) determines how many measures to look at in making
    the decision. Make it larger for pieces (like Mozart sonatas) that you expect fewer key
    changes. Make it smaller for pieces (like Bach chorales) that you expect more key changes.
    Or set it to an integer based on the number of the measures in the piece.

    The weightAlgorithm attribute determines how to scale the weight of measures according to
    their distance. Currently only one algorithm is supported: floatingKey.divide.

    TODO: Needs more work to work with second endings, partial measures, etc.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> ka = analysis.floatingKey.KeyAnalyzer(b)
    >>> ka.windowSize = 2  # chorale uses quick key changes
    >>> ka.run()  # first measure is the pickup
    [<music21.key.Key of A major>, <music21.key.Key of A major>, <music21.key.Key of A major>,
     <music21.key.Key of f# minor>, <music21.key.Key of f# minor>, <music21.key.Key of f# minor>,
     <music21.key.Key of f# minor>, <music21.key.Key of f# minor>,
     <music21.key.Key of f# minor>, <music21.key.Key of f# minor>]
    ```

    Raw analysis (no smoothing):

    ```python
    >>> ka.getRawKeyByMeasure()
    [<music21.key.Key of A major>, <music21.key.Key of E major>, <music21.key.Key of A major>,
     <music21.key.Key of f# minor>, <music21.key.Key of E major>, <music21.key.Key of A major>,
     <music21.key.Key of b minor>, <music21.key.Key of C# major>,
     <music21.key.Key of F# major>, <music21.key.Key of b minor>]
    ```

    Major smoothing:

    ```python
    >>> ka.windowSize = ka.numMeasures // 2
    >>> ka.run()  # only the pickup seems to be in A major by this approach
    [<music21.key.Key of A major>, <music21.key.Key of f# minor>, <music21.key.Key of f# minor>,
     <music21.key.Key of f# minor>, <music21.key.Key of f# minor>, <music21.key.Key of f# minor>,
     <music21.key.Key of f# minor>, <music21.key.Key of f# minor>,
     <music21.key.Key of f# minor>, <music21.key.Key of f# minor>]
    ```

    ```python
    >>> tiny = converter.parse('tinyNotation: c1 e1 g1 c1 d-4 d-4 d-4 d-4')
    >>> ka = analysis.floatingKey.KeyAnalyzer(tiny)
    >>> ka.windowSize = 1
    >>> ka.run()  # This previously only gave four elements: am, CM, CM, CM
    [<music21.key.Key of a minor>, <music21.key.Key of C major>, <music21.key.Key of C major>,
     <music21.key.Key of C major>, <music21.key.Key of b- minor>]
    ```

    No measures will fail.

    ```python
    >>> s = stream.Part([note.Note()])
    >>> ka = analysis.floatingKey.KeyAnalyzer(s)
    Traceback (most recent call last):
    music21.analysis.floatingKey.FloatingKeyException: Stream must have Measures inside it
    ```

    * Changed in v7: analysis now incorporates final measures in pieces without pickup measures:

[`KeyAnalyzer`](#music21.analysis.floatingKey.KeyAnalyzer "music21.analysis.floatingKey.KeyAnalyzer") methods

KeyAnalyzer.getInterpretationByMeasure(*mIndex*)[[source]](../_modules/music21/analysis/floatingKey.html#KeyAnalyzer.getInterpretationByMeasure)
:   Returns a dictionary of interpretations for the measure.
    mIndex is 0-indexed.

KeyAnalyzer.getRawKeyByMeasure()[[source]](../_modules/music21/analysis/floatingKey.html#KeyAnalyzer.getRawKeyByMeasure)

KeyAnalyzer.run()[[source]](../_modules/music21/analysis/floatingKey.html#KeyAnalyzer.run)

KeyAnalyzer.smoothInterpretationByMeasure()[[source]](../_modules/music21/analysis/floatingKey.html#KeyAnalyzer.smoothInterpretationByMeasure)

## Functions

music21.analysis.floatingKey.divide(*coefficient*, *distance*)[[source]](../_modules/music21/analysis/floatingKey.html#divide)
:   Divide the coefficient by the absolute value of the distance + 1

    ```python
    >>> analysis.floatingKey.divide(4.0, -1)
    2.0
    ```
