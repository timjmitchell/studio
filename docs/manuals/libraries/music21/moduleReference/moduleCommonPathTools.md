Source: https://music21.org/music21docs/moduleReference/moduleCommonPathTools.html

# music21.common.pathTools

## Functions

music21.common.pathTools.cleanpath(*path: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *\**, *returnPathlib: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[None] = None*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/common/pathTools.html#cleanpath)

music21.common.pathTools.cleanpath(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *returnPathlib: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[None] = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

music21.common.pathTools.cleanpath(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *\**, *returnPathlib: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")

music21.common.pathTools.cleanpath(*path: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *\**, *returnPathlib: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
:   Normalizes the path by expanding ~user on Unix, ${var} environmental vars
    (is this a good idea?), expanding %name% on Windows, normalizing path names
    (Windows turns backslashes to forward slashes), and finally if that file
    is not an absolute path, turns it from a relative path to an absolute path.

    v5 – returnPathlib – None (default) does not convert. False, returns a string,
    True, returns a pathlib.Path.

music21.common.pathTools.getCorpusContentDirs() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/common/pathTools.html#getCorpusContentDirs)
:   Get all dirs that are found in the CoreCorpus that contain content;
    that is, exclude dirs that have code or other resources.

    ```python
    >>> fp = common.getCorpusContentDirs()
    >>> fp  # this list will be fragile, depending on composition of dirs
    ['airdsAirs', 'bach', 'beach', 'beethoven', 'chopin',
     'ciconia', 'corelli', 'cpebach',
     'demos', 'essenFolksong', 'handel', 'haydn', 'johnson_j_r', 'joplin', 'josquin',
     'leadSheet', 'liliuokalani', 'luca', 'lusitano',
     'miscFolk', 'monteverdi', 'mozart',
     'nottingham-dataset',
     'oneills1850', 'palestrina',
     'ryansMammoth', 'schoenberg', 'schubert', 'schumann_clara', 'schumann_robert',
     'theoryExercises', 'trecento', 'verdi', 'weber', 'webern']
    ```

    Make sure that all corpus data has a directoryInformation tag in
    CoreCorpus.

    ```python
    >>> cc = corpus.corpora.CoreCorpus()
    >>> failed = []
    >>> di = [d.directoryName for d in cc.directoryInformation]
    >>> for f in fp:
    ...     if f not in di:
    ...         failed.append(f)
    >>> failed
    []
    ```

music21.common.pathTools.getCorpusFilePath() → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/common/pathTools.html#getCorpusFilePath)
:   Get the stored music21 directory that contains the corpus metadata cache.

    ```python
    >>> fp = common.getCorpusFilePath()
    >>> fp.name == 'corpus' and fp.parent.name == 'music21'
    True
    ```

music21.common.pathTools.getMetadataCacheFilePath() → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/common/pathTools.html#getMetadataCacheFilePath)
:   Get the stored music21 directory that contains the corpus metadata cache.

    ```python
    >>> fp = common.getMetadataCacheFilePath()
    >>> fp.name == '_metadataCache' and fp.parent.name == 'corpus'
    True
    ```

music21.common.pathTools.getRootFilePath() → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/common/pathTools.html#getRootFilePath)
:   Return the root directory for music21 – outside the music21 namespace
    which has directories such as “dist”, “documentation”, “music21”

    ```python
    >>> fp = common.getRootFilePath()
    >>> fp
    PosixPath('/Users/florencePrice/git/music21')
    ```

music21.common.pathTools.getSourceFilePath() → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/common/pathTools.html#getSourceFilePath)
:   Get the music21 directory that contains source files such as note.py, etc.
    This is not the same as the
    outermost package development directory.

music21.common.pathTools.relativepath(*path: StrOrPath*, *start: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → StrOrPath | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/pathTools.html#relativepath)
:   A cross-platform wrapper for os.path.relpath(), which returns path if
    under Windows, otherwise returns the relative path of path.

    This avoids problems under Windows when the current working directory is
    on a different drive letter from path.
