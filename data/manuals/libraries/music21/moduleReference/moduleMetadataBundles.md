Source: https://music21.org/music21docs/moduleReference/moduleMetadataBundles.html

# music21.metadata.bundles

## MetadataBundle

class music21.metadata.bundles.MetadataBundle(*expr: 'music21.corpus.corpora.Corpus' | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle)
:   An object that provides access to, searches within, and stores and loads
    multiple Metadata objects.

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> coreBundle
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    ```

    (The coreBundle has around 15100 entries; I’ve put ‘…’ in the
    docs so I don’t need to rewrite them every time we add a new piece)

    ```python
    >>> searchResults = coreBundle.search('bach', field='composer')
    >>> searchResults
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> resultsEntries = searchResults.search('3/4')
    >>> resultsEntries
    <music21.metadata.bundles.MetadataBundle {40 entries}>
    ```

    Results are ordered by their source path:

    ```python
    >>> resultsEntries[0]
    <music21.metadata.bundles.MetadataEntry 'bach_bwv11_6_mxl'>
    ```

    To get a score out of the entry, call .parse()

    ```python
    >>> resultsEntries[0].parse()
    <music21.stream.Score ...>
    ```

    Or pass it into converter:

    ```python
    >>> converter.parse(resultsEntries[0])
    <music21.stream.Score ...>
    ```

    A metadata bundle can be instantiated in three ways, (1) from a `Corpus` instance,
    or (2) a string indicating which corpus name to draw from, and then calling
    .read() or (3) by calling
    .metadataBundle on a corpus object. This
    calls .read() automatically:

    Method 1:

    ```python
    >>> coreCorpus = corpus.corpora.CoreCorpus()
    >>> coreBundle = metadata.bundles.MetadataBundle(coreCorpus)
    >>> localCorpus = corpus.corpora.LocalCorpus()
    >>> localBundle = metadata.bundles.MetadataBundle(localCorpus)
    ```

    Method 2:

    ```python
    >>> coreBundle = metadata.bundles.MetadataBundle('core')
    >>> localBundle = metadata.bundles.MetadataBundle('local')
    ```

    After calling these you’ll need to call `read()`:

    ```python
    >>> coreBundle
    <music21.metadata.bundles.MetadataBundle 'core': {0 entries}>
    >>> coreBundle.read()
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    >>> coreBundle
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    ```

    Method 3:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> localBundle = corpus.corpora.LocalCorpus().metadataBundle
    ```

    ```python
    >>> coreBundle
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    ```

    Additionally, any two metadata bundles can be operated on together as
    though they were sets, allowing us to build up more complex searches:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    >>> tripleMeterBundle = coreBundle.search('3/4')
    >>> tripleMeterBundle
    <music21.metadata.bundles.MetadataBundle {1875 entries}>
    >>> bachBundle.intersection(tripleMeterBundle)
    <music21.metadata.bundles.MetadataBundle {40 entries}>
    ```

    Finally, a metadata bundle need not be associated with any corpus at all,
    and can be populated ad hoc:

    ```python
    >>> anonymousBundle = metadata.bundles.MetadataBundle()
    >>> mdb = corpus.corpora.CoreCorpus().search('monteverdi')[:4]
    >>> paths = [common.getCorpusFilePath() / x.sourcePath for x in mdb]
    >>> failedPaths = anonymousBundle.addFromPaths(
    ...     paths, useMultiprocessing=False)
    >>> failedPaths
    []
    >>> anonymousBundle
    <music21.metadata.bundles.MetadataBundle {4 entries}>
    ```

[`MetadataBundle`](#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MetadataBundle`](#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle") read-only properties

MetadataBundle.filePath
:   The filesystem name of the cached metadata bundle, if the metadata
    bundle’s name is not None.

    ```python
    >>> ccPath = corpus.corpora.CoreCorpus().metadataBundle.filePath
    >>> ccPath.name
    'core.p.gz'
    >>> '_metadataCache' in ccPath.parts
    True
    ```

    ```python
    >>> localPath = corpus.corpora.LocalCorpus().metadataBundle.filePath
    >>> localPath.name
    'local.p.gz'
    ```

    Local corpora metadata is stored in the scratch dir, not the
    corpus directory

    ```python
    >>> '_metadataCache' in localPath.parts
    False
    ```

    ```python
    >>> funkCorpus = corpus.corpora.LocalCorpus('funk')
    >>> funkPath = funkCorpus.metadataBundle.filePath
    >>> funkPath.name
    'local-funk.p.gz'
    ```

MetadataBundle.name
:   The name of the metadata bundle.

    Can be ‘core’, ‘local’, ‘{name}’ where name is the name
    of a named local corpus or None.

    The names ‘core’ and ‘local’ refer to the core and local
    corpora respectively: (virtual corpus is currently offline)

    ```python
    >>> metadata.bundles.MetadataBundle().name is None
    True
    >>> corpus.corpora.CoreCorpus().metadataBundle.name
    'core'
    ```

    ```python
    >>> funkCorpus = corpus.corpora.LocalCorpus('funk')
    >>> funkCorpus.metadataBundle.name
    'funk'
    ```

    Return string or None.

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MetadataBundle`](#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle") read/write properties

MetadataBundle.corpus
:   The corpus.corpora.Corpus object associated with the metadata
    bundle’s name.

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> coreBundle
    <music21.metadata.bundles.MetadataBundle 'core': {151... entries}>
    >>> coreBundle.corpus
    <music21.corpus.corpora.CoreCorpus>
    ```

[`MetadataBundle`](#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle") methods

MetadataBundle.\_\_eq\_\_(*other*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.__eq__)
:   True if expr is of the same type, and contains an identical set of
    entries, otherwise false:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> corelliBundle = coreBundle.search('corelli', 'composer')
    >>> bachBundle == corelliBundle
    False
    >>> bachBundle == coreBundle.search(
    ...     'bach',
    ...     field='composer',
    ...     )
    True
    >>> bachBundle == 'foo'
    False
    ```

MetadataBundle.\_\_getitem\_\_(*i*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.__getitem__)

MetadataBundle.addFromPaths(*paths*, *parseUsingCorpus=False*, *useMultiprocessing=True*, *storeOnDisk=True*, *verbose=False*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.addFromPaths)
:   Parse and store metadata from numerous files.

    If any files cannot be loaded, their file paths will be collected in a
    list that is returned.

    Returns a list of file paths with errors and stores the extracted
    metadata in self.\_metadataEntries.

    ```python
    >>> metadataBundle = metadata.bundles.MetadataBundle()
    >>> p = corpus.corpora.CoreCorpus().getWorkList('bach/bwv66.6')
    >>> metadataBundle.addFromPaths(
    ...     p,
    ...     parseUsingCorpus=False,
    ...     useMultiprocessing=False,
    ...     )
    []
    >>> len(metadataBundle._metadataEntries)
    1
    ```

    Set Verbose to True to get updates even if debug is off.

MetadataBundle.clear()[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.clear)
:   Clear all keys in a metadata bundle:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> bachBundle.clear()
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {0 entries}>
    ```

    Returns None.

static MetadataBundle.corpusPathToKey(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.corpusPathToKey)
:   Given a file path or corpus path, return the metadata key:

    ```python
    >>> mb = metadata.bundles.MetadataBundle()
    >>> key = mb.corpusPathToKey('bach/bwv1007/prelude')
    >>> key.endswith('bach_bwv1007_prelude')
    True
    ```

    ```python
    >>> key = mb.corpusPathToKey('corelli/opus3no1/1grave.xml')
    >>> key.endswith('corelli_opus3no1_1grave_xml')
    True
    ```

    Numbers are appended if given

    ```python
    >>> key = mb.corpusPathToKey('corelli/opus3no1/1grave.xml', number=3)
    >>> key.endswith('corelli_opus3no1_1grave_xml_3')
    True
    ```

MetadataBundle.delete() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.delete)
:   Delete the filesystem cache of a named metadata bundle.

    Does not delete the in-memory metadata bundle.

    Return None.

MetadataBundle.difference(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.difference)
:   Compute the set-wise difference of two metadata bundles:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> tripleMeterBundle = coreBundle.search('3/4')
    >>> tripleMeterBundle
    <music21.metadata.bundles.MetadataBundle {1875 entries}>
    ```

    ```python
    >>> bachBundle.difference(tripleMeterBundle)
    <music21.metadata.bundles.MetadataBundle {323 entries}>
    ```

    Returns a new metadata bundle.

MetadataBundle.intersection(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.intersection)
:   Compute the set-wise intersection of two metadata bundles:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> tripleMeterBundle = coreBundle.search('3/4')
    >>> tripleMeterBundle
    <music21.metadata.bundles.MetadataBundle {1875 entries}>
    ```

    ```python
    >>> bachBundle.intersection(tripleMeterBundle)
    <music21.metadata.bundles.MetadataBundle {40 entries}>
    ```

    Returns a new MetadataBundle.

MetadataBundle.isdisjoint(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.isdisjoint)
:   True if the set of keys in one metadata bundle are disjoint with
    the set of keys in another:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> corelliBundle = coreBundle.search('corelli', 'composer')
    >>> corelliBundle
    <music21.metadata.bundles.MetadataBundle {1 entry}>
    ```

    ```python
    >>> bachBundle.isdisjoint(corelliBundle)
    True
    ```

    ```python
    >>> tripleMeterBundle = coreBundle.search('3/4')
    >>> tripleMeterBundle
    <music21.metadata.bundles.MetadataBundle {1875 entries}>
    ```

    ```python
    >>> bachBundle.isdisjoint(tripleMeterBundle)
    False
    ```

    Returns boolean.

MetadataBundle.issubset(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.issubset)
:   True if the set of keys in one metadata bundle are a subset of
    the keys in another:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> tripleMeterBachBundle = bachBundle.search('3/4')
    >>> tripleMeterBachBundle
    <music21.metadata.bundles.MetadataBundle {40 entries}>
    ```

    ```python
    >>> tripleMeterBachBundle.issubset(bachBundle)
    True
    ```

    ```python
    >>> bachBundle.issubset(tripleMeterBachBundle)
    False
    ```

    Returns boolean.

MetadataBundle.issuperset(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.issuperset)
:   True if the set of keys in one metadata bundle are a superset of
    the keys in another:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    ```

    ```python
    >>> tripleMeterBachBundle = bachBundle.search('3/4')
    >>> tripleMeterBachBundle
    <music21.metadata.bundles.MetadataBundle {40 entries}>
    ```

    ```python
    >>> tripleMeterBachBundle.issuperset(bachBundle)
    False
    ```

    ```python
    >>> bachBundle.issuperset(tripleMeterBachBundle)
    True
    ```

    Returns boolean.

static MetadataBundle.listSearchFields()[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.listSearchFields)
:   List all available search field names:

    ```python
    >>> for field in metadata.bundles.MetadataBundle.listSearchFields():
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

MetadataBundle.read(*filePath=None*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.read)
:   Load cached metadata from the file path suggested by the name of this
    MetadataBundle (‘core’, ‘local’, or a name).

    If a specific filepath is given with the filePath keyword, attempt to
    load cached metadata from the file at that location.

    If filePath is None, and self.filePath is also None, do nothing.

    ```python
    >>> coreBundle = metadata.bundles.MetadataBundle('core').read()
    ```

    If a metadata is unnamed, and no file path is specified, an exception
    will be thrown:

    ```python
    >>> anonymousBundle = metadata.bundles.MetadataBundle().read()
    Traceback (most recent call last):
    music21.exceptions21.MetadataException: Unnamed MetadataBundles have
        no default file path to read from.
    ```

MetadataBundle.search(*query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *field=None*, *\**, *fileExtensions: Iterable[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\*\*keywords*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.search)
:   Perform search, on all stored metadata, permit regular expression
    matching.

    ```python
    >>> workList = corpus.corpora.CoreCorpus().getWorkList('ciconia')
    >>> metadataBundle = metadata.bundles.MetadataBundle()
    >>> failedPaths = metadataBundle.addFromPaths(
    ...     workList,
    ...     parseUsingCorpus=False,
    ...     useMultiprocessing=False,
    ...     )
    >>> failedPaths
    []
    ```

    ```python
    >>> searchResult = metadataBundle.search(
    ...     'cicon',
    ...     field='composer'
    ...     )
    >>> searchResult
    <music21.metadata.bundles.MetadataBundle {1 entry}>
    >>> len(searchResult)
    1
    >>> searchResult[0]
    <music21.metadata.bundles.MetadataEntry 'ciconia_quod_jactatur_xml'>
    >>> searchResult = metadataBundle.search(
    ...     'cicon',
    ...     field='composer',
    ...     fileExtensions=('.krn',),
    ...     )
    >>> len(searchResult)  # no files in this format
    0
    ```

    ```python
    >>> searchResult = metadataBundle.search(
    ...     'cicon',
    ...     field='composer',
    ...     fileExtensions=('.xml',),
    ...     )
    >>> len(searchResult)
    1
    ```

    Searches can also use keyword args:

    ```python
    >>> metadataBundle.search(composer='cicon')
    <music21.metadata.bundles.MetadataBundle {1 entry}>
    ```

MetadataBundle.symmetric\_difference(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.symmetric_difference)
:   Compute the set-wise symmetric difference of two metadata bundles:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    >>> tripleMeterBundle = coreBundle.search('3/4')
    >>> tripleMeterBundle
    <music21.metadata.bundles.MetadataBundle {1875 entries}>
    >>> bachBundle.symmetric_difference(tripleMeterBundle)
    <music21.metadata.bundles.MetadataBundle {2158 entries}>
    ```

    Returns a new MetadataBundle.

MetadataBundle.union(*metadataBundle*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.union)
:   Compute the set-wise union of two metadata bundles:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    >>> beethovenBundle = coreBundle.search(
    ...     'beethoven',
    ...     field='composer',
    ...     )
    >>> beethovenBundle
    <music21.metadata.bundles.MetadataBundle {23 entries}>
    ```

    ```python
    >>> bachBundle.union(beethovenBundle)
    <music21.metadata.bundles.MetadataBundle {386 entries}>
    ```

    Returns a new MetadataBundle.

MetadataBundle.validate()[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.validate)
:   Validate each metadata entry in a metadata bundle.

    If the entry represents a non-virtual corpus asset, test that its
    source path is locatable on disk. If not, remove the metadata entry
    from the metadata bundle.

MetadataBundle.write(*filePath=None*)[[source]](../_modules/music21/metadata/bundles.html#MetadataBundle.write)
:   Write the metadata bundle to disk as a pickle file.

    If filePath is None, use self.filePath.

    Returns the metadata bundle.

    ```python
    >>> bachBundle = coreBundle.search('bach', 'composer')
    >>> bachBundle
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    >>> bachBundle.filePath is None
    True
    ```

    ```python
    >>> import os
    >>> e = environment.Environment()
    >>> tempFilePath = e.getTempFile()
    >>> bachBundle.write(filePath=tempFilePath)
    <music21.metadata.bundles.MetadataBundle {363 entries}>
    >>> os.remove(tempFilePath)
    ```

## MetadataEntry

class music21.metadata.bundles.MetadataEntry(*sourcePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") = ''*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *metadataPayload: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *corpusName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/metadata/bundles.html#MetadataEntry)
:   An entry in a metadata bundle.

    The metadata entry holds information about the source of the metadata,
    and can be parsed to reconstitute the score object the metadata was
    derived from:

    ```python
    >>> coreBundle = corpus.corpora.CoreCorpus().metadataBundle
    >>> metadataEntry = coreBundle.search('bwv66.6')[0]
    >>> metadataEntry
    <music21.metadata.bundles.MetadataEntry 'bach_bwv66_6_mxl'>
    ```

    The sourcePath of the metadata entry refers to the file path at which its
    score file is found, but it is usually a relative path to the top of the corpus
    directory. It is a pathlib object.

    ```python
    >>> metadataEntry.sourcePath
    PosixPath('bach/bwv66.6.mxl')
    ```

    The metadata property contains its [`RichMetadata`](moduleMetadata.html#music21.metadata.RichMetadata "music21.metadata.RichMetadata") object:

    ```python
    >>> metadataEntry.metadata
    <music21.metadata.RichMetadata object at 0x...>
    ```

    Note that the id is not necessarily the current memory location.

    And the metadata entry can be parsed:

    ```python
    >>> metadataEntry.parse()
    <music21.stream.Score ...>
    ```

[`MetadataEntry`](#music21.metadata.bundles.MetadataEntry "music21.metadata.bundles.MetadataEntry") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MetadataEntry`](#music21.metadata.bundles.MetadataEntry "music21.metadata.bundles.MetadataEntry") read-only properties

MetadataEntry.corpusName

MetadataEntry.corpusPath
:   Returns the sourcePath as a string, with \_number appended if it is not None.

MetadataEntry.metadata
:   Returns the Metadata object that is stored in the bundle.

MetadataEntry.number

MetadataEntry.sourcePath

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MetadataEntry`](#music21.metadata.bundles.MetadataEntry "music21.metadata.bundles.MetadataEntry") methods

MetadataEntry.parse()[[source]](../_modules/music21/metadata/bundles.html#MetadataEntry.parse)

MetadataEntry.search(*query=None*, *field=None*, *\*\*keywords*)[[source]](../_modules/music21/metadata/bundles.html#MetadataEntry.search)

MetadataEntry.show(*showFormat=None*)[[source]](../_modules/music21/metadata/bundles.html#MetadataEntry.show)

## Functions

music21.metadata.bundles.demo\_bundle(*which: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](../_modules/music21/metadata/bundles.html#demo_bundle)
:   This helps with testing by reusing bundles.
