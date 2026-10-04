Source: https://music21.org/music21docs/moduleReference/moduleCorpusCorpora.html

# music21.corpus.corpora

## Corpus

class music21.corpus.corpora.Corpus[[source]](../_modules/music21/corpus/corpora.html#Corpus)
:   Abstract base class of all corpora subclasses.

[`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus") read-only properties

Corpus.cacheFilePath

Corpus.directoryInformation
:   Returns a tuple of DirectoryInformation objects for
    each directory in self.\_directoryInformation.

    ```python
    >>> core = corpus.corpora.CoreCorpus()
    >>> diBrief = core.directoryInformation[0:5]
    >>> diBrief
    (<music21.corpus.work.DirectoryInformation airdsAirs>,
     <music21.corpus.work.DirectoryInformation bach>,
     <music21.corpus.work.DirectoryInformation beach>,
     <music21.corpus.work.DirectoryInformation beethoven>,
     <music21.corpus.work.DirectoryInformation chopin>)
    >>> diBrief[2].directoryTitle
    'Amy Beach'
    ```

Corpus.metadataBundle
:   The metadata bundle for a corpus:

    ```python
    >>> corpus.corpora.CoreCorpus().metadataBundle
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    ```

    As a technical aside, the metadata bundle for a corpus is actually
    stored in corpus.manager, in order to cache most effectively over
    multiple calls. There might be good reasons to eventually move them
    to each Corpus object, so long as its cached across instances of the
    class.

Corpus.name
:   The name of a given corpus.

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus") methods

Corpus.all() → [bundles.MetadataBundle](moduleMetadataBundles.html#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle")[[source]](../_modules/music21/corpus/corpora.html#Corpus.all)
:   This is a synonym for the metadataBundle property, but easier to understand
    what it does.

    ```python
    >>> corpus.corpora.CoreCorpus().all()
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    ```

Corpus.cacheMetadata(*useMultiprocessing=True*, *verbose=True*, *timer=None*)[[source]](../_modules/music21/corpus/corpora.html#Corpus.cacheMetadata)
:   Cache the metadata for a single corpus.

Corpus.getComposer(*composerName*, *\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*)[[source]](../_modules/music21/corpus/corpora.html#Corpus.getComposer)
:   Return all filenames in the corpus that match a composer’s or a
    collection’s name. A fileExtensions, if provided, defines which
    extensions are returned. A fileExtensions of (), (default) returns
    all extensions.

    Note that xml and mxl are treated equivalently.

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    >>> a = coreCorpus.getComposer('bach')
    >>> len(a) > 100
    True
    ```

    ```python
    >>> a = coreCorpus.getComposer('bach', fileExtensions=['krn'])
    >>> len(a) < 10
    True
    ```

    ```python
    >>> a = coreCorpus.getComposer('bach', fileExtensions=('xml',))
    >>> len(a) > 10
    True
    ```

abstractmethod Corpus.getPaths(*\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *expandExtensions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus/corpora.html#Corpus.getPaths)
:   The paths of the files in a given corpus.

Corpus.getWorkList(*workName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *movementNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*)[[source]](../_modules/music21/corpus/corpora.html#Corpus.getWorkList)
:   Search the corpus and return a list of filenames of works, always in a
    list.

    If no matches are found, an empty list is returned.

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    ```

    This returns 1 even though there is a ‘.mus’ file, which cannot be read:

    ```python
    >>> len(coreCorpus.getWorkList('cpebach/h186'))
    1
    >>> len(coreCorpus.getWorkList('cpebach/h186', None, fileExtensions=['.xml']))
    1
    ```

    ```python
    >>> len(coreCorpus.getWorkList('schumann_clara/opus17', 3))
    1
    >>> len(coreCorpus.getWorkList('schumann_clara/opus17', 2))
    0
    ```

    Note that ‘verdi’ just gets the single Verdi piece and not the
    Monteverdi pieces:

    ```python
    >>> len(coreCorpus.getWorkList('verdi'))
    1
    ```

Corpus.getWorkReferences()[[source]](../_modules/music21/corpus/corpora.html#Corpus.getWorkReferences)
:   Return a data dictionary for all works in this corpus
    Returns a list of corpus.work.DirectoryInformation objects, one
    for each directory. A ‘works’ dictionary for each composer
    provides references to dictionaries for all associated works.

    This is used in the generation of corpus documentation

    ```python
    >>> workRefs = corpus.corpora.CoreCorpus().getWorkReferences()
    >>> workRefs[1:3]
    [<music21.corpus.work.DirectoryInformation bach>,
     <music21.corpus.work.DirectoryInformation beach>]
    ```

Corpus.rebuildMetadataCache(*useMultiprocessing=True*, *verbose=True*)[[source]](../_modules/music21/corpus/corpora.html#Corpus.rebuildMetadataCache)
:   Rebuild a named bundle from scratch.

    If a bundle is associated with one of music21’s corpora, delete any
    metadata cache on disk, clear the bundle’s contents and reload in all
    files from that associated corpus.

    Return the rebuilt metadata bundle.

Corpus.search(*query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *field: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\*\*keywords*)[[source]](../_modules/music21/corpus/corpora.html#Corpus.search)
:   Search this corpus for metadata entries, returning a metadataBundle

    ```python
    >>> corpus.corpora.CoreCorpus().search('3/4')
    <music21.metadata.bundles.MetadataBundle {1875 entries}>
    ```

    ```python
    >>> corpus.corpora.CoreCorpus().search(
    ...      'bach',
    ...      field='composer',
    ...      )
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> predicate = lambda noteCount: noteCount < 20
    >>> corpus.corpora.CoreCorpus().search(
    ...     predicate,
    ...     field='noteCount',
    ...     )
    <music21.metadata.bundles.MetadataBundle {134 entries}>
    ```

static Corpus.translateExtensions(*fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\**, *expandExtensions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...][[source]](../_modules/music21/corpus/corpora.html#Corpus.translateExtensions)
:   Utility to get default extensions, or, optionally, expand extensions to
    all known formats.

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    >>> for extension in coreCorpus.translateExtensions():
    ...     extension
    ...
    '.abc'
    '.capx'
    '.mid'
    '.midi'
    '.xml'
    '.mxl'
    '.musicxml'
    '.md'
    '.musedata'
    '.zip'
    '.krn'
    '.rntxt'
    '.rntext'
    '.romantext'
    '.rtxt'
    '.nwctxt'
    '.nwc'
    ```

    ```python
    >>> coreCorpus.translateExtensions(('.mid',), expandExtensions=False)
    ('.mid',)
    ```

    ```python
    >>> coreCorpus.translateExtensions(('.mid',), expandExtensions=True)
    ('.mid', '.midi')
    ```

    It does not matter if you choose a canonical name or not, the output is the same:

    ```python
    >>> coreCorpus.translateExtensions(('.musicxml',), expandExtensions=True)
    ('.xml', '.mxl', '.musicxml')
    ```

    ```python
    >>> coreCorpus.translateExtensions(('.xml',), expandExtensions=True)
    ('.xml', '.mxl', '.musicxml')
    ```

    Leading dots don’t matter:

    ```python
    >>> coreCorpus.translateExtensions(('xml',))
    ('.xml', '.mxl', '.musicxml')
    ```

    # With multiple extensions:

    ```python
    >>> coreCorpus.translateExtensions(('.mid', '.musicxml'), expandExtensions=False)
    ('.mid', '.musicxml')
    >>> coreCorpus.translateExtensions(('.mid', '.musicxml'))
    ('.mid', '.midi', '.xml', '.mxl', '.musicxml')
    ```

    * Changed in v9: returns a tuple, not a list. first element must be an Iterable of strings

    TODO: unify with tools in common.formats

## CoreCorpus

class music21.corpus.corpora.CoreCorpus[[source]](../_modules/music21/corpus/corpora.html#CoreCorpus)
:   A model of the *core* corpus.

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    ```

[`CoreCorpus`](#music21.corpus.corpora.CoreCorpus "music21.corpus.corpora.CoreCorpus") bases

* [`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`CoreCorpus`](#music21.corpus.corpora.CoreCorpus "music21.corpus.corpora.CoreCorpus") read-only properties

CoreCorpus.cacheFilePath

CoreCorpus.noCorpus
:   Return True or False if this is a corpus or noCorpus distribution.

    ```python
    >>> corpus.corpora.CoreCorpus().noCorpus
    False
    ```

Read-only properties inherited from [`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus"):

|  |  |  |
| --- | --- | --- |
| * [`directoryInformation`](#music21.corpus.corpora.Corpus.directoryInformation "music21.corpus.corpora.Corpus.directoryInformation") | * [`metadataBundle`](#music21.corpus.corpora.Corpus.metadataBundle "music21.corpus.corpora.Corpus.metadataBundle") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`CoreCorpus`](#music21.corpus.corpora.CoreCorpus "music21.corpus.corpora.CoreCorpus") read/write properties

CoreCorpus.manualCoreCorpusPath
:   Set music21’s core corpus to a directory, and save that information in
    the user settings.

    This is specifically for use with “no corpus” music21 packages, where
    the core corpus was not included with the rest of the package
    functionality, and had to be installed separately.

    Set it to a directory:

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    >>> coreCorpus.manualCoreCorpusPath = '~/Desktop'
    ```

    Unset it:

    ```python
    >>> coreCorpus.manualCoreCorpusPath = None
    >>> coreCorpus.manualCoreCorpusPath is None
    True
    ```

[`CoreCorpus`](#music21.corpus.corpora.CoreCorpus "music21.corpus.corpora.CoreCorpus") methods

CoreCorpus.getPaths(*fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\**, *expandExtensions=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus/corpora.html#CoreCorpus.getPaths)
:   Get all paths in the core corpus that match a known extension, or an
    extension provided by an argument.

    If expandExtensions is True, a format for an extension, and related
    extensions, will be replaced by all known input extensions.

    This is convenient when an input format might match for multiple
    extensions.

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    >>> corpusFilePaths = coreCorpus.getPaths()
    >>> 3000 < len(corpusFilePaths) < 4000
    True
    ```

    ```python
    >>> kernFilePaths = coreCorpus.getPaths(['krn'])
    >>> len(kernFilePaths) >= 500
    True
    ```

    ```python
    >>> abcFilePaths = coreCorpus.getPaths(['abc'])
    >>> len(abcFilePaths) >= 100
    True
    ```

Methods inherited from [`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus"):

|  |  |  |
| --- | --- | --- |
| * [`all()`](#music21.corpus.corpora.Corpus.all "music21.corpus.corpora.Corpus.all") * [`cacheMetadata()`](#music21.corpus.corpora.Corpus.cacheMetadata "music21.corpus.corpora.Corpus.cacheMetadata") * [`getComposer()`](#music21.corpus.corpora.Corpus.getComposer "music21.corpus.corpora.Corpus.getComposer") | * [`getWorkList()`](#music21.corpus.corpora.Corpus.getWorkList "music21.corpus.corpora.Corpus.getWorkList") * [`getWorkReferences()`](#music21.corpus.corpora.Corpus.getWorkReferences "music21.corpus.corpora.Corpus.getWorkReferences") * [`rebuildMetadataCache()`](#music21.corpus.corpora.Corpus.rebuildMetadataCache "music21.corpus.corpora.Corpus.rebuildMetadataCache") | * [`search()`](#music21.corpus.corpora.Corpus.search "music21.corpus.corpora.Corpus.search") * [`translateExtensions()`](#music21.corpus.corpora.Corpus.translateExtensions "music21.corpus.corpora.Corpus.translateExtensions") |

## LocalCorpus

class music21.corpus.corpora.LocalCorpus(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/corpus/corpora.html#LocalCorpus)
:   A model of a *local* corpus.

    ```python
    >>> localCorpus = corpus.corpora.LocalCorpus()
    ```

    The default local corpus is unnamed (or called “local” or None), but an arbitrary number of
    independent, named local corpora can be defined and persisted:

    ```python
    >>> namedLocalCorpus = corpus.corpora.LocalCorpus('funk')
    ```

    Illegal local corpus name (‘core’ or ‘virtual’)

    ```python
    >>> corpus.corpora.LocalCorpus('core')
    Traceback (most recent call last):
    music21.exceptions21.CorpusException: The name 'core' is reserved.
    ```

[`LocalCorpus`](#music21.corpus.corpora.LocalCorpus "music21.corpus.corpora.LocalCorpus") bases

* [`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LocalCorpus`](#music21.corpus.corpora.LocalCorpus "music21.corpus.corpora.LocalCorpus") read-only properties

LocalCorpus.directoryPaths
:   The directory paths in use by a given local corpus.

LocalCorpus.existsInSettings
:   True if this local corpus has a corresponding entry in music21’s user
    settings, otherwise false.

LocalCorpus.name
:   The name of a given local corpus. Either ‘local’ for the unnamed corpus
    or a name for a named corpus

    ```python
    >>> corpus.corpora.LocalCorpus().name
    'local'
    ```

    ```python
    >>> corpus.corpora.LocalCorpus('funkCorpus').name
    'funkCorpus'
    ```

Read-only properties inherited from [`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus"):

|  |  |  |
| --- | --- | --- |
| * [`directoryInformation`](#music21.corpus.corpora.Corpus.directoryInformation "music21.corpus.corpora.Corpus.directoryInformation") | * [`metadataBundle`](#music21.corpus.corpora.Corpus.metadataBundle "music21.corpus.corpora.Corpus.metadataBundle") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LocalCorpus`](#music21.corpus.corpora.LocalCorpus "music21.corpus.corpora.LocalCorpus") read/write properties

LocalCorpus.cacheFilePath
:   Get the path to the file path that stores the .json file.

    returns a pathlib.Path

[`LocalCorpus`](#music21.corpus.corpora.LocalCorpus "music21.corpus.corpora.LocalCorpus") methods

LocalCorpus.addPath(*directoryPath*)[[source]](../_modules/music21/corpus/corpora.html#LocalCorpus.addPath)
:   Add a directory path to a local corpus:

    ```python
    >>> localCorpus = corpus.corpora.LocalCorpus('a new corpus')
    >>> localCorpus.addPath('~/Desktop')
    ```

    Paths added in this way will not be persisted from session to session
    unless explicitly saved by a call to `LocalCorpus.save()`.

LocalCorpus.delete()[[source]](../_modules/music21/corpus/corpora.html#LocalCorpus.delete)
:   Delete a non-default local corpus from the user settings.

LocalCorpus.getPaths(*\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *expandExtensions=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus/corpora.html#LocalCorpus.getPaths)
:   Access files in additional directories supplied by the user and defined
    in environment settings in the ‘localCorpusSettings’ list.

    If additional paths are added on a per-session basis with the
    [`addPath()`](moduleCorpus.html#music21.corpus.addPath "music21.corpus.addPath") function, these paths are also returned
    with this method.

LocalCorpus.removePath(*directoryPath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/corpus/corpora.html#LocalCorpus.removePath)
:   Remove a directory path from a local corpus.

    If that path is included in the list of persisted paths for the given
    corpus, it will be removed permanently.

    ```python
    >>> testCorpus = corpus.corpora.LocalCorpus(name='test')
    >>> testCorpus.addPath('~/Desktop')
    >>> len(testCorpus.directoryPaths)
    1
    >>> testCorpus.removePath('~/Desktop')
    >>> testCorpus.directoryPaths
    ()
    ```

    TODO: test for corpus persisted to disk without actually reindexing
    files on user’s Desktop.

LocalCorpus.save()[[source]](../_modules/music21/corpus/corpora.html#LocalCorpus.save)
:   Save the current list of directory paths in use by a given corpus in
    the user settings. And reindex.

Methods inherited from [`Corpus`](#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus"):

|  |  |  |
| --- | --- | --- |
| * [`all()`](#music21.corpus.corpora.Corpus.all "music21.corpus.corpora.Corpus.all") * [`cacheMetadata()`](#music21.corpus.corpora.Corpus.cacheMetadata "music21.corpus.corpora.Corpus.cacheMetadata") * [`getComposer()`](#music21.corpus.corpora.Corpus.getComposer "music21.corpus.corpora.Corpus.getComposer") | * [`getWorkList()`](#music21.corpus.corpora.Corpus.getWorkList "music21.corpus.corpora.Corpus.getWorkList") * [`getWorkReferences()`](#music21.corpus.corpora.Corpus.getWorkReferences "music21.corpus.corpora.Corpus.getWorkReferences") * [`rebuildMetadataCache()`](#music21.corpus.corpora.Corpus.rebuildMetadataCache "music21.corpus.corpora.Corpus.rebuildMetadataCache") | * [`search()`](#music21.corpus.corpora.Corpus.search "music21.corpus.corpora.Corpus.search") * [`translateExtensions()`](#music21.corpus.corpora.Corpus.translateExtensions "music21.corpus.corpora.Corpus.translateExtensions") |
