Source: https://music21.org/music21docs/moduleReference/moduleSearchSegment.html

# music21.search.segment

tools for segmenting – that is, dividing up a score into small, possibly overlapping
sections – for searching across pieces for similarity.

Speed notes:

> this module is definitely a case where running PyPy rather than cPython will
> give you a 3-5x speedup.
>
> If you really want to do lots of comparisons, the scoreSimilarity method will
> use python-Levenshtein if it is installed, unless forceDifflib is set to True.
> python-Levenshtein can be installed via **pip install python-Levenshtein**.
> The ratios are very slightly different, but the speedup is between 10 and 100x!
> (But then PyPy probably won’t work.)

## Functions

music21.search.segment.getDifflibOrPyLev(*seq2=None*, *junk=None*, *forceDifflib=False*)[[source]](../_modules/music21/search/segment.html#getDifflibOrPyLev)
:   Returns either a difflib.SequenceMatcher or pyLevenshtein
    StringMatcher.StringMatcher object depending on what is installed.

    If forceDifflib is True then use difflib even if pyLevenshtein is installed:

music21.search.segment.indexOnePath(*filePath*, *\*\*keywords*)[[source]](../_modules/music21/search/segment.html#indexOnePath)
:   Index a single path. Returns a scoreDictEntry

music21.search.segment.indexScoreFilePaths(*scoreFilePaths*, *\**, *giveUpdates=False*, *runMulticore=True*, *\*\*keywords*)[[source]](../_modules/music21/search/segment.html#indexScoreFilePaths)
:   Returns a dictionary of the lists from indexScoreParts for each score in
    scoreFilePaths

    ```python
    >>> searchResults = corpus.search('bwv190')
    >>> fpsNamesOnly = sorted([searchResult.sourcePath for searchResult in searchResults])
    >>> len(fpsNamesOnly)
    2
    ```

    ```python
    >>> scoreDict = search.segment.indexScoreFilePaths(fpsNamesOnly)
    >>> len(scoreDict['bwv190.7.mxl'])
    4
    ```

    ```python
    >>> scoreDict['bwv190.7.mxl'][0]['measureList']
    [(0, 9), (6, 15), (11, 20), (17, 25), (22, 31), (27, 32)]
    ```

    ```python
    >>> scoreDict['bwv190.7.mxl'][0]['segmentList'][0]
    'NNJLNOLLLJJIJLLLLNJJJIJLLJNNJL'
    ```

music21.search.segment.indexScoreParts(*scoreFile*, *\*\*keywords*)[[source]](../_modules/music21/search/segment.html#indexScoreParts)
:   Creates segment and measure lists for each part of a score
    Returns list of dictionaries of segment and measure lists

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> scoreList = search.segment.indexScoreParts(bach)
    >>> scoreList[1]['segmentList'][0]
    '@B@@@@ED@DBDA=BB@?==B@@EBBDBBA'
    >>> scoreList[1]['measureList'][0:3]
    [(0, 7), (4, 9), (8, 9)]
    ```

music21.search.segment.loadScoreDict(*filePath*)[[source]](../_modules/music21/search/segment.html#loadScoreDict)
:   Load the scoreDictionary from filePath.

music21.search.segment.saveScoreDict(*scoreDict*, *filePath=None*)[[source]](../_modules/music21/search/segment.html#saveScoreDict)
:   Save the score dict from indexScoreFilePaths as a .json file for quickly
    reloading

    Returns the filepath (assumes you’ll probably be using a temporary file)
    as a pathlib.Path()

music21.search.segment.scoreSimilarity(*scoreDict*, *minimumLength=20*, *giveUpdates=False*, *includeReverse=False*, *forceDifflib=False*)[[source]](../_modules/music21/search/segment.html#scoreSimilarity)
:   Find the level of similarity between each pair of segments in a scoreDict.

    This takes twice as long as it should because it does not cache the
    pairwise similarity.

    ```python
    >>> filePaths = []
    >>> for p in ('bwv197.5.mxl', 'bwv190.7.mxl', 'bwv197.10.mxl'):
    ...     source = corpus.search(p)[0].sourcePath
    ...     filePaths.append(source)
    >>> scoreDict = search.segment.indexScoreFilePaths(filePaths)
    >>> scoreSim = search.segment.scoreSimilarity(scoreDict)
    >>> len(scoreSim)
    496
    ```

    Returns a list of tuples of first score name, first score voice number, first score
    measure number, second score name, second score voice number, second score
    measure number, and similarity score (0 to 1).

    ```python
    >>> for result in scoreSim[133:137]:
    ...     result
    ('bwv197.5.mxl', 1, 1, (4, 10), 'bwv190.7.mxl', 3, 4, (22, 30), 0.13...)
    ('bwv197.5.mxl', 1, 1, (4, 10), 'bwv197.10.mxl', 0, 0, (0, 8), 0.2)
    ('bwv197.5.mxl', 1, 1, (4, 10), 'bwv197.10.mxl', 1, 0, (0, 7), 0.266...)
    ('bwv197.5.mxl', 1, 1, (4, 10), 'bwv197.10.mxl', 1, 1, (4, 9), 0.307...)
    ```

music21.search.segment.translateMonophonicPartToSegments(*inputStream*, *\**, *segmentLengths=30*, *overlap=12*, *algorithm=None*, *jitter=0*)[[source]](../_modules/music21/search/segment.html#translateMonophonicPartToSegments)
:   Translates a monophonic part with measures to a set of segments of length
    segmentLengths (measured in number of notes) with an overlap of overlap notes
    using a conversion algorithm of algorithm (default: search.translateStreamToStringNoRhythm).
    Returns two lists, a list of segments, and a list of tuples of measure start and end
    numbers that match the segments.

    If algorithm is None then a default algorithm of music21.search.translateStreamToStringNoRhythm
    is used

    ```python
    >>> luca = corpus.parse('luca/gloria')
    >>> lucaCantus = luca.parts[0]
    >>> segments, measureLists = search.segment.translateMonophonicPartToSegments(lucaCantus)
    >>> segments[0:2]
    ['HJHEAAEHHCE@JHGECA@A>@A><A@AAE', '@A>@A><A@AAEEECGHJHGH@CAE@FECA']
    ```

    Segment zero begins at measure 1 and ends in m. 12. Segment 1 spans m.7 - m.18:

    ```python
    >>> measureLists[0:2]
    [(1, 12), (7, 18)]
    ```

    ```python
    >>> segments, measureLists = search.segment.translateMonophonicPartToSegments(
    ...     lucaCantus,
    ...     algorithm=search.translateDiatonicStreamToString)
    >>> segments[0:2]
    ['CRJOMTHCQNALRQPAGFEFDLFDCFEMOO', 'EFDLFDCFEMOOONPJDCBJSNTHLBOGFE']
    ```

    ```python
    >>> measureLists[0:2]
    [(1, 12), (7, 18)]
    ```
