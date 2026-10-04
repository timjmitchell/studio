Source: https://music21.org/music21docs/moduleReference/moduleAnalysisDiscrete.html

# music21.analysis.discrete

Modular analysis procedures for use alone or
applied with [`music21.analysis.windowed.WindowedAnalysis`](moduleAnalysisWindowed.html#music21.analysis.windowed.WindowedAnalysis "music21.analysis.windowed.WindowedAnalysis") class.

All procedures should inherit from
[`music21.analysis.discrete.DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"),
or provide a similar interface.

The [`music21.analysis.discrete.KrumhanslSchmuckler`](#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler")
(for algorithmic key detection) and
[`music21.analysis.discrete.Ambitus`](#music21.analysis.discrete.Ambitus "music21.analysis.discrete.Ambitus") (for pitch range analysis) provide examples.

## DiscreteAnalysis

class music21.analysis.discrete.DiscreteAnalysis(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis)
:   Parent class for analytical methods.

    Each analytical method returns a discrete numerical (or other)
    results as well as a color. Colors can be used in mapping output.

    Analytical methods may make use of a referenceStream to
    configure the processor on initialization.

[`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis") methods

DiscreteAnalysis.clearSolutionsFound()[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.clearSolutionsFound)
:   Clear all stored solutions

DiscreteAnalysis.getColorsUsed()[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.getColorsUsed)
:   Based on solutions found so far with this processor,
    return the colors that have been used.

DiscreteAnalysis.getSolution(*subStream*)[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.getSolution)
:   For a given Stream, apply the analysis and return the best solution.

DiscreteAnalysis.getSolutionsUsed()[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.getSolutionsUsed)
:   Based on solutions found so far with this processor,
    return the solutions that have been used.

DiscreteAnalysis.process(*sStream*)[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.process)
:   Given a Stream, apply the analysis to all components of this Stream.
    Expected return is a solution (method-specific) and a color value.

DiscreteAnalysis.solutionLegend(*compress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]]]][[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.solutionLegend)
:   A list of pairs showing all discrete results and the assigned color.
    Data should be organized to be passed to
    `music21.graph.GraphColorGridLegend`.

    If compress is True, the legend will only show values for solutions
    that have been encountered.

DiscreteAnalysis.solutionToColor(*solution*)[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.solutionToColor)
:   Given an analysis specific result, return the appropriate color.
    Must be able to handle None in the case that there is no result.

DiscreteAnalysis.solutionUnitString()[[source]](../_modules/music21/analysis/discrete.html#DiscreteAnalysis.solutionUnitString)
:   Return a string describing the solution values. Used in Legend formation.

## Ambitus

class music21.analysis.discrete.Ambitus(*referenceStream: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/analysis/discrete.html#Ambitus)
:   A basic analysis method for measuring register.

    ```python
    >>> ambitusAnalysis = analysis.discrete.Ambitus()
    >>> ambitusAnalysis.identifiers[0]
    'ambitus'
    ```

[`Ambitus`](#music21.analysis.discrete.Ambitus "music21.analysis.discrete.Ambitus") bases

* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`Ambitus`](#music21.analysis.discrete.Ambitus "music21.analysis.discrete.Ambitus") methods

Ambitus.getPitchSpan(*subStream*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/analysis/discrete.html#Ambitus.getPitchSpan)
:   For a given subStream, return a tuple consisting of the two pitches
    with the minimum and maximum pitch space value.

    This public method may be used by other classes. It ignores ChordSymbol objects.

    Demonstration:

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = analysis.discrete.Ambitus()
    >>> pitchMin, pitchMax = p.getPitchSpan(s.parts[0].getElementsByClass(stream.Measure)[3])
    >>> pitchMin.ps, pitchMax.ps
    (66.0, 71.0)
    >>> p.getPitchSpan(s.parts[0].getElementsByClass(stream.Measure)[6])
    (<music21.pitch.Pitch A4>, <music21.pitch.Pitch C#5>)
    ```

    ```python
    >>> s = stream.Stream()
    >>> c = chord.Chord(['a2', 'b4', 'c8'])
    >>> s.append(c)
    >>> p.getPitchSpan(s)
    (<music21.pitch.Pitch A2>, <music21.pitch.Pitch C8>)
    ```

    Returns None if the stream contains no pitches.

    ```python
    >>> s = stream.Stream(note.Rest())
    >>> p.getPitchSpan(s) is None
    True
    ```

Ambitus.getSolution(*sStream*)[[source]](../_modules/music21/analysis/discrete.html#Ambitus.getSolution)
:   Procedure to only return an Interval object.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = analysis.discrete.Ambitus()
    >>> p.getSolution(s)
    <music21.interval.Interval m21>
    ```

Ambitus.process(*sStream*)[[source]](../_modules/music21/analysis/discrete.html#Ambitus.process)
:   Given a Stream, return a solution (as an interval) and a color string.

    ```python
    >>> p = analysis.discrete.Ambitus()
    >>> s = stream.Stream()
    >>> c = chord.Chord(['a2', 'b4', 'c8'])
    >>> s.append(c)
    >>> p.process(s)
    (<music21.interval.Interval m38>, '#665288')
    ```

Ambitus.solutionLegend(*compress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]]]][[source]](../_modules/music21/analysis/discrete.html#Ambitus.solutionLegend)
:   Return legend data.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> soprano = s.parts[0]
    >>> p = analysis.discrete.Ambitus(soprano)  # provide ref stream
    >>> p.solutionLegend()
    [['',
      [(0, '#130f19'), (1, '#211a2c'), (2, '#2f263f'),
       (3, '#3e3253'), (4, '#4c3d66'), (5, '#5b4979')]],
     ['',
      [(6, '#69548c'), (7, '#775f9f'), (8, '#866bb2'), (9, '#9476c5'),
       (10, '#a382d9'), (11, '#b18eec'), (12, '#bf99ff')]]]
    ```

    ```python
    >>> len(p.solutionLegend())
    2
    >>> [len(x) for x in p.solutionLegend()]
    [2, 2]
    ```

    ```python
    >>> [len(y) for y in [x for x in p.solutionLegend()]]
    [2, 2]
    ```

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = analysis.discrete.Ambitus()
    >>> p.solutionLegend(compress=True)  # empty if nothing processed
    [['', []], ['', []]]
    ```

    ```python
    >>> x = p.process(s.parts[0])
    >>> [len(y) for y in [x for x in p.solutionLegend(compress=True)]]
    [2, 2]
    ```

    ```python
    >>> x = p.process(s.parts[1])
    >>> [len(y) for y in [x for x in p.solutionLegend(compress=True)]]
    [2, 2]
    ```

Ambitus.solutionToColor(*solution: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/analysis/discrete.html#Ambitus.solutionToColor)
:   ```python
    >>> p = analysis.discrete.Ambitus()
    >>> s = stream.Stream()
    >>> c = chord.Chord(['a2', 'b4', 'c8'])
    >>> s.append(c)
    >>> minPitch, maxPitch = p.getPitchSpan(s)
    >>> p.solutionToColor(maxPitch.ps - minPitch.ps).startswith('#')
    True
    ```

Ambitus.solutionUnitString()[[source]](../_modules/music21/analysis/discrete.html#Ambitus.solutionUnitString)
:   Return a string describing the solution values. Used in Legend formation.

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## MelodicIntervalDiversity

class music21.analysis.discrete.MelodicIntervalDiversity(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#MelodicIntervalDiversity)
:   An analysis method to determine the diversity of intervals used in a Stream.

[`MelodicIntervalDiversity`](#music21.analysis.discrete.MelodicIntervalDiversity "music21.analysis.discrete.MelodicIntervalDiversity") bases

* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`MelodicIntervalDiversity`](#music21.analysis.discrete.MelodicIntervalDiversity "music21.analysis.discrete.MelodicIntervalDiversity") methods

MelodicIntervalDiversity.countMelodicIntervals(*sStream*, *found=None*, *ignoreDirection=True*, *ignoreUnison=True*)[[source]](../_modules/music21/analysis/discrete.html#MelodicIntervalDiversity.countMelodicIntervals)
:   Find all unique melodic intervals in this Stream.

    If found is provided as a dictionary, this dictionary will be used to store Intervals,
    and counts of Intervals already found will be incremented.

MelodicIntervalDiversity.getSolution(*sStream*)[[source]](../_modules/music21/analysis/discrete.html#MelodicIntervalDiversity.getSolution)
:   Solution is the number of unique intervals.

MelodicIntervalDiversity.process(*sStream*, *ignoreDirection=True*)[[source]](../_modules/music21/analysis/discrete.html#MelodicIntervalDiversity.process)
:   Find how many unique intervals are used in this Stream

MelodicIntervalDiversity.solutionToColor(*solution*)[[source]](../_modules/music21/analysis/discrete.html#MelodicIntervalDiversity.solutionToColor)
:   Given an analysis specific result, return the appropriate color.
    Must be able to handle None in the case that there is no result.

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") * [`solutionLegend()`](#music21.analysis.discrete.DiscreteAnalysis.solutionLegend "music21.analysis.discrete.DiscreteAnalysis.solutionLegend") | * [`solutionUnitString()`](#music21.analysis.discrete.DiscreteAnalysis.solutionUnitString "music21.analysis.discrete.DiscreteAnalysis.solutionUnitString") |

## KeyWeightKeyAnalysis

class music21.analysis.discrete.KeyWeightKeyAnalysis(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis)
:   Base class for all key-weight key analysis subclasses.

[`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis") bases

* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis") methods

KeyWeightKeyAnalysis.getSolution(*sStream*)[[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis.getSolution)
:   Return a music21 Key object defining the results of the analysis.
    Do not call process before calling this method, as this method calls process.

    Note that all alternative solutions are returned as Key objects and stored
    on a list found at Key.alternateInterpretations.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = analysis.discrete.KrumhanslSchmuckler()
    >>> p.getSolution(s)  # this seems correct
    <music21.key.Key of f# minor>
    ```

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = analysis.discrete.KrumhanslSchmuckler(s)
    >>> p.getSolution(s)
    <music21.key.Key of B- major>
    ```

KeyWeightKeyAnalysis.getWeights(*weightType='major'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis.getWeights)
:   Returns the key weights. To provide different key weights,
    subclass and override this method. The defaults here are KrumhanslSchmuckler.

    ```python
    >>> a = analysis.discrete.KrumhanslSchmuckler()
    >>> len(a.getWeights('major'))
    12
    >>> len(a.getWeights('minor'))
    12
    ```

KeyWeightKeyAnalysis.process(*sStream*, *storeAlternatives=False*)[[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis.process)
:   Takes in a Stream or sub-Stream and performs analysis
    on all contents of the Stream. The
    [`WindowedAnalysis`](moduleAnalysisWindowed.html#music21.analysis.windowed.WindowedAnalysis "music21.analysis.windowed.WindowedAnalysis")
    windowing system can be used to get many results
    by calling this method.

    Returns two values, a solution data list and a color string.

    The data list contains a key (as a string), a mode
    (as a string), and a correlation value (degree of certainty)

KeyWeightKeyAnalysis.solutionLegend(*compress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]]]][[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis.solutionLegend)
:   Returns a list of lists of possible results for the creation of a legend.

    ```python
    >>> p = analysis.discrete.KrumhanslSchmuckler()
    >>> post = p.solutionLegend()
    ```

KeyWeightKeyAnalysis.solutionToColor(*solution*)[[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis.solutionToColor)
:   Given a two-element tuple of (tonicPitch, modality) return the proper color

    ```python
    >>> p = analysis.discrete.KrumhanslSchmuckler()
    >>> solution = (pitch.Pitch('C'), 'major')
    >>> p.solutionToColor(solution)
    '#ff816b'
    ```

KeyWeightKeyAnalysis.solutionUnitString()[[source]](../_modules/music21/analysis/discrete.html#KeyWeightKeyAnalysis.solutionUnitString)
:   Return a string describing the solution values. Used in Legend formation.

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## SimpleWeights

class music21.analysis.discrete.SimpleWeights(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#SimpleWeights)
:   Implementation of simple weights by Craig Sapp for Krumhansl-Schmuckler
    key determination algorithm.

    Values from <https://extras.humdrum.org/man/keycor/>, which describes
    these weightings as “Performs most consistently with large regions of music,
    becomes noisier with smaller regions of music.”

[`SimpleWeights`](#music21.analysis.discrete.SimpleWeights "music21.analysis.discrete.SimpleWeights") bases

* [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis")
* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`SimpleWeights`](#music21.analysis.discrete.SimpleWeights "music21.analysis.discrete.SimpleWeights") methods

SimpleWeights.getWeights(*weightType='major'*)[[source]](../_modules/music21/analysis/discrete.html#SimpleWeights.getWeights)
:   Returns the key weights.

    ```python
    >>> a = analysis.discrete.SimpleWeights()
    >>> len(a.getWeights('major'))
    12
    >>> len(a.getWeights('minor'))
    12
    ```

Methods inherited from [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`getSolution()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution "music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution") * [`process()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.process "music21.analysis.discrete.KeyWeightKeyAnalysis.process") | * [`solutionLegend()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend") * [`solutionToColor()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor") | * [`solutionUnitString()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString") |

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## AardenEssen

class music21.analysis.discrete.AardenEssen(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#AardenEssen)
:   Implementation of Aarden-Essen weightings for Krumhansl-Schmuckler key determination algorithm.

    Values from <https://extras.humdrum.org/man/keycor/>, which
    describes these weightings as “Weak tendency to identify the subdominant key as the tonic.”

    (N.B. – we are not sure exactly where the minor weightings come from, and recommend
    only using these weights for major).

[`AardenEssen`](#music21.analysis.discrete.AardenEssen "music21.analysis.discrete.AardenEssen") bases

* [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis")
* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`AardenEssen`](#music21.analysis.discrete.AardenEssen "music21.analysis.discrete.AardenEssen") methods

AardenEssen.getWeights(*weightType='major'*)[[source]](../_modules/music21/analysis/discrete.html#AardenEssen.getWeights)
:   Returns the key weights.

    ```python
    >>> a = analysis.discrete.AardenEssen()
    >>> len(a.getWeights('major'))
    12
    >>> len(a.getWeights('minor'))
    12
    ```

Methods inherited from [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`getSolution()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution "music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution") * [`process()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.process "music21.analysis.discrete.KeyWeightKeyAnalysis.process") | * [`solutionLegend()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend") * [`solutionToColor()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor") | * [`solutionUnitString()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString") |

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## BellmanBudge

class music21.analysis.discrete.BellmanBudge(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#BellmanBudge)
:   Implementation of Bellman-Budge weightings for Krumhansl-Schmuckler key determination algorithm.

    Values from <https://extras.humdrum.org/man/keycor/>, which describes these
    weightings as “No particular tendencies for confusions with neighboring keys.”

[`BellmanBudge`](#music21.analysis.discrete.BellmanBudge "music21.analysis.discrete.BellmanBudge") bases

* [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis")
* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`BellmanBudge`](#music21.analysis.discrete.BellmanBudge "music21.analysis.discrete.BellmanBudge") methods

BellmanBudge.getWeights(*weightType='major'*)[[source]](../_modules/music21/analysis/discrete.html#BellmanBudge.getWeights)
:   Returns the key weights.

    ```python
    >>> a = analysis.discrete.BellmanBudge()
    >>> len(a.getWeights('major'))
    12
    >>> len(a.getWeights('minor'))
    12
    >>> a.getWeights('major')
    [16.8..., 0.8..., 12.9..., 1.4..., ...]
    ```

Methods inherited from [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`getSolution()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution "music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution") * [`process()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.process "music21.analysis.discrete.KeyWeightKeyAnalysis.process") | * [`solutionLegend()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend") * [`solutionToColor()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor") | * [`solutionUnitString()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString") |

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## KrumhanslSchmuckler

class music21.analysis.discrete.KrumhanslSchmuckler(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#KrumhanslSchmuckler)
:   Implementation of Krumhansl-Schmuckler/Kessler weightings for
    Krumhansl-Schmuckler key determination algorithm.

    Values from <https://extras.humdrum.org/man/keycor/>, which describes these
    weightings as “Strong tendency to identify the dominant key as the tonic.”

    * Changed in v6.3: it used to be that these were different from the
      Kessler profiles, but that was likely a typo. Thus, KrumhanslKessler and
      KrumhanslSchmuckler are synonyms of each other.

[`KrumhanslSchmuckler`](#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler") bases

* [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis")
* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`KrumhanslSchmuckler`](#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler") methods

KrumhanslSchmuckler.getWeights(*weightType='major'*)[[source]](../_modules/music21/analysis/discrete.html#KrumhanslSchmuckler.getWeights)
:   Returns the key weights. To provide different key weights,
    subclass and override this method. The defaults here are KrumhanslSchmuckler.

    ```python
    >>> a = analysis.discrete.KrumhanslSchmuckler()
    >>> len(a.getWeights('major'))
    12
    >>> len(a.getWeights('minor'))
    12
    ```

Methods inherited from [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`getSolution()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution "music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution") * [`process()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.process "music21.analysis.discrete.KeyWeightKeyAnalysis.process") | * [`solutionLegend()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend") * [`solutionToColor()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor") | * [`solutionUnitString()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString") |

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## TemperleyKostkaPayne

class music21.analysis.discrete.TemperleyKostkaPayne(*referenceStream=None*)[[source]](../_modules/music21/analysis/discrete.html#TemperleyKostkaPayne)
:   Implementation of Temperley-Kostka-Payne weightings for Krumhansl-Schmuckler
    key determination algorithm.

    Values from <https://extras.humdrum.org/man/keycor/>, which describes
    these weightings as “Strong tendency to identify the relative major as the tonic
    in minor keys. Well-balanced for major keys.”

[`TemperleyKostkaPayne`](#music21.analysis.discrete.TemperleyKostkaPayne "music21.analysis.discrete.TemperleyKostkaPayne") bases

* [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis")
* [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")

[`TemperleyKostkaPayne`](#music21.analysis.discrete.TemperleyKostkaPayne "music21.analysis.discrete.TemperleyKostkaPayne") methods

TemperleyKostkaPayne.getWeights(*weightType='major'*)[[source]](../_modules/music21/analysis/discrete.html#TemperleyKostkaPayne.getWeights)
:   Returns the key weights.

    ```python
    >>> a = analysis.discrete.TemperleyKostkaPayne()
    >>> len(a.getWeights('major'))
    12
    >>> len(a.getWeights('minor'))
    12
    ```

Methods inherited from [`KeyWeightKeyAnalysis`](#music21.analysis.discrete.KeyWeightKeyAnalysis "music21.analysis.discrete.KeyWeightKeyAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`getSolution()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution "music21.analysis.discrete.KeyWeightKeyAnalysis.getSolution") * [`process()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.process "music21.analysis.discrete.KeyWeightKeyAnalysis.process") | * [`solutionLegend()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionLegend") * [`solutionToColor()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionToColor") | * [`solutionUnitString()`](#music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString "music21.analysis.discrete.KeyWeightKeyAnalysis.solutionUnitString") |

Methods inherited from [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`clearSolutionsFound()`](#music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound "music21.analysis.discrete.DiscreteAnalysis.clearSolutionsFound") | * [`getColorsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getColorsUsed "music21.analysis.discrete.DiscreteAnalysis.getColorsUsed") | * [`getSolutionsUsed()`](#music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed "music21.analysis.discrete.DiscreteAnalysis.getSolutionsUsed") |

## Functions

music21.analysis.discrete.analyzeStream(*streamObj: stream.Stream*, *method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\*\*keywords*)[[source]](../_modules/music21/analysis/discrete.html#analyzeStream)
:   Public interface to discrete analysis methods to be applied
    to a Stream given as an argument. Methods return process-specific data format.
    See subclasses for details.

    Analysis methods can be specified as arguments or by use of a method
    keyword argument. If method is the class name, that class is returned.
    Otherwise, the `identifiers`
    list of all [`DiscreteAnalysis`](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis") subclass objects
    will be searched for matches. The first match that is found is returned.

    [`Ambitus`](#music21.analysis.discrete.Ambitus "music21.analysis.discrete.Ambitus")
    [`KrumhanslSchmuckler`](#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler")

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> analysis.discrete.analyzeStream(s, 'Krumhansl')
    <music21.key.Key of f# minor>
    >>> analysis.discrete.analyzeStream(s, 'ambitus')
    <music21.interval.Interval m21>
    ```

    ```python
    >>> analysis.discrete.analyzeStream(s, 'key')
    <music21.key.Key of f# minor>
    >>> analysis.discrete.analyzeStream(s, 'span')
    <music21.interval.Interval m21>
    ```

    Note that the same results can be obtained by calling “analyze” directly on the stream object:
    >>> s.analyze(‘key’)
    <music21.key.Key of f# minor>
    >>> s.analyze(‘span’)
    <music21.interval.Interval m21>

music21.analysis.discrete.analysisClassFromMethodName(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[DiscreteAnalysis](#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/analysis/discrete.html#analysisClassFromMethodName)
:   Returns an analysis class given a method name, or None if none can be found

    Searches first the class name, then the .identifiers array for each class,
    then a subset of any identifier.

    ```python
    >>> acfmn = analysis.discrete.analysisClassFromMethodName
    >>> acfmn('aarden')
    <class 'music21.analysis.discrete.AardenEssen'>
    >>> acfmn('span')
    <class 'music21.analysis.discrete.Ambitus'>
    ```

    This one is fundamentally important:

    ```python
    >>> acfmn('key')
    <class 'music21.analysis.discrete.AardenEssen'>
    ```

    ```python
    >>> print(repr(acfmn('unknown-format')))
    None
    ```
