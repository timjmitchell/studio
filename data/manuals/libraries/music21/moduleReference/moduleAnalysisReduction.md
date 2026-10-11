Source: https://music21.org/music21docs/moduleReference/moduleAnalysisReduction.html

# music21.analysis.reduction

Tools for generation reduction displays, showing a score and or a chord reduction,
and one or more reductive representation lines.

Used by graph.PlotHorizontalBarWeighted()

## PartReduction

class music21.analysis.reduction.PartReduction(*srcScore=None*, *\**, *partGroups: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fillByMeasure: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *segmentByTarget: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *normalize: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *normalizeByPart: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*keywords*)[[source]](../_modules/music21/analysis/reduction.html#PartReduction)
:   A part reduction reduces a Score into one or more parts.
    Parts are combined based on a part group dictionary.
    Each resulting part is then segmented by an object.
    This object is assigned as floating-point value.

    This reduction is designed to work with the GraphHorizontalBarWeighted and related Plot
    subclasses.

    If the fillByMeasure parameter is True, and if measures are available,
    each part will segment by Measure divisions, and look for the target activity only
    once per Measure.

    If more than one target is found in the Measure, values will be averaged.

    If fillByMeasure is False, the part will be segmented by each Note.

    The segmentByTarget parameter is True, segments, which may be Notes or Measures,
    will be divided if necessary to show changes that occur over the duration of the
    segment by a target object.

    If the normalizeByPart parameter is True, each part will be normalized within
    the range only of that part. If False, all parts will be normalized by the max
    of all parts. The default is True.

    If the normalize parameter is False, no normalization will take place. The default is True.

[`PartReduction`](#music21.analysis.reduction.PartReduction "music21.analysis.reduction.PartReduction") methods

PartReduction.getGraphHorizontalBarWeightedData()[[source]](../_modules/music21/analysis/reduction.html#PartReduction.getGraphHorizontalBarWeightedData)
:   Get all data organized into bar span specifications.

PartReduction.process()[[source]](../_modules/music21/analysis/reduction.html#PartReduction.process)
:   Core processing routines.

## ReductiveNote

class music21.analysis.reduction.ReductiveNote(*specification*, *inputNote*, *measureIndex*, *measureOffset*)[[source]](../_modules/music21/analysis/reduction.html#ReductiveNote)
:   The extraction of an event from a score and specification of where
    and how it should be presented in a reductive score.

    A specification string, as well as Note, must be provided for parsing.

    A specification must be created when access the Measure that the source note
    is found in. Storing the measure and index position provides significant
    performance optimization, as we do no have to search
    every note when generated the reduction.

    The measureIndex is the index of measure where this is found, not
    the measure number. The measureOffset is the position in the measure
    specified by the index.

[`ReductiveNote`](#music21.analysis.reduction.ReductiveNote "music21.analysis.reduction.ReductiveNote") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ReductiveNote`](#music21.analysis.reduction.ReductiveNote "music21.analysis.reduction.ReductiveNote") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ReductiveNote`](#music21.analysis.reduction.ReductiveNote "music21.analysis.reduction.ReductiveNote") methods

ReductiveNote.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/analysis/reduction.html#ReductiveNote.__getitem__)

ReductiveNote.getNoteAndTextExpression()[[source]](../_modules/music21/analysis/reduction.html#ReductiveNote.getNoteAndTextExpression)
:   Produce a new note, a deep copy of the supplied note
    and with the specified modifications.

ReductiveNote.isParsed() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/analysis/reduction.html#ReductiveNote.isParsed)

## ScoreReduction

class music21.analysis.reduction.ScoreReduction(*\*\*keywords*)[[source]](../_modules/music21/analysis/reduction.html#ScoreReduction)
:   An object to reduce a score.

[`ScoreReduction`](#music21.analysis.reduction.ScoreReduction "music21.analysis.reduction.ScoreReduction") read/write properties

ScoreReduction.chordReduction
:   Get or set a Chord reduction as a Stream or Score. Setting the this values
    set a deepcopy of the reduction; the reduction set here will not be altered.

ScoreReduction.score
:   Get or set the Score. Setting the score set a deepcopy of the score; the score
    set here will not be altered.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> sr = analysis.reduction.ScoreReduction()
    >>> sr.score = s
    ```

[`ScoreReduction`](#music21.analysis.reduction.ScoreReduction "music21.analysis.reduction.ScoreReduction") methods

ScoreReduction.reduce()[[source]](../_modules/music21/analysis/reduction.html#ScoreReduction.reduce)
:   Given a score, populate this Score reduction
