Source: https://music21.org/music21docs/moduleReference/moduleCorpusManager.html

# music21.corpus.manager

The manager module handles requests across multiple corpora. It should be the default
interface to searching corpora.

New in v3 – previously most were static methods on corpus.corpora.Corpus, but that
seemed inappropriate since these work across corpora.

## Functions

music21.corpus.manager.cacheMetadataBundleFromDisk(*corpusObject: [Corpus](moduleCorpusCorpora.html#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/corpus/manager.html#cacheMetadataBundleFromDisk)
:   Update a corpus’ metadata bundle from its stored JSON file on disk.

music21.corpus.manager.fromName(*name*)[[source]](../_modules/music21/corpus/manager.html#fromName)
:   Instantiate a specific corpus based on name:

    ```python
    >>> corpus.manager.fromName('core')
    <music21.corpus.corpora.CoreCorpus>
    ```

    ```python
    >>> corpus.manager.fromName('local')
    <music21.corpus.corpora.LocalCorpus: 'local'>
    ```

    ```python
    >>> corpus.manager.fromName(None)
    <music21.corpus.corpora.LocalCorpus: 'local'>
    ```

    Note that this corpus probably does not exist on disk, but it’s ready to have
    paths added to it and to be stored on disk.

    ```python
    >>> corpus.manager.fromName('testDummy')
    <music21.corpus.corpora.LocalCorpus: 'testDummy'>
    ```

music21.corpus.manager.getMetadataBundleByCorpus(*corpusObject: [corpora.Corpus](moduleCorpusCorpora.html#music21.corpus.corpora.Corpus "music21.corpus.corpora.Corpus")*) → [bundles.MetadataBundle](moduleMetadataBundles.html#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle")[[source]](../_modules/music21/corpus/manager.html#getMetadataBundleByCorpus)
:   Return the metadata bundle for a single Corpus object

    ```python
    >>> cc = corpus.corpora.CoreCorpus()
    >>> mdb1 = corpus.manager.getMetadataBundleByCorpus(cc)
    >>> mdb1
    <music21.metadata.bundles.MetadataBundle 'core': {... entries}>
    ```

    This is the same as calling metadataBundle on the corpus itself,
    but this is the routine that actually does the work. In other words,
    it’s the call on the object that is redundant, not this routine.

    ```python
    >>> mdb1 is cc.metadataBundle
    True
    ```

    Non-existent corpus:

    ```python
    >>> lc = corpus.corpora.LocalCorpus('junk')
    >>> mdb1 = corpus.manager.getMetadataBundleByCorpus(lc)
    >>> mdb1
    <music21.metadata.bundles.MetadataBundle 'junk': {0 entries}>
    ```

music21.corpus.manager.getWork(*workName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *movementNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")][[source]](../_modules/music21/corpus/manager.html#getWork)
:   this parse function is called from corpus.parse() and does nothing differently from it.

    Searches all corpora for a file that matches the name and returns it parsed.

music21.corpus.manager.iterateCorpora(*returnObjects=True*)[[source]](../_modules/music21/corpus/manager.html#iterateCorpora)
:   a generator that iterates over the corpora (either as objects or as names)
    for use in pan corpus searching.

    This test will only show the first two, because it needs to run the same
    on every system:

    ```python
    >>> for i, corpusObject in enumerate(corpus.manager.iterateCorpora()):
    ...     print(corpusObject)
    ...     if i == 1:
    ...        break
    <music21.corpus.corpora.CoreCorpus>
    <music21.corpus.corpora.LocalCorpus: 'local'>
    ```

    We can also get names instead.
    (Note that the name of the main local corpus is “local” not None)

    ```python
    >>> for i, corpusName in enumerate(corpus.manager.iterateCorpora(returnObjects=False)):
    ...     print(corpusName)
    ...     if i == 1:
    ...        break
    core
    local
    ```

    * New in v3.

music21.corpus.manager.listLocalCorporaNames(*skipNone=False*)[[source]](../_modules/music21/corpus/manager.html#listLocalCorporaNames)
:   List the names of all user-defined local corpora.

    The entry for None refers to the default local corpus.

music21.corpus.manager.listSearchFields()[[source]](../_modules/music21/corpus/manager.html#listSearchFields)
:   List all available search field names:

    ```python
    >>> for field in corpus.manager.listSearchFields():
    ...     field
    ...
    'abstract'
    'accessRights'
    'accompanyingMaterialWriter'
    ...
    'composer'
    'composerAlias'
    'composerCorporate'
    'conceptor'
    'conductor'
    ...
    'dateCreated'
    'dateFirstPublished'
    'dateIssued'
    'dateModified'
    'dateSubmitted'
    'dateValid'
    ...
    'tempoFirst'
    'tempos'
    'textLanguage'
    'textOriginalLanguage'
    'timeSignatureFirst'
    'timeSignatures'
    'title'
    ...
    ```

music21.corpus.manager.parse(*workName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *\**, *movementNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fileExtensions: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *forceSource: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *format: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → stream.Score | stream.Part | stream.Opus[[source]](../_modules/music21/corpus/manager.html#parse)

music21.corpus.manager.readAllMetadataBundlesFromDisk()[[source]](../_modules/music21/corpus/manager.html#readAllMetadataBundlesFromDisk)
:   Read each corpus’s metadata bundle and store it in memory.

music21.corpus.manager.search(*query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *field: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *corpusNames=None*, *fileExtensions: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ()*, *\*\*keywords*)[[source]](../_modules/music21/corpus/manager.html#search)
:   Search all stored metadata bundles and return a list of file paths.

    This function uses stored metadata and thus, on first usage, will incur a
    performance penalty during metadata loading.

    ```python
    >>> corpus.search('china')
    <music21.metadata.bundles.MetadataBundle {1235 entries}>
    ```

    ```python
    >>> corpus.search('china', fileExtensions=('.mid',))
    <music21.metadata.bundles.MetadataBundle {0 entries}>
    ```

    ```python
    >>> corpus.search('bach', field='composer')
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    Note the importance of good metadata – there’s almost 400 pieces by
    Bach in the corpus, but many do not have correct metadata entries.

    This can also be specified as:

    ```python
    >>> corpus.search(composer='bach')
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    Or, to get all the chorales (without using corpus.chorales.Iterator):

    ```python
    >>> corpus.search(sourcePath='bach', numberOfParts=4)
    <music21.metadata.bundles.MetadataBundle {368 entries}>
    ```

    This function is implemented in corpus.manager as a method there but also directly
    available in the corpus module for ease of use.

    The `corpusNames` parameter can be used to specify which corpora to search,
    for example:

    ```python
    >>> corpus.manager.search(
    ...     'bach',
    ...     corpusNames=('core',),
    ...     )
    <music21.metadata.bundles.MetadataBundle {564 entries}>
    ```

    ```python
    >>> corpus.manager.search(
    ...     'bach',
    ...     corpusNames=('core',),
    ...     fileExtensions=('xml',),
    ...     )
    <music21.metadata.bundles.MetadataBundle {412 entries}>
    ```

    If `corpusNames` is None, all corpora known to music21 will be searched.

    See usersGuide (chapter 11) for more information on searching
