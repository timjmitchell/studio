Source: https://music21.org/music21docs/moduleReference/moduleAnalysisPitchAnalysis.html

# music21.analysis.pitchAnalysis

## Functions

music21.analysis.pitchAnalysis.pitchAttributeCount(*s*, *pitchAttr='name'*)[[source]](../_modules/music21/analysis/pitchAnalysis.html#pitchAttributeCount)
:   Return a collections.Counter of pitch class usage (count)
    by selecting an attribute of the Pitch object.

    * Changed in v4: Returns a collections.Counter object.

    ```python
    >>> bach = corpus.parse('bach/bwv324.xml')
    >>> pcCount = analysis.pitchAnalysis.pitchAttributeCount(bach, 'pitchClass')
    >>> for n in sorted(pcCount):
    ...     print(f'{n:2d}: {pcCount[n]:2d}')
     0:  3
     2: 26
     3:  3
     4: 13
     6: 15
     7: 13
     9: 17
    11: 14
    ```

    List in most common order:

    ```python
    >>> nameCount = analysis.pitchAnalysis.pitchAttributeCount(bach, 'name')
    >>> for n, count in nameCount.most_common(3):
    ...     print(f'{n:>2s}: {nameCount[n]:2d}')
     D: 26
     A: 17
    F#: 15
    ```

    ```python
    >>> nameOctaveCount = analysis.pitchAnalysis.pitchAttributeCount(bach, 'nameWithOctave')
    >>> for n in sorted(nameOctaveCount):
    ...     print(f'{n:>3s}: {nameOctaveCount[n]:2d}')
     A2:  2
     A3:  5
     A4: 10
     B2:  3
     B3:  4
     B4:  7
     C3:  2
     C5:  1
    D#3:  1
    D#4:  2
    ...
    ```
