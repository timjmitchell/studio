Source: https://music21.org/music21docs/usersGuide/usersGuide_53_advancedCorpus.html

# User’s Guide, Chapter 53: Advanced Corpus and Metadata Searching

We saw in [Chapter 11](usersGuide_11_corpusSearching.html#usersguide-11-corpussearching) some ways
to work with and search through the “core” corpus. Not everything is in
the core corpus, of course, so the `converter.parse()` function is a
great way of getting files from a local hard drive or the internet. But
the “core” corpus also has many great search functions, and these can be
helpful for working with your own files and files on the web as well.

In this chapter, we’ll introduce the other “Corpora” in addition to the
“core” corpus and how they might be used.

## The Default Local Corpus

```python
from music21 import *

localCorpus = corpus.corpora.LocalCorpus()
localCorpus
```

```python
 <music21.corpus.corpora.LocalCorpus: 'local'>
```

You can add and remove paths from a *local* corpus with the
`addPath()` and `removePath()` methods:

## Creating multiple corpus repositories via local corpora

In addition to the default local corpus, music21 allows users to create
and save as many named local corpora as they like, which will persist
from session to session.

Let’s create a new *local* corpus, give it a directory to find music
files in, and then save it:

```python
from music21 import *

aNewLocalCorpus = corpus.corpora.LocalCorpus('newCorpus')
aNewLocalCorpus.existsInSettings
```

```python
 False
```

```python
aNewLocalCorpus.addPath('~/Desktop')
aNewLocalCorpus.directoryPaths
```

```python
 ('/Users/j_wolf/Desktop',)
```

```python
aNewLocalCorpus.save()
aNewLocalCorpus.existsInSettings
```

```python
 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: newCorpus metadata cache: starting processing of paths: 0
 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: cache: filename: /var/folders/bb/bmq3z9hs3njfyvpdh88z6v340000gn/T/music21/local-newCorpus.p.gz
 metadata.bundles: WARNING: MetadataBundle Modification Time: 1767557505.539169
 metadata.bundles: WARNING: Skipped 0 sources already in cache.
 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: cache: writing time: 0.025 md items: 0

 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: cache: filename: /var/folders/bb/bmq3z9hs3njfyvpdh88z6v340000gn/T/music21/local-newCorpus.p.gz
```

```python
 True
```

We can see that our new *local* corpus is saved by checking for the
names of all saved *local* corpora using the corpus.manager list:

```python
corpus.manager.listLocalCorporaNames()
```

```python
 [None, 'funk', 'newCorpus', 'bach']
```

Note

When running `listLocalCorporaNames()`, you will see `None` -
indicating the default *local* corpus - along with the names of any
non-default *local* corpora you’ve manually created yourself. In the above
example, a number of other corpora have already been created.

Finally, we can delete the *local* corpus we previously created like
this:

```python
aNewLocalCorpus.delete()
aNewLocalCorpus.existsInSettings
```

```python
 False
```

## Inspecting metadata bundle search results

Let’s take a closer look at some search results:

```python
bachBundle = corpus.corpora.CoreCorpus().search('bach', 'composer')
bachBundle
```

```python
 <music21.metadata.bundles.MetadataBundle {363 entries}>
```

```python
bachBundle[0]
```

```python
 <music21.metadata.bundles.MetadataEntry 'bach_bwv10_7_mxl'>
```

```python
bachBundle[0].sourcePath
```

```python
 PosixPath('bach/bwv10.7.mxl')
```

```python
bachBundle[0].metadata
```

```python
 <music21.metadata.RichMetadata object at 0x10af31690>
```

```python
bachBundle[0].metadata.all()
```

```python
 (('ambitus',
   AmbitusShort(semitones=34, diatonic='m7', pitchLowest='G2', pitchHighest='F5')),
  ('composer', 'J.S. Bach'),
  ('fileFormat', 'musicxml'),
  ('filePath',
   '/Users/cuthbert/git/music21base/music21/corpus/bach/bwv10.7.mxl'),
  ('keySignatureFirst', -2),
  ('keySignatures', [-2]),
  ('movementName', 'bwv10.7.mxl'),
  ('noteCount', 214),
  ('numberOfParts', 4),
  ('pitchHighest', 'F5'),
  ('pitchLowest', 'G2'),
  ('quarterLength', 88.0),
  ('software', 'MuseScore 2.1.0'),
  ('software', 'music21 v.6.0.0a'),
  ('software', 'music21 v.9.1.0'),
  ('sourcePath', 'bach/bwv10.7.mxl'),
  ('tempoFirst', None),
  ('tempos', []),
  ('timeSignatureFirst', '4/4'),
  ('timeSignatures', ['4/4']))
```

```python
mdpl = bachBundle[0].metadata
mdpl.noteCount
```

```python
 214
```

```python
bachAnalysis0 = bachBundle[0].parse()
bachAnalysis0.show()
```

[![../_images/usersGuide_53_advancedCorpus_20_0.png](../_images/usersGuide_53_advancedCorpus_20_0.png)](../_images/usersGuide_53_advancedCorpus_20_0.png)[![../_images/usersGuide_53_advancedCorpus_20_2.png](../_images/usersGuide_53_advancedCorpus_20_2.png)](../_images/usersGuide_53_advancedCorpus_20_2.png)

## Manipulating multiple metadata bundles

Another useful feature of `music21`’s metadata bundles is that they
can be operated on as though they were sets, allowing you to union,
intersect and difference multiple metadata bundles, thereby creating
more complex search results:

```python
corelliBundle = corpus.search('corelli', field='composer')
corelliBundle
```

```python
 <music21.metadata.bundles.MetadataBundle {1 entry}>
```

```python
bachBundle.union(corelliBundle)
```

```python
 <music21.metadata.bundles.MetadataBundle {364 entries}>
```

Consult the API for [`MetadataBundle`](../moduleReference/moduleMetadataBundles.html#music21.metadata.bundles.MetadataBundle "music21.metadata.bundles.MetadataBundle")
for a more in depth look at how this works.

## Getting a metadata bundle

In music21, metadata is information *about* a score, such as its
composer, title, initial key signature or ambitus. A metadata *bundle*
is a collection of metadata pulled from an arbitrarily large group of
different scores. Users can search through metadata bundles to find
scores with certain qualities, such as all scores in a given corpus with
a time signature of `6/8`, or all scores composed by Monteverdi.

There are a number of different ways to acquire a metadata bundle. The
easiest way to get the metadataBundle for the core corpus is simply to
download music21: we include a pre-made metadataBundle (in
`corpus/metadataCache/core.json`) so that this step is unnecessary for
the core corpus unless you’re contributing to the project. But you may
want to create metadata bundles for your own local corpora. Access the
`metadataBundle` attribute of any `Corpus` instance to get its
corresponding metadata bundle:

```python
coreCorpus = corpus.corpora.CoreCorpus()
coreCorpus.metadataBundle
```

```python
 <music21.metadata.bundles.MetadataBundle 'core': {15112 entries}>
```

Music21 also provides a handful of convenience methods for getting
metadata bundles associated with the *virtual*, *local* or *core*
corpora:

```python
coreBundle = corpus.corpora.CoreCorpus().metadataBundle
localBundle = corpus.corpora.LocalCorpus().metadataBundle
otherLocalBundle = corpus.corpora.LocalCorpus('blah').metadataBundle
```

But really advanced users can also make metadata bundles manually, by
passing in the name of the corpus you want the bundle to refer to, or,
equivalently, an actual `Corpus` instance itself:

```python
coreBundle = metadata.bundles.MetadataBundle('core')
coreBundle = metadata.bundles.MetadataBundle(corpus.corpora.CoreCorpus())
```

However, you’ll need to read the bundle’s saved data from disk before
you can do anything useful with the bundle. Bundles don’t read their
associated JSON files automatically when they’re manually instantiated.

```python
coreBundle
```

```python
 <music21.metadata.bundles.MetadataBundle 'core': {0 entries}>
```

```python
coreBundle.read()
```

```python
 <music21.metadata.bundles.MetadataBundle 'core': {15112 entries}>
```

## Creating persistent metadata bundles

Metadata bundles can take a long time to create. So it’d be nice if they
could be written to and read from disk. Unfortunately we never got
around to…nah, just kidding. Of course you can. Just call `.write()`
on one:

```python
coreBundle = metadata.bundles.MetadataBundle('core')
coreBundle.read()
```

```python
 <music21.metadata.bundles.MetadataBundle 'core': {15112 entries}>
```

```python
coreBundle.write()
```

They can also be completely rebuilt, as you will want to do for local
corpora. To add information to a bundle, use the `addFromPaths()`
method:

```python
newBundle = metadata.bundles.MetadataBundle()
paths = corpus.corpora.CoreCorpus().search('corelli')
failedPaths = newBundle.addFromPaths(paths)
failedPaths
```

```python
 []
```

then call `.write()` to save to disk

```python
newBundle
```

```python
 <music21.metadata.bundles.MetadataBundle {1 entry}>
```

Note

Building metadata information can be an incredibly intensive process. For
example, building the *core* metadata bundle can easily take as long as an
hour! And this is even though the building process uses multiple cores.
Please use caution, and be patient, when building metadata bundles
from large corpora. To monitor the corpus-building progress, make sure to
set ‘debug’ to True in your user settings:

```python
>>> environment.UserSettings()['debug'] = True
```

You can delete, rebuild and save a metadata bundle in one go with the
`rebuildMetadataCache()` method:

```python
localBundle = corpus.corpora.LocalCorpus().metadataBundle
localBundle.rebuildMetadataCache()
```

The process of rebuilding will store the file as it goes (for safety) so
at the end there is no need to call `.write()`.

To delete a metadata bundle’s cached-to-disk JSON file, use the
`delete()` method:

```python
localBundle.delete()
```

Deleting a metadata bundle’s JSON file won’t empty the in-memory
contents of that bundle. For that, use `clear()`:

```python
localBundle.clear()
```

With local corpora you will be able to develop your own collections of
pieces to analyze, work on a new self-contained project with, and index
and search through them.

But what if some of your music is in a file format that `music21` does
not yet support? Maybe it’s time to write your own converter or notation
format. To learn how to do that, go to the next chapter,
[Chapter 54: Extending Converter with New Formats](usersGuide_54_extendingConverter.html#usersguide-54-extendingconverter).
