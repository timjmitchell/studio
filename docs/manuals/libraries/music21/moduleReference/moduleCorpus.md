Source: https://music21.org/music21docs/moduleReference/moduleCorpus.html

# music21.corpus

The music21 corpus includes a collection of freely distributable
music in MusicXML, Humdrum, and other representations. The corpus
package is an interface for easily working with this data.

To see a complete listing of the works in the music21 corpus,
visit [List of Works Found in the music21 Corpus](../about/referenceCorpus.html#referencecorpus). Note that music21 does not own
most of the music in the corpus – it has been licensed to us (or
in a free license). It may not be free in all parts of the world,
but to the best of our knowledge is true for the US.

Use corpus.parse if you know the name of a file in the corpus:

```python
>>> b = corpus.parse('bwv66.6')
>>> b
<music21.stream.Score bach/bwv66.6.mxl>
```

And use corpus.search if you do not:

```python
>>> cb = corpus.search('shandy')
>>> cb
<music21.metadata.bundles.MetadataBundle {1 entry}>
>>> cb[0]
<music21.metadata.bundles.MetadataEntry 'airdsAirs_book1_abc_191'>
>>> cb[0].parse()
<music21.stream.Score airdsAirs/book1.abc>
```

## Functions

music21.corpus.addPath(*filePath*, *corpusName=None*)[[source]](../_modules/music21/corpus.html#addPath)
:   Add a directory path to the Local Corpus on a *temporary* basis, i.e., just
    for the current Python session.

    All directories contained within the provided directory will be searched
    for files with file extensions matching the currently readable file types.
    Any number of file paths can be added one at a time.

    An error will be raised if the file path does not exist, is already defined
    as a temporary, or is already being searched by being defined with the
    [`Environment`](moduleEnvironment.html#music21.environment.Environment "music21.environment.Environment") ‘localCorpusSettings’ setting.

    To permanently add a path to the list of stored local corpus paths,
    set the ‘localCorpusPath’ or ‘localCorpusSettings’ setting of
    the [`UserSettings`](moduleEnvironment.html#music21.environment.UserSettings "music21.environment.UserSettings") object.

    ```python
    >>> corpus.addPath('~/Documents')
    ```

    Alternatively, add a directory permanently (see link above
    for more details):

    ```python
    >>> us = environment.UserSettings()
    >>> us['localCorpusPath'] = 'd:/desktop/'
    ```

    Restart music21 after adding paths.

music21.corpus.cacheMetadata(*corpusNames=('local',)*, *verbose=True*)[[source]](../_modules/music21/corpus.html#cacheMetadata)
:   Rebuild the metadata cache.

music21.corpus.getComposer(*composerName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*)[[source]](../_modules/music21/corpus.html#getComposer)
:   Return all filenames in the corpus that match a composer’s or a
    collection’s name. An fileExtensions, if provided, defines which
    extensions are returned. An fileExtensions of None (default) returns all
    extensions.

    Note that xml and mxl are treated equivalently.

    ```python
    >>> a = corpus.getComposer('schoenberg')
    >>> len(a) > 1
    True
    ```

    ```python
    >>> a = corpus.getComposer('bach', fileExtensions=('krn',))
    >>> len(a) < 10
    True
    ```

    ```python
    >>> a = corpus.getComposer('bach', fileExtensions=('xml',))
    >>> len(a) > 10
    True
    ```

music21.corpus.getCorePaths(*\**, *fileExtensions: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *expandExtensions=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus.html#getCorePaths)
:   Get all paths in the corpus that match a known extension, or an extension
    provided by an argument.

    If expandExtensions is True, a format for an extension, and related
    extensions, will be replaced by all known input extensions.

    This is convenient when an input format might match for multiple
    extensions.

    ```python
    >>> corpusFilePaths = corpus.getCorePaths()
    >>> cpl = len(corpusFilePaths)
    >>> 3000 < cpl < 4000
    True
    ```

    ```python
    >>> kernFilePaths = corpus.getCorePaths(fileExtensions=('krn',))
    >>> len(kernFilePaths) >= 500
    True
    ```

    ```python
    >>> abcFilePaths = corpus.getCorePaths(fileExtensions=('abc',))
    >>> len(abcFilePaths) >= 100
    True
    ```

music21.corpus.getLocalPaths(*\**, *fileExtensions: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *expandExtensions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus.html#getLocalPaths)
:   Access files in additional directories supplied by the user and defined in
    environment settings in the ‘localCorpusSettings’ list.

    If additional paths are added on a per-session basis with the
    [`addPath()`](#music21.corpus.addPath "music21.corpus.addPath") function, these paths are also returned
    with this method.

music21.corpus.getPaths(*\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *expandExtensions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *name: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ('local', 'core')*)[[source]](../_modules/music21/corpus.html#getPaths)
:   Get paths from core and/or local corpora.
    This is the public interface for getting all corpus
    paths with one function.

music21.corpus.getWork(*workName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *movementNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *fileExtensions: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*) → [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus.html#getWork)
:   Search all Corpora for a work, and return a file path.
    N.B. does not parse the work: but it’s suitable for passing
    to converter.parse.

    This method will return either a list of file paths or, if there is a
    single match, a single file path. If no matches are found an Exception is
    raised.

    ```python
    >>> import os, pathlib
    >>> luca = corpus.getWork('luca/gloria')
    >>> isinstance(luca, pathlib.Path)
    True
    >>> luca.name
    'gloria.xml'
    >>> luca.parent.name
    'luca'
    ```

    Multiple works give multiple paths.

    ```python
    >>> trecentoFiles = corpus.getWork('trecento')
    >>> isinstance(trecentoFiles, list)
    True
    >>> isinstance(trecentoFiles[0], pathlib.Path)
    True
    >>> 100 < len(trecentoFiles) < 200
    True
    ```

    Note: if the Virtual corpus is ever brought back, it may return a URL.

music21.corpus.noCorpus()[[source]](../_modules/music21/corpus.html#noCorpus)
:   Return True or False if this is a corpus or noCorpus distribution.

    ```python
    >>> corpus.noCorpus()
    False
    ```

music21.corpus.parse(*workName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *movementNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fileExtensions: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *forceSource: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *format: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/corpus.html#parse)
:   The most important method call for corpus.

    Similar to the [`parse()`](moduleConverter.html#music21.converter.parse "music21.converter.parse") function of converter (which
    takes in a filepath on the local hard drive), this function searches the
    corpus (including local corpora) for a work fitting the workName
    description and returns a `music21.stream.Stream`.

    If movementNumber is defined, and a movement is included in the corpus,
    that movement will be returned.

    If number is defined, and the work is a collection with multiple
    components, that work number will be returned. For instance, some of our
    ABC documents contain dozens of folk songs within a single file.

    Advanced: if forceSource is True, the original file will always be loaded
    freshly and pickled (e.g., pre-parsed) files will be ignored. This should
    not be needed if the file has been changed, since the filetime of the file
    and the filetime of the pickled version are compared. But it might be
    needed if the music21 parsing routine has changed.

    Example, get a chorale by Bach. Note that the source type does not need to
    be specified, nor does the name Bach even (since it’s the only piece with
    the title BWV 66.6)

    ```python
    >>> bachChorale = corpus.parse('bwv66.6')
    >>> len(bachChorale.parts)
    4
    ```

    After parsing, the file path within the corpus is stored as
    .metadata.corpusFilePath

    ```python
    >>> bachChorale.metadata.corpusFilePath
    'bach/bwv66.6.mxl'
    ```

    Changed in v9: corpusFilePath is stored in metadata and now has a capital ‘P’
