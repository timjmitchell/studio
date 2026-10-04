Source: https://music21.org/music21docs/moduleReference/moduleAnalysisCorrelate.html

# music21.analysis.correlate

Various tools and utilities to find correlations between disparate objects in a Stream.

## ActivityMatch

class music21.analysis.correlate.ActivityMatch(*streamObj*)[[source]](../_modules/music21/analysis/correlate.html#ActivityMatch)
:   Given a Stream, find if one object is active while another is also active.

    Plotting routines to graph the output of dedicated methods in this class are available.

    [`ScatterPitchSpaceDynamicSymbol`](moduleGraphPlot.html#music21.graph.plot.ScatterPitchSpaceDynamicSymbol "music21.graph.plot.ScatterPitchSpaceDynamicSymbol") and
    [`ScatterWeightedPitchSpaceDynamicSymbol`](moduleGraphPlot.html#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol")
    employs the [`pitchToDynamic()`](#music21.analysis.correlate.ActivityMatch.pitchToDynamic "music21.analysis.correlate.ActivityMatch.pitchToDynamic") method.

    Sample output is as follows:

    [![../_images/ScatterWeightedPitchSpaceDynamicSymbol.png](../_images/ScatterWeightedPitchSpaceDynamicSymbol.png)](../_images/ScatterWeightedPitchSpaceDynamicSymbol.png)

[`ActivityMatch`](#music21.analysis.correlate.ActivityMatch "music21.analysis.correlate.ActivityMatch") methods

ActivityMatch.pitchToDynamic(*dataPoints=True*)[[source]](../_modules/music21/analysis/correlate.html#ActivityMatch.pitchToDynamic)
:   Create an analysis of pitch to dynamic symbol.

    If dataPoints is True, all data matches between source and destination are returned.
    If False, 3 point weighted coordinates are created for each unique match.

    No dynamics here.

    ```python
    >>> s = corpus.parse('bach/bwv8.6.xml')
    >>> am = analysis.correlate.ActivityMatch(s.parts.first().flatten())
    >>> am.pitchToDynamic()
    Traceback (most recent call last):
    music21.analysis.correlate.CorrelateException: cannot create correlation:
        an object that is not found in the Stream: <class 'music21.dynamics.Dynamic'>
    ```

    Many dynamics

    ```python
    >>> s = corpus.parse('schoenberg/opus19/movement2')
    >>> am = analysis.correlate.ActivityMatch(s.parts.first().flatten())
    >>> data = am.pitchToDynamic()
    >>> len(data)
    39
    >>> data[0]
    (83.0, 7)
    ```
