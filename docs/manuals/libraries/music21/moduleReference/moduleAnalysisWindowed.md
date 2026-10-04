Source: https://music21.org/music21docs/moduleReference/moduleAnalysisWindowed.html

# music21.analysis.windowed

This module describes classes for performing windowed and overlapping windowed analysis.
The [`music21.analysis.windowed.WindowedAnalysis`](#music21.analysis.windowed.WindowedAnalysis "music21.analysis.windowed.WindowedAnalysis") provides a reusable framework for
systematic overlapping window analysis at the starting at the level of the quarter note
and moving to the size of an entire `music21.stream.Stream`.

Modular analysis procedures inherit from [`music21.analysis.discrete.DiscreteAnalysis`](moduleAnalysisDiscrete.html#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis").
The [`music21.analysis.discrete.KrumhanslSchmuckler`](moduleAnalysisDiscrete.html#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler") (for algorithmic key detection)
and [`music21.analysis.discrete.Ambitus`](moduleAnalysisDiscrete.html#music21.analysis.discrete.Ambitus "music21.analysis.discrete.Ambitus") (for pitch range analysis) classes provide examples.

## WindowedAnalysis

class music21.analysis.windowed.WindowedAnalysis(*streamObj*, *analysisProcessor*)[[source]](../_modules/music21/analysis/windowed.html#WindowedAnalysis)
:   Create a WindowedAnalysis object.

    The provided analysisProcessor must provide a process() method that,
    when given a windowed Stream (a Measure) returns two element tuple containing
    (a) a data value (implementation dependent) and (b) a color code.

[`WindowedAnalysis`](#music21.analysis.windowed.WindowedAnalysis "music21.analysis.windowed.WindowedAnalysis") methods

WindowedAnalysis.analyze(*windowSize*, *windowType='overlap'*)[[source]](../_modules/music21/analysis/windowed.html#WindowedAnalysis.analyze)
:   Calls, for a given window size, an analysis method across all windows in the source Stream.

    If windowType is “overlap”, windows above size 1 are always overlapped, so if a window
    of size 2 is used, windows 1-2, then 2-3, then 3-4 are compared. If a window of size 3
    is used, windows 1-3, then 2-4, then 3-5 are compared.

    Windows are assumed to be partitioned by `music21.stream.Measure` objects.

    Returns two lists for results, each equal in size to the length of minimum windows
    minus the window size plus one. If we have 20 1/4 windows, then the results lists
    will be of length 20 for window size 1, 19 for window size 2, 18 for window size 3, etc.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = analysis.discrete.Ambitus()
    >>> wa = analysis.windowed.WindowedAnalysis(s.flatten(), p)
    >>> len(wa._windowedStream)
    36
    >>> a, b = wa.analyze(1)
    >>> len(a), len(b)
    (36, 36)
    ```

    ```python
    >>> a, b = wa.analyze(4)
    >>> len(a), len(b)
    (33, 33)
    ```

    ```python
    >>> a, b = wa.analyze(1, windowType='noOverlap')
    >>> len(a), len(b)
    (37, 37)
    ```

    ```python
    >>> a, b = wa.analyze(4, windowType='noOverlap')
    >>> len(a), len(b)
    (10, 10)
    ```

    ```python
    >>> a, b = wa.analyze(1, windowType='adjacentAverage')
    >>> len(a), len(b)
    (36, 36)
    ```

WindowedAnalysis.getMinimumWindowStream(*timeSignature='1/4'*)[[source]](../_modules/music21/analysis/windowed.html#WindowedAnalysis.getMinimumWindowStream)
:   Take the loaded stream and restructure it into measures of 1 quarter note duration.

    ```python
    >>> s = corpus.parse('bach/bwv324')
    >>> p = analysis.discrete.Ambitus()
    ```

    Placing one part into analysis:

    ```python
    >>> wa = analysis.windowed.WindowedAnalysis(s.parts[0], p)
    ```

    ```python
    >>> post = wa.getMinimumWindowStream()
    >>> len(post.getElementsByClass(stream.Measure))
    42
    >>> post.getElementsByClass(stream.Measure).first()
    <music21.stream.Measure 1 offset=0.0>
    ```

    Time signature set to 1/4 time signature

    ```python
    >>> post.getElementsByClass(stream.Measure).first().timeSignature
    <music21.meter.TimeSignature 1/4>
    ```

    leaves one note in this measure

    ```python
    >>> len(post.getElementsByClass(stream.Measure)[1].notes)
    1
    ```

    Placing a score with parts into analysis will automatically flatten
    the stream. So these two calls are equivalent:

    ```python
    >>> wa1 = analysis.windowed.WindowedAnalysis(s, p)
    >>> wa2 = analysis.windowed.WindowedAnalysis(s.flatten(), p)
    ```

WindowedAnalysis.process(*minWindow: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *maxWindow: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *windowStepSize: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 1*, *windowType='overlap'*, *includeTotalWindow=True*)[[source]](../_modules/music21/analysis/windowed.html#WindowedAnalysis.process)
:   Main method for windowed analysis across one or more window sizes.

    Calls `analyze()` for
    the number of different window sizes to be analyzed.

    The minWindow and maxWindow set the range of window sizes in quarter lengths.
    The windowStepSize parameter determines the increment between these window sizes,
    in quarter lengths.

    If minWindow or maxWindow is None, the largest window size available will be set.

    If includeTotalWindow is True, the largest window size will always be added.

    ```python
    >>> s = corpus.parse('bach/bwv324')
    >>> ksAnalyzer = analysis.discrete.KrumhanslSchmuckler()
    ```

    placing one part into analysis

    ```python
    >>> sopr = s.parts[0]
    >>> wa = analysis.windowed.WindowedAnalysis(sopr, ksAnalyzer)
    >>> solutions, colors, meta = wa.process(1, 1, includeTotalWindow=False)
    >>> len(solutions)  # we only have one series of windows
    1
    ```

    ```python
    >>> solutions, colors, meta = wa.process(1, 2, includeTotalWindow=False)
    >>> len(solutions)  # we have two series of windows
    2
    ```

    ```python
    >>> solutions[1]
    [(<music21.pitch.Pitch B>, 'major', 0.6844...),
     (<music21.pitch.Pitch B>, 'minor', 0.8308...),
     (<music21.pitch.Pitch D>, 'major', 0.6844...),
     (<music21.pitch.Pitch B>, 'minor', 0.8308...),...]
    ```

    ```python
    >>> colors[1]
    ['#ffb5ff', '#9b519b', '#ffd752', '#9b519b', ...]
    ```

    ```python
    >>> meta
    [{'windowSize': 1}, {'windowSize': 2}]
    ```

## MockObjectProcessor

class music21.analysis.windowed.MockObjectProcessor[[source]](../_modules/music21/analysis/windowed.html#MockObjectProcessor)

[`MockObjectProcessor`](#music21.analysis.windowed.MockObjectProcessor "music21.analysis.windowed.MockObjectProcessor") methods

MockObjectProcessor.process(*subStream*)[[source]](../_modules/music21/analysis/windowed.html#MockObjectProcessor.process)
:   Simply count the number of notes found
