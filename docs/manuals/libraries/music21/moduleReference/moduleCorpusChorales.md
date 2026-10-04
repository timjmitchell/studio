Source: https://music21.org/music21docs/moduleReference/moduleCorpusChorales.html

# music21.corpus.chorales

This file makes it easier to access Bach’s chorales through various
numbering schemes and filters and includes the corpus.chorales.Iterator()
class for easily iterating through the chorale collection.

## ChoraleList

class music21.corpus.chorales.ChoraleList[[source]](../_modules/music21/corpus/chorales.html#ChoraleList)
:   A searchable list of Bach’s chorales by various numbering systems:

    Note that multiple chorales share the same title, so it’s best to
    iterate over one of the other lists to get them all.

    The list of chorales comes from
    <https://en.wikipedia.org/wiki/List_of_chorale_harmonisations_by_Johann_Sebastian_Bach>
    which does not have all chorales in the Bärenreitter-Kirnberger or Riemenschneider
    numberings since it only includes BWV 250-438.

    ```python
    >>> bcl = corpus.chorales.ChoraleList()
    >>> info358 = bcl.byBudapest[358]
    >>> for key in sorted(list(info358)):
    ...   print(f'{key} {info358[key]}')
    baerenreiter 68
    budapest 358
    bwv 431
    kalmus 358
    notes None
    riemenschneider 68
    title Wenn wir in höchsten Nöten sein
    >>> c = corpus.parse('bach/bwv' + str(info358['bwv']))
    >>> c.show()  # shows Bach BWV431
    ```

    More fully:

    ```python
    >>> b = corpus.parse('bwv' + str(corpus.chorales.ChoraleList().byRiemenschneider[2]['bwv']))
    >>> b
    <music21.stream.Score ...>
    ```

[`ChoraleList`](#music21.corpus.chorales.ChoraleList "music21.corpus.chorales.ChoraleList") methods

ChoraleList.prepareList()[[source]](../_modules/music21/corpus/chorales.html#ChoraleList.prepareList)
:   puts a list of Bach Chorales into dicts of dicts called

    self.byBudapest
    self.byBWV
    self.byRiemenschneider

    etc.

## ChoraleListRKBWV

class music21.corpus.chorales.ChoraleListRKBWV[[source]](../_modules/music21/corpus/chorales.html#ChoraleListRKBWV)
:   A searchable list of Bach’s chorales by various numbering systems:

    Note that multiple chorales share the same title, so it’s best to
    iterate over one of the other lists to get them all.

    The list of chorales comes from Margaret Greentree (formerly at
    jsbchorales.net) who compiled
    all chorales in the corpus, but only had numbers for the kalmus,
    riemenschneider, and bwv numbering systems.

    ```python
    >>> bcl = corpus.chorales.ChoraleListRKBWV()
    >>> info155 = bcl.byRiemenschneider[155]
    >>> for key in sorted(list(info155)):
    ...   print(f'{key} {info155[key]}')
    bwv 344
    kalmus 173
    riemenschneider 155
    title Hilf, Herr Jesu, laß gelingen
    >>> c = corpus.parse('bach/bwv' + str(info155['bwv']))
    >>> c.show()  # shows Bach BWV344
    ```

    More fully:

    ```python
    >>> theNumber = corpus.chorales.ChoraleListRKBWV().byRiemenschneider[2]['bwv']
    >>> b = corpus.parse('bwv' + str(theNumber))
    >>> b
    <music21.stream.Score ...>
    ```

[`ChoraleListRKBWV`](#music21.corpus.chorales.ChoraleListRKBWV "music21.corpus.chorales.ChoraleListRKBWV") methods

ChoraleListRKBWV.prepareList()[[source]](../_modules/music21/corpus/chorales.html#ChoraleListRKBWV.prepareList)
:   puts a list of Bach Chorales into dicts of dicts called

    self.byKalmus
    self.byBWV
    self.byRiemenschneider
    self.byTitle

## Iterator

class music21.corpus.chorales.Iterator(*currentNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *highestNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *numberingSystem: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'riemenschneider'*, *returnType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'stream'*, *iterationType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'number'*, *analysis: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *numberList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *titleList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/corpus/chorales.html#Iterator)
:   This is a class for iterating over many Bach Chorales. It is designed
    to make it easier to use
    one of music21’s most accessible datasets. It will parse each chorale
    in the selected
    range in a lazy fashion so that a list of chorales need not be parsed up front. To select a
    range of chorales, first select a .numberingSystem
    (‘riemenschneider’, ‘bwv’, ‘kalmus’, ‘budapest’,
    ‘baerenreiter’, or ‘title’). Then, set .currentNumber to the lowest
    number in the range and
    .highestNumber to the highest in the range. This can either be done by catalogue number
    (iterationType = ‘number’) or by index (iterationType = ‘index’).

    Note that these numbers are 1-indexed (as most catalogues are) and
    unlike Python’s range feature, the final number is included.

    Changing the numberingSystem will reset the iterator and
    change the range values to span the entire numberList.
    The iterator can be initialized with three parameters
    (currentNumber, highestNumber, numberingSystem). For example
    corpus.chorales.Iterator(1, 26,’riemenschneider’) iterates
    through the riemenschneider numbered chorales from 1 to 26.
    Additionally, the following keywords can be set:

    * returnType = either ‘stream’ (default) or ‘filename’
    * iterationType = either ‘number’ or ‘index’
    * titleList = [list, of, titles]
    * numberList = [list, of, numbers]

    ```python
    >>> for chorale in corpus.chorales.Iterator(1, 4, returnType='filename'):
    ...    print(chorale)
    bach/bwv269
    bach/bwv347
    bach/bwv153.1
    bach/bwv86.6
    ```

    ```python
    >>> BCI = corpus.chorales.Iterator()
    >>> BCI.numberingSystem
    'riemenschneider'
    ```

    ```python
    >>> BCI.currentNumber
    1
    ```

    ```python
    >>> BCI.highestNumber
    371
    ```

    An Exception will be raised if the number set is not in the
    numbering system selected, or if the numbering system selected is not valid.

    ```python
    >>> BCI.currentNumber = 377
    Traceback (most recent call last):
    ...
    music21.corpus.chorales.BachException: 377 does not correspond to a
        chorale in the riemenschneider numbering system
    ```

    ```python
    >>> BCI.numberingSystem = 'not a numbering system'
    Traceback (most recent call last):
    ...
    music21.corpus.chorales.BachException: not a numbering system is not a valid
        numbering system for Bach Chorales.
    ```

    If the numberingSystem ‘title’ is selected, the iterator must be
    initialized with a list of titles.
    It will iterate through the titles in the order of the list.

    ```python
    >>> BCI.numberingSystem = 'title'
    >>> BCI.returnType = 'filename'
    >>> BCI.titleList = ['Jesu, meine Freude',
    ...                  'Gott hat das Evangelium',
    ...                  'Not a Chorale']
    'Not a Chorale' will be skipped because it is not a recognized title.
    ```

    ```python
    >>> for chorale in BCI:
    ...    print(chorale)
    bach/bwv358
    bach/bwv319
    ```

    The numberList, which, by default, includes all chorales in the chosen numberingSystem,
    can be set like the titleList. In the following example,
    note that the first chorale in the given
    numberList will not be part of the iteration because the
    first currentNumber is set to 2 at the
    start by the first argument. (If iterationType==’index’,
    setting the currentNumber to 1 and the highestNumber to 7
    would have the same effect as the given example.

    ```python
    >>> BCI = corpus.chorales.Iterator(2, 371, numberingSystem='riemenschneider',
    ...                                numberList=[1, 2, 3, 4, 6, 190, 371, 500],
    ...                                returnType='filename')
    500 will be skipped because it is not in the numberingSystem riemenschneider
    ```

    ```python
    >>> for chorale in BCI:
    ...    print(chorale)
    bach/bwv347
    bach/bwv153.1
    bach/bwv86.6
    bach/bwv281
    bach/bwv337
    bach/bwv278
    ```

    Elements in the iterator can be accessed by index as well as slice.

    ```python
    >>> for chorale in corpus.chorales.Iterator(returnType='filename')[4:10]:
    ...    print(chorale)
    bach/bwv86.6
    bach/bwv267
    bach/bwv281
    bach/bwv17.7
    bach/bwv40.8
    bach/bwv248.12-2
    bach/bwv38.6
    ```

    ```python
    >>> print(corpus.chorales.Iterator(returnType='filename')[55])
    bach/bwv121.6
    ```

    For the first 20 chorales in the Riemenschneider numbering system, there are professionally
    annotated roman numeral analyses in romanText format, courtesy of Dmitri Tymoczko of Princeton
    University. To get them as an additional part to the score set returnType to “stream”, and
    add a keyword “analysis = True”:

    If chorales are accessed through the Iterator(), the metadata.title attribute will have the
    correct German title. This is different from the metadata returned by the parser which does
    not give the German title but rather the BWV number.

    ```python
    >>> corpus.chorales.Iterator(returnType='stream')[1].metadata.title
    'Ich dank’ dir, lieber Herre'
    ```

[`Iterator`](#music21.corpus.chorales.Iterator "music21.corpus.chorales.Iterator") read/write properties

Iterator.currentNumber
:   The currentNumber is the number of the
    chorale (in the set numberingSystem) for the
    next chorale to be parsed by the iterator.
    It is initially the first chorale in whatever
    numberingSystem is set, but it can be changed
    to any other number in the numberingSystem
    as desired as long as it does not go above
    the highestNumber which is the boundary
    of the iteration.

Iterator.highestNumber
:   The highestNumber is the number of the chorale
    (in the set numberingSystem) for the
    last chorale to be parsed by the iterator.
    It is initially the highest numbered chorale in whatever
    numberingSystem is set, but it can be changed
    to any other number in the numberingSystem
    as desired as long as it does not go below
    the currentNumber of the iteration.

Iterator.iterationType
:   This property determines how boundary numbers are
    interpreted, as indices or as catalogue numbers.

Iterator.numberList
:   Allows access to the catalogue numbers
    (or indices if iterationType == ‘index’)
    that will be iterated over. This can be
    set to a specific list of numbers.
    The list will be sorted.

Iterator.numberingSystem
:   This property determines which numbering
    system to iterate through chorales with.
    It can be set to ‘bwv’, ‘kalmus’, ‘baerenreiter’,
    ‘budapest’, or ‘riemenschneider’.
    It can also be set to ‘title’ in which case the
    iterator needs to be given a list
    of chorale titles in .titleList. At this time,
    the titles need to be exactly as they
    appear in the dictionary it queries.

Iterator.returnType
:   This property determines what the iterator
    returns; ‘stream’ is the default and causes the iterator to parse
    each chorale. If this is set to ‘filename’, the
    iterator will return the filename of each chorale but not
    parse it.

Iterator.titleList
:   A list of titles to iterate over
    if .numberingSystem is set to ‘title’.

[`Iterator`](#music21.corpus.chorales.Iterator "music21.corpus.chorales.Iterator") methods

Iterator.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/corpus/chorales.html#Iterator.__getitem__)

## Functions

music21.corpus.chorales.getByTitle(*title*)[[source]](../_modules/music21/corpus/chorales.html#getByTitle)
:   Return a Chorale by title (or title fragment) or None

    ```python
    >>> germanTitle = "Sach' Gott heimgestellt"
    >>> c = corpus.chorales.getByTitle(germanTitle)
    >>> c.metadata.title
    "Ich hab' mein' Sach' Gott heimgestellt"
    ```
