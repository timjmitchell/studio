Source: https://music21.org/music21docs/moduleReference/moduleAnalysisSegmentByRests.html

# music21.analysis.segmentByRests

## Segmenter

class music21.analysis.segmentByRests.Segmenter[[source]](../_modules/music21/analysis/segmentByRests.html#Segmenter)
:   Given a work or part, returns a list of melodic segments or intervals.

[`Segmenter`](#music21.analysis.segmentByRests.Segmenter "music21.analysis.segmentByRests.Segmenter") methods

classmethod Segmenter.getIntervalList(*workOrPart*)[[source]](../_modules/music21/analysis/segmentByRests.html#Segmenter.getIntervalList)
:   Given a work or part, returns a list of intervals between contiguous notes.
    NB Uses .recurse() internally so
    if called on a work then returns a list of lists with one list per part.

    ```python
    >>> example = converter.parse("tinyNotation: 4/4 E4 r F G A r g c r c")
    >>> intList = analysis.segmentByRests.Segmenter.getIntervalList(example)
    >>> [x.name for x in intList]
    ['M2', 'M2', 'P5']
    ```

classmethod Segmenter.getSegmentsList(*workOrPart*, *removeEmptyLists=True*)[[source]](../_modules/music21/analysis/segmentByRests.html#Segmenter.getSegmentsList)
:   Segments a part by its rests (and clefs) and returns a list of lists where
    each sublist is one segment of contiguous notes. NB Uses .recurse() internally.

    ```python
    >>> example = converter.parse("tinyNotation: C4 r D E r r F r G r A B r c")
    >>> segments = analysis.segmentByRests.Segmenter.getSegmentsList(example)
    >>> segments
    [[<music21.note.Note C>],
     [<music21.note.Note D>, <music21.note.Note E>],
     [<music21.note.Note F>],
     [<music21.note.Note G>],
     [<music21.note.Note A>, <music21.note.Note B>],
     [<music21.note.Note C>]]
    ```
